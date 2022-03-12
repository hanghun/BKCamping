from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#-*- coding: utf-8 -*-
import urllib.request
import time

pageLinkAddress = 'https://camp.xticket.kr/web/main?shopEncode=d92f3bd48a33183707d6d8bfce8238949624e25b7f23c18487570e3edac7fc3e'

serverTime = urllib.request.urlopen('https://google.com').headers['Date']




userId = 'ph6601'
userPassword = 'dltjswjd1wh'

#XPath list
idXPath = '/html/body/div[1]/div[1]/div[2]/fieldset/form/ul[1]/li[1]/input'
passwordXPath = '/html/body/div[1]/div[1]/div[2]/fieldset/form/ul[1]/li[2]/input'
loginXPath = '/html/body/div[1]/div[1]/div[2]/fieldset/form/ul[1]/li[3]/a'
nextButtonXPath = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/ul[2]/li[2]/a'
dateXPath = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/table[1]/tbody/tr[6]/td[3]' #3월29일 화요일
periodOptionXPath = '/html/body/div[1]/div[2]/div/div[2]/div[2]' #메뉴 옵션 선택
periodXPath = '/html/body/div[1]/div[2]/div/div[2]/div[2]/ul/li[2]/a' #2박 3일
positionXPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[19]' # 위치 1-18
reservationXPath = '/html/body/div[1]/div[2]/div/div[1]/div/p/a'

s = Service("C:/dev/chromedriver/chromedriver.exe")
chromeDriver = webdriver.Chrome(service=s)
chromeDriver.get(pageLinkAddress)
handles = chromeDriver.window_handles

# 아이디 입력
passFlag = 0
while passFlag == 0 :
    try:
        idEdit = chromeDriver.find_element(By.XPATH, value=idXPath)
        idEdit.send_keys(userId)
        passFlag = 1
    except:
        ...

#패스워드 입력
passFlag = 0
while passFlag == 0 :
    try:
        passwordEdit = chromeDriver.find_element(By.XPATH, value=passwordXPath)
        passwordEdit.send_keys(userPassword)
        passFlag = 1
    except:
        ...

#로그인 버튼 클릭
passFlag = 0
while passFlag == 0 :
    try:
        loginButton = chromeDriver.find_element(By.XPATH, value=loginXPath)
        loginButton.click()
        passFlag = 1
    except:
        ...

# 다음달로 이동
passFlag = 0
while passFlag == 0 :
    try:
        nextButton = chromeDriver.find_element(By.XPATH, value=nextButtonXPath)
        nextButton.click()
        passFlag = 1
    except:
        ...

# 날짜 선택
passFlag = 0
while passFlag == 0 :
    try:
        dateButton = chromeDriver.find_element(By.XPATH, value=dateXPath)
        dateButton.click()
        passFlag = 1
    except:
        ...

# 사용 일수 옵션 선택
passFlag = 0
while passFlag == 0 :
    try:
        periodOptionButton = chromeDriver.find_element(By.XPATH, value=periodOptionXPath)
        periodOptionButton.click()
        passFlag = 1
    except:
        ...

# 사용 일수 선택
passFlag = 0
while passFlag == 0:
    try:
        periodButton = chromeDriver.find_element(By.XPATH, value=periodXPath)
        periodButton.click()
        passFlag = 1
    except:
        ...

# 위치 선택
passFlag = 0
while passFlag == 0 :
    try:
        positionButton = chromeDriver.find_element(By.XPATH, value=positionXPath)
        className = positionButton.get_attribute('class')
        positionButton.click()
        passFlag = 1
    except:
        ...

#예약하기 클릭
passFlag = 0
while passFlag == 0 :
    try:
        reservationButton = chromeDriver.find_element(By.XPATH, value=reservationXPath)
        reservationButton.click()
        passFlag = 1
    except:
        ...

time.sleep(100)
