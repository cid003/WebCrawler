from selenium import webdriver
import csv  
class instaBot:
    def __init__(self):
        fields = ['Name', 'date','numofviews','numoflikes','numofcomments']  
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/p/B9y7pTAAW0n/?utm_source=ig_web_copy_link")
        #sleep(2)
        date = self.driver.find_element_by_css_selector('time._1o9PC.Nzb55').get_attribute('title')
        #date = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/div[2]/a/time')
        #print(date.text)
        comments = self.driver.find_elements_by_class_name("Mr508")
        commentarray = [i for i in comments]
        numofcomments = len(commentarray)
        numofviews = self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/span/span')[0].text
        #print(numofviews)
        self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/span')[0].click()
        numoflikes = self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/div/div[4]/span')[0].text
        #print(numoflikes)
        rows = [ ["try", date,numofviews,numoflikes,numofcomments]] 
        # name of csv file  
        filename = "try.csv"
        # writing to csv file  
        with open(filename, 'w') as csvfile:  
            # creating a csv writer object  
            csvwriter = csv.writer(csvfile)  
            # writing the fields  
            csvwriter.writerow(fields)                
            # writing the data rows  
            csvwriter.writerows(rows) 
        
instaBot()