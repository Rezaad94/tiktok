from scenario1 import *

def search2():	
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
		scenario2()

def scenario2():
	findAds()
	driver.swipe(250, 700, 250, 170, 1000)
	findAds()
	el = WebDriverWait(driver, 40).until(EC.presence_of_element_located((MobileBy.ID, "com.ss.android.ugc.trill:id/k_")))
	el.click()

loginWithUsername()
search2()