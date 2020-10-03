DEBUG=True

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
	  "app": "c:\\work\\tiktok\\tiktok-asia-17-6-41.apk",
	  "appActivity":"com.ss.android.ugc.aweme.splash.SplashActivity"
	}
