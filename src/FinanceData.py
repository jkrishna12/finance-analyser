import requests
import os
import pandas as pd
from dotenv import load_dotenv 

class FinanceData:
    def __init__(self, ticker):
        load_dotenv()

        self.api_key = os.getenv('FINANCIAL_MODELLING_API_KEY')

        self.ticker = self.set_ticker(ticker)
        self.balance_sheet_api = None
        self.balance_sheet_df = None

    def set_ticker(self, ticker):

        url = 'https://financialmodelingprep.com/api/v3/stock/list'

        payload = {"apikey" : self.api_key}
        headers = {}

        try:
            response = requests.request("GET", url, headers=headers, params=payload)    

            stock_ticker = pd.json_normalize(response.json())['symbol'].to_list()

            if ticker not in stock_ticker:              
                raise ValueError(f"{ticker} is an invalid ticker name")
            
            return ticker
        
        except requests.exceptions.RequestException as e:
            print('Unable to access the stock list endpoint')
            raise e
        
        except Exception as e:
            raise e

    def get_balance_sheet_api(self):
        """
        """
        url = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/" + self.ticker

        try:

            payload = {"period" : "annual", "apikey" : self.api_key}
            headers = {}

            response = requests.request("GET", url, headers=headers, params=payload)

            self.balance_sheet_api = response.json()

            return 
        
        except Exception as e:

            print('Error accessing balance sheet API')

            raise e

    def get_balance_sheet_df(self):
        """
        """

        self.get_balance_sheet_api()

        self.balance_sheet_df = pd.json_normalize(self.balance_sheet_api)

        return

    def hello(self):
        self.greeting = 'hello'
        return self.greeting
    
test_stock = FinanceData('AAPL')

print(test_stock.ticker)

test_stock.get_balance_sheet_df()

print(test_stock.balance_sheet_df.head())

