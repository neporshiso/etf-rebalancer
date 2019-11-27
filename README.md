# ETF-Rebalancer

My old 401k plan had a really simple system that made it easy to rebalance the funds in your portfolio. What this means is that say you had:
- Fund A: 10%
- Fund B: 60%
- Fund C: 30%

You decide you want to change these weights. For example, it could be that you don't like that Fund B is over half of your portfolio and you don't like that concentration.
You could tell the system at my old plan that you want to reallocate your portfolio to:

- Fund A: 30%
- Fund B: 40%
- Fund C: 30%

The purpose of my script is that in my Vanguard portfolio, there is no similar system in place to make it easy for someone to rebalance their account. 

The way the script works is you tell the program how many investments are in the portfolio you'd like to rebalance. You then tell it what your desired allocation to those funds are and it then calculates what trades you need to make to reach your desired portfolio.

## Demo
![](rebalancer.gif)

http://theautomatic.net/yahoo_fin-documentation/