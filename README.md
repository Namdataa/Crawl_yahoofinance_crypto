# ETL Project and Data Search Application
![FRAMEWORK](https://github.com/user-attachments/assets/a0adf2fb-d2b5-4f03-a757-4490fd4f381e)

With the project “**ETL Project and Data Search Application**”, our goal is to learn and master the operations from getting data from a website written in JavaScript to loading data into the Database and then building a website connected to the Database to display jobs based on the entered keyword name. Stay tuned!
# (Phase 1): Extract - Transform - Load (ETL) 
![image](https://github.com/user-attachments/assets/fea2986f-cb09-4555-bf89-28dba5949a44)

**ETL Project and Data Search Application** we will get data from the largest job website in Vietnam: https://www.vietnamworks.com/
## Extraction Data:
- I accessed each link of each job on the website:
  + Then went to each link and got the detailed information of each job
  + `Tên công việc`: Job title or position being recruited.
  + `Ngày đăng`: The date the job posting was made public.
  + `Ngày Hết hạn`: The deadline for submitting applications.
  + `Công ty`: The name of the recruiting company.
  + `Địa điểm`: The address of the workplace.
  + `Đường dẫn`: URL link to the detailed job posting.
  + `Chức vụ`: Job level or position rank.
  + `Lương`: The expected or negotiable salary for the position.
  + `Loại hình`: The type of employment (full-time, part-time, etc.).
  + `Ngành nghề`: Industry or field of work.
  + `Mô tả công việc`: Detailed description of job responsibilities and tasks.
  + `Yêu cầu công việc`: Criteria required for applicants to fit the position.
  + `Phúc lợi`: Benefits provided by the company.
  + `Từ khóa`: Keywords related to the job position, skills, or company.
  + `Học vấn`: Educational qualifications required.
  + `Độ tuổi`: Age range of applicants.
  + `Số lượng`: The number of positions being recruited.
  + `Giờ làm việc`: Working hours during the day.
  + `Quốc tịch`: Nationality requirements for applicants.
  + `Hồ sơ`: Language of presentation of profile.
  + `Giới tính`: Gender requirements (if any).
  + `Hôn nhân`: Marital status requirements (if any).
  + `Ngày làm việc`: Working days of the week.
  + `Kỹ năng`: Skills required for the job position.
  + `Lĩnh vực`: Field of work for the job position.
  + `Lượt xem`: The number of views for the job posting.
  + `index_`: Index or serial number of the job posting in the system.
- The work done and the results are in the file `Crawl_Vietnamwork.ipynb`
## Transform Data:
- Since the data is taken from the website, the data is quite clean, so here I just handle it simply as follows :
  + Delete `index` column
  + Reselect DataFrame that does not contain empty work locations
  + Treat empty values ​​​​to ` Không hiển thị `
  + Convert `>` to `,` in `Ngành nghề` column
  + Convert `\n` to `,` in `Từ khóa` column
  + Create `tag` column by merging `Kỹ năng`, `Ngành nghề`, `Từ khóa`, `Công ty`, `Lĩnh vực` columns
  + Delete `Từ khóa` column
### Data Cleaned
+ `Tên công việc`: Job title or position being recruited.
+ `Ngày đăng`: The date the job posting was made public.
+ `Ngày Hết hạn`: The deadline for submitting applications.
+ `Công ty`: The name of the recruiting company.
+ `Địa điểm`: The address of the workplace.
+ `Đường dẫn`: URL link to the detailed job posting.
+ `Chức vụ`: Job level or position rank.
+ `Lương`: The expected or negotiable salary for the position.
+ `Loại hình`: The type of employment (full-time, part-time, etc.).
+ `Ngành nghề`: Industry or field of work.
+ `Mô tả công việc`: Detailed description of job responsibilities and tasks.
+ `Yêu cầu công việc`: Criteria required for applicants to fit the position.
+ `Phúc lợi`: Benefits provided by the company.
+ `Học vấn`: Educational qualifications required.
+ `Độ tuổi`: Age range of applicants.
+ `Số lượng`: The number of positions being recruited.
+ `Giờ làm việc`: Working hours during the day.
+ `Quốc tịch`: Nationality requirements for applicants.
+ `Hồ sơ`: Language of presentation of profile.
+ `Giới tính`: Gender requirements (if any).
+ `Hôn nhân`: Marital status requirements (if any).
+ `Ngày làm việc`: Working days of the week.
+ `Kỹ năng`: Skills required for the job position.
+ `Lĩnh vực`: Field of work for the job position.
+ `Lượt xem`: The number of views for the job posting.
+ `tag`: Include keywords to help display jobs.
- The work to be performed is specified in the `transform_data()` function in the `ETL_to_Database.ipynb` file.
## Load Data:
- In the part of putting data into the Database, we will do:
  + Set up connection with the Database
  + Create Database and table to store data
  + Then we will put data into
- The work to be performed is specified in the `DatabaseManager()` class in the `ETL_to_Database.ipynb` file.
# (Phase 2): Build Web App
![image](https://github.com/user-attachments/assets/b7ff6bb6-8f70-473e-8000-b674f43ed01a)

For Web App I will use Streamlit, a framework that allows running App with localhost address
- I connect to Database and create & present my website.
- Next is the part of creating function `recommend()`  and setting up the result display `paginate_dataframe()` function.
- Finally, set up the feedback and problem contact section.
All the above steps are in the file `App.py`
