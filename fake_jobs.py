import requests
import pandas

from bs4 import BeautifulSoup

def get_jobs(soup,limit=10):
    list_=[]
    jobs = soup.find_all('h2',class_='title',limit=limit)
    for item in jobs:
        list_.append(item.text)
    return list_

def get_companys(soup,limit=10):
    list_=[]
    companys = soup.find_all('h3',class_='company',limit=limit)
    for item in companys:
        list_.append(item.text)
    return list_

def get_locations(soup,limit=10):
    list_=[]
    locations = soup.find_all('p',class_='location',limit=limit)
    for item in locations:
        list_.append(item.text.replace('  ','').replace('\n',''))
    return list_

def get_dates(soup,limit=10):
    list_=[]
    dates = soup.find_all('time',limit=limit)
    for item in dates:
        list_.append(item.text)
    return list_

def get_links(soup,limit=10):
    list_=[]
    links = soup.find_all('footer',class_='card-footer',limit=limit)
    for item in links:
        list_.append(item.findChildren()[1]['href'])
    return list_

def main():
    url = 'https://realpython.github.io/fake-jobs/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    data = {
        'job': get_jobs(soup),
        'company': get_companys(soup),
        'location': get_locations(soup),
        'date': get_dates(soup),
        'link': get_links(soup)
    }

    df = pandas.DataFrame(data)
    df.to_csv('resources/export/fake_jobs.csv',index=False)

if __name__ == '__main__':
    main()