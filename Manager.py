import ctypes

from selenium import webdriver
import time
import requests, json, datetime, os;
import random

os.system("clear")

from selenium.webdriver.common.by import By

# options
options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=NiggerOS/5.0 (X11; Nazi; YourMom i686; rv:15.0) Gecko/20100101 Firefox/15.0.1 ua.safari")
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe")

import random
lower_case = "squeazzy"
upper_case = lower_case.upper()
num = "0123456789"
symbol = ""
ans = lower_case + upper_case + num + symbol
length = 6
password = "".join(random.sample(ans,length))
#print(password)



try:
    os.system("color 02")
    print("""
 $$$$$$\            $$\             $$\               $$\ $$\                  $$$$$$\                      
$$  __$$\           \__|            $$ |              $$ |\__|                $$  __$$\                     
$$ /  \__| $$$$$$\  $$\  $$$$$$$\ $$$$$$\    $$$$$$\  $$ |$$\ $$\   $$\       $$ /  \__| $$$$$$\  $$$$$$$\  
$$ |      $$  __$$\ $$ |$$  _____|\_$$  _|   \____$$\ $$ |$$ |\$$\ $$  |      $$ |$$$$\ $$  __$$\ $$  __$$\ 
$$ |      $$ |  \__|$$ |\$$$$$$\    $$ |     $$$$$$$ |$$ |$$ | \$$$$  /       $$ |\_$$ |$$$$$$$$ |$$ |  $$ |
$$ |  $$\ $$ |      $$ | \____$$\   $$ |$$\ $$  __$$ |$$ |$$ | $$  $$<        $$ |  $$ |$$   ____|$$ |  $$ |
\$$$$$$  |$$ |      $$ |$$$$$$$  |  \$$$$  |\$$$$$$$ |$$ |$$ |$$  /\$$\       \$$$$$$  |\$$$$$$$\ $$ |  $$ |
 \______/ \__|      \__|\_______/    \____/  \_______|\__|\__|\__/  \__|       \______/  \_______|\__|  \__|
                                                                                                            
                                                                                                            
                                                                                                            
    """)
    driver.get("https://new.cristalix.ru/register")
    time.sleep(3)
    # email-input
    # username-input
    # password-input
    # repeat-password-input
    # register-button
    # agreed-input
    # cookieBtn
    driver.find_element(By.ID, 'cookieBtn').click()
    nickname_input = driver.find_element(By.ID, 'username-input')
    nickname_input.send_keys("squeazzy_" + password)
    nickname_input = driver.find_element(By.ID, 'email-input')
    #nickname_input.send_keys(adolf)
    print("OPEN email.py U HAVE 8 SECONDS")

    os.startfile("mail.py")
    time.sleep(3)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    nickname_input = driver.find_element(By.ID, 'password-input')
    print("FUCKED.")
    ctypes.windll.kernel32.SetConsoleTitleW("Cristalix Gen v 1.0.0")
    os.system("cls")
    os.system("color 03")
    nickname_input.send_keys('Squeazzy_GenA4$')
    nickname_input = driver.find_element(By.ID, 'repeat-password-input')
    nickname_input.send_keys('Squeazzy_GenA4$')
    time.sleep(3)
    driver.find_element(By.ID, 'agreed-input').click()
    time.sleep(3)
    driver.find_element(By.ID, 'register-button').click()
    driver.get_screenshot_as_file("1.png")
    driver.save_screenshot("2.png")
    x = open("accounts.txt")
    print(x.read())
    passwordd = "Squeazzy_GenA4$"
    nigga = "squeazzy_" + password
    print("CHECK OUT email.py")
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r") as SAVEACCOUNTS:
            LASTACCOUNTS = SAVEACCOUNTS.read()
            SAVEACCOUNTS.close()
    else:
        LASTACCOUNTS = ""

    with open("accounts.txt", "w+") as ACCOUNT:
        if LASTACCOUNTS == "":
            ACCOUNT.write("Cristalix Gen\n\n")
        else:
            ACCOUNT.write(f"{LASTACCOUNTS}\n\n")
        ACCOUNT.write(f"Nickname: {nigga}\n")
        ACCOUNT.write(f"Password: {passwordd}\n")
        ACCOUNT.close()

except Exception as ex:
    print(ex)
finally:
    print("Hallo!")
