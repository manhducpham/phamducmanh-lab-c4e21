# 1.1 Open connection to page
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'https://dantri.com.vn'
conn = urlopen(url)

# 1.2 Read data
raw_data = conn.read()

# 1.3 Decode data
html_page = raw_data.decode('utf-8')

# print(html_page)
# 1.4 Save data to file
# 1.4.1 Open connection to file
# f_conn = open('dantri.html', 'wb') # w means write, wb means write binary or raw data

# # 1.4.2 Write data
# f_conn.write(raw_data)

# # 1.4.3 Close connection
# f_conn.close()
# print('done')
# co data moi thi moi build lai.

soup = BeautifulSoup(html_page, 'html.parser')
# print(soup.prettify())
ul = soup.find('ul', 'ul1 ulnew') #class thi khong can dien thong tin nhu href... sau nay thi tim id = 'tbl_grade'
# print(ul.prettify())

# 3. Extract Data
li_list = ul.find_all('li')
# li = li_list[0] # thu de scale
# # h4 = li.find('h4', '') #cach cu
# a = li.h4.a
# # print(a.prettify())
# title = a.string
# # print(title)
# link = url + a['href']
# # print(link)
# print(title, link) #thua / thi xoa o tren url

news_list = []

for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a['href']
    news = {
        'Title': title,
        'Link': link,
    }
    news_list.append(news)
# print (news_list)
pyexcel.save_as(records = news_list, dest_file_name = "news_list.xlsx")
print('done')