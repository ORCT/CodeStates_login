import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil

def test():
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
    
    login_btn_xpath = '//*[@id="root"]/div/div/div[3]/div/div/div/div[2]/button[1]'
    login_btn = driver.find_element_by_xpath(login_btn_xpath)
    login_btn.click()

    login_id = 'sonic407@naver.com'
    login_pw = 'sonic0989'
    
    driver.find_element_by_name('email').send_keys(login_id)
    driver.find_element_by_name('password').send_keys(login_pw)

    login_btn1_xpath = '//*[@id="login-form"]/fieldset/div[8]/button[1]'
    login_btn1 = driver.find_element_by_xpath(login_btn1_xpath)
    login_btn1.click()

id_xpath = '//*[@id="id_email_2_label"]'
pw_xpath = '//*[@id="id_password_3_label"]'

if __name__ == '__main__':
    test()
    print('fin')