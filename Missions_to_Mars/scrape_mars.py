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


# In[ ]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[ ]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


news_title=soup.find(["h3"])
for heading in soup.find_all(["h3"]):
    print(heading.text.strip())


# In[ ]:


newstitle=news_title.text.strip()
print(newstitle)


# In[ ]:


url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


# In[ ]:


background=browser.find_by_id("full_image")
background.click()


# In[ ]:


browser.is_element_present_by_text('more info', wait_time=2)
links_found2 = browser.find_link_by_partial_text('more info')
links_found2.click()


# In[ ]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


url2_image = soup.select_one("figure.lede a img").get("src")
featured_image_url = 'https://www.jpl.nasa.gov' + url2_image
print(featured_image_url)


# In[ ]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


url3 = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url3)


# In[ ]:


mars_weather_list = []
find_h=browser.find_by_css('div[class="js-tweet-text-container"] p')
for i in find_h:
    mars_weather_list.append(i.text)


# In[ ]:


#print(mars_weather)
mars_weather =  [ mars_weather_list[0]] 
print(mars_weather)


# In[ ]:


# put link to image below....DO WE HAVE TO HAVE A LINK?  I AM CONFUSED!!
#mars_weather = ''


# In[ ]:


url4 = 'https://space-facts.com/mars/'
browser.visit(url4)


# In[ ]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


tables = pd.read_html(url4)
#tables.column= ("Description","Mars")


# In[ ]:


type(tables)


# In[ ]:


df = tables[0]
df.columns = ['Description', 'Mars','Earth']


# In[ ]:


# axis = 1 is dropping a column, axis = 0 is dropping a row.
df2=df.drop('Earth', axis=1)


# In[ ]:


#output to html
df2.to_html('test.html')


# In[ ]:


result=df2.to_html()
#print(result)


# In[3]:


url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url5)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[5]:


hemisphere_image_urls = []

# First, get a list of all of the hemispheres
links = browser.find_by_css("a.product-item h3")

# Next, loop through those links, click the link, find the sample anchor, return the href
for i in range(len(links)):
    hemisphere = {}
    
    # We have to find the elements on each loop to avoid a stale element exception
    browser.find_by_css("a.product-item h3")[i].click()
    
    # Next, we find the Sample image anchor tag and extract the href
    sample_elem = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
    # Get Hemisphere title
    hemisphere['title'] = browser.find_by_css("h2.title").text
    
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    
    # Finally, we navigate backwards
    browser.back()


# In[6]:


print(hemisphere_image_urls)

