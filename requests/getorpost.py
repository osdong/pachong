import requests


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
url="https://umbra.nascom.nasa.gov/cgi-bin/eit-catalog.cgi"
values = {'obs_year':'2018','obs_month':'March',
                             'obs_day':'8','start_year':'2011'
                             ,'start_month':'March','start_day':'8'
                             ,'start_hour':'All Hours','stop_year':'2011'
                             ,'stop_month':'March','stop_day':'8'
                             ,'stop_hour':'All Hours','xsize':'All'
                             ,'ysize':'All','wave':'all'
                             ,'filter':'all','object':'all'
                             ,'xbin':'all','ybin':'all'
                             ,'highc':'all'}
req=requests.post(url,headers=headers)
print req.text.encode("utf-8")