from bs4 import BeautifulSoup
import requests

url = 'https://www.tripadvisor.com/Travel_Guide-g60763-New_York_City_New_York.html'

# get_vacationRentals
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select('h2.title')
imgs = soup.select('div.photo')
cates = soup.select('li.tag')

for title, img, cate in zip(titles, imgs, cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': list(cate.stripped_strings),
    }
    print(data)
