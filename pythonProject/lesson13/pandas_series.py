import  pandas as pd

produktet = ["Molla","Banane","Portokajt","Rrushi"]

sales = [150,200,180,190]

sales_series = pd.Series(sales, index=produktet)

print(sales_series)

print(sales_series["Rrushi"])

shitjetTotale = sales_series.sum()

print(shitjetTotale)

shitjaMaEMadhe = sales_series.idxmax()

print(f"Shitje me se shumti ka pasur :{shitjaMaEMadhe}")