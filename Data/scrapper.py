from bs4 import BeautifulSoup
import requests
import csv
import datetime

ans1=[]
ans2=[]

y=2015
for n in range(3):
    y+=1
    response=requests.get('https://www.poundsterlinglive.com/bank-of-england-spot/historical-spot-exchange-rates/usd/USD-to-INR-'+str(y)).text
    soup=BeautifulSoup(response,'lxml')
    table=soup.find('table',class_="curlist")
    rows=table.findAll('tr')
    l1=[]
    l2=[]
    for i in range(len(rows)):
        cols=rows[i].findAll('td')
        try:
            l1.append(cols[0].text)
            l2.append(cols[1].text)
        except:
            continue

    finall1=[]
    finall2=[]
    for i in range(len(l1)):
        a=l1[i].split(", ")
        if(len(a)==2):
            finall1.append(a[1])
        try:
            finall2.append(l2[i].split(" ")[3])
        except:
            continue

    finall1.reverse()
    finall2.reverse()
    
    l1=[]
    for i in range(len(finall1)):
        date_str =  finall1[i]
        format_str = '%d %b %Y ' 
        datetime_obj = datetime.datetime.strptime(date_str, format_str)
        l1.append(datetime_obj.date())
        
    ans1+=l1
    ans2+=finall2

file=open('scrape.csv','w')

csv_writer=csv.writer(file)
csv_writer.writerow(['date','rupee'])

for i in range(len(ans1)):
    csv_writer.writerow([ans1[i],ans2[i]])

file.close()

