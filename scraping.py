import requests 
from bs4 import BeautifulSoup 
import time
import re
import os
def getdata(url): 
    r = requests.get(url)
    return r.text 

carCat={"Toyota Prius":["/vehicle/2583782","/vehicle/2496145","/vehicle/2542016","/vehicle/2509242","/vehicle/2450458"],
        "Hyundai Accent":["/vehicle/2513630","/vehicle/2551954","/vehicle/2486009","/vehicle/2557279","/vehicle/2365008"],
        "Honda Civic":["/vehicle/2508556","/vehicle/2555096","/vehicle/2564580","/vehicle/2495306","/vehicle/2496222"],
        "Dodge Challenger":["/vehicle/2595098","/vehicle/2519380","/vehicle/2431889","/vehicle/2516708","/vehicle/2510479"],
        "Ford Mustang":["/vehicle/2582184","/vehicle/2524709","/vehicle/2455758","/vehicle/2524709","/vehicle/2542815"],
        "Tesla Model Y":["/vehicle/2455613","/vehicle/2519315","/vehicle/2427195","/vehicle/2456302","/vehicle/2550407"],
        "Toyota Camry":["/vehicle/2481286","/vehicle/2485884","/vehicle/2590222","/vehicle/2516288","/vehicle/2486178"],
        "Honda CR-V":["/vehicle/2489713","/vehicle/2533662","/vehicle/2414775","/vehicle/2584937","/vehicle/2457447"],
        "Audi A5":["/vehicle/2433004","/vehicle/2509994","/vehicle/2565949","/vehicle/2431696","/vehicle/2576868"]}



template=["mosaic_1920-2-80-1.jpg","mosaic_1920-2-80-0.jpg"]
BasePath="dataset/"
BaseUrl="https://www.carvana.com"


for dir,siteAr in carCat.items():
    print(dir)
    a=os.listdir(BasePath)
    if dir not in a:
        os.mkdir(BasePath+dir)
    ctr=0
    path=BasePath+dir+"/"
    for car in siteAr:
        link= BaseUrl + car
        htmldata = getdata(link)
        soup = BeautifulSoup(htmldata, 'html.parser')
        x="SPIN_VIDEO_FLOOR_CLEANER"
        for item in soup.find_all('img'):
            url=item["src"]
            if x in url:
                loc=url.find(x)+len(x)+1
                baseUrl=url[:loc]
                for i in template:
                    u=baseUrl+i
                    print(u)
                    img_data = requests.get(u,stream=True).content
                    with open(f'{path}{ctr}.jpg', 'wb') as handler:
                        handler.write(img_data)
                    print(ctr)
                    ctr+=1
                break
        time.sleep(5)