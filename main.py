from user_input import get_user_input 


def main():
    
    user_data = get_user_input()
    
    print("\nUser Input Summary:")
    print(f"Stock Symbol: {user_data['symbol']}")
    print(f"Chart Type: {user_data['chart_type']}")
    print(f"Time Series: {user_data['time_series']}")
    print(f"Start Date: {user_data['start_date']}")
    print(f"End Date: {user_data['end_date']}")
    

if __name__ == "__main__":
    main()