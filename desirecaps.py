
#DEBUG = True, your environemt
#DEBUG = False, my enviroment
DEBUG=False

if DEBUG:
	desired_caps = {
	  "platformName": "Android",
	  "platformVersion": "6.0",
	  "deviceName": "29aad0ed", 
	  # "deviceName": "192.168.56.103:5555",
	  "appPackage": "com.ss.android.ugc.trill",
	  # "app": "D:\\Reza\\tiktok-asia-17-6-3.apk",
	  "app" : "/home/tester/Downloads/tiktok-asia-17-6-3.apk",
	  "appActivity":"com.ss.android.ugc.aweme.splash.SplashActivity"
	}
else:
	desired_caps = {
	  "platformName": "Android",
	  "platformVersion": "10",
	  "deviceName": "5d71e577", # this for real device
	  #"deviceName": "192.168.56.103:5555",
	  "appPackage": "com.ss.android.ugc.trill",
	  "app": "c:\\work\\tiktok\\assets\\tiktok-asia-17-6-41.apk",
	  "appActivity":"com.ss.android.ugc.aweme.splash.SplashActivity"
	}

#change username an password in here
if DEBUG:
	username= 'testersky219@gmail.com'
	password='tidakada1'
else:
	username= 'catwillwork@gmail.com'
	password='whenyousleep!@#'

#keywords
keyword=['청소신','깔끔대장','denps','비타민','곰팡이제거제','생활공작소','윤주부','YJB','오늘습관','하수구','냄새','BLACK','HOLE','거치대','일상공감','브랜드리스','침대의진실','커먼하우스','만능혀클리너','궁서체','만능청소부','두피쿨리닉','LIFE GOODS','곰팡이','세탁기','청소','해충차단','세탁조크리너','깨끗한가','오늘의','발견','크릴오일','화장실','청소','뒤꿈치','각질','레알캠','Real Cam','WHIA휘아','쪽쪽이살균기','라이프굿즈','마사지']
