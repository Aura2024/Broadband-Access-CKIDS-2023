import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
address_book = [["1 62nd Place", "","90803"], ["10 17th Avenue","","90291"],["100 19th Street","","90254"], ["1000 245th Street","","90710"], ["10000 Aldea Avenue", "", "91325"]]
def plan_set(full_address: list[str]) -> dict:
    serviced = True
    prices = []
    speeds = []
    plan = {}
    while len(prices) < 1 and serviced:
        address = full_address[:]
        WEBSITE = "https://www.spectrum.com/address/localization"
        PATH = "C:\Program Files (x86)\chromedriver.exe"

        driver = webdriver.Chrome(PATH)
        driver.get(WEBSITE)
        # Wait for initial page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address-line1--/address/localization/jcr:content/root/responsivegrid/responsivegrid/addressentryform")))
        # Collect the address fields
        street = driver.find_elements(By.ID, "address-line1--/address/localization/jcr:content/root/responsivegrid/responsivegrid/addressentryform")
        unit = driver.find_elements(By.ID, "address-line2--/address/localization/jcr:content/root/responsivegrid/responsivegrid/addressentryform")
        zipcode = driver.find_elements(By.ID, "zipcode--/address/localization/jcr:content/root/responsivegrid/responsivegrid/addressentryform")

        # Send the address to the fields
        for i in street:
            time.sleep(0.5)
            i.send_keys(address[0])
            i.send_keys(Keys.ESCAPE)
        for i in unit:
            time.sleep(0.5)
            i.send_keys(address[1])
            i.send_keys(Keys.ESCAPE)
        for i in zipcode:
            time.sleep(0.5)
            i.send_keys(address[2])
            time.sleep(0.5)
            i.send_keys(Keys.RETURN)

        # Check if address is serviced
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "localization-error__error-text"))
            )
            serviced = False
            driver.quit()
            return {}
        except:
            pass

        if serviced:
            # Check if multiple units are available
            try:
                unit_link = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "multiple-units__apt-cta"))
                )
                unit_link.click()

            except:
                pass

        if serviced:
            # Check if existing customer
            try:
                existing_customer = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "I’m a new customer at this address"))
                )
                existing_customer.click()

            except:
                pass

        if serviced:
            # Only select internet plans
            try:
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "card--header--toggle-switch"))
                )
                plans = driver.find_elements(By.CLASS_NAME, "card--header--toggle-switch")
                x = 0
                for i in plans:
                    if x == 1:
                        i.click()
                    x += 1
            except:
                pass

        if serviced:
            # Get the prices and speeds
            try:
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "feature-offer__pricing__text--price--value"))
                )
                time.sleep(3)
                plan_list = driver.find_elements(By.CLASS_NAME, "feature-offer__pricing__text--price--value")
                for i in plan_list:
                    price = i.text + ".99"
                    prices.append(price)

                speeds_list = driver.find_elements(By.CLASS_NAME, "feature-offer__text__card-header__title__text")
                for i in speeds_list:
                    speed = i.text
                    speeds.append(speed)
                # feature-offer__text__card-header__title__subheader
            except:
                pass



            driver.quit()

    for i, x in enumerate(speeds):
        plan[x] = prices[i]
    return plan

