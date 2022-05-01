import csv
import requests
from bs4 import BeautifulSoup
import  openpyxl  as  op
import re



def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    html = res.text

    soup = BeautifulSoup(res.text, "lxml")
    bs = BeautifulSoup(html, 'html.parser')

    return soup

##NA##
ixic ="https://kr.investing.com/indices/nasdaq-composite"
spx ="https://kr.investing.com/indices/us-spx-500"
dji ="https://kr.investing.com/indices/us-30"

##Germany, UK, Canada##
dax = "https://kr.investing.com/indices/germany-30"
ftse = "https://kr.investing.com/indices/uk-100"
gsptse = "https://kr.investing.com/indices/s-p-tsx-composite"

##Asia##
ssec = "https://kr.investing.com/indices/shanghai-composite"
szse = "https://kr.investing.com/indices/szse-component"
hsi = "https://kr.investing.com/indices/hang-sen-40"
n225 = "https://kr.investing.com/indices/japan-ni225"

##Korea##
ks11 = "https://kr.investing.com/indices/kospi"
kq11 = "https://kr.investing.com/indices/kosdaq"

def index(url):
    try:
        print("index : ")

        soup = create_soup(url)
        index = soup.find("span", {"class":"text-2xl"}).get_text()
        index_p = soup.find("span", {"class":"instrument-price_change-percent__19cas ml-2.5 text-positive-main"}).get_text()
        
        if not index_p:
            index_p = soup.find("span", {"class":"instrument-price_change-percent__19cas ml-2.5 text-negative-main"}).get_text()
        
        index_p = index_p[1:-1]

        print(index)
        print(index_p)

    except Exception as  e:
        print(e)

usd = "https://kr.investing.com/currencies/usd-krw"
eur = "https://kr.investing.com/currencies/eur-krw"
jpy = "https://kr.investing.com/currencies/jpy-krw"
wti = "https://kr.investing.com/commodities/crude-oil"
gold_f = "https://kr.investing.com/commodities/gold"
bdi = "https://kr.investing.com/indices/baltic-dry"
vix = "https://kr.investing.com/indices/volatility-s-p-500"
ksv = "https://kr.investing.com/indices/kospi-volatility"

def money(url):
    try:
        print("money : ")

        soup = create_soup(url)
        money = soup.find("span", {"data-test":"instrument-price-last"}).get_text()
        
        print(money)

    except Exception as  e:
        print(e)

##etf
kodex=[0,0,0,0]
kodex[0]="https://kr.investing.com/etfs/samsung-kodex-leverage"
kodex[1]="https://kr.investing.com/etfs/samsung-kodex-inverse"
kodex[2]="https://kr.investing.com/etfs/samsung-kodex-ksdq150-lev"
kodex[3]="https://kr.investing.com/etfs/samsung-kodex-kosdaq150-inverse"

##bond
us10bond="https://kr.investing.com/rates-bonds/u.s.-10-year-bond-yield"
kr10bond="https://kr.investing.com/rates-bonds/south-korea-10-year-bond-yield"

def etf(url):
    try:
        print("etf : ")

        soup = create_soup(url)
        etf=[0,0,0,0]
        num=["953502","953498","1055084","1095948"]
        
            #etf[i] = soup.find("span", {"class":"arial_26 inlineblock pid-"+num[i]+"-last"})
        etf = soup.select('#last_last')[0]
        etf = re.findall(r'\d+',str(etf))
        etf = etf[2]+etf[3]   

        print(etf)

        

    except Exception as  e:
        print(e)


event1="https://kr.investing.com/economic-calendar/"

def event(url):
    try:
        print("event : ")

        soup = create_soup(url)
        calendar = soup.find("table", attrs = {"id":"economicCalendarData"}).find_all("td")
        for index, star in enumerate(calendar):
            star = soup.find("td", {"title":"높은 변동성이 예상됨"}).string

            if star:
                event = soup.find("a", {"target":"_blank"})


                print(event)

    except Exception as  e:
        print(e)


#event(event1)

index(ixic)
#money(gold_f)
#etf(kodex[3])
#etf(us10bond)
#money(ksv)




#if __name__ == "__main__":
#    money()
#    index()