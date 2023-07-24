# Mini project: Webscraping - market research/retailer analysis


## Objective

In this project I was using webscraping methods for market research, in order to evaluate potential retail partners. As a model, I scraped the website of a UK retailer [Brothers we Stand](https://www.brotherswestand.com). They work as a concept store, selling several clothing brands.

The goal was to understand the fit for a brand who would potentially consider selling their product on a wholesale basis through this particular retailer.

## Methods

Working with libraries BeautifulSoup, pandas, regex and numpy.

#### 1. Get all brand names and corresponding links to sub-pages.

#### 2. Prepare dataframe model for single brand. Webscraping:
- products
- prices
- brand name

#### 3. Apply single brand dataframe to all brands (and their corresponding links), and join everything in a new dataframe.

#### 4. Get info on:
- all brand names
- number of products per brand
- averages on prices

#### 5. Add new column, with a price-range for each brand, based on the average price of all products in the 75th percentile.

## Output

As a result, we receive a dataframe to help us analyze the retailer's fit based on:
- which brands are in the retailer's portfolio
- number of products per brand
- price-point of retailed brands

![All brands and products in portfolio](/images/price_point_brands.png)


![Price-point of retailed brands](/images/price_point_analysis.png)



    



