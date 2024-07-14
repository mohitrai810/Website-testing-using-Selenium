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
from selenium import webdriver
from selenium.webdriver.common.by import By

# Path to your WebDriver
driver = webdriver.Chrome('/path/to/chromedriver')

# Open the Sort Craft website
driver.get('http://localhost:3000')

# Example: Interact with the Home link
home_link = driver.find_element(By.LINK_TEXT, 'Home')
home_link.click()

# Add more interactions here

# Close the browser
driver.quit()

