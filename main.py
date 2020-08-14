from insta_crawler.insta_crawler import InstaBot
from fb_crawler.fb_crawler import FacebookBot
from twitter_crawler.twitter_crawler import TwitterBot
from insta_profile.insta_profile import InstaProfileBot
from twitter_profile.twitter_profile import TwitterProfileBot
from selenium import webdriver
import time
import csv

# load the list of urls here, 5 separate .txt files => 5 CSV files
# get lists of posts from facebook, twitter, and instagram 
# get lists of profiles from facebook, twitter, and instagram
def readLinks(urls):
	f = open(urls, "r")
	f1 = f.readlines()
	result = []
	for x in f1:
		result.append(str(x))
	f.close()
	return result
	
IGPostURLS = readLinks('igpost_urls.txt')
IGProfileURLS = readLinks('igprofile_urls.txt')
FacebookURLS = readLinks('fbpost_urls.txt')
TwitterPostURLS = readLinks('twitterpost_urls.txt')
TwitterProfileURLS = readLinks('twitterprofile_urls.txt')

# to-do: call imported scripts here
# Scrape IG Posts
IGPostBot = InstaBot(IGPostURLS)
IGPostBot.driver.close()

# Make CSV
print('Generating CSV file for IG posts...')
fields = ['URL', 'Comments', 'Views', 'Likes', 'Date']
filename = 'instagram_stats.csv'
data = []
for i in range(len(IGPostBot.comments)):
    data.append([IGPostBot.urls[i], IGPostBot.comments[i], IGPostBot.views[i], IGPostBot.likes[i], IGPostBot.dates[i]])
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
print('Generated IG post stats!')

# Scrape IG Profiles
IGProfileBot = InstaProfileBot(IGProfileURLS)
IGProfileBot.driver.close()

# Make CSV
print('Generating CSV file for IG profiles...')
fields = ['URL', 'Posts', 'Followers']
filename = 'ig_profile_stats.csv'
data = []
for i in range(len(IGProfileBot.spanElement)): 
    data.append([IGProfileBot.urls[i], IGProfileBot.spanPosts[i], IGProfileBot.spanFollowers[i]])
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)
print('Generated IG profile stats!')

# Scrape FB Posts
FBPostBot = FacebookBot(FacebookURLS)
FBPostBot.driver.close()

# Make CSV
print('Generating CSV file for FB posts...')
fields = ['URL', 'Comments', 'Views', 'Likes', 'Date']
filename = 'fb_stats.csv'
data = []
for i in range(len(FBPostBot.comments)):
    data.append([FBPostBot.urls[i], FBPostBot.comments[i], FBPostBot.views[i], FBPostBot.likes[i], FBPostBot.dates[i]])
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
print('Generated FB post stats!')

# Scrape Twitter Posts
TwitterPostBot = TwitterBot(TwitterPostURLS)
TwitterPostBot.driver.close()
# Make CSV
print('Generating CSV file for Twitter posts...')
fields = ['URL', 'Comments', 'Views', 'Likes', 'Date']
filename = 'twitter_stats.csv'
data = []
for i in range(len(TwitterPostBot.urls)):
    data.append([TwitterPostBot.urls[i], 'N/A', 'N/A', TwitterPostBot.likes[i], TwitterPostBot.dates[i]])
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
print('Generated Twitter post stats!')

# Scrape Twitter Profiles
TwProfileBot = TwitterProfileBot(TwitterProfileURLS)
TwProfileBot.driver.close()
# Make CSV

print('Generating CSV file for Twitter profiles...')
fields = ['URL', 'Tweets', 'Followers']
filename = 'twitter_profile_stats.csv'
data = []
for i in range(len(TwProfileBot.urls)): 
     data.append([TwProfileBot.urls[i], TwProfileBot.spanTweets[i], TwProfileBot.spanFollowers[i]])
     with open(filename, 'w') as csvfile:
         csvwriter = csv.writer(csvfile)
         csvwriter.writerow(fields)
         csvwriter.writerows(data)

print('Generated Twitter profile stats!')
print('Successfully executed data scraping!')
print('Exiting...')