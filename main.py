from sys import exit
import copy
import math

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

# Determines how many times we will loop through the portfolio. Only need to loop as much as the portfolio is.
num_loops = input("How many investments are in your total portfolio? >> ")

if(num_loops.isdigit() and int(num_loops) < 10): # check to see if user input is a number and that number is less than 10
    for i in range(int(num_loops)):
        ticker = input("Enter Ticker >> ")
        price = float(input("Enter Price >> "))
        shares = float(input("Enter Shares >> "))
        print("\n")
        i = Investment(ticker, price, shares)
        current_portfolio.append(i)

else:
    print("Please type in a number.")
    exit() 

# Need a deep copy of the current porfolio list of objects to use for comparison later.
desired_portfolio = copy.deepcopy(current_portfolio)

print("Just to confirm your input, your portfolio looks like this: ")

for i in range(int(num_loops)):
    print(f"You have {current_portfolio[i].shares} shares of {current_portfolio[i].ticker} currently trading at ${current_portfolio[i].price} per share.")
    value += current_portfolio[i].value
    print("\n")

value = round(value, 2)

print(f"Your total portfolio is valued at ${value}.")

response = input("Is this correct? yes or no? >> ")
response = response.lower()
print("\n")

if (response == 'y' or response == 'yes'):
    
    for i in range(int(num_loops)):

        percent = round((current_portfolio[i].value / value) * 100, 2)
        print(f"{current_portfolio[i].ticker} represents {percent}% of your portfolio")
        print("\n")

        desired_allocation = float(input("What percent would you like it to be? >> "))
        desired_allocation = round(desired_allocation / 100, 2)

        desired_portfolio[i].value = round(desired_allocation * value, 2)
        print("More debugging >>>")
        print(f">>> Let's check the comparison between desired and current. Desired Investment:  {desired_portfolio[i].ticker} {desired_portfolio[i].value}")
        print(f">>> Let's check the comparison between desired and current. Desired Investment:  {current_portfolio[i].ticker} {current_portfolio[i].value}")
        print("<<<")
        if desired_portfolio[i].value > current_portfolio[i].value:
            print(f">>> NUM SHARES {desired_portfolio[i].value / current_portfolio[i].value}")  # <<< THIS IS THE PROBLEM MATH. FIGURE THIS SHIT OUT 
            num_shares = desired_portfolio[i].value / value   # 0.49999999
            num_shares = math.floor(num_shares)   # NEED TO ADJUST THE NUM SHARES FROM THE CURRENT NUM SHARES BEFORE WE SIMPLY ADD 
            desired_portfolio[i].shares += num_shares
            desired_portfolio[i].shares = math.floor(desired_portfolio[i].shares)
            print(f"You need to buy {num_shares} shares of {current_portfolio[i].ticker}.")
            print("\n")

        elif desired_portfolio[i].value == 0:
            desired_portfolio[i].shares = 0
            print(f"You need to sell all of {current_portfolio[i].ticker}.")

        elif desired_portfolio[i].value < current_portfolio[i].value:
            num_shares = desired_portfolio[i].value / value
            num_shares = math.floor(num_shares)
            desired_portfolio[i].shares -= num_shares
            desired_portfolio[i].shares = math.floor(desired_portfolio[i].shares)
            print(f"You need to sell {num_shares} shares of {current_portfolio[i].ticker}.")
            print("\n")
        
        else:
            print("No Change on this security.")

elif (response == 'n' or response == 'no'):
    exit()

else:
    print("Invalid entry")
    exit()

print("To sum it all up, your rebalanced portfolio should have:")
for i in range(len(desired_portfolio)):
    print(f"{desired_portfolio[i].shares} shares of {desired_portfolio[i].ticker}")
