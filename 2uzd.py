""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.
1) RSS?
RSS ir tehnoloģija kas ļauj cilvēkiem ļoti vieglā veidā atrast un sekot jaunākajām ziņām internetā.
2) Plūsmu no google.lv?
Google ir vietne, bet nav satura radītāja.

"""
import feedparser

# URL to RSS plūsmu

rss_url='https://news.google.com/home?hl=en-MY&gl=MY&ceid=MY:lv'

# iegūstam RSS plūsmas datus un veicam analaīzi...
kkk=feedparser.parse(rss_url)

# noformēšana...
for entry in kkk.entries:
    print("Virsraksts", entry.title)
    print("Saite:", entry.link)
    print("Publicēšanas datums", entry.published)
    print("\n")
    