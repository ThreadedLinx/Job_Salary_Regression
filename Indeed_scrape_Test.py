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
#driver.get("https://www.indeed.com/jobs?q=ios%20developer&l=Los%20Angeles")

#Variables

#List Of Pages As Web Elements
pages = []
#List of All Postings that have the salary listed - Emptied Every Loop
job_list_with_salary_listed = []
#Post That Contain these strings have the salary listed
money_matches = ['an hour', '$', 'a year', 'Estimated']
#List of Job Objects That Contains Position, Company, Location, and Salary
job_postings = []

#Functions

#This Function Grabs The Necessary Data From Each Job Listing: Position, Company Name, Location, and Salary
def get_job_info():

    for salary in job_list_with_salary_listed:

        #Job Title
        job_title = salary.find_element(By.CLASS_NAME, "jobTitle")
        print(job_title.text)

        #Company Name
        company_name = salary.find_element(By.CLASS_NAME, "companyName")
        print(company_name.text)

        #Location - Returned From HTML : Will Be From User Input By Their Search C
        location = salary.find_element(By.CLASS_NAME, "companyLocation")
        print(location.text)

        #Float Value for Salary 
        salary_float = 0.0

        #Accessing The Target Elements For Salary Information
        salary_test_three = salary_string = WebDriverWait(salary, 5).until(
        EC.presence_of_element_located((By.XPATH, "*//div[@class='metadata salary-snippet-container' or @class='metadata estimated-salary-container']"))
        )

        #Holds The List of Salary String For Each Position - Emptied Everytime it Loops
        salary_list = []

        #If Salary Info is a Yearly Estimate
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
            salary_float = float_mean

        #If Salary info is Yearly and Not Estimated
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
            float_yearly_mean = ((float_yearly_min + float_yearly_max) / 2) / 1000

            print(float_yearly_mean)
            salary_float = float_yearly_mean 

        #If Salary Info is Hourly
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
            float_hourly_mean_converted_to_yearly = (float_hourly_mean * 40 * 52) / 1000

            print(float_hourly_mean_converted_to_yearly)

            salary_float = float_hourly_mean_converted_to_yearly



        #Creating Dictionary of Job with All Relevant Data
        job_object = {
            'position': job_title.text,
            'company': company_name.text,
            'location': location.text,
            'salary': salary_float
        }

        job_postings.append(job_object)

#This Function Populates job_list_with_salary_listed
def get_jobs_with_salary_listed():

    #Finding Job List
    try:
        job_list = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul'))
        )
        #print('Job List Found')

        #Once Job List Is Found - Create A List Of 'Li' Elements Which Is Each Job Listing On This Job Board Website
        try:
            jobs = job_list.find_elements_by_tag_name('li')
            #print(jobs)

            try: 
                #For Loop to append each listing that contains salary information to the job_with_salary_listed list
                for job in jobs:

                    listing = job.text

                    #Checking if any strings in the listing contain strings in money matches - signifying the salary is present
                    if any(x in listing for x in money_matches):
                        #Appending Job Listing That Matches Criteria To job_with_salary_listed list
                        job_list_with_salary_listed.append(job)
                        #Checking if Length of List is Growing
                        print(len(job_list_with_salary_listed))
            except:
                print('Failed To Loop Through List and Extract Jobs That Contain Salaries')
        except:
            print('Failed To Extract Each Job Element')
    except:
        print('Failed To Find List Of Jobs')

#This Function isnt 'Necessary' - Its a Checkpoint To Make Sure Salary Info Is Listed Before Extraction Of Data Is Performed
def salary_checkpoint():
    #These are the class name identifiers for each type of salary listed
    #x - x an hour --- metadata salary-snippet-container
    # Estimated Salary x - x --- metadata estimated-salary-container
    #$xx - $xx -- metadata salary-snippet-container
    #Stored each in a lisg
    html_list = ['metadata salary-snippet-container', 'metadata estimated-salary-container', 'metadata salary-snippet-container']

    try:

        #print(job_list_with_salary_listed)
        #Checking if Jobs in jobs_list all have a class tag to access the salary data
        for job in job_list_with_salary_listed:

            #print('Inner Html For Job ... ')
            get_html = job.get_attribute('innerHTML')
            #print(get_html)

            #If the inner HTML contains any string from the html_list - The Salary Data will be accessible
            if any(x in get_html for x in html_list):
                #print('Salary Html Is Present')
                pass
            else:
                print('Missing Salary Class')
        
        #Communicate To Console Final Check Is Successful
        print('Data is Present: Continue To Extraction')
    except:
        print('Something Went Wrong: Salary Items Missing')

#This Function Holds All Above Functions And Executes Them In Order
def get_data():
    get_jobs_with_salary_listed()
    salary_checkpoint()
    try:
        get_job_info()
    except:
        print('Data Scrape Failed: Could not Retreive Info')

#This Function Clicks Away From Any PopUp
def avoid_pop_up():
    #Closing Popups If They Exist
    try:
        #Locating 'x' symbol on pop window
        popup_window = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='popover-x-button-close icl-CloseButton']"))
        )
        print('Pop Up Appeared')

        print('Closing Pop Up With Action Chain')

        #Moving Mouse
        #Create action chain object
        action = ActionChains(driver)
        #Moving Mouse Away From Pop Up
        action.move_to_element(popup_window)
        action.click(popup_window)
        action.move_to_element_with_offset(popup_window, 40, 50)
        action.click()
        action.perform()

        print('Pop Up Window Closed')

    except:
        print('No Pop Up, Continue Scraping')


#Get Page Link (i.e. "1", "2", "3", "4") Elements In Global Scope for pages variable
def get_pages():
    try:
        page_count = WebDriverWait(driver, 5).until(
         EC.presence_of_element_located((By.CLASS_NAME, "pagination-list"))
        )
        print('Got page count')

        #Get Each Element and Populate Pages List
        try:
            pages_buttons = page_count.find_elements_by_tag_name("li")
            #pages = pages_buttons
            #print('Success???')
            print(pages)

            return pages_buttons

        except:
            print('Page Link Elements Failed To Be Found or Populated')

    except:
        print('Page UL Failed To Be Found')

#Locate Next Arrow - If Exist Click It and Go To Next Page
def next_page():
    try:
        #clickable arrow
        arrow = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "np"))
        )

        arrow.click()
        print('Going To Next Page')

    except:
        print('This Was The Final Page')

#Go To Search With Designated Search Criteria - Location and Position
def go(city_to_search):
    try:
        driver.get("https://www.indeed.com/jobs?q=" + job_position + "&l=" + city_to_search)
    except:
        print('Getting Webpage for the ' + job_position + ' in ' + city_to_search + ' was unsuccessful')

#Scrape
def scrape():
    for page in pages:

        #List of All Postings that have the salary listed - Emptied Every Loop
        job_list_with_salary_listed = []

        time.sleep(2)
        get_data()
        time.sleep(2)
        next_page()
        avoid_pop_up()

#City and Position Input Prompt - Removing Any Whitespace - Replacing Any Spaces With %20
city_one = input('What The First City Would You Like To Search? ').strip().replace(' ', '%20')
city_two = input('What The Second City Would You Like To Search? ').strip().replace(' ', '%20')
city_three = input('What The Third City Would You Like To Search? ').strip().replace(' ', '%20')
job_position = input('What Position Are You Interested In? ').strip().replace(' ', '%20')

#Making City List From Input
city_list = [city_one, city_two, city_three]

print(city_list)
print(len(city_list))

print(job_position)
print(len(job_position))

#search_string = "https://www.indeed.com/jobs?q=" + job_position + "&l=" + city
#print(search_string)

#driver.get("https://www.indeed.com/jobs?q=" + job_position + "&l=" + city)

#Maximize Window
driver.maximize_window()

#Loop Through Cities and Get Data For The Desired Position
for city in city_list:
    print('Searching for the ' + job_position + 'in ' + city + ' . . .')

    time.sleep(3)
    #Going To Search Url
    go(city)
    #Setting Pages Variable To Returned list Of Page Link Web Elements
    pages = get_pages()
    print('Search Succesful')
    print("\n")
    print('Now Scraping Data For The ' + job_position + ' in' + city + ' . . .')
    #Scraping
    scrape()



# for page in pages:

#     #List of All Postings that have the salary listed - Emptied Every Loop
#     job_list_with_salary_listed = []

#     time.sleep(2)
#     get_data()
#     time.sleep(2)
#     next_page()
#     avoid_pop_up()


#Putting Job Postings List Into Data Frame
df = pd.DataFrame(job_postings)
print(df)




#Do a xpath with class and contains 'Salary' as text
#*//div[contains(@class,'salary')]

#Try Block - Getting all relevant data and storing it in a job dictionary then appending it to the job postings list
# try:
#     #print('Getting By Xpath Contains Text .... ')

#     #This Was A Check To See How To Access The Salary Information
#     # salary_test_one = WebDriverWait(job_list_with_salary_listed[2], 5).until(
#     #     EC.presence_of_element_located((By.XPATH, "*//div[contains(@class,'salary')]"))
#     # )

#     get_data()
# except:
#     print('Xpath Text Contains Failed')





