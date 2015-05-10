import requests
from bs4 import BeautifulSoup
import os
import urllib
import urlpath
from urllib import request

class Working:

    def download(url, folder_name):                 #for downloading the file, takes url of the image and folder to be created
        dir = r"C:\Users\Sid\Downloads" + "/FilmyCart/" + folder_name
        os.makedirs(dir,exist_ok=True)              #create dir if not exist
        name = dir + "/"+ str(urlpath.URL(url).name)
        if not os.path.exists(name):        #check if file already exist
            print("Downloading " + str(urlpath.URL(url).name))
            urllib.request.urlretrieve(url, name)       #download the image
            return 1  #successful
        else:
            return 0  #unsuccessful


    def main_page(url):         #go to given url
        base_url = url.split(".com")
        base_url = base_url[0] + ".com"     #get the website's url
        source_code = requests.get(url)     #get source code
        text = source_code.text
        soup = BeautifulSoup(text)          #make a soup object
        folder_name = soup.find("h1").string        #get heading of article to use it as folder name
        next_page = soup.find_all("a", "ngg-browser-next")
        next_page = base_url + next_page[0].get('href')     #url of next page
        stop_url = soup.find_all("a", "ngg-browser-prev")
        stop_url = base_url + stop_url[0].get('href')     #url of prev page
        Working.crawling_pages(next_page, stop_url, folder_name)        #call the next page

    def crawling_pages(next, stop, folder_name):        #iterating through all pages of given article
        total_downloads = 0
        base_url_next = next.split(".com")
        base_url_next = base_url_next[0] + ".com"
        i = 0
        while i <= 1:       #traverse until all pages are visited once
            if i == 1:
                i += 1
            if next == stop:
                i += 1
            source_code = requests.get(next)
            text = source_code.text
            soup = BeautifulSoup(text)
            for tmp in soup.find_all("div","pic"):      #finding the image code
                link = tmp.contents[1]                  #get image tag
                link = link.get('href')                 #get image url
            response = Working.download(link, folder_name)          #call downloading function
            if response is 1:           #if an image is downloaded
                    total_downloads += 1
            next_page = soup.find_all("a", "ngg-browser-next")
            next = base_url_next + next_page[0].get('href')
        print("*" * 30)
        print(str(total_downloads) + " Files Downloaded.")
        print("*" * 30)

#pass the url of article
Working.main_page("http://filmycart.com/2015/05/15-before-and-after-vfx-pictures-of-movie-scenes-that-show-the-importance-of-visual-effects/")