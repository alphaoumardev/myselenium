import csv
import time

from selenium import webdriver

tags = ['music', 'gaming', 'cooking', 'fashion', 'travel']

driver = webdriver.Chrome()

# Open a CSV file to store the results
with open('channels.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tag', 'Channel'])

    # Loop through each tag
    for tag in tags:
        # Load the search results page for the current tag
        driver.get(f'https://www.youtube.com/results?search_query={tag}&sp=EgIQAg%253D%253D')
        time.sleep(2)  # Wait for the page to load

        # Scroll down the page to load more channels
        last_height = driver.execute_script('return document.documentElement.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
            time.sleep(2)
            new_height = driver.execute_script('return document.documentElement.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height

        # Extract the channel names and store them in the CSV file
        channel_elements = driver.find_elements('xpath', '//*[@id="subscribers"]')

        channel_names = [elem.text for elem in channel_elements]
        for channel_name in channel_names:
            writer.writerow([tag, channel_name])
