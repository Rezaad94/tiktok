from appium.webdriver.appium_service import AppiumService
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from desirecaps import *
import platform
import logging
import datetime

# Path
if platform.system() == 'Windows':
	logPath = "logs\\"
	adsPath = "db\\"
else:
	logPath = "logs/"
	adsPath = "db/"

# Log
dtime = datetime.datetime.now() 
logName = logPath+dtime.strftime("%d-%m-%Y")+"-output.log"
logFormat = "%(asctime)s: %(message)s"
logging.basicConfig(filename=logName, level=logging.INFO, format=logFormat, datefmt="%d-%m-%Y %H:%M")

# Driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# wait time in seecond, increase wait time if element not found,  
waitTime= 80

def loginWithUsername():
	logging.info("Try to login")
	el = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/bno")))
	el.click()
	# login Username and password
	el = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")))
	el.click()
	# skip no telp
	# try:
	# 	el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.google.android.gms:id/cancel")))
	# 	el.click()
	# except:
	el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.b[2]")))
	el.click()
	usr = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/b1j"))).send_keys(username)
	psw = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/agc"))).send_keys(password)
	loginbtn = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/box"))).click()
	# skip	
	el = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/ctj")))
	el.click()
	# start watching
	el = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/cxc")))
	el.click()
	logging.info("Login Success")


def scrollOneTime():
	el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/as7")))
	driver.swipe(250, 700, 250, 100, 1000)

def findAdsHome():
	logging.info('find Ads')
	beginTime = time.time()

	try: 
		el = WebDriverWait(driver, 30).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/air")))
		logging.info("Try to find sponsor element: found")
		el.click()
		writeFile(getLink())
	except:
		logging.info("Try to find sponsor element: not found")

	driver.swipe(250, 700, 250, 100, 1000)
	c = True
	watchTime = round(time.time() - beginTime)
	logging.info("Watching : "+str(watchTime)+"s")
	logging.info("Try to swipe")
	return c

def getLink():
	el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/crn")))
	el.click()
	# el = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]")))
	el = driver.find_element_by_android_uiautomator('new UiSelector().text("Copy link")')
	el.click()
	link = driver.get_clipboard_text()
	logging.info("Get Current url: "+link)
	return link

def writeFile(link):
	f = open(adsPath+"AD_lists.csv", "a")
	f.write(link)
	f.write('\n')
	f.close()


def run():
	loginWithUsername()
	scrollOneTime()
	g = True

	while g == True:
		g = findAdsHome()

run()