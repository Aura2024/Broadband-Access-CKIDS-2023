import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def plan_set(full_address: list[str]) -> dict:
    plan = {}
    serviced = True
    while len(plan) == 0 and serviced:
        WEBSITE = "https://frontier.com/buy"
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get(WEBSITE)
        # Wait for initial page to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "street-address"))
            )
        except:
            pass


        input_field = driver.find_elements(By.ID, "street-address")

        # Send the address to the fields
        for i in input_field:
            for item in full_address:
                for letter in item:
                     i.send_keys(letter)
                time.sleep(0.2)
                i.send_keys(Keys.SPACE)
            time.sleep(1.5)
            i.send_keys(Keys.ENTER)
            time.sleep(.5)
            i.send_keys(Keys.ENTER)

        # Check if address is serviced
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("unserviceable")
            )

            serviced = False
            driver.quit()
            return plan
        except:
            pass
        if serviced:
            # Checks to see if there is an existing customer page
            try:
                WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.CLASS_NAME, "ButtonStyled-sc-nyrb95-0 bKOgHY are-you-moving__button btn"), "Yes, I'm moving")
                    # presence_of_element_located((By.CLASS_NAME, "are-you-moving__address"))
                )
                moving = driver.find_elements(By.CLASS_NAME, "ButtonStyled-sc-nyrb95-0 bKOgHY are-you-moving__button btn")
                time.sleep(0.5)
                # Click the "I'm moving here" button
                for i in moving:
                    if moving.index(i) == 0:
                        i.click()
            except:
                pass

            speeds_list = []
            prices_list = []

            # Checks to see if the address is correct
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "edit-address__button fs-mask"))
                )
                address = driver.find_elements(By.CLASS_NAME, "edit-address__button fs-mask")
                if full_address[2] not in address[0].text:
                    driver.quit()
            except:
                pass


            # Wait for the plans to load
            try:
                WebDriverWait(driver, 2).until(
                    EC.url_contains("plan-package")
                )
                # Find the next button
                next_arrow = driver.find_elements(By.TAG_NAME, "button")
                # Click the next button 7 times
                for i in range(0, 7): # Arbitrary number, should not be more than 7 plans
                    # Find the plans
                    packages = driver.find_elements(By.CLASS_NAME, "plan-packages__cards")
                    # Find the speeds and prices
                    for x in packages:
                        ls = x.text.split("\n")
                        if len(ls) == 12:
                            slash = ls[1].find("/")
                            speed = ls[1][slash + 1:]
                            if ls[4] == 'Best value':
                                price = ls[5]
                            else:
                                price = ls[4]
                        else:
                            slash = ls[2].find("/")
                            speed = ls[2][slash + 1:]
                            if ls[4] == 'Best value':
                                price = ls[7]
                            else:
                                price = ls[6]
                        if speed in speeds_list:
                            break
                        else:
                            speeds_list.append(speed)
                            prices_list.append(price)
                    # Show the next plan
                    next_arrow[5].click()
                    time.sleep(1)
            except:
                pass
            # Turn the lists into a dictionary
            for i, x in enumerate(speeds_list):
                plan[x] = prices_list[i]
    return plan
