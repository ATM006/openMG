import os

# adb shell input text 'xxx'

os.system("adb connect 127.0.0.1:5555")
os.system('adb shell input swipe 50 250 250 250 500')