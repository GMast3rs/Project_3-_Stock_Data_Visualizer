import requests

def get_stock_data(stock_symbol, chart_type, time_series, start_date, end_date):
  base_url = "https://www.alphavantage.co/query"

if time_series == "Daily":
        function = "TIME_SERIES_DAILY"
    elif time_series == "Weekly":
        function = "TIME_SERIES_WEEKLY"
    elif time_series == "Monthly":
        function = "TIME_SERIES_MONTHLY"
    else:
        print("Invalid time series type.")
        return None

params = {
        "function": function,
        "symbol": stock_symbol,
        "apikey": "87NEGSG5QAFMUBW0",  
    }

response = requests.get(base_url, params=params)

if response.status_code == 200:
        stock_data = response.json()
        
        if "Error Message" in stock_data:
            print(f"Error from API: {stock_data['Error Message']}")
            return None
        
        return stock_data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None
