from selenium import webdriver
import json
import time

def write_json(new_data, filename='some.json'):
    """Writes information to the json file

    Args:
        new_data (_type_): _description_
        filename (str, optional): _description_. Defaults to 'data.json'.
    """
    
    with open(filename, 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4, ensure_ascii=False)


# Function to scroll to the bottom of the page
def scroll_to_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the new content to load (adjust as needed)