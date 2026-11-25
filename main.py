import requests
import requests_cache
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = "e26e5f2c7fb94a7ba54f5135830a6c96"
STOCK_API_KEY = "78LPWCZN2PP4E5LM"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

session = requests_cache.CachedSession(
    "api_cache",
    expire_after=3600
)

news_params = {
    "q": COMPANY_NAME,
    "language": "en",
    "pageSize": 1,
    "apiKey": NEWS_API_KEY,
}

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY
}

def day_before(str_date):
    date_obj = datetime.datetime.strptime(str_date, "%Y-%m-%d").date()
    day_before_date = date_obj - datetime.timedelta(days=1)
    return day_before_date.strftime("%Y-%m-%d")

def check_percentage_change(today_close, yesterday_close):
    today_close = float(today_close)
    yesterday_close = float(yesterday_close)
    percentage_change = ((today_close - yesterday_close) / yesterday_close) * 100
    return percentage_change

stock_response = session.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]
print("Stock: Cache status:", "From Cache" if stock_response.from_cache else "From API")

today_dict = {key: value["4. close"] for key, value in stock_data.items()}
first_two = dict(list(today_dict.items())[:2])
print(first_two)


today = datetime.date.today().strftime("%F")

is_today_available = True
is_yesterday_available = True
# today = "2026-11-24"
print(f"Real Today: {today}")

while is_today_available:
    print(today)
    if today not in first_two:
        today = day_before(today)
        print(f"Today is not available in the stock data. Checking for the day before: {today}")
        continue
    else:
        print(f"Today is available in the stock data: {today}")
        break

print(f"Today: {today}")

yesterday = day_before(today)

while is_yesterday_available:
    print(yesterday)
    if yesterday not in first_two:
        yesterday = day_before(yesterday)
        print(f"Yesterday is not available in the stock data. Checking for the day before: {yesterday}")
        continue
    else:
        print(f"Yesterday is available in the stock data: {yesterday}")
        break

print(f"Yesterday: {yesterday}")
percentage_change = check_percentage_change(first_two[today], first_two[yesterday])
print(percentage_change)

if percentage_change > 5.0 or percentage_change < -5.0:
    print("Get News")
    news_response = session.get(NEWS_ENDPOINT, params=news_params)
    print("News: Cache status:", "From Cache" if news_response.from_cache else "From API")
    print(news_response.json())




# if today not in first_two:
#     today = day_before(today)
#     print(f"Today is not available in the stock data. Checking for the day before: {today}")
# else:
#     print(f"Today is available in the stock data: {today}")
#     yesterday = day_before(today)
#     print(f"Today: {today}, Yesterday: {yesterday}")
#     if yesterday not in first_two:
#         yesterday = day_before(yesterday)
#         print(f"Yesterday is not available in the stock data. Checking for the day before: {yesterday}")
#     else:
#         print(f"Yesterday is available in the stock data: {yesterday}")


# for limit in range(5):
#     try:
#         if today in first_two:
#             yesterday = day_before(today)
#             print(f"Today: {today}, Yesterday: {yesterday}")
#             if yesterday in first_two:
#                 today_close = first_two[today]
#                 yesterday_close = first_two[yesterday]
#                 percentage_change = check_percentage_change(today_close, yesterday_close)
#                 if percentage_change >= 5.0 or percentage_change <= -5.0:
#                     print("Get News")
#             else:
#                 print("Second date is not available in the stock data.")
#     except KeyError as e:
#         print(f"Date is not available in the stock data: {e}")
#         today = day_before(today)
#     finally:
#         print(f"Next date to check: {today}")
#         today = day_before(today)

    # else:
    #     print("First date is not available in the stock data.")
    #     today = day_before(today)


# print(type(datetime.date.today()))
# print(datetime.timedelta(days=1))
# yesterday = datetime.date.today() - datetime.timedelta(days=1)
# print(yesterday)






# %F Equivalent to %Y-%m-%d, the ISO 8601 format.
# import datetime as dt
# dt.datetime.strptime('31/01/22 23:59:59.999999',
#                      '%d/%m/%y %H:%M:%S.%f')
# datetime.datetime(2022, 1, 31, 23, 59, 59, 999999)
# _.strftime('%a %d %b %Y, %I:%M%p')
# 'Mon 31 Jan 2022, 11:59PM'

2025-10-11, 1001-12-30
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# for date in stock_data:
    # print(stock_data[date]["4. close"])


#     if (float(stock_data[0].get("4. close")) < float(stock_data[1].get("4. close"))):
#         news_response = session.get(NEWS_ENDPOINT, params=news_params)
#         print("News: Cache status:", "From Cache" if news_response.from_cache else "From API") 


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# print(news_response.json())
# print(stock_response.from_cache)  # True if the response was served from cache, False if it was fetched from the API
#check cache status




# time.sleep(5)  # Wait for a second to ensure cache is cleared

# stock_response_lain = session.get(STOCK_ENDPOINT, params=stock_params)
# news_response_lain = session.get(NEWS_ENDPOINT, params=news_params)

# print(stock_response_lain.from_cache)  # True if the response was served from cache, False if it was fetched from the API


# print("Stock: Cache status:", "From Cache" if stock_response_lain.from_cache else "From API")
# print("News: Cache status:", "From Cache" if news_response_lain.from_cache else "From API") 


# time.sleep(11)  # Wait for a second to ensure cache is cleared

# stock_response_lainlain = session.get(STOCK_ENDPOINT, params=stock_params)
# news_response_lainlain = session.get(NEWS_ENDPOINT, params=news_params)

# print(stock_response_lainlain.from_cache)  # True if the response was served from cache, False if it was fetched from the API


# print("Stock: Cache status:", "From Cache" if stock_response_lainlain.from_cache else "From API")
# print("News: Cache status:", "From Cache" if news_response_lainlain.from_cache else "From API") 


# print("Stock: Cache expiration:", "Expired" if stock_response.is_expired else "Not expired")
# print("News: Cache expiration:", "Expired" if news_response.is_expired else "Not expired")

# print("Stock: Live data contained in Cache:", "Saved " if session.cache.contains(stock_response.url) else "Not saved")
# print("News: Live data contained in Cache:", "Saved " if session.cache.contains(news_response.url) else "Not saved")

# time.sleep(5)  # Wait for a second to ensure cache is cleared

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

