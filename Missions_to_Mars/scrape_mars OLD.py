#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[5]:


news_title=soup.find(["h3"])
for heading in soup.find_all(["h3"]):
    print(heading.text.strip())


# In[6]:


newstitle=news_title.text.strip()
print(newstitle)


# In[7]:


url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


# In[8]:


background=browser.find_by_id("full_image")
background.click()


# In[9]:


browser.is_element_present_by_text('more info', wait_time=2)
links_found2 = browser.find_link_by_partial_text('more info')
links_found2.click()


# In[10]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[11]:


url2_image = soup.select_one("figure.lede a img").get("src")
featured_image_url = 'https://www.jpl.nasa.gov' + url2_image
print(featured_image_url)


# In[12]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[13]:


url3 = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url3)


# In[14]:


mars_weather_list = []
find_h=browser.find_by_css('div[class="js-tweet-text-container"] p')
for i in find_h:
    mars_weather_list.append(i.text)


# In[15]:


#print(mars_weather)
mars_weather =  [ mars_weather_list[0]] 
print(mars_weather)


# In[16]:


# put link to image below....DO WE HAVE TO HAVE A LINK?  I AM CONFUSED!!
#mars_weather = ''


# In[17]:


url4 = 'https://space-facts.com/mars/'
browser.visit(url4)


# In[18]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[19]:


tables = pd.read_html(url4)
#tables.column= ("Description","Mars")


# In[20]:


type(tables)


# In[21]:


df = tables[0]
df.columns = ['Description', 'Mars','Earth']


# In[22]:


# axis = 1 is dropping a column, axis = 0 is dropping a row.
df2=df.drop('Earth', axis=1)


# In[23]:


#output to html
df2.to_html('test.html')


# In[24]:


result=df2.to_html()
#print(result)


# In[25]:


url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url5)


# In[26]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[27]:


# Clicking using Splinter properly
hemi1 = browser.find_by_css('h3')
hemi1.click()


# In[28]:


# Struggling to pull out the image src with soup.select_one.  Can only get the first image on the page.
hemi1a = browser.find_by_id('downloads wide-image img')
hemi1a_image = soup.select_one("img").get("src")
hemi1a_image_url = 'https://www.astrogeology.usgs.gov' + hemi1a_image


# In[29]:


print(hemi1a_image_url)


# In[30]:


# MAKING DUMMY URL'S UNTIL I CAN FIGURE OUT HOW TO EXTRACT THEM AND PROPERLY LOAD IN DICTIONARY


url1=hemi1a_image_url
url2="www.cnn.com"
url3="www.github.com"
url4="www.outlook.live.com"
d = {
    'title': [],
    'url': []
}
header_list = soup.find_all(["h3"])

for header_list in soup.find_all(["h3"]):
    d['title'].append(header_list.text.strip())
d['url'].append(url1)
d['url'].append(url2),
d['url'].append(url3),
d['url'].append(url4)
print (d)


# In[31]:


# Added the Splinter clicks required for other images in next few boxes
hemi1 = browser.find_by_css('h3').first
hemi1.click()


# In[32]:


browser.back()


# In[33]:


hemi2 = browser.find_by_css('h3')[1]
hemi2.click()


# In[34]:


browser.back()


# In[35]:


hemi3 = browser.find_by_css('h3')[2]
hemi3.click()


# In[36]:


browser.back()


# In[37]:


hemi4 = browser.find_by_css('h3')[3]
hemi4.click()


# In[38]:


browser.back()


# In[39]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

