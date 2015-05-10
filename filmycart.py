import requests
from bs4 import BeautifulSoup
import os
import urllib
import urlpath
from urllib import request

class Working:

    def download(url, folder_name):
        dir = r"C:\Users\Sid\Downloads" + "/FilmyCart/" + folder_name
        os.makedirs(dir,exist_ok=True)
        name = dir + "/"+ str(urlpath.URL(url).name)
        if not os.path.exists(name):
            print("Downloading " + str(urlpath.URL(url).name))
            urllib.request.urlretrieve(url, name)
            return 1
        else:
            return 0


    def main_page(url):
        base_url = url.split(".com")
        base_url = base_url[0] + ".com"
        source_code = requests.get(url)
        text = source_code.text
        soup = BeautifulSoup(text)
        folder_name = soup.find("h1").string
        next_page = soup.find_all("a", "ngg-browser-next")
        next_page = base_url + next_page[0].get('href')
        stop_url = soup.find_all("a", "ngg-browser-prev")
        stop_url = base_url + stop_url[0].get('href')
        Working.crawling_pages(next_page, stop_url, folder_name)

    def crawling_pages(next, stop, folder_name):
        total_downloads = 0
        base_url_next = next.split(".com")
        base_url_next = base_url_next[0] + ".com"
        i = 0
        while i <= 1:
            if i == 1:
                i += 1
            if next == stop:
                i += 1
            source_code = requests.get(next)
            text = source_code.text
            soup = BeautifulSoup(text)
            for tmp in soup.find_all("div","pic"):
                link = tmp.contents[1]
                link = link.get('href')
            response = Working.download(link, folder_name)
            if response is 1:
                    total_downloads += 1
            next_page = soup.find_all("a", "ngg-browser-next")
            next = base_url_next + next_page[0].get('href')
        print("=" * 15)
        print(str(total_downloads) + " Files Downloaded.")
        print("=" * 15)


Working.main_page("http://filmycart.com/2015/05/15-before-and-after-vfx-pictures-of-movie-scenes-that-show-the-importance-of-visual-effects/")