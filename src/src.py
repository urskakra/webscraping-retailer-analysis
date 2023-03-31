# Import all the needed libraries.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np


# Get all brand names and corresponding links to sub-pages.

def retailer_scraping (url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    brands_ = soup.find_all("h4", {"class":"u-textUpper"})
    brands = [i.getText() for i in brands_]
    
    description_ = soup.find_all("div", {"class":"page-content"})
    description = [i.getText().strip() for i in description_]

    links_ = soup.find_all("div", {"class":"o-grid o-grid--item"})
    links = [i.find('a').get('href') for i in links_]

    retailer_brands = {
        'Brands': brands,
        'Description': description,
        'Links': links
    }
    
    return pd.DataFrame(retailer_brands)


# Prepare dataframe model for single brand.

def single_brand (url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    product_ = soup.find_all("p", {"class": "block__p"})
    product = [i.getText().strip() for i in product_]

    price_s = soup.find_all("strong", {"class": "price-item price-item--sale"})
    price_sale = [i.getText().replace('£', '').strip() for i in price_s]
    
    brand_ = soup.find_all("h4", {"class": "block__title block__title--small"})
    brand = [i.getText() for i in brand_]

    brand_products = {
        'Product': product,
        'Selling price': price_sale,
        'Brand': brand
    }
    
    return pd.DataFrame(brand_products) 


# Apply single brand dataframe to all brands (and their corresponding links), and join everything in a new dataframe.

def all_brands (column_retailer):   
    column_retailer = column_retailer.apply(lambda x: f"https://www.brotherswestand.com{x}")
        
    all_products = pd.DataFrame()
    
    for i in column_retailer:
        df = single_brand(i)
        
        all_products = pd.concat([all_products, df], ignore_index=True)
            
    return pd.DataFrame(all_products)


# Get info on:
    # all brand names
    # number of products per brand
    # averages on prices
    
# Convert price type to integer.
# Store result as a new dataframe.

def brand_analysis (df):   
    retailers = all_brands (retailer_scraping(url).Links)
    
    retailers['Selling price'] = retailers['Selling price'].apply(lambda x: int(float(x)))

    retailers['Price-point'] = retailers['Selling price'].apply(lambda x: 'low-end' if x <= 40 
                                                                else ('mid-end' if 41 < x < 99 else 'high-end'))
    
    return retailers['Selling price'].groupby(retailers.Brand).describe()


# Add new column, with a price-range for each brand, based on the average price of all products in the 75th percentile.

def price_point_brands (df):
    result = brand_analysis (all_brands)
    
    result['Price-point'] = result['75%'].apply(lambda x: 'low-end' if x <= 40 
                                                 else ('mid-end' if 41 < x < 99 else 'high-end'))
    
    return result


