import yfinance as yf
import pandas as pd
from requests_html import HTMLSession
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


#Question 1

#Tesla Stock Data
tesla = yf.Ticker("TSLA")
tesla_history = tesla.history(period="max")
tesla_history.reset_index(inplace=True)
print(tesla_history.head())


#Question 2
#Webscraping

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in soup.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue:
            tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])], ignore_index=True)

print(tesla_revenue.head())


# #Question 3


# #GameStop Stock

gme = yf.Ticker("GME")
gme_history = gme.history(period="max")
gme_history.reset_index(inplace=True)
print(gme_history.head())



# #Question 4

#Webscraping
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in soup.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue:
            gme_revenue = pd.concat([gme_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])], ignore_index=True)

print(gme_revenue.head())





# #Question 5

# # Tesla Stock Plot
plt.figure(figsize=(12,5))
plt.plot(tesla_history["Date"], tesla_history["Close"], label="Tesla Stock Price")
plt.title("Tesla Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid()
plt.legend()
plt.show()

#Tesla Revenue Plot
plt.figure(figsize=(12,5))
plt.plot(tesla_revenue["Date"], tesla_revenue["Revenue"], label="Tesla Revenue")
plt.title("Tesla Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.grid()
plt.legend()
plt.show()




# #Question 6

# #GameStop Stock Plot
plt.figure(figsize=(12,5))
plt.plot(gme_history["Date"], gme_history["Close"], label="GameStop Stock Price")
plt.title("GameStop Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid()
plt.legend()
plt.show()

# # GameStop Revenue Plot
plt.figure(figsize=(12,5))
plt.plot(gme_revenue["Date"], gme_revenue["Revenue"], label="GameStop Revenue")
plt.title("GameStop Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.grid()
plt.legend()
plt.show()




