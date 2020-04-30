from bs4 import BeautifulSoup as soup
import requests


my_url = 'https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_4&otracker1=AS_QueryStore_OrganicAutoSuggest_0_4&as-pos=0&as-type=RECENT&as-backfill=on'


response = requests.get(url)

page_soup = soup(response.text,"html.parser")


containers = page_soup.findAll("div", {"class":"_3O0U0u"})
print(len(containers))
print(soup.prettify(containers[0]))

container = containers[0]
print(container.div.img["alt"])
 
price = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
print(price[0].text)
 
ratings = container.findAll("div",{"class":"niH0FQ"})
print (ratings[0].text)

filename = "Scrappeddata.csv"
f = open(filename,"w")
 
headers = "Products_Name, Pricing , Ratings\n"
f.write(headers)

for container in containers:
     product_name = container.div.img["alt"]
     price_container = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
     price = price_container[0].text.strip()
     rating_container = container.findAll("div",{"class":"niH0FQ"}) 
     rating = rating_container[0].text
     print("product_name:" + product_name)
     #print("price:" + price) 
     #print("ratings:" + rating)

     trim_price = ''.join(price.split(','))
     rm_rupee = trim_price.split("₹") 
     add_rs_price = "Rs." + rm_rupee[1] 
     split_price = add_rs_price.split('E')  
     final_price = split_price[0]
    
     split_rating = rating.split(" ")
     final_rating = split_rating[0]
     #print(product_name.replace(",","|") + "," + final_price + "," +  final_rating + "\n")
     f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
 
f.close()
