from sys import exit
import copy
import math
from yahoo_fin.stock_info import get_live_price
from timeit import default_timer as timer

# TODO: all price variables need 2 decimals
# TODO: Need to figure out a way to raise an exception after certain amount of time has passed

# Base class for all investments
class Investment:

    def __init__(self, ticker, price, shares):
        self.ticker = ticker
        self.price = price
        self.shares = shares
        self.value = round(price * shares, 2)

# Each investment object is placed into this empty list. We access them with bracket notation e.g current_portfolio[0].ticker
current_portfolio = []
value = 0

# Determines how many times we will loop through the portfolio.
num_loops = input("How many investments are in your total portfolio? >> ")

# check to see if user input is a number and that number is less than 15
if(num_loops.isdigit() and int(num_loops) <= 15):
    for i in range(int(num_loops)):

        ticker = input("Enter Ticker >> ")

        try:
            print("Fetching price data...")
            # ! Remove timer code prior to pushing to gh
            start = timer()
            price = round(get_live_price(ticker), 2)
            if price:
                pass
                end = timer()
                print(end - start)
            else:
                raise Exception

            print("\n")
            print(f"{ticker} Current Price >> ${price} ")
            
        except:
            print("Can't read the investment.")
            print("I can't find the price for that investment. ")
            price = round(float(input("Go ahead and enter it manually. >> ")), 2)

        shares = float(input("Enter Shares >> "))
        print("\n")
        i = Investment(ticker, price, shares)
        current_portfolio.append(i)

else:
    print("Please type in a valid number.")
    exit()

# Create deep copy of the current portfolio list of objects to manipulate and use for comparison later
desired_portfolio = copy.deepcopy(current_portfolio)

print("Just to confirm your input, your portfolio looks like this: ")
print("\n")

# Look through all investments and calculate current portfolio value
for i in range(int(num_loops)):
    print(
        f"You have {current_portfolio[i].shares} shares of {current_portfolio[i].ticker} currently trading at ${current_portfolio[i].price} per share.")
    value += current_portfolio[i].value

# Total current portfolio value
value = round(value, 2)

print(f"Your total portfolio is valued at ${value}.")
print("\n")
response = input("Is this correct? yes or no? >> ")
response = response.lower()
print("\n")

if (response == 'y' or response == 'yes'):

    for i in range(len(desired_portfolio)):

        percent = round((current_portfolio[i].value / value) * 100, 2)
        print(
            f"{current_portfolio[i].ticker} represents {percent}% of your portfolio")
        print("\n")

        desired_allocation = float(
            input("What percent would you like it to be? >> "))
        desired_allocation = round(desired_allocation / 100, 2)

        desired_portfolio[i].value = round(desired_allocation * value, 2)

        # If the desired investment value is larger than what you currently have, you need to buy more shares
        if desired_portfolio[i].value > current_portfolio[i].value:
            num_shares = (
                desired_portfolio[i].value - current_portfolio[i].value) / current_portfolio[i].price
            num_shares = math.floor(num_shares)
            desired_portfolio[i].shares += num_shares
            desired_portfolio[i].shares = math.floor(
                desired_portfolio[i].shares)
            print(
                f"You need to buy {num_shares} shares of {current_portfolio[i].ticker}.")
            print("\n")

        elif desired_portfolio[i].value == 0:  # Liquidate the holdings
            desired_portfolio[i].shares = 0
            print(f"You need to sell all of {current_portfolio[i].ticker}.")

        # If the desired investment value is smaller than what you currently have, you need to sell shares
        elif desired_portfolio[i].value < current_portfolio[i].value:
            num_shares = (
                current_portfolio[i].value - desired_portfolio[i].value) / current_portfolio[i].price
            num_shares = math.floor(num_shares)
            desired_portfolio[i].shares -= num_shares
            desired_portfolio[i].shares = math.floor(
                desired_portfolio[i].shares)
            print(
                f"You need to sell {num_shares} shares of {current_portfolio[i].ticker}.")
            print("\n")

        else:
            print("No change on this security.")

elif (response == 'n' or response == 'no'):
    exit()

else:
    print("Invalid entry")
    exit()

# Calculate the value of the rebalanced portfolio
desired_value = 0
for i in range(len(desired_portfolio)):
    desired_value += desired_portfolio[i].value

desired_value = round(desired_value, 2)

# defining slippage as the dollar value of value not reallocated. Simple comparison between old value and new value. Want this to be minimal.
slippage = round(value - desired_value, 2)

print("\n")

# Want to display a check to make sure the user didn't misallocate funds.
print("Let's compare the rebalanced portfolio value to its previous value.")

print(f'''Your old portfolio value was ${value}. 
Your rebalanced portfolio is ${desired_value}. 
These two values should be the same. 
If not, make sure your desired allocation percentages total 100%.
Due to rounding, ${slippage} was not reallocated. 
We want this number to be as low as possible, preferably $0.''')

print("\n")

print("To sum it all up, your rebalanced portfolio should have:")
for i in range(len(desired_portfolio)):
    print(
        f"{desired_portfolio[i].shares} shares of {desired_portfolio[i].ticker}")