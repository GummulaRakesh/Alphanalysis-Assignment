import pandas as pd
import yfinance as yf
from datetime import datetime

def main():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    investment_amount = float(input("Enter the total investment amount: "))

    stock_exchange = input("Select the following Stock Exchange you want:\n1.NS(National Stock Exchange)\n2.BO(Bombay Stock Exchange) \nJust enter the short form only \n")

    stock_exchange = stock_exchange.upper()

    stock_exchange = "." + stock_exchange
    stocks_df = pd.read_csv('Stocks.csv')

    tickers = stocks_df['Ticker'].tolist()
    weightages = stocks_df['Weightage'].tolist()

    stock_data = {}
    for ticker in tickers:
        try:
            string = ticker + stock_exchange
            stock_data[ticker] = yf.download(string, start=start_date, end=end_date).loc[:, "Close"].squeeze()
        except Exception as e:
            print(f"Failed to fetch data for {ticker}: {e}")

    result_data = []
    for ticker, close_prices in stock_data.items():
        if close_prices.empty:
            continue

        weightage = stocks_df[stocks_df['Ticker'] == ticker]['Weightage'].values[0]
        allocated_amount = weightage * investment_amount

        for date, closing_price in close_prices.items():
            if pd.notna(closing_price):
                shares = allocated_amount / closing_price
                result_data.append({
                    'Date': date,
                    'Ticker': ticker,
                    'Weightage': weightage,
                    'Closing Price': close_prices,
                    'Allocated Amount': allocated_amount,
                    'Shares Bought': shares
                })

    result_df = pd.DataFrame(result_data)
    output_file = input("\nEnter the file name to save the result(without Extension) \n")

    output_path = output_file + ".csv"

    wide_df = result_df.pivot(index=['Ticker', 'Weightage'], columns='Date', values='Shares Bought')
    wide_df.columns = wide_df.columns.strftime('%Y-%m-%d')
    wide_df = wide_df.reset_index()

    wide_df.to_csv(output_path, index=False)

    print(f"Restructured file saved to: {output_path}")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
