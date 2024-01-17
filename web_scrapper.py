import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
months=["0"+str(i) for i in range(1,10)]
months.extend(['10','11','12'])

##section to gather the data for all the months
table0=[]

for month in months:
    url= "https://www.estesparkweather.net/archive_reports.php?date=2023"+month
    response = requests.get(url)
    print(response)
    soup=BeautifulSoup(response.text,'html.parser')
    div=soup.find('div',{"id":"main-copy"})
    table0.append(div.find_all('table'))
table=[]

##Section to extract the data from the website html and put them into assorted lists
for j in table0:
    hi=[]
    lo=[]
    for i in j[:len(j)-1]:
        f=i.find_all('td')[2::2]
        g=f[10:12]
        if len(g)!=2:
            continue
        g[0]=g[0].text
        s=""
        for k in g[0]:
            if k in "-.0987654321":
                s+=k
            if k in "0987654321" and "." in s:
                break
        g[0]=float(s)
        g[1]=g[1].text
        s=""
        for k in g[1]:
            if k in "-.0987654321":
                s+=k
            if k in "0987654321" and "." in s:
                break
        g[1]=float(s)

        hi.append(g[0])
        lo.append(g[1])
    table.append([hi[:-1],lo[0:-1]])
    
    
    
##Section to show the lists generated for the year
    
for i in range(len(table)):
    m=table[i]
    print(i)
    print(m)
    


#### Plotting Section
