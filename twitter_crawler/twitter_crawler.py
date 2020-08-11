from selenium import webdriver
import time
import csv

class TwitterBot:
  def __init__(self, urls):
    self.driver = webdriver.Chrome()
    self.urls = urls
    self.comments = []
    self.views = []
    self.likes = []
    self.dates = []

    # Automate for every link in url
    for url in urls:
      # Get url
      self.driver.get(url)
      time.sleep(5)
      print('\nURL: ' + str(url))

      # Get the number of comments for current post
      # No comments found in Twitter posts


      # Get the number of views for current post
      # Can't see views for Twitter posts

      # Get the number of likes for current post
      likes = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[4]/div/div[2]/div/a/div/span/span').text
      print('Likes: ' + str(likes))
      self.likes.append(likes)

      # Get the date of current post
      date = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[3]/div/div[1]/span[1]/span').text
      print('Date posted: ' + str(date))
      self.dates.append(date)

      # Sleep a bit before moving onto next url
      time.sleep(3)

    # Zip up info and store into a list

urls = ['https://twitter.com/BLKBOXapp/status/1286051479946702851', 'https://twitter.com/BLKBOXapp/status/1273655517823541249']

test = TwitterBot(urls)

test.driver.close()