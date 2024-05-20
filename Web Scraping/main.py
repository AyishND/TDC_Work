from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
print('')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if '1 day' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ',' ')
        skills = job.find('span', class_='srp-skills').text.replace(' ','')
        job_description = job.header.h2.a['href']
        exp_require = job.find('li', class_='').text
        location = job.find('li', class_='')

        print(f'Company Name: {company_name.strip()}')
        print(f'Requied Skills: {skills.strip()}')
        print(f'Job Description: {job_description}')
        print(f'Job Experience: {exp_require.strip('card_travel')}')
        print(f'Location: {location.strip()}')
        print('-------------------------------')
        print('')