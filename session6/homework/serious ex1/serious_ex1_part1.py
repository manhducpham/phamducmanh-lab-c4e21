from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = 'https://www.apple.com/itunes/charts/songs/'
conn = urlopen(url)
raw_data = conn.read()
html_page = raw_data.decode('utf-8')
# f_conn = open('itunes.html', 'wb')
# f_conn.write(raw_data)
# f_conn.close()

soup = BeautifulSoup(html_page, 'html.parser')
ul_parent = soup.find('section', 'section chart-grid')
ul = ul_parent.div.ul
# print(ul.prettify())
li_list = ul.find_all('li')

songs_list = []

for song in li_list:
    # print(song.prettify())
    h3 = song.h3.a
    h4 = song.h4.a
    name = h3.string
    artist = h4.string
    # print(name)
    # print(artist)
    new_song = OrderedDict({
        'Name': name,
        'Artist': artist,
    })
    songs_list.append(new_song)

# print(songs_list)
pyexcel.save_as(records = songs_list, dest_file_name = "itunes_top100songs_2.xlsx")
print('done')
