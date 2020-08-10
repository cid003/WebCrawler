from selenium import webdriver
import time

class InstaBot:
  def __init__(self): # no need for user info
    self.driver = webdriver.Chrome()

    # will be a list of urls to automate through, work with one for now
    # get url
    self.driver.get('https://www.instagram.com/p/B9y7pTAAW0n/')
    time.sleep(5)

    # Get the number of comments for current post
    comments_list = self.driver.find_element_by_css_selector('ul.XQXOT.pXf-y')
    num_comments = len(comments_list.find_elements_by_css_selector('ul.Mr508'))
    print('comments: ' + str(num_comments))

    # Get the number of views for current post
    parent_view = self.driver.find_element_by_css_selector('span.vcOH2')
    views = parent_view.find_element_by_tag_name('span').text
    print('views: ' + str(views))

    # Get the number of likes for current post
    parent_view.click()
    parent_likes = self.driver.find_element_by_css_selector('div.vJRqr')
    likes = parent_likes.find_element_by_tag_name('span').text
    print('likes: ' + str(likes))

    # Get the date of current post
    date = self.driver.find_element_by_css_selector('time._1o9PC.Nzb55').get_attribute('title')
    print('date posted: ' + str(date))

test = InstaBot()