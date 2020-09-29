import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from desirecaps import *

#change username an password in here
username= 'testersky219@gmail.com'
password='tidakada1'
keyword=['청소신','깔끔대장','denps','비타민','곰팡이제거제','생활공작소','윤주부','YJB','오늘습관','하수구','냄새','BLACK','HOLE','거치대','일상공감','브랜드리스','침대의진실','커먼하우스','만능혀클리너','궁서체','만능청소부','두피쿨리닉','LIFE GOODS','곰팡이','세탁기','청소','해충차단','세탁조크리너','깨끗한가','오늘의','발견','크릴오일','화장실','청소','뒤꿈치','각질','레알캠','Real Cam','WHIA휘아','쪽쪽이살균기','라이프굿즈','마사지']



driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def loginWithUsername():
	el = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/bno")))
	el.click()
	# login Username and password
	el = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")))
	el.click()
	# skip no telp
	try:
		el = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.google.android.gms:id/cancel")))
		el.click()
	finally:
		el = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.b[2]")))
		el.click()
		usr = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/b1j"))).send_keys(username)
		psw = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/agc"))).send_keys(password)
		loginbtn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/box"))).click()

# google login
# el = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]")))
# el.click()
# print(4)
# el = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.google.android.gms:id/account_name")))
# el.click()
# print(5)

def search():
	# skip	
	el = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/ctj")))
	el.click()
	# start watching
	el = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/cxc")))
	el.click()
	el = WebDriverWait(driver, 40).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/b8l")))
	driver.swipe(250, 700, 250, 170, 1000)
	el = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/br3")))
	el.click()

	for i in keyword:
		# input keyword
		print(i)
		el = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/age")))
		el.click()
		el.send_keys(i)
		# enter search
		el = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/dn2")))
		el.click()
		# click video tab
		el = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.b[3]")))
		el.click()
		# click first video
		el = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((MobileBy.XPATH, "hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView")))
		el.click()
		scenario1()


def findAds():
	el = WebDriverWait(driver, 40).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/a7y")))
	driver.implicitly_wait(5)
	li = list(str(el.text).split(" "))
	if ['#ad','#ads','#광고','광고'] in li:
		getLink()


def getLink():
	el = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/crn")))
	el.click()
	el = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]")))
	el.click()
	link = driver.get_clipboard_text()
	writeFile(link)

def writeFile(link):
	f = open("link.csv", "a")
	f.write(link)
	f.write('\n')
	f.close()

def scenario1():
	findAds()
	driver.swipe(250, 700, 250, 170, 1000)
	findAds()
	driver.swipe(250, 700, 250, 170, 1000)
	findAds()
	driver.swipe(250, 700, 250, 170, 1000)
	findAds()
	el = WebDriverWait(driver, 40).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/k_")))
	el.click()


# run code
loginWithUsername()
search()