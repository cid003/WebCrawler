from selenium import webdriver
import time
import csv

class InstaProfileBot:
  def __init__(self, urls): # no need for user info
    self.driver = webdriver.Chrome()
    self.urls = urls
    self.spanElement = []
    self.spanPosts = []
    self.spanFollowers = []

    # Automate for every link in url
    for url in urls:
      # Get url
      self.driver.get(url)
      time.sleep(5)      
      print('\nURL: ' + str(url))

      # Get number of posts and followers for current profile, returns a list of elements
      parent_spanElement = self.driver.find_elements_by_css_selector('span.g47SY')
      print('Posts: ' + str(parent_spanElement[0].text))
      print('Followers: ' + str(parent_spanElement[1].text))
      
      spanPosts = str(parent_spanElement[0].text)
      spanFollowers = str(parent_spanElement[1].text)

      self.spanElement.append(parent_spanElement)
      self.spanPosts.append(spanPosts)
      self.spanFollowers.append(spanFollowers)

      # Sleep a bit before moving onto next url
      time.sleep(3)
    
# # Populate url list, these are profile links
# urls = ['https://www.instagram.com/lovexstereo/?hl=en', 'https://www.instagram.com/candyambulanceband/?hl=en',
# 'https://www.instagram.com/spenceryenson/?hl=en']

# # Run bot
# test = InstaProfileBot(urls)
# test.driver.close()

# # MAKE CSV
# print('Generating CSV file...')
# fields = ['URL', 'Posts', 'Followers']
# filename = 'ig_profile_stats.csv'
# data = []
# for i in range(len(test.spanElement)): 
#     data.append([test.urls[i], test.spanPosts[i], test.spanFollowers[i]])
#     with open(filename, 'w') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(fields)
#         csvwriter.writerows(data)

# print('Done!')