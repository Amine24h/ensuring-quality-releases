# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

print ('Starting the browser...')
options = ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Start the browser and login with standard_user
def login (user, password):
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    
    print (f'Trying to login a user {user}')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_css_selector("input[id='login-button']").click()

    products_title = driver.find_element_by_css_selector("div[id='header_container'] > div > span.title").text
    if "PRODUCTS" in products_title:
        print("Login successfully. Navigating to the demo page to products")
    else:
        print('ERROR! when login you in!')

def add_products ():
    print ('Adding all products to cart...')
    buttons_add_to_cart = driver.find_elements_by_css_selector("button[class='btn btn_primary btn_small btn_inventory']")
    for button in buttons_add_to_cart:
        button.click()
    
    print ('Removing all products from cart...')
    buttons_remove_from_cart = driver.find_elements_by_css_selector("button[class='btn btn_secondary btn_small btn_inventory']")
    for button in buttons_remove_from_cart:
        button.click()


login('standard_user', 'secret_sauce')
add_products()
