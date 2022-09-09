import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil

#If there are important files, you have to back up them. You can't restore the files to use funciton that recycle bin recovery.
try:
    shutil.rmtree(r'C:\chrometemp') #remove cookie, cache
except FileNotFoundError:
    pass

subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')#run chrome debugger mode

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]#get chrome driver version 
# chrome_ver = chromedriver_autoinstaller.get_chrome_version()

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)#add options mean 'open debugger mode chrome only'
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

driver.implicitly_wait(10)

login_url = 'https://urclass.codestates.com/login'#login url
driver.get(login_url)

if __name__ == '__main__':
    #login button click
    print(chrome_ver)