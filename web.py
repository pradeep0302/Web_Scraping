import requests
from bs4 import BeautifulSoup


familar_skill=input("Enter the skill that you are familar in comma seperated: ")
fs=[] 
fs=familar_skill.split(',')
print("filitering out fimilar skill")


def find_jobs():    
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    jobs = soup.find_all("li",class_ ='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span',class_="sim-posted").span.text
        if 'few' in published_date:
            company_name= soup.find("h3",class_="joblist-comp-name").text.replace('  ','')
            skills = job.find('span',class_="srp-skills").text.replace('  ','')
            more_info=job.header.h2.a['href']
            for i in fs:
                if i in skills:
                    
                    print("company name: ",company_name.strip())
                    print("Skills required: ",skills.strip())
                    print("more info:",more_info)
                
        print("")
    
    

find_jobs()
  