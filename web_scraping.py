from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(url)
soup=bs(page.text,"html.passer")
star_table=soup.find("table")
temp_list=[]
table_rows=star_table[7].find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)
star_names=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=["star_names","distance","mass","radius"])
df.to_csv('dwarf_stars.csv')