import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the web driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the Amazon website
driver.get("https://www.amazon.com/")

# Search for a product
search_bar = driver.find_element_by_id("twotabsearchtext")
search_bar.send_keys("iPhone 13")
search_bar.submit()

# Click on the first product in the search results
product_link = driver.find_element_by_xpath("//div[@class='a-section a-spacing-small']//h2//a")
product_link.click()

# Add the product to the cart
add_to_cart_button = driver.find_element_by_id("add-to-cart-button")
add_to_cart_button.click()

# Proceed to checkout
proceed_to_checkout_button = driver.find_element_by_id("proceed-to-checkout-button")
proceed_to_checkout_button.click()

# Enter your shipping information
shipping_address = driver.find_element_by_id("shipping-address-1-line1")
shipping_address.send_keys("123 Main Street")
shipping_city = driver.find_element_by_id("shipping-address-1-city")
shipping_city.send_keys("Anytown")
shipping_state = driver.find_element_by_id("shipping-address-1-state")
shipping_state.send_keys("CA")
shipping_zip_code = driver.find_element_by_id("shipping-address-1-postal-code")
shipping_zip_code.send_keys("12345")

# Click on the continue button
continue_button = driver.find_element_by_id("continue-to-payment")
continue_button.click()

# Select your payment method
payment_method = driver.find_element_by_id("payment-method-1")
payment_method.click()

# Enter your credit card information
credit_card_number = driver.find_element_by_id("cc-number")
credit_card_number.send_keys("1234-5678-9012-3456")
expiration_month = driver.find_element_by_id("cc-expiration-month")
expiration_month.send_keys("12")
expiration_year = driver.find_element_by_id("cc-expiration-year")
expiration_year.send_keys("2023")
cvv = driver.find_element_by_id("cc-cvv")
cvv.send_keys("123")

# Click on the place order button
place_order_button = driver.find_element_by_id("place-your-order-button")


