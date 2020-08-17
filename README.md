# BLKBoxSpider
Webcrawler for Instagram/Facebook/Twitter post scraping  
Dependencies required: Selenium, Chromedriver  

## Dependency Setup
Follow these steps depending on which OS is being used to set up Chromedriver

**BEFORE setting up Chromedriver you must have Chrome installed and know what version of Chrome you are using**
You can figure this out by opening the menu on the top-right of your browser -> Help -> About Google Chrome  
The version number can be found there. [Please download the correct Chromedriver for your version](https://chromedriver.chromium.org/downloads)
(**Use the link only if you are a Windows user**)

### Windows
1. Extract the Chromedriver.exe and save it somewhere that is appropriate for an application to be saved in;  
possibly in the local disk.
2. Open control panel and navigate to (System and Security) -> (System) -> (Advanced System Settings) -> (Environment Variables)
3. Under the system variables section, highlight 'Path' and click 'Edit' then click 'New'
4. Figure out the full directory path of the Chromedriver.exe and provide that value as a new system variable path
5. You are now able to run Chromedriver; open command prompt and enter the command `chromedriver`, a prompt will show if you properly installed it.

### Mac
1. Open terminal and enter the command: `brew cask install chromedriver`
2. You are now able to run Chromedriver; open command prompt and enter the command `chromedriver`, a prompt will show if you properly installed it.

## How to run the webcrawler
1. Update the txt files of all sites to crawl.
2. Under the assumption that the user is on a MacOS, navigate to the text files by going into the `dist` folder.
3. Right click on main to open file options, click Show Package Contents. 
4. Navigate to `Contents`, then `Resources`.
5. From here, update **ALL** *.txt files that are seen within this folder with the urls that are appropriate to the
text file's name. e.g. fbpost_urls.txt should have urls that are ONLY Facebook posts.
6. Once the text files are updated. Navigate out of the `Resources` folder and access the `MacOS` folder.
7. Run the `main` Unix executable.

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

| URL                                                      | Comments | Views | Likes | Date           |
|:-------------------------------------------------------- | -------- | ----- | ----- | -------------- |
| https://twitter.com/BLKBOXapp/status/1286051479946702851 | N/A      | N/A   | 2     |  Jul 22, 2020  |
| https://twitter.com/BLKBOXapp/status/1273655517823541249 | N/A      | N/A   | 3     |  Jun 18, 2020  |

The CSV results from scraping Twitter profiles are as shown:

| URL                                            | Tweets           | Followers |
|:---------------------------------------------- | ---------------- | --------- |
| https://twitter.com/lovexstereo?lang=en        | 3,685 Tweets     | 1882      |
| https://twitter.com/candyambulance?lang=en     | 127 Tweets       | 121       |
| https://twitter.com/littlemanmusic?lang=en     | 1,217 Tweets     | 554       |