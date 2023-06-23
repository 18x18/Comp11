#https://www.youtube.com/watch?v=XVv6mJpFOb0 37:30

from bs4 import BeautifulSoup
import requests
#pip install requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text) # <Response [200]> get rid of it (fix by writing '.text' at the end)
soup = BeautifulSoup(html_text, 'lxml') #ul is unordered list, li is list
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '') #not =find all to bring first element with 'li' #replace to replace ' ' with ''
print(company_name)

