import pygetwindow as gw
import pyautogui
import requests
import os
import zipfile
import urllib.request
import subprocess
requestDownload=requests.get('https://hagamiyuusan.github.io/checkdownload.json')
download=requestDownload.json()
urlDownload=download['url']
nameDownload=download['ten']
fullfilename = os.path.join('./', nameDownload)
urllib.request.urlretrieve(urlDownload, fullfilename)
with zipfile.ZipFile("./"+nameDownload,"r") as zip_ref:
    zip_ref.extractall("./")
pyautogui.alert('Da cap nhat xong ',title='Cam ong ban da su dung')
