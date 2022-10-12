import requests
from bs4 import BeautifulSoup

def get_prices(soup, limit = 3):
    p_list = []
    p_whole = soup.find_all('span',class_='a-price-whole',limit=limit)
    p_fraction = soup.find_all('span',class_='a-price-fraction',limit=limit)
    for i in range(limit):
        p_list.append(p_whole[i].text + p_fraction[i].text) 
    return  p_list

def get_titles(soup, limit = 3):
    t_list = []
    titles = soup.find_all('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal',limit=limit)
    for item in titles:
        t_list.append(item.text)
    return  t_list

def get_urls(soup, limit = 3):
    u_list = []
    urls = soup.find_all('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal',limit=limit)
    for item in urls:
        u_list.append(item['href'])
    return  u_list

def main():
    headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'personal@domain.com'
    }
    r = requests.get('https://www.amazon.com/s?k=iphone',headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    prices = get_prices(soup)
    titles = get_titles(soup)
    urls = get_urls(soup)
    for i in prices:
        print(i)
    for i in titles:
        print(i)
    for i in urls:
        print('https://amazon.com'+i)

if __name__ == '__main__':
    main()