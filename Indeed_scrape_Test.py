from cgitb import html
import string
from turtle import pos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

#Path Name Of Chrome Driver
PATH = "/Users/nay/Desktop/Development/Drivers/chromedriver"

#Selecting The webdriver / broswer 

driver = webdriver.Chrome(PATH)
driver.maximize_window()


#Going To Website
driver.get("https://www.indeed.com/jobs?q=ios%20developer&l=Los%20Angeles")

# jobsearch-ResultsList css-0


#Finding Job List
try:
    job_list = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul'))
    )

    #print('Job List Found')

except:
    print('Couldnt Find List Of Jobs')



try:
    jobs = job_list.find_elements_by_tag_name('li')
    #print(jobs)
except:
    print('No salary Found')

money_matches = ['an hour', '$', 'a year', 'Estimated']

job_list_with_salary_listed = []

for job in jobs:

    listing = job.text

    if any(x in listing for x in money_matches):

        #print('This listing has salary listed')
        #print(listing)
        job_list_with_salary_listed.append(job)
        print(len(job_list_with_salary_listed))

#x - x an hour --- metadata salary-snippet-container
# Estimated Salary x - x --- metadata estimated-salary-container
#$xx - $xx -- metadata salary-snippet-container

html_list = ['metadata salary-snippet-container', 'metadata estimated-salary-container', 'metadata salary-snippet-container']


try:

    print(job_list_with_salary_listed)

    for job in job_list_with_salary_listed:

        print('Inner Html For Job ... ')
        get_html = job.get_attribute('innerHTML')
        #print(get_html)

        if any(x in get_html for x in html_list):
            print('Salary Html Is Present')
        else:
            print('Missing Class')


except:
    print('Something Went Wrong')


#Do a xpath with class and contains 'Salary' as text
#*//div[contains(@class,'salary')]

salary_section = []

try:
    print('Getting By Xpath Contains Text .... ')

    salary_test_one = WebDriverWait(job_list_with_salary_listed[2], 5).until(
        EC.presence_of_element_located((By.XPATH, "*//div[contains(@class,'salary')]"))
    )
    print('Salary Retreived')
    
    #//input[@value = 'Log In' or @type = 'submit']

    print(salary_test_one.text)

    for salary in job_list_with_salary_listed:

        salary_test_three = salary_string = WebDriverWait(salary, 5).until(
        EC.presence_of_element_located((By.XPATH, "*//div[@class='metadata salary-snippet-container' or @class='metadata estimated-salary-container']"))
        )

        salary_list = []

        if "Estimated" in salary_test_three.text and "a year" in salary_test_three.text:
            print('Estimated Yearly String')
            print(salary_test_three.text)
            for word in salary_test_three.text:
                salary_list.append(word)
            print(salary_list)


        # elif "a year" in salary_test_three.text:
        #     print('Yearly Salary Range String')
        # elif 'an hour' in salary_test_three.text:
        #     print('Hourly Salary String')

        #print(salary_test_three.text)

    #     salary_test_two = WebDriverWait(job, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "*//div[contains(@class,'salary')]"))
    # )
    #     print(salary_test_two.text)
    #     salary_section.append(salary_test_two)
    #     print('Success, Element Appended')


    # print(len(salary_section))
    # print(salary_section[0].text)


    # for salary in salary_section:

    #     salary_string = WebDriverWait(salary, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "*//div[@class='attribute_snippet']"))
    # )

    #     print(salary_string.text)
    #     #print('Working Fine ... ')



# estimated-salary
# attribute_snippet

    #print(job_list_with_salary_listed[0].text)

    # for x in job_list_with_salary_listed:

    #     salary_in_html = x.find_element_by_xpath("*//div[contains(@class,'salary')]")

    #     print(salary_in_html.text)


except:
    print('Xpath Text Contains Failed')


#an hour
#$
#a year
#Estimated

# try:
#     salary = jobs[0].find_element_by_class_name('metadata salary-snippet-container')

#     print('Salary Found')

# except NoSuchElementException:
#     print('Element Doesnt Exist')



# for job in jobs:

#     if job.find_element_by_class_name('metadata salary-snippet-container') == True:
#         continue


#     print(job.find_element_by_class_name('metadata salary-snippet-container').text)





#metadata salary-snippet-container


# for job in job_list:


#     if job.find_element_by_class_name('metadata salary-snippet-container') == True:
#         continue

#         print(job.find_element_by_class_name('metadata salary-snippet-container').text)

