import pygal
from datetime import datetime

def filter_stock_data(stock_data, start_date, end_date):
    #convert into objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    #just checks if daily, weekly and monthly
    time_series_key = None
    for key in stock_data:
        if "Time Series" in key:
            time_series_key = key
            break
    if not time_series_key:
        print("Invalid stock data format.")
        return None, None

    #return the data
    filtered_data = {
        date: float(data['4. close'])
        for date, data in stock_data[time_series_key].items()
        if start_date <= datetime.strptime(date, "%Y-%m-%d") <= end_date
    }

    #sort the data.
    sorted_dates = sorted(filtered_data.keys())
    sorted_prices = [filtered_data[date] for date in sorted_dates]

    return sorted_dates, sorted_prices


def graph_generator(chart_type, dates, prices):

    if chart_type == "Line":
        chart = pygal.Line()
    elif chart_type == "Bar":
        chart = pygal.Bar()
    else:
        print("Somehow got the pass chart check, invalid chart type")
        return
    
    chart.title = "Stock Prices Over Time"
    chart.x_labels = dates
    chart.add("Stock Price", prices)

    chart.render_in_browser()