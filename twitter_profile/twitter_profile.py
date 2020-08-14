from selenium import webdriver
import time
import csv

class TwitterProfileBot:
  def __init__(self, urls): # no need for user info
    self.driver = webdriver.Chrome()
    self.urls = urls
    self.spanTweets = []
    self.spanFollowers = []

    # Automate for every link in url
    for url in urls:
      # Get url
      self.driver.get(url)
      time.sleep(5)      
      print('\nURL: ' + str(url))

      # Get number of tweets and followers for current profile
      parent_tweetCount = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/div').text
      parent_spanFollowers = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span').text
      
      print('Tweets: ' + str(parent_tweetCount))
      print('Followers: ' + str(parent_spanFollowers))
      
      tweetNum = str(parent_tweetCount)
      followerNum = str(parent_spanFollowers)

      self.spanTweets.append(tweetNum)
      self.spanFollowers.append(followerNum)
      
      # Sleep a bit before moving onto next url
      time.sleep(3)
    
# # Populate url list, these are profile links
# urls = ['https://twitter.com/lovexstereo?lang=en', 'https://twitter.com/candyambulance?lang=en',
# 'https://twitter.com/littlemanmusic?lang=en']


# # Run bot
# test = InstaProfileBot(urls)
# test.driver.close()

# # MAKE CSV
# print('Generating CSV file...')
# fields = ['URL', 'Tweets', 'Followers']
# filename = 'twitter_profile_stats.csv'
# data = []
# for i in range(len(test.urls)): 
#      data.append([test.urls[i], test.spanTweets[i], test.spanFollowers[i]])
#      with open(filename, 'w') as csvfile:
#          csvwriter = csv.writer(csvfile)
#          csvwriter.writerow(fields)
#          csvwriter.writerows(data)

# print('Done!')