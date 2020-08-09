# StockPriceGenerator  

Implementing different Methods of Stock Price Simulation:
- Random Walk
- Poisson Jumps
- Swarm 



## Random Walk, aka Diffusion Process  

The usual basic method: generate random draws from a normal distribution with a selected annualized volatility level and scale to a chosen timestep.    

This model is very simple, easy to compute and resource-efficient. But it only models normally distributed stock returns with constant volatility, which is an extremely naïve approach.  

## Poisson Jumps  

[From Wikipedia:](https://en.wikipedia.org/wiki/Jump_process)
```
A jump process is a type of stochastic process that has discrete movements, called jumps, with random arrival times, rather than continuous movement, typically modelled as a simple or compound Poisson process.
```

Basically a Random Walk, with an added chance of a big jump in stock price: the poisson distribution models the frequency of occurence of an event.  

Adding jumps in price simulations is a nice and simple way to simulate "external shocks", such as: 
- Earnings announcement
- Mergers and Acquisition offers  
- Trade War News

This model enables us to correct one of the flaws of the Random Walk: asset prices are not always continuous. This is especially true in legacy financial markets (by this I mean not crypto markets) since most/all products are not traded 24/7 and exchanges implement limits on price movements to avoid cascading liquidations.  

## Swarm  

This is an agent-based simulation process. 

While the previous models were stochastic processes with closed form solutions, this approach simulates the way a market actually runs: 
- First, we generate a pool of Traders, with a given buying/selling power 
- Then, at each step we decide for each trader whether it wants to buy/sell 
- We reconcile the trades done and compute the new market price
- Repeat until target number of periods is reached  

This approach is much less efficient than the previous ones, but it has several benefits:
- It is closer to the way markets actually behave  
- It enables the use of Market State, so you can hook up a State Machine / Markov Process to switch between Bull/Bear/Sideways Markets  

