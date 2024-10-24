import requests
import os
import pandas as pd
from dotenv import load_dotenv 

class FinanceData:
    def __init__(self, ticker):
        # Assign env variable api key to attribute
        load_dotenv()
        self.api_key = os.getenv('FINANCIAL_MODELLING_API_KEY')

        # initialise relevant attributes
        self.ticker = self.set_ticker(ticker)
        self.balance_sheet_api = None
        self.balance_sheet_df = None
        self.income_statement_api = None
        self.income_statement_df = None
        self.cashflow_statement_api = None
        self.cashflow_statement_df = None

    def set_ticker(self, ticker):
        """
        Ensures that ticker passed to object is acceptable
        """
        # Assign endpoint url, payload and headers
        url = 'https://financialmodelingprep.com/api/v3/stock/list'

        payload = {"apikey" : self.api_key}
        headers = {}

        # access endpoint and check whether stock in list
        try:
            response = requests.request("GET", url, headers=headers, params=payload)    

            # convert to a pandas dataframe, select symbol column and convert to a list
            stock_ticker = pd.json_normalize(response.json())['symbol'].to_list()

            # checks if ticker not in list
            if ticker not in stock_ticker:              
                raise ValueError(f"{ticker} is an invalid ticker name")
            
            return ticker
        
        # raises exception if unable to access endpoint
        except requests.exceptions.RequestException as e:
            print('Unable to access the stock list endpoint')
            raise e
        
        # raises exception if ticker not in list
        except Exception as e:
            raise e

    def get_balance_sheet_api(self):
        """
        This method assigns the json response from the balance sheet endpoint to balance_sheet_api attribute
        """
        # Assign url endpoint, payload and header parameters
        url = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/" + self.ticker

        payload = {"period" : "annual", "apikey" : self.api_key}
        headers = {}

        # access endpoint and assign json response to attribure
        try:

            response = requests.request("GET", url, headers=headers, params=payload)

            self.balance_sheet_api = response.json()

            return 
        
        # raise excpetion if unable to access endpoint
        except Exception as e:

            print('Error accessing balance sheet API')

            raise e

    def get_balance_sheet_df(self):
        """
        Method gets balance sheet api data and stores it as a pandas dataframe in the balance_sheet_df attribute
        """

        # calls get_balance_sheet_api method
        self.get_balance_sheet_api()

        # assigns pandas dataframe to balance_sheet_df
        self.balance_sheet_df = pd.json_normalize(self.balance_sheet_api)

        return

    def get_income_statement_api(self):
        """
        This method assigns the json response from the income statement endpoint to income_statement_api attribute
        """
        # Assign url endpoint, payload and header parameters
        url = 'https://financialmodelingprep.com/api/v3/income-statement/' + self.ticker

        payload = {"period" : "annual", "apikey" : self.api_key}
        headers = {}

        # access endpoint and assign json response to attribute
        try:

            response = requests.request("GET", url, headers=headers, params=payload)

            self.income_statement_api = response.json()
            return
        
        # raise exception if unable to access endpoint
        except Exception as e:

            print("Unable to access income statement api")
            
            raise e

    def get_income_statement_df(self):
        """
        Method gets income statement api data and stores it as a pandas dataframe in the balance_sheet_df attribute
        """
        # calls get_income_statement_api method
        self.get_income_statement_api()

        # assigns pandas dataframe to income_statement_df
        self.income_statement_df = pd.json_normalize(self.income_statement_api)

        return

    def get_cashflow_statement_api(self):
        """
        This method assigns the json response from the income statement endpoint to cashflow_statement_api attribute
        """
        # Assign url endpoint, payload and header parameters
        url = "https://financialmodelingprep.com/api/v3/cash-flow-statement/" + self.ticker

        payload = {"period" : "annual", "apikey" : self.api_key}
        headers = {}

        # access endpoint and assign json response to attribure
        try:

            response = requests.request("GET", url, headers=headers, params=payload)

            self.cashflow_statement_api = response.json()

            return 
        
        # raise excpetion if unable to access endpoint
        except Exception as e:

            print('Error accessing balance sheet API')

            raise e

        return
    
    def get_cashflow_statement_df(self):
        """
        Method gets cashflow statement api data and stores it as a pandas dataframe in the cashflow_statement_df attribute
        """

        # calls get_cashflow_statement_api method
        self.get_cashflow_statement_api()

        # assigns pandas dataframe to cashflow_statement_df
        self.cashflow_statement_df = pd.json_normalize(self.cashflow_statement_api)
        return

    def hello(self):
        self.greeting = 'hello'
        return self.greeting
    
test_stock = FinanceData('AAPL')

print(test_stock.ticker)

print("Balance sheet")
test_stock.get_balance_sheet_df()

print(test_stock.balance_sheet_df.head())

print("Income statement")
test_stock.get_income_statement_df()

print(test_stock.income_statement_df.head())

print("Cashflow statement")
test_stock.get_cashflow_statement_df()

print(test_stock.cashflow_statement_df.head())