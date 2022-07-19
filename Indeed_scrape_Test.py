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

        #Job Title
        job_title = salary.find_element(By.CLASS_NAME, "jobTitle")
        # //*[@span="title"]
        #"*//div[@class='attribute_snippet']"
        print(job_title.text)

        company_name = salary.find_element(By.CLASS_NAME, "companyName")
        print(company_name.text)

        location = salary.find_element(By.CLASS_NAME, "companyLocation")
        print(location.text)

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

            #Index of $ +1 and K Because Tagret Numbers Lie In between these Characters - First Number In Sequence
            sal_min_start = salary_list.index('$') + 1
            sal_min_end = salary_list.index('K')

            print(sal_min_start)
            print(sal_min_end)

            #Slicing Target Number Using Specific Index of $ + 1 and K
            sal_min_list = salary_list[sal_min_start:sal_min_end]

            print(sal_min_list)

            #Joining Min Numbers Into a String
            string_min_string = ''.join(sal_min_list)

            print(string_min_string)
            print(type(string_min_string))

            #Turning String of Min Into a Float
            float_min = float(string_min_string)
            print(float_min)
            print(type(float_min))

            print('Getting Max')

            #Index of $ +1 and K Because Tagret Numbers Lie In between these Characters - Second Number In Sequence
            sal_max_start = salary_list.index('$', 17) + 1
            sal_max_end = salary_list.index('K', 17)

            print(sal_max_start)
            print(sal_max_end)

            #Slicing Target Number Using Specific Index of $ + 1 and K
            sal_max_list = salary_list[sal_max_start:sal_max_end]
            print(sal_max_list)

            #Joining Max Numbers Into A String
            string_max_string = ''.join(sal_max_list)
            
            print(string_max_string)
            print(type(string_max_string))

            #Turning String Of Max Into A Float
            float_max = float(string_max_string)
            print(float_max)
            print(type(float_max))


            #Getting The Mean Of The Salary Range
            float_mean = (float_max + float_min) / 2

            print(float_mean)

        elif "Estimated" not in salary_test_three.text and "a year" in salary_test_three.text:

            print('This Is A Year String Only')
            print(salary_test_three.text)

            for word in salary_test_three.text:
                salary_list.append(word)
            print(salary_list)

            #Index of $ +1 and *Space* Because Tagret Numbers Lie In between these Characters - First Number In Sequence
            year_salary_min_start = salary_list.index('$') + 1
            year_salary_min_end = salary_list.index(' ')

            print(year_salary_min_start)
            print(year_salary_min_end)

            #Slicing Target Number Using Specific Index of $ + 1 and *Space*
            year_sal_min_list = salary_list[year_salary_min_start:year_salary_min_end]
            print(year_sal_min_list)

            #Removing Comma From List
            year_sal_min_list.remove(',')
            print(year_sal_min_list)

            #Joining Min Numbers Into A String
            string_year_min = ''.join(year_sal_min_list)
            
            print(string_year_min)
            print(type(string_year_min))

            #Turning Minimum Salary String Into A Float
            float_yearly_min = float(string_year_min)
            print(float_yearly_min)
            print(type(float_yearly_min))


            print('Now Getting Max Value ...')
            #Index of $ +1 and *Space* Starting At Specific Index Because Tagret Numbers Lie In between these Characters - Second Number In Sequence
            yearly_max_start = salary_list.index('$', 9) + 1
            yearly_max_end = salary_list.index('a', 9) - 1

            print(yearly_max_start)
            print(yearly_max_end)

            #Slicing Target Number Using Specific Index of $ + 1 and 'a' - 1
            year_sal_max_list = salary_list[yearly_max_start:yearly_max_end]
            print(year_sal_max_list)

            #Removing Comma
            year_sal_max_list.remove(',')

            #Joining Max Numbers Into A String
            string_year_max = ''.join(year_sal_max_list)

            print(string_year_max)
            print(type(string_year_max))

            #Turning Maximum Salary String Into A Float
            float_yearly_max = float(string_year_max)
            print(float_yearly_max)
            print(type(float_yearly_max))

            #Getting Mean of Salary Range
            float_yearly_mean = (float_yearly_min + float_yearly_max) / 2

            print(float_yearly_mean)

        else:
            print(salary_test_three.text)
            print('Should Be By The Hour')

            for word in salary_test_three.text:
                salary_list.append(word)
            print(salary_list)

            #Index of $ + 1 and '-' minus 1
            hourly_min_start = salary_list.index('$') + 1
            hourly_min_end = salary_list.index('-') - 1
            print(hourly_min_start)
            print(hourly_min_end)

            #Slicing Target Number Using Specifc Index of $ + 1 and '-' Minus 1
            hourly_salary_min_list = salary_list[hourly_min_start:hourly_min_end]
            print(hourly_salary_min_list)

            #Joining Numbers Into A String
            hourly_sal_min_string = ''.join(hourly_salary_min_list)

            print(hourly_sal_min_string)
            print(type(hourly_sal_min_string))

            #Turning Min Salary String Into A Float
            float_hourly_min = float(hourly_sal_min_string)

            print(float_hourly_min)
            print(type(float_hourly_min))

            #Getting Max Hourly Value
            print('Now Getting Hourly Max Value')

            #Index Of $ + 1 and 'a' minus 1 Starting At Specific Index Because Tagret Numbers Lie In between these Characters - Second Number In Sequence
            hourly_max_start = salary_list.index('$', 4) + 1
            hourly_max_end = salary_list.index('a', 4) - 1
            
            print(hourly_max_start)
            print(hourly_max_end)

            #Slicing Target Number Using Specifc Index Of $ + 1 and 'a' minus 1
            hourly_sal_max_list = salary_list[hourly_max_start:hourly_max_end]
            print(hourly_sal_max_list)

            #Joing Max Number Into A String
            hourly_sal_max_string = ''.join(hourly_sal_max_list)

            print(hourly_sal_max_string)
            print(type(hourly_sal_max_string))

            #Turning Max Hourly Salary String Into A Float
            float_hourly_max = float(hourly_sal_max_string)
            print(float_hourly_max)
            print(type(float_hourly_max))

            #Getting Mean of Hourly Salary Range
            float_hourly_mean = (float_hourly_min + float_hourly_max) / 2
            print(float_hourly_mean)

            #Converting Hourly Mean To Yearly Salary
            float_hourly_mean_converted_to_yearly = float_hourly_mean * 40 * 52

            print(float_hourly_mean_converted_to_yearly)














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

