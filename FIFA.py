import re
import requests
from bs4 import BeautifulSoup as Soup
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# url link is connected to a variable
url = "https://sofifa.com/players?offset="
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


# column = ['ID','picture','Flag','Name','Age','Position','Overall','Potential',
#           'Team_Image','Team','Value','Wage','Total_Point']
# FIFAdata = pd.DataFrame(columns = column)

## List to store_data
player_data  = []


for offset in range(0,2):
    url = url + str(offset*61)
    
    p_html = requests.get(url, headers=headers) #request the url to fetch to link
    
    p_soup = p_html.text #will get the textual html format
    data = Soup(p_soup,'html.parser')
    table = data.find('tbody') #finding the body of the table
    for i in table.findAll('tr'):   # to check entire the table having Table row 
        data_dic = {}   # Crete a Dictonary to keep all the keys and values 
        td = i.findAll('td')
        try:
            data_dic["picture"] = td[0].find('img').get('data-src')   # In Picture Column we are extract the image
        except:
            pass
        try:        
            data_dic["ID"] = td[0].find('img').get('id')  # Get the id of an image
        except:
            pass
        try:

            data_dic["flag"] = td[1].find('img').get('data-src') # Get the Flag for each country for players 
        except:
            pass
        try:        

            data_dic["Name"] = td[1].find("a").text # Name of the players findig all letters
        except:
            pass
        try:        
            
            data_dic["Age"] = td[2].text.split()   # Age to extarct for each playesrs age
        except:
            pass
        try:
            # parse carefully to find right
            pos = td[1].find_all("span")
            totl_pos = ""
            for i in pos:
                totl_pos += f", {i.text}"

            data_dic["Position"] = totl_pos.strip(", ") #Extract the position of the player and remove wide spaces
        except:
            pass
        try:

            data_dic["Overall"] = td[3].find('span').text   #Know the overal Performance of each player
        except:
            pass
        try:        
            data_dic["Potential"] = td[4].find('span').text  # Extract the potential for each
        except:
            pass
        try:        

            data_dic["Team_image"] = td[5].find('img').get('data-src')  # team Iamge can fetch to know persona
        except:
            pass
        try:        
            data_dic["Team"] = td[5].find('a').text  # Know the team Person
        except:
            pass
        try:        
            data_dic["Value"] = td[6].text.strip()#'M'    # Value for each emploeyee
        except:
            pass
        try:        
            data_dic["Wage"] = td[7].text.strip()#'K'   # Wage for each Employee
        except:
            pass
        try:        

            data_dic["Total_Point"] = td[8].text.strip()   # Know the total Poits to eacn Team and individual of the employee
        except:
            pass
        player_data.append(data_dic)   # adding all keys and values to player_data which we created before its an list form.   
        
FIFAdata = pd.DataFrame(player_data) # Convert them into DataFrame using Pandas

print(FIFAdata)