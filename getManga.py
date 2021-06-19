from requests_html import HTMLSession
from getChapter import get_chapter

session = HTMLSession()

# Doi cai nay bang link truyen muon tai
# url = "http://www.nettruyentop.com/truyen-tranh/amagami-san-chi-no-enmusubi-40237"
url = input("Nhap link truyen ban muon tai: ")
r = session.get(url)

# Class html phai co dau cham
rs = r.html.find("#nt_listchapter .chapter a",first = False)

for x in rs:
    chapter_url = x.attrs['href']
    manga_name = chapter_url.split('/')[-3]
    get_chapter(chapter_url, manga_name)
    
# print(rs)