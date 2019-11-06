{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mars InSight's Mole Has Partially Backed Out of Its Hole\n",
      "After making progress over the past several weeks digging into the surface of Mars, InSight's mole has backed about halfway out of its hole this past weekend.\n"
     ]
    }
   ],
   "source": [
    "#NASA Mars News\n",
    "\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome')\n",
    "\n",
    "url1 = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url1)\n",
    "\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "\n",
    "article = soup.find('div', class_='image_and_description_container')\n",
    "\n",
    "title = article.h3.text\n",
    "summary = article.div.text\n",
    "\n",
    "print(title)\n",
    "print(summary)\n",
    "\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA18284_ip.jpg\n",
      "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA18284\n",
      "Stuck on the Rings\n"
     ]
    }
   ],
   "source": [
    "#JPL Mars Space Images - Featured Image\n",
    "\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome')\n",
    "\n",
    "url2 = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "\n",
    "browser.visit(url2)\n",
    "\n",
    "url_string = \"https://www.jpl.nasa.gov\"\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "\n",
    "featured = soup.find('div', class_='carousel_items')\n",
    "\n",
    "image_url = featured.a.get('data-fancybox-href')\n",
    "data_url = featured.a.get('data-link')\n",
    "image_link = f'{url_string}{image_url}'\n",
    "data_link = f'{url_string}{data_url}'\n",
    "description = featured.article.get('alt')\n",
    "\n",
    "print(image_link)\n",
    "print(data_link)\n",
    "print(description)\n",
    "\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 334 (2019-11-04) low -100.0ºC (-148.1ºF) high -23.8ºC (-10.8ºF)\n",
      "winds from the SSW at 5.1 m/s (11.4 mph) gusting to 19.9 m/s (44.4 mph)\n",
      "pressure at 7.00 hPa\n",
      "https://t.co/D4EX1MROay\n"
     ]
    }
   ],
   "source": [
    "#Mars Weather\n",
    "\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome')\n",
    "\n",
    "url3 = \"https://twitter.com/marswxreport?lang=en\"\n",
    "\n",
    "browser.visit(url3)\n",
    "\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "\n",
    "tweet = soup.find('p', class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\")\n",
    "\n",
    "mars_weather = tweet.contents[0]\n",
    "tweet_link = tweet.contents[1].get('href')\n",
    "\n",
    "print(mars_weather)\n",
    "print(tweet_link)\n",
    "\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-153 to 20 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mars - Earth Comparison             Mars            Earth\n",
       "0               Diameter:         6,779 km        12,742 km\n",
       "1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "2                  Moons:                2                1\n",
       "3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "4         Length of Year:   687 Earth days      365.24 days\n",
       "5            Temperature:    -153 to 20 °C      -88 to 58°C"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Mars Facts\n",
    "\n",
    "url4 = \"https://space-facts.com/mars/\"\n",
    "\n",
    "tables = pd.read_html(url4)\n",
    "\n",
    "mars_earth = pd.DataFrame(tables[0])\n",
    "\n",
    "mars_facts = pd.DataFrame(tables[1])\n",
    "\n",
    "mars_facts.to_html(\"mars_facts.html\")\n",
    "mars_facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere\n",
      "/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg\n",
      "----------\n",
      "Schiaparelli Hemisphere\n",
      "/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg\n",
      "----------\n",
      "Syrtis Major Hemisphere\n",
      "/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg\n",
      "----------\n",
      "Valles Marineris Hemisphere\n",
      "/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg\n",
      "----------\n",
      "['Cerberus Hemisphere', 'Schiaparelli Hemisphere', 'Syrtis Major Hemisphere', 'Valles Marineris Hemisphere']\n",
      "['https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg', 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg', 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg', 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg']\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome')\n",
    "\n",
    "url5 = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "url_text = \"https://astrogeology.usgs.gov\"\n",
    "\n",
    "browser.visit(url5)\n",
    "\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "\n",
    "hemispheres = soup.find_all('div', class_='item')\n",
    "\n",
    "\n",
    "titles = []\n",
    "urls = []\n",
    "\n",
    "for item in hemispheres:\n",
    "    title = item.h3.text\n",
    "    title = title.replace(' Enhanced', '')\n",
    "    titles.append(title)\n",
    "    print(title)\n",
    "    \n",
    "    browser.click_link_by_partial_text(title)\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "\n",
    "    image = soup.find('img', class_='wide-image')\n",
    "    link = image.get('src')\n",
    "    urls.append(f'{url_text}{link}')\n",
    "    print(link)\n",
    "    \n",
    "    browser.visit(url5)\n",
    "    print(\"----------\")\n",
    "    time.sleep(5)\n",
    "    \n",
    "print(titles)\n",
    "print(urls)\n",
    "\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Cerberus Hemisphere': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg',\n",
       " 'Schiaparelli Hemisphere': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg',\n",
       " 'Syrtis Major Hemisphere': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg',\n",
       " 'Valles Marineris Hemisphere': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_urls = dict(zip(titles, urls))\n",
    "\n",
    "hemisphere_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
