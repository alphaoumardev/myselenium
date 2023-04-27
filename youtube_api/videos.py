import csv

from selenium import webdriver

# Set up Chrome driver
driver = webdriver.Chrome()

# Go to the YouTube channel page
driver.get("https://www.youtube.com/@SampsonBoatCo/videos")

# Wait for the page to load
driver.implicitly_wait(10)

# Get the 3 latest video links
video_links = []
videos = driver.find_elements(by='xpath', value='//*[@id="thumbnail"]')
for video in videos[:3]:
    video_links.append(video.get_attribute('href'))

# Close the driver
driver.quit()

# Write the video links to a CSV file
with open('video_links.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Video Links'])
    for link in video_links:
        writer.writerow([link])

print("Done!")
