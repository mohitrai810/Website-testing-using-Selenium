# Sort Craft Selenium Tests

## Overview
This repository contains Selenium scripts to automate the testing of the Sort Craft website. The scripts interact with and traverse each element of the website to ensure that all functionalities are working as expected.

## Technologies Used
- **Automation Tool:** Selenium
- **Programming Language:** Python

## How to Run
1. Clone the repository: `git clone https://github.com/your-username/sort-craft-selenium`
2. Navigate to the project directory: `cd sort-craft-selenium`
3. Install dependencies:
    ```bash
    pip install selenium
    ```
4. Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
5. Update the script with the path to your WebDriver.
6. Run the script:
    ```bash
    python test_sort_craft.py
    ```

## License
This project is licensed under the MIT License.

## Some demo usage of selenium 
1. from selenium import webdriver
2. from selenium.webdriver.common.by import By
3. driver = webdriver.Chrome('/path/to/chromedriver')
4. driver.get('http://localhost:3000')
5. home_link = driver.find_element(By.LINK_TEXT, 'Home')
6. home_link.click()
7. driver.quit()

