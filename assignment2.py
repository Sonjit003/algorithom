import pandas as pd
fruit_bank = {
    "india": {
        "apple": {"amount": 100, "unit": "pcs"}, 
        "orange": {"amount": 300, "unit": "kg"}
    }, 
    "bangladesh": {
        "apple": {"amount": 500, "unit": "pcs"}, 
        "orange": {"amount": 800, "unit": "kg"}
    },
    "czech-republic": {
        "apple": {"amount": 1000, "unit": "pcs"}, 
        "orange": {"amount": 200, "unit": "kg"}
    },
}

product_prices = {
    "india": {
        "apple": {"price": 3, "unit": "usd"}, 
        "orange": {"price": 7, "unit": "usd"}
    }, 
    "bangladesh": {
        "apple": {"price": 5, "unit": "usd"}, 
        "orange": {"price": 9, "unit": "usd"}
    },
    "czech-republic": {
        "apple": {"price": 15, "unit": "usd"}, 
        "orange": {"price": 20, "unit": "usd"}
    },
}

# Total price of Apple across all storage hubs: Ex: expected = {"apple": ..., "unit": "usd"}


def calculate_apple_price(x, y):
    if x in product_prices and y in product_prices[x] and x in fruit_bank and y in fruit_bank[x]:
        price_per_apple = product_prices[x][y]["price"]
        amount_of_apples = fruit_bank[x][y]["amount"]
        total_price = price_per_apple * amount_of_apples
        return total_price



total_price = calculate_apple_price("czech-republic", "orange")
# print(total_price)


# Total product cost per hub Ex. expected = {"india": ..., "bangladesh": ..., "czech-republic": ..., "unit": "usd"}
def product_cost_per_hub(x: str, data1: pd.DataFrame, data2: pd.DataFrame):
    for x in data1:
        if x in data2 :
            
            price_of_product = (data1[x]["apple"]["price"])*(data2[x]["apple"]["amount"]) + (data1[x]["orange"]["price"])*(data2[x]["orange"]["amount"])
            return price_of_product


p = product_cost_per_hub("india", product_prices, fruit_bank)
# print(p)
        
total_product_cost_per_hub = {}

for hub, fruits in fruit_bank.items():
    
    total_cost = 0
    for fruit, info in fruits.items():

        amount = info["amount"]
        price = product_prices[hub][fruit]["price"]
        
        total_cost += amount * price
       
    total_product_cost_per_hub[hub] = (total_cost)  

print(total_product_cost_per_hub)

# Which hub is more costly in terms of price of total apple and orange combined? 