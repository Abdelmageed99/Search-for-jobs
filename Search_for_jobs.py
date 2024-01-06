from bs4 import BeautifulSoup
import requests
import pandas as pd 
import lxml

job = input("Enter job you want to search about : ")
response = requests.get(f"https://wuzzuf.net/search/jobs/?q={job}&a=navbl")
# print(response)

src = response.content
# print(src)

soup = BeautifulSoup(src, "lxml")
# print(soup)

# We need to find 5 elements ==> [job_title, company_name,campany_location, announce_time, job_type, job_skills]:

Job_Details = []

jobs = soup.find_all("div", {"class" :"css-pkv5jc"})
# print(jobs)
# print(len(jobs))

for i in range(len(jobs)):

    # get job_title
    job_title = jobs[i].find("h2", {"class" : "css-m604qf"}).text.strip()
    # print(f"job_title : {job_title}")

    # get company_name
    company_name = jobs[i].find("a", {"class" : "css-17s97q8"}).text.strip()
    # print(f"company_name : {company_name}")


    # get company_loction
    company_location =  jobs[i].find("span", {"class" : "css-5wys0k"}).text.strip()
    # print(f"company_location : {company_location}")

    # get announce_time
    announce_time = jobs[i].find("div", {"class" : ["css-4c4ojb" , "css-do6t5g"]}).text.strip()
    # print(f"announce_time : {announce_time}")

    # get job_type
    # job_type = jobs[i].find("span", {"class" : "css-1ve4b75 eoyjyou0"}).text.strip()
    # print(job_type)

    # get job_skills
    # job_skills = jobs[i].find("div", {"class" : "css-y4udm8"}).contents[1].text.strip()
    # print(job_skills)   

    # get job_description
    job_description = jobs[i].find("div", {"class" :"css-y4udm8"}).text.strip()
    # print(f"job_description : {job_description}")

    # print("=" * 60)

    Job_Details.append({"job_title" : job_title, "company_name" : company_name, "company_location" : company_location, 
                        "announce_time" : announce_time, "job_description" : job_description})

# save information about the job you search into Excel file
jobs = pd.DataFrame.from_dict(Job_Details)
print(jobs.head())
jobs.to_excel(f"{job}.xlsx", index = False)