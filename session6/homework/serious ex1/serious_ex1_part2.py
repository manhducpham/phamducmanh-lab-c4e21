import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

songs_list = pyexcel.get_records(file_name = 'itunes_top100songs_2.xlsx')
# print(songs_list)

for song in songs_list:
# song = songs_list[0]
    name = song['Name']
    artist = song['Artist']
    search = name + " " + artist
    search_list = [search]
    options = {
        'default_search': 'ytsearch', 
        'max_downloads': 1, 
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download(search_list)
print('Done!')