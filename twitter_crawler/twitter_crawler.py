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