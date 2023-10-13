from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import os
import urllib.parse
import requests

# set up selenium
service = Service('msedgedriver.exe')
driver = webdriver.Edge(service=service)

# get product urls
with open("links.txt", "r") as file:
    urls = file.readlines() 

# create and go to products directory
root_dir = 'products'
if not os.path.exists(root_dir):
    os.mkdir(root_dir)
os.chdir(root_dir)

# iterate through link of every product
for url in urls:
    url = url.strip()
    
    # create an id for the current product
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path.lstrip("/")
    id = "".join(c if c.isalnum() or c in ('_', '-') else '_' for c in path)

    if not os.path.exists(id):
        driver.get(url) # connect
        
        os.mkdir(id)
        # get product details
        parent_element = driver.find_element(By.XPATH, "//body[1]/div[1]/div[3]/div[1]/div[2]")
        name = parent_element.find_element(By.XPATH,".//div[1]/span[1]")
        price = parent_element.find_element(By.XPATH,".//div[1]/div[1]/h4[1]")
        sizes = parent_element.find_element(By.XPATH,".//div[2]/div[1]/div[1]")
        desc = driver.find_element(By.XPATH,"//body[1]/div[1]/div[3]/div[1]/div[2]/div[3]/div[1]")
        details = "ID: " + id + "\nLink: " + url + "\nTitle: " + name.text + "\nPrice: " + price.text + "\nSizes:\n" + sizes.text + "\nDescription:\n" + desc.text
        details = '\n'.join(details.split('\n')[:-1]) # remove "More Information" part
        with open(f'{id}/details.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(details)

        # download images
        os.mkdir(f'{id}/images')
        images = driver.find_elements(By.XPATH, "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]//img") 
        image = driver.find_element(By.XPATH, "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/img[1]")
        for i in range(len(images)):
            images[i].click()
            current_image_link = image.get_attribute('src')
            response = requests.get(current_image_link)
            file_name = f'image_{i}.webp'
            file_path = f'{id}/images/{file_name}'
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"Image {i} for {id} downloaded successfully as '{file_name}'")
            else:
                print(f"Failed to download image {i} for {id}. Status code:", response.status_code)
    else:
        print("This product's directory already exists. Skipped.")
driver.quit()