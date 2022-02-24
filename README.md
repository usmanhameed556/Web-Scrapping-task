## Web_Scrapping-Task



## Description:

The code will scrap the data which has been asked e.g. hotel name , reviews, stars etc given to the hotel.

To perform the task I used BeautifulSoup Python library as it is mostly used for this purpose.

At the end all the details are saved in JSON as asked is the task

The current code is unit tested, although there is a possibility to add more complex test cases

## Running the Project:

Visual studio code is used as IDE to implement the code. The code can run and the output will be stored in JSON file.

Individually I checked by printing whether I am getting the required data and then at the end transferred it to JSON file

## How to Use:

- The Url link for the hotel data you want to extract is passed from booking.com 
- Download the project files along with the json and app.py.
- Run the code via visual studio code or alternatively you can run via command line.
- The app.py will run by listening or request to the endpoint URL, requesting the response contains HTML, response header and response data. 
- Next, I check whether the API endpoint is working.
- Next, I use BeautifulSoap to scrape the data (i.e. text) from the website using span and id.
- Next, I save all the data into JSON format and dump into JSON file called hotel_data.json   
- Followed by various test-cases to test the URL working and variable in which data is required and mentioned in the file.
