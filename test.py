import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')#run chrome debugger mode

option = Options()
option.add_experimental_option("debuggerAddress", "")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]#get chrome driver version 
# chrome_ver = chromedriver_autoinstaller.get_chrome_version()

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')


if __name__ == '__main__':
    login_url = 'https://urclass.codestates.com/login'#login url
    #login button click
    print(chrome_ver)
    driver.implicitly_wait(10)