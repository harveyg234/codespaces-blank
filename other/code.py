import pandas as pd
import matplotlib.pyplot as plt
 
def menu():
    while True:
        print("######################################################")


        print("Welcome to RBSX Group Ltd\n")
        print("Select one of the available options:")
        print("1. Which conversion would you like to make today? ")
        print("2. Compare GBP with other currencies")
        print("3. Select the currency for performance check")
        choice = input()
        if choice.isdigit() and int(choice) == 1:
            print("1. Pound Sterling (GBP) to Euros (EUR)")
            print("2. Euros (EUR) to Pound Sterling (GBP)")
            print("3. Pound (GBP) to Australian Dollars (AUD)")
            print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
            print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
            print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
            print("7. Pound Sterling (GBP) to American Dollar (USD)")
            print("8. American Dollar(USD) to Pound Sterling (GBP)")
            print("######################################################")
            return choice
        elif choice.isdigit() and int(choice) == 2:
            print(" comparison matrix")
            df = pd.read_csv("Task4a_RBSX_data.csv")
            df.drop_duplicates(inplace = True)
            df['Date'] = pd.to_datetime(df['Date'], format='mixed')              
            abc={}
            for c in df.columns:
                if(c.startswith("GBP")):
                    # abc[c]=float(df[c].max())
                    abc.update({"the value of 1"+c[:3]+"in"+c[-3:]:float(df[c].max())})
            print("max value for GBP over 12 week period = ")
            print(abc)
            se=pd.Series(abc)
            se.plot()
            plt.show()
    
        elif choice.isdigit() and int(choice) == 3:
            print("######################################################")
            print("Currency Performance Check")
            print("######################################################")
            print("Select a currency pair to check performance:")
            print("1. GBP +AC0- EUR (British Pound to Euros)")
            print("2. EUR +AC0- GBP (Euros to British Pound)")
            print("3. GBP +AC0- AUD (British Pound to Australian Dollars)")
            print("4. AUD +AC0- GBP (Australian Dollars to British Pound)")
            print("5. GBP +AC0- JPY (British Pound to Japanese Yen)")
            print("6. JPY +IBM- GBP (Japanese Yen to British Pound)")
            print("7. GBP +AC0- USD (British Pound to US Dollar)")
            print("8. USD +AC0- GBP (US Dollar to British Pound)")
            print("######################################################")
            
            currency_choice = input("Enter your choice (1-8): ")
            
            if currency_choice.isdigit() and 1 <= int(currency_choice) <= 8:
                currency_pair = get_currency(currency_choice)
                performance_check(currency_pair)
            else:
                print("Sorry, you did not enter a valid choice")

def get_currency(menu_choice):
    currencies = {
        '1': 'GBP +AC0- EUR',
        '2': 'EUR +AC0- GBP',
        '3': 'GBP +AC0- AUD',
        '4': 'AUD +AC0- GBP',
        '5': 'GBP +AC0- JPY',
        '6': 'JPY +IBM- GBP',
        '7': 'GBP +AC0- USD',
        '8': 'USD +AC0- GBP',
    }
    return currencies.get(menu_choice)
 
def get_conversion_rate(currency):
    df = pd.read_csv("Task4a_RBSX_data.csv") #read the .csv file
    df.drop_duplicates(inplace = True) #remove duplicate terms
    df['Date'] = pd.to_datetime(df['Date'], format='mixed') #sorts the dates in accending order
    return round(df[currency].iloc[-1], 2) #Rounds the currency to 2 decimial places
 
def get_amount_to_convert():
    while True:
        amount = input("Please enter the amount you wish to convert: ")
        try:
            return float(amount)
        except ValueError:
            print("Sorry, you must enter a numerical value")
 
def perform_conversion(amount, rate, currency):
    received = round(amount * rate, 2)
    print("##################################")
    print(f"You are converting {amount} {currency[:3]}")
    print(f"You will receive {received} {currency[-3:]}")
    print()
    a=input("Do you wish to continue (Y/N) : ")
    return a

def performance_check(currency_pair):
    """Analyze and display performance metrics for a selected currency pair"""
    try:
        df = pd.read_csv("Task4a_RBSX_data.csv")
        df.drop_duplicates(inplace=True)
        
        # --- FIX 1: Strict Date Formatting ---
        # We use format='%d/%m/%Y' so Python knows 01/04 is April 1st, not Jan 4th.
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
        
        # --- FIX 2: Sort by Date immediately ---
        df.sort_values(by='Date', inplace=True)
        
        # Get the currency data (now that df is sorted, this stays in sync)
        currency_data = df[currency_pair]
        
        # Calculate performance Data
        min_value = currency_data.min()
        max_value = currency_data.max()
        avg_value = currency_data.mean()
        start_value = currency_data.iloc[0]
        end_value = currency_data.iloc[-1]
        percent_change = round(((end_value - start_value) / start_value) * 100, 2)
        
        # Display results
        print("\n######################################################")
        print(f"Performance Report for {currency_pair}")
        print("######################################################")
        print(f"Minimum Exchange Rate:  {min_value:.6f}")
        print(f"Maximum Exchange Rate:  {max_value:.6f}")
        print(f"Average Exchange Rate:  {avg_value:.6f}")
        print(f"Starting Rate:          {start_value:.6f}")
        print(f"Ending Rate:            {end_value:.6f}")
        print(f"Percentage Change:      {percent_change}%")
        print("######################################################\n")
        
        # Ask if user wants to see a graph
        graph_choice = input("Would you like to see a graph of this currency pair? (Y/N): ")
        if graph_choice.upper() == 'Y':
            plt.figure(figsize=(12, 6))
            
            # --- FIX 3: The plotting command ---
            # This line was missing in your last attempt! It actually draws the line.
            plt.plot(df['Date'], currency_data, linestyle='-', linewidth=3, color='#9b59b6', label=currency_pair)
            
            plt.title(f"Exchange Rate Performance: {currency_pair}")
            plt.xlabel("Date")
            plt.ylabel("Exchange Rate")
            plt.grid(True, alpha=0.5)
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            plt.savefig("plot2.png", dpi=300)
    
    except FileNotFoundError:
        print("Error: CSV file not found")
    except KeyError:
        print("Error: Currency pair not found in data")
    except Exception as e:
        print(f"Error: {str(e)}")
 
while True:
    menu_choice = menu()
    currency = get_currency(menu_choice)
    rate = get_conversion_rate(currency)
    amount = get_amount_to_convert()
    ab=perform_conversion(amount, rate, currency)
    if ab=='N':
        print("Thank you for using the services of RBSX Group Ltd")
        break
 