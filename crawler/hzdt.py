from bs4 import BeautifulSoup
import requests

url = 'http://hzdt.ustc.edu.cn/index.php?m=content&c=index&a=lists&catid=12'
urls = ['http://hzdt.ustc.edu.cn/index.php?m=content&c=index&a=lists&catid=12&page={}'.format(str(i)) for i in range(2, 15, 1)]
# get_vacationRentals
def get_pages(url, data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.show-pic-con-list-title > p')
    imgs = soup.select('img[width="188"]')
    times = soup.select('p.show-pic-con-list-time-2')
    # cates = soup.select('li.tag')

    for title, img, time in zip(titles, imgs, times):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'time': time.get_text(),
        }
        print(data)
for single_url in urls:
    get_pages(single_url)
