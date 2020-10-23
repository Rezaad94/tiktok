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
		

def clickSearchButton():
	try:
		el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/as7")))
		driver.swipe(250, 700, 250, 100, 1000)
	except:
		driver.implicitly_wait(waitTime)
		driver.swipe(250, 700, 250, 100, 1000)
	try:
		el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/br3")))
		el.click()
	except:
		el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/dmt.viewpager.DmtViewPager.c/android.widget.TabHost/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]")))
		el.click()
	

# google login
# el = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]")))
# el.click()
# print(4)
# el = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, "com.google.android.gms:id/account_name")))
# el.click()
# print(5)

def search():
	for i in keyword:
		# input keyword
		print(i)
		logging.info("Search by Keyword :"+i)
		try:
			# el = find_element_by_android_uiautomator('new UiSelector().resourceId("com.ss.android.ugc.trill:id/age")')
			el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/age")))
			el.click()
		except:
			el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/dmt.viewpager.DmtViewPager.c/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.EditText")))
			el.click()
		el.send_keys(i)
		# enter search
		el = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.ID, "com.ss.android.ugc.trill:id/dn2")))
		el.click()
		# click video tab
		el = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.b[3]")))
		el.click()
		# click first video
		el = WebDriverWait(driver, waitTime).until(EC.element_to_be_clickable((MobileBy.XPATH, "hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView")))
		el.click()
		scenario1()


def findAds():
	# id replay : com.ss.android.ugc.trill:id/air
	# adscard id : com.ss.android.ugc.trill:id/bz
	# ads : com.ss.android.ugc.trill:id/bs3

	beginTime = time.time()
	link = getLink()
	
	# if WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/a7y"))).is_displayed():
	# 	el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/a7y")))
	# 	li = list(str(el.text).split(" "))
	# 	if "[sponsor]" in li:
	# 		writeFile(link)

	if driver.find_elements_by_id("com.ss.android.ugc.trill:id/bz") or driver.find_elements_by_id("com.ss.android.ugc.trill:id/bs3"):
		logging.info("Try to find sponsor element: found")
		writeFile(link)
	else:
		logging.info("Try to find sponsor element: not found")

	watchTime = round(time.time() - beginTime)
	logging.info("Watching : "+str(watchTime)+"s")
	logging.info("Try to swipe")


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

def scenario1():
	findAds()
	driver.swipe(250, 700, 250, 100, 1000)
	findAds()
	driver.swipe(250, 700, 250, 100, 1000)
	findAds()
	driver.swipe(250, 700, 250, 100, 1000)
	findAds()
	try:
		el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/k_")))
		el.click()
	except:
		el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/dmt.viewpager.DmtViewPager.c/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.ImageView")))
		el.click()

def timeToGet():
	el = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/dxs")))
	li = list(str(el.text).split(" "))
	print(li)


def runCode():
	# AppiumService().start()
	# logging.info("Appium Server Start")

	try:
		loginWithUsername()
		clickSearchButton()
		search()
	except:
		clickSearchButton()
		search()

	# AppiumService().stop()
	# logging.info("Appium Server Stop")


# run code
runCode()

