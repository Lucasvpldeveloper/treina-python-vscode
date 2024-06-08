#!/usr / bin /python  
# -* - coding : utf -8 -* -
produtos = {
    "prod1": 15.39,
    "prod2": 21.75
}

print(produtos)
produtos["prod1"] = 98.75
print(produtos)

produtos["prod1"] = float(input("prod1: "))
produtos["prod2"] = float(input("prod2: "))
print(produtos)
print("A parcela do prod1: {0}, prod2: {1}".format(produtos["prod1"]/5, produtos["prod2"]))
print(f"A parcela do prod2: {produtos["prod2"] / 5:.2f}")