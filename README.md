This Python script automates the process of logging into Amazon India, searching for a product, adding it to the cart, and proceeding to checkout using the UPI payment method.

Features

1. Amazon Login: Logs in using provided credentials.
2. Product Search: Searches for "Wired Earphones" on Amazon.
3. Add Product to Cart: Add the wired Earphone to cart.
4. Cart Management: Navigates to the cart and proceeds to checkout.
5. UPI Payment Selection: Selects "Other UPI Apps" as the payment method.
6. Automated Order Placement: Clicks "Verify UPI", "Use Payment Method", and "Pay Now" buttons.
7. Handles CAPTCHA Manually: If Amazon asks for CAPTCHA, user intervention is required.

Prerequisites

1. Install Python Dependencies: 
Ensure Python is installed, then install the required libraries: pip install selenium twilio

2. Install ChromeDriver: Download Chrome WebDriver that matches the Google Chrome version from here and place it in the project folder or system PATH.

3. Twilio Setup (Optional - SMS Notifications) : If SMS alerts is required for order status, sign up on Twilio and get:
  (a) Account SID
  (b) Auth Token
  (c) Twilio Phone Number

Usage : 

1. Update Credentials : Edit the script and replace placeholders with the credentials:
      AMAZON_EMAIL = "email@example.com"
      AMAZON_PASSWORD = "password"
      TWILIO_ACCOUNT_SID = "twilio-sid"
      TWILIO_AUTH_TOKEN = "twilio-auth-token"
      MY_PHONE_NUMBER = "+91XXXXXXXXXX"

2. Run the Script : Execute the script with: python amazon.py

3.  Solve CAPTCHA (if prompted) : Amazon may show a CAPTCHA for login. We have to Solve it manually, then the script continues automatically.
