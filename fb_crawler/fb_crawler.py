from selenium import webdriver
import time
import csv
from selenium.common.exceptions import NoSuchElementException

class InstaBot:
  def __init__(self, urls): # no need for user info
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
        try:
            comment=self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a').text.split(' ')[0]
        except NoSuchElementException:
            comment = 0
        self.comments.append(str(comment))
        print(comment)
        
        # Get the date of current post
        date = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/span[1]/span/a/abbr/span').text
        print(date)
        self.dates.append(date)

        # Get the number of likes for current post
        likes=self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[1]/a/span[2]/span/span').text
        print(likes)
        self.likes.append(likes)
        
        # get the number of views
        self.driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/span[1]/span/a/abbr/span')[0].click()
        # can change based on internet condition
        time.sleep(5)
        #view=self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/span[1]')
        view = self.driver.find_elements_by_class_name('fcg')
        a = [i.text for i in view]
        singleview = str(a[7]).split(' ')[0]
        print(singleview)
        self.views.append(singleview)
        
        
        # Sleep a bit before moving onto next url
        time.sleep(3)

# Populate url list
urls = ['https://www.facebook.com/lovexstereo/videos/855000578361086/','https://www.facebook.com/lovexstereo/videos/217040609601399/']


#make csv
test = InstaBot(urls)
test.driver.close()
fields = ['URL', 'Comments', 'Views', 'Likes', 'Date']
filename = 'fb_stats.csv'
data = []
for i in range(len(test.comments)):
    data.append([test.urls[i],test.comments[i],test.views[i],test.likes[i],test.dates[i]])
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
