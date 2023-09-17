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


# Total Number of apple across all countries
#Total number of orange across all countries


def total_number_of_fruit(fruit: str, data:pd.DataFrame)-> int:
    total_fruit = 0
    for i in data.values():
        if fruit in i:
            total_fruit = i[fruit]["amount"] + total_fruit
    return {"amount": total_fruit, "unit": "pcs", "Product": fruit}
  
result = total_number_of_fruit("apple", fruit_bank)
expected = {"amount": "1300", "unit": "pcs", "product": "orange"}
# assert result == expected()
print(result)



# percentage of amount orange in Bangladesh storage with respect to other stores

def percentage_fruit ( fruit: str,country:str, data1:  pd.DataFrame):
    total_fruit = 0
    for i in data1.values():
        if fruit in i:
            total_fruit = i[fruit]["amount"]
    total = data1[country][fruit]["amount"]
    percentage_of_fruit = (total/total_fruit)/100


    return(percentage_of_fruit)


per = percentage_fruit("orange","india", fruit_bank)

# Consider 4 apple is approximately 1 kg, what is the amount of apple in kg  in total
def amount_of_apple_in_kg(x: str, data: pd.DataFrame):
   total_fruit = 0
   num_fruit_per_kg = 4
   for i in data.values():
    if x in i:
       total_fruit = i[x]["amount"] + total_fruit
   amount_of_apple = total_fruit/num_fruit_per_kg

   return{"amount": amount_of_apple, "unit": "kg", "Product": x}

f = amount_of_apple_in_kg("apple", fruit_bank)
print(f)

#  Consider 5 orange becomes 1 kg, how many oranges are stored

def fruit_in_kg (x: str, data: pd.DataFrame)-> int:
   total_fruit = 0
   fruit_per_kg = 5
   for i in data:
      if x in i:
         total_fruit = i[x]["amount"] + total_fruit
   kg_of_fruit = total_fruit/fruit_in_kg
   return kg_of_fruit