from selenium import webdriver
import time

class InstaBot:
  def __init__(self, urls): # no need for user info
    self.driver = webdriver.Chrome()

    # Automate for every link in url
    for url in urls:
      # Get url
      self.driver.get(url)
      time.sleep(5)      
      print('\nURL: ' + str(url))

      # Get the number of comments for current post
      comments_list = self.driver.find_element_by_css_selector('ul.XQXOT.pXf-y')
      num_comments = len(comments_list.find_elements_by_css_selector('ul.Mr508'))
      print('Comments: ' + str(num_comments))

      # Get the number of views for current post
      parent_view = self.driver.find_element_by_css_selector('span.vcOH2')
      views = parent_view.find_element_by_tag_name('span').text
      print('Views: ' + str(views))

      # Get the number of likes for current post
      parent_view.click()
      parent_likes = self.driver.find_element_by_css_selector('div.vJRqr')
      likes = parent_likes.find_element_by_tag_name('span').text
      print('Likes: ' + str(likes))

      # Get the date of current post
      date = self.driver.find_element_by_css_selector('time._1o9PC.Nzb55').get_attribute('title')
      print('Date posted: ' + str(date))

      # Sleep a bit before moving onto next url
      time.sleep(3)

# Populate url list
urls = ['https://www.instagram.com/p/CB1XK-BH5ez/', 'https://www.instagram.com/p/B9y7pTAAW0n/',
        'https://www.instagram.com/p/CDuO-OHjeej/']

# Run the bot
test = InstaBot(urls)
test.driver.close()