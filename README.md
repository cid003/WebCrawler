# BLKBoxSpider
Webcrawler for Instagram/Facebook/Twitter post scraping  
Dependencies required: Selenium, Chromedriver  

## How To Run Appropriate Crawlers
1. Change directory within appropriate webcrawler.
2. Modify the urls list within the scripts with posts that are going to be scraped.
3. Run the command: `py <insta/facebook/twitter>_crawler.py`
4. The resulting data will be saved in the appropriate directory as a CSV file.

## Expected Data Tables Per Script Execution
This section will display expected CSV outputs for each respective webcrawler for Instagram/Facebook/Twitter.

### Instagram
The CSV results from scraping Instagram posts are as shown:  

| URL                                      | Comments | Views | Likes | Date         |
|:---------------------------------------- | -------- | ----- | ----- | ------------ |
| https://www.instagram.com/p/CB1XK-BH5ez/ | 2        | 233   | 37    | Jun 24, 2020 |
| https://www.instagram.com/p/B9y7pTAAW0n/ | 7        | 491   | 91    | Mar 16, 2020 |
| https://www.instagram.com/p/CDuO-OHjeej/ | 3        | 96    | 14    | Aug 10, 2020 |

The CSV results from scraping Instagram profiles are as shown:

| URL                                                 | Posts    | Followers |
|:--------------------------------------------------- | -------- | --------- |
| https://www.instagram.com/lovexstereo/?hl=en        | 2961     | 2256      |
| https://www.instagram.com/candyambulanceband/?hl=en | 640      | 1966      |
| https://www.instagram.com/spenceryenson/?hl=en      | 48       | 6085      |

### Facebook
The CSV results from scraping Facebook posts are as shown:

| URL                                                          | Comments | Views | Likes | Date                 |
|:------------------------------------------------------------ | -------- | ----- | ----- | -------------------- |
| https://www.facebook.com/lovexstereo/videos/855000578361086/ | 6        | 243   | 35    | July 18 at 10:48 AM  |
| https://www.facebook.com/lovexstereo/videos/217040609601399/ | 0        | 50    | 10    | July 31 at 4:03 PM   |

### Twitter
The CSV results from scraping Twitter posts are as shown:

| URL                                                      | Comments | Views | Likes | Date                    |
|:-------------------------------------------------------- | -------- | ----- | ----- | ----------------------- |
| https://twitter.com/BLKBOXapp/status/1286051479946702851 | N/A      | N/A   | 2     | 2:32 PM - Jul 22, 2020  |
| https://twitter.com/BLKBOXapp/status/1273655517823541249 | N/A      | N/A   | 3     | 9:35 AM - Jun 18, 2020  |
