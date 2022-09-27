from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import getopt
from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.by import By


LYRICSI = "https://lyricsi.com/"

artist = str(input("Enter the name of an artist: "))

artist = artist.lower()
artist = artist.strip()
artist = artist.replace(" ", "-")

link = LYRICSI + artist + "-lyrics/"
content = requests.get(link)
soup = BeautifulSoup(content.content, "html.parser")
songs = soup.findAll('a',attrs={"class":"link1"})
print(songs[0]['href'])

urls = []

print('Finding URL of each song...' )
for song in songs:
    url=song['href']
    if artist in url:
        with open('songlist.txt', 'a') as f:
            f.write(url + "\n")
        urls.append(url)
        print('Adding song... ' + url)

print( str(len(urls)) + " songs found!")

for url in urls:
    print('Retrieving lyrics for ' + url)
    content = requests.get(LYRICSI + url)
    soup = BeautifulSoup(content.content, 'html.parser')
    lyrics = soup.find('div',attrs={'class':'song-text'})
    with open('lyrics.txt', 'a') as f:      
        f.write(lyrics.text + '\n')
