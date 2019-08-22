# Base Class for all investments
class Investment:

    def __init__(self, ticker, price, shares):
        self.ticker = ticker
        self.price = price
        self.shares = shares
        self.value = round(price * shares, 2)

current_portfolio = []

num_loops = input("How many investments are in your total portfolio? >> ")

if(num_loops.isdigit() and int(num_loops) < 10):
    for i in range(int(num_loops)):
        ticker = input("Enter Ticker >> ")
        price = float(input("Enter Price >> "))
        shares = int(input("Enter Shares >> "))
        print("\n\n")
        i = Investment(ticker, price, shares)
        current_portfolio.append(i)
else:
    print("Please type in a number.")

print("Just to confirm your input, your portfolio looks like this: ")

value = 0

for i in range(int(num_loops)):
    print(f"You have {current_portfolio[i].shares} of {current_portfolio[i].ticker} currently trading at ${current_portfolio[i].price} per share.")
    value += current_portfolio[i].value
    print("\n")

print(f"Your total portfolio is valued at ${value}.")