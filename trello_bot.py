from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import json
from datetime import date

EDGE_DRIVER_PATH=os.path.join(os.getcwd(), 'msedgedriver.exe')
# OP=webdriver.EdgeOptions()
# OP.add_argument('--headless')
service = Service(executable_path=EDGE_DRIVER_PATH)
DRIVER = webdriver.Edge(service=service)

def login():
    with open('config.json')as configFile:
        credentials=json.load(configFile)
        time.sleep(1)
        login_button = WebDriverWait(DRIVER, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="BXP-APP"]/header/div/div[1]/div[2]/a[1]')))
        login_button.click()
        time.sleep(2)
        Username=WebDriverWait(DRIVER,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        Username.click()
        Username.clear()
        Username.send_keys(credentials["USERNAME"])
        time.sleep(2)
        Continue=WebDriverWait(DRIVER,5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-178ag6o')))
        Continue.click()
        Password=WebDriverWait(DRIVER,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
        Password.click()
        Password.clear()
        Password.send_keys(credentials["PASSWORD"])
        Continue=WebDriverWait(DRIVER,5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-178ag6o')))
        Continue.click()
        
def navigating_the_board():
    time.sleep(2)
    Board=WebDriverWait(DRIVER, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div[1]/a')))
    Board.click()

def writing_in_board():
    Create=WebDriverWait(DRIVER,5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="board"]/li[1]/div/div[3]//button[1]')))
    Create.click()
    textarea=WebDriverWait(DRIVER,5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="board"]/li[1]/div/ol//textarea')))
    textarea.click()
    textarea.send_keys("writing some shit")
    time.sleep(2)
    #posting the do thing in the list
    Send_button=WebDriverWait(DRIVER,5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="board"]/li[1]/div/ol/li[5]/form//button[1]')))
    Send_button.click()

def get_screenshot():
    srttime=date.today().strftime("%m-%d-%Y")
    fpath=os.path.join(os.getcwd(), 'downloads/{}.png'.format(srttime))
    DRIVER.get_screenshot_as_file(fpath)


def main():
    try:
        DRIVER.get("https://trello.com/")
        WebDriverWait(DRIVER, 10).until(EC.url_contains('trello.com'))
        login()
        navigating_the_board()
        writing_in_board()
        get_screenshot()
        input("Bot operation completed. Press any key...")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()

if __name__=='__main__':
    main()