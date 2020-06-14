from selenium import webdriver
import time
tags=["tech","programming"]
driver=webdriver.Chrome(executable_path="D:\chromedriver")
driver.get("https://www.instagram.com/")
time.sleep(2)
driver.find_element_by_name("username").send_keys("grabthepy")
driver.find_element_by_name("password").send_keys("grabthepy123")
driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@class,'sqdOP  L3NKy   y3zKF     ')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@class,'aOOlW   HoLwm ')]").click()
time.sleep(2)
for tag in tags:
    driver.get(f"https://www.instagram.com/explore/tags/{tag}")
    time.sleep(3)
    driver.find_element_by_xpath("//*[contains(@class,'eLAPa')]").click()  # open first post
    for i in range(0, 3):
        time.sleep(4)
        driver.find_element_by_xpath("//*[contains(@class,'wpO6b ')]").click()  # like
        time.sleep(4)
        driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]").click()  # next

    time.sleep(4)




