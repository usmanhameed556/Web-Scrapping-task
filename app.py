
# Importing Libraries 
import json 
from bs4 import BeautifulSoup
import requests
import json
import lxml
import unittest


class WebScraping(unittest.TestCase):

    # Web URL for scrapping 
    url = "https://www.booking.com/hotel/de/kempinskibristolberlin.en-gb.html?aid=356980;label=gog235jc-1DCAsoO0IWa2VtcGluc2tpYnJpc3RvbGJlcmxpbkgzWANoO4gBAZgBCbgBF8gBDNgBA-gBAYgCAagCA7gCw9z-jwbAAgHSAiQzYzc5YjdiZC1kZTFhLTQ3OTAtOWMwYi1hMDFiNWE4MWEyZjjYAgTgAgE;sid=be6a1c5a75082bf10b0d1baa40302593;dist=0&group_adults=2&keep_landing=1&sb_price_type=total&type=total&"


    try: 
        response = requests.get(url)
        response.raise_for_status()
        response = response.text
        # Code here will only run if the request is successful
    except requests.exceptions.HTTPError as error:
        print(error)
    except requests.ConnectionError as error:
        print(error)
    except requests.Timeout as error:
        print(error)

    soup = BeautifulSoup(response, 'lxml')

    # Extraction Mechanism

    hotel_name = soup.find('h2', class_="hp__hotel-name").get_text().split("\n")[2]
    hotel_address = soup.find('span', class_="hp_address_subtitle").text.split('\n')[1]
    description = soup.find('div', id="property_description_content").text.split('\n')[1:-1]
    review_rating = soup.find('div', class_="_9c5f726ff bd528f9ea6").text
    reviews = int(float("".join(soup.find('div', class_="_4abc4c3d5 _1e6021d2f _6e869d6e0").text.split()[0].split(","))))
    print("reviews =  {} type = {}".format(reviews, type(reviews)))
    alt_hotels = soup.find_all(name="ul", class_="bui-carousel__inner")

    stars = 0
    for span in soup.find_all('span', class_= "_3ae5d40db _617879812 _6ab38b430"):
        stars+=1
    categories = []
    for item in soup.find_all('a', class_="jqrt togglelink"):
        category = item.get_text().split("\n")[2]
        categories.append(category)


    # ------------- Converting into Json File --------------------- 
    dataDictionary = {
        "Hotel Name":hotel_name,
        "Hotel Address": hotel_address,
        "Stars/Classifications": stars,
        "Review Points": review_rating, 
        "Number of Reviews": reviews,
        "Description": description,
        "Room Categories": categories,    
    } 


    with open("hotel_data.json", "w") as outfile:
        json.dump(dataDictionary, outfile, indent=4)


    def test_url_check(self, url=url):
        response = requests.get(url)
        status_code = 200
        message = "the request was not successful"
        self.assertEqual(response.status_code, status_code, message)
    
    def testCheckHotelnstance(self, hotel_name=hotel_name):
        self.assertTrue(type(hotel_name) == str)

    def test_check_hotel_instance(self, hotel_address=hotel_address):
        self.assertTrue(type(hotel_address) == str)
    
    def test_check_hotel_address(self, hotel_address=hotel_address):
        self.assertFalse(not hotel_address)

    def test_check_reviews_number(self, stars=stars):
        count = True if stars <= 5 else False
        self.assertTrue(count)


if __name__ == "__main__":
    unittest.main()
