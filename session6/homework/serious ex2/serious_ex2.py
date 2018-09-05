from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
conn = urlopen(url)
raw_data = conn.read()
html_page = raw_data.decode('utf-8')
# f_conn = open('vnmis.html', 'wb')
# f_conn.write(raw_data)
# f_conn.close()

soup = BeautifulSoup(html_page, 'html.parser')

ul = soup.find('table', id = 'tableContent')
tr_list = ul.find_all('tr')

title = ['Chỉ tiêu', 'Quý 4 2016', 'Quý 1 2017', 'Quý 2 2017', 'Quý 3 2017']
num = len(title)
vnm_is = []
len_is = len(tr_list)

for j in range(len_is):
    if j%3 == 0:
        td = tr_list[j].find_all('td')
        td_filter = td[:5]
        index_dict = OrderedDict({})
        for i in range(num):
            content = td_filter[i].string
            index_dict[title[i]] = content
        vnm_is.append(index_dict)

def del_space(t): # xoa cac dau thua nhu tab, space
    t = t.replace("\n", "")
    t = t.replace("\r", "")
    t = t.replace("\xa0", "")
    while True:
        t = t.replace("  ", " ")
        spaces = '  '
        if spaces not in t:
            break
    return t
for dic in vnm_is:
    dic_index = dic['Chỉ tiêu']
    new_content = del_space(dic_index)
    dic['Chỉ tiêu'] = new_content

pyexcel.save_as(records = vnm_is, dest_file_name = "vnm_is.xlsx")
print('Done!')