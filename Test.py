from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome driver
op = Options()
driver = webdriver.Chrome(options=op)

# Open the URL
driver.get('http://localhost:3000/')
try:
    driver.implicitly_wait(1000)
    wait = WebDriverWait(driver,1000)
    algorithm_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.algorithm-button')))
    in_sh=0
    final_sh=0
    # Click on the Bubble Sort buthon
    for button in algorithm_buttons:
        ## Merge sort
        if button.text.strip() == 'Merge Sort':
            button.click()
            scroll_pause_time = 0.2
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            in_sh=scroll_height
            current_position = 0
            cp=0
            #Down to Languages 
            while current_position < scroll_height:
                current_position += 50
                driver.execute_script(f"window.scrollTo(0, {current_position});")
                time.sleep(scroll_pause_time)
            language_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.language-button')))
            lang_cp=current_position
            for C in language_buttons:
                
                ## C lang
                if C.text.strip() == 'C':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    final_sh=scroll_height
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                        
                ## Java lang
                if C.text.strip() == 'Java':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    
                ## Python lang
                if C.text.strip() == 'Python':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50  
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
            while current_position>cp:
                    current_position -= 50 
                    driver.execute_script(f"window.scrollTo(0, {current_position});")
                    time.sleep(scroll_pause_time)
            button.click()
        ## Bubble sort 
        if button.text.strip() == 'Bubble Sort':
            button.click()
            scroll_pause_time = 0.3 
            current_position = 0
            cp=0
            #Down to Languages 
            while current_position < in_sh:
                current_position += 50 
                driver.execute_script(f"window.scrollTo(0, {current_position});")
                time.sleep(scroll_pause_time)
            language_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.language-button')))
            lang_cp=current_position
            for C in language_buttons:
                ## C lang
                if C.text.strip() == 'C':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                ## Java lang
                if C.text.strip() == 'Java':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < sh:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                ## Python lang
                if C.text.strip() == 'Python':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50  
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
            while current_position>cp:
                    current_position -= 50 
                    driver.execute_script(f"window.scrollTo(0, {current_position});")
                    time.sleep(scroll_pause_time)
            button.click()
            
        #Selection Sort
        if button.text.strip() == 'Selection Sort':
            button.click()
            scroll_pause_time = 0.2  
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            current_position = 0
            cp=0
            #Down to Languages 
            while current_position < scroll_height:
                current_position += 50
                driver.execute_script(f"window.scrollTo(0, {current_position});")
                time.sleep(scroll_pause_time)
            language_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.language-button')))
            lang_cp=current_position
            for C in language_buttons:
                
                ## C lang
                if C.text.strip() == 'C':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                        
                ## Java lang
                if C.text.strip() == 'Java':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    
                ## Python lang
                if C.text.strip() == 'Python':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
            while current_position>cp:
                    current_position -= 50 
                    driver.execute_script(f"window.scrollTo(0, {current_position});")
                    time.sleep(scroll_pause_time)
            button.click()
                    
        ##Radix sort
        if button.text.strip() == 'Radix Sort':
            button.click()
            scroll_pause_time = 0.2 
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            current_position = 0
            cp=0
            #Down to Languages 
            while current_position < scroll_height:
                current_position += 50
                driver.execute_script(f"window.scrollTo(0, {current_position});")
                time.sleep(scroll_pause_time)
            language_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.language-button')))
            lang_cp=current_position
            for C in language_buttons:
                
                ## C lang
                if C.text.strip() == 'C':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                        
                ## Java lang
                if C.text.strip() == 'Java':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    
                ## Python lang
                if C.text.strip() == 'Python':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
            while current_position>cp:
                    current_position -= 50  
                    driver.execute_script(f"window.scrollTo(0, {current_position});")
                    time.sleep(scroll_pause_time)
            button.click()
        
        ##Couting Sort
        
        if button.text.strip() == 'Counting Sort':
            button.click()
            scroll_pause_time = 0.2
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            current_position = 0
            cp=0
            #Down to Languages 
            while current_position < scroll_height:
                current_position += 50 
                driver.execute_script(f"window.scrollTo(0, {current_position});")
                time.sleep(scroll_pause_time)
            language_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.language-button')))
            lang_cp=current_position
            for C in language_buttons:
                
                ## C lang
                if C.text.strip() == 'C':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                        
                ## Java lang
                if C.text.strip() == 'Java':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50  
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    
                ## Python lang
                if C.text.strip() == 'Python':
                    C.click()
                    scroll_height = driver.execute_script("return document.body.scrollHeight")
                    while current_position < scroll_height:
                        current_position += 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
                    while current_position>lang_cp:
                        current_position -= 50 
                        driver.execute_script(f"window.scrollTo(0, {current_position});")
                        time.sleep(scroll_pause_time)
            while current_position>cp:
                    current_position -= 50  
                    driver.execute_script(f"window.scrollTo(0, {current_position});")
                    time.sleep(scroll_pause_time)
            button.click()
    about = driver.find_element(By.XPATH, "//*[contains(text(), 'About')]")
    about.click()
    driver.implicitly_wait(102)
    
    contact = driver.find_element(By.XPATH, "//*[contains(text(), 'Contact')]")
    contact.click()
    driver.implicitly_wait(120)
    
except Exception as e:
    print(f"An error occurred: {e}")

