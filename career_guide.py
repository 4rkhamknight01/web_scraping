from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://in.indeed.com/")
#chromedriver to get site running

job_what = browser.find_element_by_id("text-input-what")
#input job title
job = input("job title")
#input of job title in website
job_what.send_keys(job)
job_where = browser.find_element_by_id("text-input-where") #location
where = input("location")
job_where.send_keys(where)

submit_button = browser.find_element_by_class_name("yosegi-InlineWhatWhere-primaryButton")
submit_button.click()
#finding and clicking the submit button

#appending job title, company name and location to array
title = []
jobs = browser.find_elements_by_class_name("jobTitle")

for i in jobs:
    title.append(i.text)

name = []

comp = browser.find_elements_by_class_name("companyName")

for i in comp:
    name.append(i.text)


location = []

loc = browser.find_elements_by_class_name("companyLocation")

for i in loc:
    location.append(i.text)

# k = len(location)
#
# for i in range(0, k):
#     print(location[i])

col = ["Title", "Company", "Location"]
df = pd.DataFrame({"Title":title, "Company":name, "Location":location})

df.to_csv("indeed_scraping.csv")

#just expand the csv file a bit you will see all the relevant info




