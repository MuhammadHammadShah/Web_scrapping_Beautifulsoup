from bs4 import BeautifulSoup
import time
import requests
def find_jobs():
    print("put some skills that you are not familiar with")
    unfamiliar_skills = input(">")
    print(f"Unfimiliar Skill : {unfamiliar_skills}")
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text,"lxml")
    jobs = soup.find_all("li",class_ = "clearfix job-bx wht-shd-bx")
    # print(job)
    # for job in jobs:
    for num, job in enumerate(jobs):
        published_date = job.find("span",class_="sim-posted").span.text
        if "few" in published_date:
            company_name = job.find("h3",class_ = "joblist-comp-name").text.replace(" ","")
            # print(company_name)
            skills = job.find("span",class_ = "srp-skills").text.replace(" ",'')
            # print(skills)
            # print(f'''
            # Company Name : {company_name}
            # Required Skill : {skills}
            # ''')
            more_info = job.header.h2.a["href"]
            if unfamiliar_skills not in skills:
                with open (f'posts/{num}',"w") as f:
                        f.write(f"Company Name: {company_name.strip()} \n")
                        f.write(f"Requirement : {skills.strip()} \n")
                        f.write(f"More Info: {more_info}")
                print(f"File Saved {num}")  
                    # print(f"Company Name: {company_name.strip()}")
                    # print(f"Requirement : {skills.strip()}")
                    # print(f"More Info: {more_info}")
                    # print(" ")  
if __name__ == "__main__":
        while True:
            find_jobs()
            time_wait = 10
            print(f"Waiting {time_wait} minutes")
            time.sleep(time_wait*60)