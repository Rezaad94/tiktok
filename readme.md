# Description

## note:
1. This script develop with real device because in emulator tiktok always fail login
2. I search in internet there a restriction from tiktok for emulator(detected by tiktok)
3. When i develop i don't find ads, so the script search ads by text under username with keyword #ad, #ads, #광고, 광고 
4. As long as i develop i using my username and password, if you want change username and password, you can change in file scenario1.py line 10 and 11

## dependencies:
1. Install python3
2. Install pip3
3. Install appium server
4. Install appium client
5. Install selenium library

# How to run
1. Connect phone
check device
$ adb devices
2. Start appium server
3. Uninstall tiktok if version is not 17.6.41
$ adb install tiktok-asia-17-6-41.apk
push install button on phone ( if you do not push install buton within 10seconds, it will be canlced )
4. Run Python
$ python scenario1.py


# Todo 
Stopped first screen of "Swipe up for more".

