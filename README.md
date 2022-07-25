# Job Salary Data Scrape
Web Scrape and Clean Salary Data From Popular Job Board Site Based On User Input

This Project Is Broken Into 4 Parts:
1. Getting User Input
2. Collecting Salary Data
3. Cleaning & Structuring Data
4. Save Data In Excel and CSV for Easy Data Science Techniques I.E. Linear Regression


# User Input
User Inputs The City and Job Position They Are Interested In - Prompted By Terminal

![Screen Shot 2022-07-25 at 9 48 50 AM](https://user-images.githubusercontent.com/108707233/180871621-a335fa32-a203-402f-bc60-ce0c8274f4c0.png)
![Screen Shot 2022-07-25 at 9 49 52 AM](https://user-images.githubusercontent.com/108707233/180871700-c33f66a1-18a1-4f36-b834-3bb7e6004348.png)
![Screen Shot 2022-07-25 at 9 50 08 AM](https://user-images.githubusercontent.com/108707233/180871774-9c39f040-d330-4ab9-a289-06632e9caf03.png)


# Collecting Salary Data
Program Searches Job Board By Each City For Input Job Position

<img width="1673" alt="Screen Shot 2022-07-25 at 9 53 49 AM" src="https://user-images.githubusercontent.com/108707233/180872169-c7d751d1-0e7a-46d1-a2d1-14202558c9d7.png">

<img width="1677" alt="Screen Shot 2022-07-25 at 9 51 56 AM" src="https://user-images.githubusercontent.com/108707233/180872185-74237019-80b8-4521-aa7d-53fba4775010.png">


# Data Structured In Pandas DataFrame
* Position = Exact Job Title From Company
* Input Position = Searched Job Position - Input From User
* Company = Company Name
* Location = Exact Location of Job
* Input City = Searched City - Input From User
* Salary = Yearly Salary in Demonations of One Thousand - 120.00 is $120,000

![Screen Shot 2022-07-25 at 10 10 43 AM](https://user-images.githubusercontent.com/108707233/180872902-62dad7b3-41fc-47d8-bef3-46425eeccedf.png)


# Saving Data To CSV and Excel Spreadsheet
_*_Note:_*_ 
* When Using This Code, Change Filepath To Where You Want To Save It On Your Local Machine
* Filename Structure: 'job position' in 'city one' _ 'city two' _ 'city three'
* --- Spaces replaced with '%20'

_*_CSV_*_
<img width="801" alt="Screen Shot 2022-07-25 at 9 58 24 AM" src="https://user-images.githubusercontent.com/108707233/180874264-ecbe244e-7d76-42f2-a586-f0ceb1ba501f.png">

_*_Excel_*_
<img width="797" alt="Screen Shot 2022-07-25 at 9 58 32 AM" src="https://user-images.githubusercontent.com/108707233/180873616-2ebca7d1-c79d-4cc9-baa0-d719b06bff38.png">

_*_Easily Uploaded Into Google Sheets_*_
<img width="1623" alt="Screen Shot 2022-07-25 at 10 00 08 AM" src="https://user-images.githubusercontent.com/108707233/180874332-09fb544f-f38c-483b-a89a-f255c75bfc8e.png">

<img width="1043" alt="Screen Shot 2022-07-25 at 10 00 19 AM" src="https://user-images.githubusercontent.com/108707233/180874362-84fe1942-e764-4183-8b0c-0ceb02f2ace2.png">

<img width="670" alt="Screen Shot 2022-07-25 at 10 00 40 AM" src="https://user-images.githubusercontent.com/108707233/180874380-a47c8151-31ff-4595-a874-261575cd183c.png">

<img width="521" alt="Screen Shot 2022-07-25 at 10 01 01 AM" src="https://user-images.githubusercontent.com/108707233/180874409-21902155-09cf-4366-8e2e-c7a67ef59696.png">

<img width="1623" alt="Screen Shot 2022-07-25 at 10 02 47 AM" src="https://user-images.githubusercontent.com/108707233/180874439-ba7035b2-cd76-44fc-9621-db20f8fa6741.png">

  # Foot Notes
  The Data is Collected From 'Indeed.com' Which Is An Online Job Board Similar To ZipRecruiter, SimplyHired, and 
  FlexJobs.
  
  To Collect the Data Im Using Python and Selenium on a Mac (But This Will Also Work On A Windows Operating System)
  
  The 'Input' Prompt Will Ask The User For The Desired Position and Which Cities They Are Interested In Comparing
  
  Selenium Will Search The Desired Position in The Desired Cities, and Only Pull Data From The Job Listings That    
  Have Salary Data Listed
  
  
  
