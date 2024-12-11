import streamlit as st
import pandas as pd
import numpy as np
import os
import urllib
from streamlit_option_menu import option_menu
from sqlalchemy import create_engine
from datetime import datetime
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="Job Now", page_icon=":tada:", layout="wide")
st.markdown("""
    <style>
        @keyframes moveText {
            0% { transform: translateX(0); }
            50% { transform: translateX(50px); }
            100% { transform: translateX(0); }
        }
        .blink-text {
            animation: moveText 4s infinite;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown('<h1 class="blink-text">Chào Mừng Bạn Đến Với Job47 !! </h1>', unsafe_allow_html=True)

class DatabaseManager:
    def __init__(self, server, database, username, password):
        """
        Khởi tạo đối tượng DatabaseManager.

        Parameters:
            server (str): Tên server SQL Server.
            database (str): Tên database.
            username (str): Tên tài khoản đăng nhập.
            password (str): Mật khẩu tài khoản.
        """
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.engine = None

    def connect(self):
        """
        Tạo kết nối đến SQL Server và khởi tạo SQLAlchemy engine.
        """
        try:
            params = urllib.parse.quote_plus(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password};"
                f"Trusted_Connection=no;"
            )
            self.engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
        except Exception as e:
            st.write(f"Không thể kết nối đến database. Lỗi: {e}")
            
def recommend(df,key):
    indices_to_return = []
    # Vòng lặp qua từng dòng trong DataFrame
    for i in range(len(df)):
        if key.lower() in (df['tag'][i]).lower():  # Kiểm tra điều kiện
            # Lấy chỉ mục của dòng thỏa mãn điều kiện
            movie_index = df.index[i]
            indices_to_return.append(movie_index)  # Lưu chỉ mục dưới dạng số nguyên
    # Lấy DataFrame kết quả với các chỉ mục đã thu thập
    data=df.drop('tag', axis=1)
    result_df_limited = data.loc[indices_to_return].head(50)
    return result_df_limited

def paginate_dataframe(df, page_size=10, page_num=1):
    start_idx = (page_num - 1) * page_size
    end_idx = start_idx + page_size
    return df[start_idx:end_idx]

#-------------- Kết nối vào Database
server = r'DESKTOP-Q6B5CSD\NAMNH' # Thay thế lại server của bạn
database = 'recommend_job' #Tên Database của bạn
username = 'sa' #Tài khoản của bạn
password = 'Nam@15092003' #Mật khẩu của bạn
db_manager = DatabaseManager(server, database, username, password)
db_manager.connect()

#------------- Lấy dữ liệu từ bảng đã tạo và load dữ liệu vào
query = '''
Select * from [recommend_job].[dbo].[job]
'''
with db_manager.engine.connect() as connection:
    df = pd.read_sql(query, connection)
    
#--------------- Tạo một khối để nhập từ khóa và Search kết quả dựa trên từ khóa
container = st.container()
container.write("---")
container.header("Đề Xuất Công Việc")
key = st.text_input("Tìm kiếm ở đây nhé👋")
if key:
    recommend_job = recommend(df,key)
    st.write("Kết quả tìm kiếm:")
    num_rows = len(recommend_job)
    # Nếu số lượng dòng ít hơn hoặc bằng 10, không cần slider
    if num_rows <= 10:
        page_num = 1  # Chỉ có một trang duy nhất
        paginated_df = recommend_job  # Hiển thị toàn bộ dữ liệu
    else:
        # Nếu có nhiều hơn 10 dòng, tính số trang cần phân trang
        max_page = (num_rows // 10) + 1  # Tổng số trang
        page_num = st.slider("Page", 1, max_page)
        paginated_df = paginate_dataframe(recommend_job, page_size=10, page_num=page_num)
    # Hiển thị bảng phân trang hoặc toàn bộ bảng nếu không cần phân trang
    st.dataframe(paginated_df)
    st.markdown("<h1 style='text-align: center; color: whie; font-size: 36px;'>Chúc bạn chọn được công việc thích hợp! 🎉</h1>",unsafe_allow_html=True)
    
#-------------------- Phần cuối trang để contact khi có vấn đề
container = st.container()
container.write("---")
container.header("Để Cập Nhật Nhiều Thông Tin Mới Nhất")
contact_form = """
<form action="https://formsubmit.co/Nam.studyjob@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="Feedback" placeholder="Feedback">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <button type="submit">Send</button>
</form>
"""
container.markdown(contact_form, unsafe_allow_html=True)
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha384-GLhlTQ8iN17PdjIq+EQJ4QjsiFDbtZxZ5l5FmvFFPnhIbbVLFYBbuysFBEUVTyHqd" crossorigin="anonymous">
    """,
    unsafe_allow_html=True)
st.header("Liên Hệ")
facebook_link = "https://www.facebook.com/namnew2003/"
st.write(f"<i class='fas fa-phone'></i> Facebook : {facebook_link}", unsafe_allow_html=True)
phone_number = "0888087278"
st.write(f"<i class='fas fa-phone'></i> Phone number: {phone_number}", unsafe_allow_html=True)
st.write(f"<i class='fas fa-phone'></i> Gmail: Nam.studyjob@gmail.com ", unsafe_allow_html=True)