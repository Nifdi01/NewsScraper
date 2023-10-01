from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
from utils import write_json, scroll_to_bottom


links_list = list()


with open('some.json', 'w') as f:
    json.dump([], f)


# Initialize the WebDriver
driver = webdriver.Chrome()




def scrape_data(url):

    # Set the initial number of items and a target number of items to collect
    initial_item_count = 0
    target_item_count = 1  # Adjust as needed


    # Create an empty list to store scraped data
    scraped_data = []

    driver.get(url)
    all_news = driver.find_element(By.XPATH, "//div/h3/a").get_attribute('href')
    driver.get(all_news)

    while initial_item_count < target_item_count:
        # Scroll down to load more items
        scroll_to_bottom()

        # Find the new items that have appeared
        new_items = driver.find_elements(By.XPATH, '//div/a[@class="news-of-day"]')

        # Process and collect information from the new items
        for item in new_items[initial_item_count:]:
            link = item.get_attribute('href')
            links_list.append(link)
            
            print(f"Link: {link}")

        # Update the count of collected items
        initial_item_count = len(new_items)

    for link in links_list:
        driver.get(link)
        title = driver.find_element(By.XPATH, '//div[@class="news-content"]/h2').text
        content = driver.find_element(By.XPATH, '//div[@class="text-content"]').text
        date = driver.find_element(By.XPATH, '//span[contains(@class, "news-inner-date")]').text
        category = driver.find_element(By.XPATH, '//span[contains(@class, "news-category")]').text
        views = driver.find_element(By.XPATH, '//span[contains(@class, "read-count")]').text
        time.sleep(2)
        # Write JSON and print here
        write_json({
            'title': title,
            'category': category,
            'content': content,
            'views': views,
            'date':date,
            'link':link
        })     
    # Close the WebDriver when done
    driver.quit()
    


scrape_data("https://musavat.com")