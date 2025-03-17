from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from twilio.rest import Client

# Twilio Credentials (Get from Twilio Console)
TWILIO_ACCOUNT_SID = "AC2c0807fcb4fa4bab7653f4d69db4a2a"
TWILIO_AUTH_TOKEN = "4c2521f2cedcfe9f446cb60ed66b4cc"
TWILIO_PHONE_NUMBER = "+91 7085431394"
MY_PHONE_NUMBER = "+91 7085431394"

# Amazon Credentials
AMAZON_EMAIL = "+91 7085431394"
AMAZON_PASSWORD = "Bhowmik@990"
CARD_NUMBER = "5089 7900 "
EXPIRY_DATE = "08"
CVV = "123"

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

try:
    
    try:
        captcha_image = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'captcha')]"))
        )
        print("🔹 CAPTCHA detected! Please solve it manually.")
        time.sleep(10)  
    except:
        print("  No CAPTCHA detected, continuing...")

    
    driver.find_element(By.ID, "nav-link-accountList").click()

    WebDriverWait(driver, 20).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_input.send_keys(AMAZON_EMAIL, Keys.RETURN)

    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ap_password"))
    )
    password_input.send_keys(AMAZON_PASSWORD)

   
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signInSubmit"))
    )
    sign_in_button.click()

    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nav-link-accountList"))
    )
    print("  Login Successful!")


    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("Wired Earphones", Keys.RETURN)

    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")  

    
    try:
        print("🔹 Clicking on 'Proceed to Buy'...")
        proceed_to_buy_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "proceedToRetailCheckout"))
        )
        proceed_to_buy_button.click()
    except Exception as e:
        print(f"  ERROR: Could not find 'Proceed to Buy' button! {e}")
        # driver.quit()
        exit()

    try:
        
        print("🔹 Waiting for the payment method section to load...")

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Another payment method')]"))
        )

        
        print("🔹 Selecting 'Other UPI Apps' payment method...")
        # upi_radio_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and following-sibling::span[contains(text(),'Other UPI Apps')]]"))
        # )
        # driver.execute_script("arguments[0].click();", upi_radio_button)
        # Wait for the radio button to be clickable
        upi_radio_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio' and @name='ppw-instrumentRowSelection'])[last()-2]")))
        upi_radio_button.click()
        print(" Selected 'Other UPI Apps'.")

        
        print("🔹 Waiting for the UPI input field to load after selecting 'Other UPI Apps'...")
        time.sleep(2)  

        upi_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter UPI ID' or @name='ppw-other-upi-id']"))
        )
        
        print("🔹 Entering UPI ID...")
        upi_input.clear()
        upi_input.send_keys("abhishekbhowmik990@ybl")
        print("Entered UPI ID.")

        
        print("🔹 Clicking 'Verify' button...")
        # verify_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Verify')]"))
        # )
        # driver.execute_script("arguments[0].click();", verify_button)

        verify_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='ppw-widgetEvent:ValidateUpiIdEvent']"))
        )
        verify_button.click()
        print(" Clicked 'Verify'.")

        
        print("🔹 Clicking 'Use this payment method' button...")
        use_payment_method_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='secondary-continue-button']"))
        )
        use_payment_method_button.click()
        print("Final Payment Confirmation")

        try:
            print("🔹 Checking for 'No Thanks' button...")
            no_thanks_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a#prime-interstitial-nothanks-button"))
            )
            no_thanks_button.click()

            print("Clicked 'No Thanks' button.")
        except:
            print("No Thanks button not found, skipping...")

        print("🔹 Clicking 'Pay Now' button...")
        pay_now_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submitOrderButtonId"))
        )

        pay_now_button.click()
        print("🔹 Clicked 'Pay Now' button...")

    except Exception as e:
        print(f" ERROR: Could not complete UPI selection. {e}")
        # driver.quit()
        # exit()

except Exception as e:
    print(f" ERROR: {e}")
    # driver.quit()
    # exit()

finally:
    input("🔹 Press Enter to close the browser manually...")
   # driver.quit()