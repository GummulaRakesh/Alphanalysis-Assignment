#Stock Investment Allocation

This program allows users to calculate the number of shares to buy from different stocks based on an investment amount and weightage for each stock. It retrieves historical stock prices from Yahoo Finance, allocates the total investment according to the specified weightage, and calculates how many shares of each stock can be bought on each date in the selected date range.

#Features

*Fetches historical stock data from Yahoo Finance using yfinance.
*Allows the user to specify a date range and stock exchange.
*Reads stock tickers and their weightage from a CSV file (Stocks.csv).
*Allocates investment based on stock weightages.
*Calculates how many shares can be bought for each stock on each date.
*Outputs the results as a CSV file, with dates as columns and stock tickers as rows.

#Requirements

1.Python 3.x
2.pandas library
3.yfinance library
4.openpyxl (optional for Excel support)
You can install the required libraries using pip:
	pip install pandas yfinance openpyxl

#Given the Stocks.csv file:

*The CSV file should contain at least two columns: Ticker and Weightage.
*The Ticker column should contain the stock ticker symbols (e.g., AAPL, TCS.NS).
*The Weightage column should contain the weightage for each stock (e.g., 0.2 for 20%).

Example of Stocks.csv:

Ticker,Weightage
AAPL,0.5
TCS.NS,0.3
RELIANCE.NS,0.2

#Run the Program:

*After running the script, you will be prompted to provide the following inputs:
	*Start Date: The start date of the investment (e.g., 2023-01-01).
	*End Date: The end date of the investment (e.g., 2023-12-31).
	*Total Investment Amount: The total amount you are willing to invest (e.g., 10000).
	*Stock Exchange: Choose from the available stock exchanges by entering their short form 
	 (e.g., NS for National Stock Exchange or BO for Bombay Stock Exchange).

#Result:

The script will calculate how many shares can be bought for each stock and output the results in a CSV file.
The file will be saved in a format with dates as columns and stock tickers as rows.
Example of the output format:

Ticker,Weightage,2023-01-01,2023-01-02,2023-01-03
AAPL,0.5,10.5,10.8,11.0
TCS.NS,0.3,20.2,20.3,20.5
RELIANCE.NS,0.2,15.0,15.2,15.3



#Example Usage

$ python stock_investment.py
Enter the start date (YYYY-MM-DD): 2023-01-01
Enter the end date (YYYY-MM-DD): 2023-12-31
Enter the total investment amount: 10000
Select the following Stock Exchange you want:
1.NS(National Stock Exchange)
2.BO(Bombay Stock Exchange)
Just enter the short form only
NS
Enter the file name to save the result(without Extension) 
investment_results
Restructured file saved to: investment_results.csv
Results saved to investment_results
