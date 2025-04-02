import datetime

def get_user_input():
    
    stock_symbol = input("Enter A stock symbol :").strip()
    
    chart_types = ["Bar", "Line"]
    while True:
        chart_type = input("Enter chart type (Bar/Line): ").strip()
        if chart_type in chart_types:
            break
        print("Invalid chart. Enter (Bar or Line).")
        
        
    time_series_options = ["Daily", "Weekly", "Monthly"]
    while True:
        time_series = input("Enter time series (Daily/Weekly/Monthly): ").strip()
        if time_series in time_series_options:
            break
        print("Invalid time series. Enter: Daily, Weekly, Monthly")
        
    
    while True:
        start_date = input("Start date (YYYY-MM-DD): ").strip()
        end_date = input("End date (YYYY-MM-DD): ").strip()
        
        try:
            startDate = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            endDate = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            
            if startDate <= endDate:
                break
            else: 
                print("End date must be after start date.")
        except:
            print("Use YYYY-MM-DD format.")
            
    return {
        "stock_symbol" : stock_symbol,
        "chart_type" : chart_type,
        "time_series" : time_series,
        "start_date" : start_date,
        "end_date" : end_date
    }
        
        
    