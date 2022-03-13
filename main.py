from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chromeDriverPath = 'C:/Johnny/ChromeDriver/chromedriver.exe'
pageLinkAddress = 'https://camp.xticket.kr/web/main?shopEncode=d92f3bd48a33183707d6d8bfce8238949624e25b7f23c18487570e3edac7fc3e'

userId = 'ph6601'
userPassword = 'dltjswjd1wh'

# XPath list
idXPath = '/html/body/div[1]/div[1]/div[2]/fieldset/form/ul[1]/li[1]/input'
passwordXPath = '/html/body/div[1]/div[1]/div[2]/fieldset/form/ul[1]/li[2]/input'
loginXPath = '/html/body/div[1]/div[1]/div[2]/fieldset/form/ul[1]/li[3]/a'
nextButtonXPath = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/ul[2]/li[2]/a'
targetDateXPath = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/table[1]/tbody/tr[2]/td[6]'  # 4월 1일


reservationXPath = '/html/body/div[1]/div[2]/div/div[1]/div/p/a'

# 크롬 실행, 홈페이지 열기
s = Service(chromeDriverPath)
chromeDriver = webdriver.Chrome(service=s)
chromeDriver.get(pageLinkAddress)
handles = chromeDriver.window_handles

# 아이디 입력
passFlag = 0
while passFlag == 0:
    try:
        idEdit = chromeDriver.find_element(By.XPATH, value=idXPath)
        idEdit.send_keys(userId)
        passFlag = 1
    except:
        ...

# 패스워드 입력
passFlag = 0
while passFlag == 0:
    try:
        passwordEdit = chromeDriver.find_element(By.XPATH, value=passwordXPath)
        passwordEdit.send_keys(userPassword)
        passFlag = 1
    except:
        ...

# 로그인 버튼 클릭
passFlag = 0
while passFlag == 0:
    try:
        loginButton = chromeDriver.find_element(By.XPATH, value=loginXPath)
        loginButton.click()
        passFlag = 1
    except:
        ...

serverOpenedFlag = 0

while serverOpenedFlag == 0:
    chromeDriver.refresh()
    monthTextLabelXPath = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/ul[1]/li'  # 달력 글씨
    # 22년 3월인지 확인
    passFlag = 0
    while passFlag == 0:
        try:
            monthTextLabel = chromeDriver.find_element(By.XPATH, value=monthTextLabelXPath)
            monthText = monthTextLabel.text
            if monthTextLabel.text == '2022.03':
                passFlag = 1
        except:
            ...

    # 다음 달로 이동
    passFlag = 0
    while passFlag == 0:
        try:
            nextButton = chromeDriver.find_element(By.XPATH, value=nextButtonXPath)
            nextButton.click()
            passFlag = 1
        except:
            ...


    passFlag = 0
    while passFlag == 0:
        try:
            targetDateButton = chromeDriver.find_element(By.XPATH, value=targetDateXPath)
            targetDateClassName = targetDateButton.get_attribute('class')
            if targetDateClassName == 'available':
                serverOpenedFlag = 1
            passFlag = 1
        except:
            ...

# 날짜 선택
passFlag = 0
while passFlag == 0:
    try:
        dateButton = chromeDriver.find_element(By.XPATH, value=targetDateXPath)

        dateButton.click()
        passFlag = 1
    except:
        ...

# 사용 일수 옵션 선택
periodOptionXPath = '/html/body/div[1]/div[2]/div/div[2]/div[2]'  # 메뉴 옵션 선택
passFlag = 0
while passFlag == 0:
    try:
        periodOptionButton = chromeDriver.find_element(By.XPATH, value=periodOptionXPath)
        periodOptionButton.click()
        passFlag = 1
    except:
        ...

# 사용 일수 선택
periodXPath = '/html/body/div[1]/div[2]/div/div[2]/div[2]/ul/li[2]/a'  # 2박 3일
passFlag = 0
while passFlag == 0:
    try:
        periodButton = chromeDriver.find_element(By.XPATH, value=periodXPath)
        periodButton.click()
        passFlag = 1
    except:
        ...

positionChecked = 0

# 시설 선택
facility2XPath = '/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[5]/td[1]/input'  # 제 2야영장(오토캠핑)
passFlag = 0
while passFlag == 0:
    try:
        facilityButton = chromeDriver.find_element(By.XPATH, value=facility2XPath)
        facilityButton.click()
        passFlag = 1
    except:
        ...

if positionChecked == 0:
    # 위치 선택 2-19
    date2_19XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[18]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date2_19XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 2-18
    date2_18XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[19]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date2_18XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 2-17
    date2_17XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[20]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date2_17XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 시설 선택
    facility1XPath = '/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[2]/td[1]/input'  # 제 1야영장(오토캠핑)
    passFlag = 0
    while passFlag == 0:
        try:
            facilityButton = chromeDriver.find_element(By.XPATH, value=facility1XPath)
            facilityButton.click()
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-27
    date1_27XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[28]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_27XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-28
    date1_28XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[29]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_28XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-21
    date1_21XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[22]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_21XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-22
    date1_22XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[23]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_22XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-33
    date1_33XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[34]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_33XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-35
    date1_35XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[36]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_35XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-25
    date1_25XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[26]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_25XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 시설 선택
    facility2XPath = '/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[5]/td[1]/input'  # 제 2야영장(오토캠핑)
    passFlag = 0
    while passFlag == 0:
        try:
            facilityButton = chromeDriver.find_element(By.XPATH, value=facility2XPath)
            facilityButton.click()
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 2-16
    date2_16XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[17]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date2_16XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 시설 선택
    facility1XPath = '/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[2]/td[1]/input'  # 제 1야영장(오토캠핑)
    passFlag = 0
    while passFlag == 0:
        try:
            facilityButton = chromeDriver.find_element(By.XPATH, value=facility1XPath)
            facilityButton.click()
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-13
    date1_13XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[14]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_13XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...


if positionChecked == 0:
    # 위치 선택 1-14
    date1_14XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[15]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_14XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-16
    date1_16XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[17]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_16XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-17
    date1_17XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[18]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_17XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-18
    date1_18XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[19]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_18XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-21
    date1_21XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[22]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_21XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-22
    date1_22XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[23]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_22XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

if positionChecked == 0:
    # 위치 선택 1-22
    date1_23XPath = '/html/body/div[1]/div[2]/div/div[3]/div[2]/div/img[24]'
    passFlag = 0
    while passFlag == 0:
        try:
            positionButton = chromeDriver.find_element(By.XPATH, value=date1_23XPath)
            className = positionButton.get_attribute('class')
            if className == 'product_box normal':
                positionButton.click()
                positionChecked = 1
            passFlag = 1
        except:
            ...

# 예매하기 클릭
passFlag = 0
while passFlag == 0:
    try:
        reservationButton = chromeDriver.find_element(By.XPATH, value=reservationXPath)
        reservationButton.click()
        passFlag = 1
    except:
        ...

time.sleep(1000)
