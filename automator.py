from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from urllib.parse import quote
import os

# Setting up Chrome options
options = Options()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("********************************************************************")
print("********************************************************************")
print("********************************************************************")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ****************")
print("*****This tool was built by  https://github.com/MajidAhangari ******")
print("***** My email majidahangari2015@gmail.com                         ****************")
print("********************************************************************")
print("********************************************************************")
print("********************************************************************")
print(style.RESET)

# Load the message to be sent from a file
with open("message.txt", "r") as f:
    message = f.read()

print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

# Load the list of phone numbers from a file
numbers = []
with open("numbers.txt", "r") as f:
    for line in f.read().splitlines():
        if line.strip() != "":
            numbers.append(line.strip())

total_number = len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 60  # Increased delay

# Initialize the Chrome WebDriver using WebDriver Manager with Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)

# Sending the message to each number
for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx + 1), total_number, number) + style.RESET)
    try:
        url = f'https://web.whatsapp.com/send?phone={number}&text={message}'
        sent = False
        for i in range(3):
            if not sent:
                driver.get(url)
                try:
                    # Wait for the message box to be ready
                    WebDriverWait(driver, delay).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
                    )
                    sleep(1)  # Small delay to ensure the message is loaded

                    # More robust XPath for the send button
                    send_button = WebDriverWait(driver, delay).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send' or @aria-label='Send']"))
                    )
                    
                    # Ensure the button is visible
                    driver.execute_script("arguments[0].scrollIntoView(true);", send_button)  
                    
                    # Diagnostic print to confirm the button is located
                    print(f"Send button found for {number}. Clicking the button...")
                    
                    # Click the send button
                    send_button.click()
                    sent = True
                    sleep(3)  # Wait for the message to be sent
                    print(style.GREEN + 'Message sent to: ' + number + style.RESET)
                except Exception as e:
                    print(style.RED + f"\nFailed to send message to: {number}, retry ({i + 1}/3)")
                    print("Make sure your phone and computer is connected to the internet.")
                    print("If there is an alert, please dismiss it." + style.RESET)
                    print("Exception:", str(e))
    except Exception as e:
        print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)

driver.close()
