# Scraping Land Fair Prices from E-government Platform

In this project, street by street land fair prices in several districts of Istanbul have been extracted from e-government platform. In order to automate navigation, selenium library has been used since the platform uses javascript to load all contents. Extracted information has been formed into pandas dataframe in desired format and exported to csv or xlsx files.   

Sample Query Forms:
![Query 1](/images/query1.png)
![Query 2](/images/query2.png)

Result Pages of the Queries:
![Result 1](/images/result1.png)
![Result 2](/images/result2.png)

The Result File for Beyoglu District in csv format:

![Result File](/images/result_file.png)

## Requirements

This project requires [selenium](https://pypi.org/project/selenium/) package and web driver in order to automate web navigation and pandas package in order to keep the result in a table and export to csv or xlsx file. 
