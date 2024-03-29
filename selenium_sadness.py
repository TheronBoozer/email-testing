from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



def ask_gpt():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = 'https://chat.openai.com/authorize'
    
    driver.get(url)

    prompt_box = driver.find_element(By.ID, "prompt-textarea")
    print(prompt_box.text)