# Web scrapper using BeautifulSoup4 
import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="enter no, of pages to parse", type=int)
parser.add_argument("--dbname", help="enter the name of dc",type=str)
arge=parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX = args.page_num_max
scrappes_info_list = []
connect.connect(args.dbname)

for page_num in range(1, page_num_MAX):
    url = oyo_url+str(page_num)
    print("Get request for:"+url)
    req = requests.get(oyo.url+str(page_num))
    content = req.content

    soup=BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div", {"class", "hotelCardListing"})
    scrapped_info_list = []
    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span",{"itemprop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span",{"class":"listingPrice__finalPrice"}).text
        #try......except
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            pass

        parent_amenities_element = hotel.find("div", {"class": "amenityWrappee"})

        amenities_list = []
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
                              amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())

        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])

        scrapped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))

dataFrame = pandas.dataFrame(scrapped_info_list)
print("Creating csv file....")
dataFrame.to_csv("oyo.csv")
connect.get_hotel_info(args.dbname)
