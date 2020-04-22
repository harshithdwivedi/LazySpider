import requests 
import uuid
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import urllib

keyword = 'dog'
url = "https://www.pexels.com/search/" + keyword 
def download_image(image_url, image_id):
    with open('./_images/{}.jpeg'.format(image_id), 'wb') as handle:
            response = requests.get(image_url, stream=True)

            if not response.ok:
                print response

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)


browser = webdriver.Chrome()

browser.get(url)
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 200

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_class_name("photo-item")

for post in post_elems:
    id = post.get_attribute("data-photo-modal-medium-id")
    url = "https://www.pexels.com/photo/{}/download".format(id)
    download_image(url, id)
