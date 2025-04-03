from user_input import get_user_input 
from api_connection import get_stock_data

def main():
    
    user_data = get_user_input()
    
    print("\nUser Input Summary:")
    print(f"Stock Symbol: {user_data['stock_symbol']}")
    print(f"Chart Type: {user_data['chart_type']}")
    print(f"Time Series: {user_data['time_series']}")
    print(f"Start Date: {user_data['start_date']}")
    print(f"End Date: {user_data['end_date']}")

    stock_data = get_stock_data(
        user_data['stock_symbol'],
        user_data['chart_type'],
        user_data['time_series'],
        user_data['start_date'],
        user_data['end_date']
    )

    if stock_data:
        print("\nStock Data Retrieved:")
        print(stock_data)
    else:
        print("\nFailed to retrieve stock data.")
        
if __name__ == "__main__":
    main()
