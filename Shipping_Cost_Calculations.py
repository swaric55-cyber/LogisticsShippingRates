#Shipping Cost Calculator

##input package weight and shippig rate
weight=float(input("enter the package weight in kiograms :") )
rate=float(input("enter the shipping  rate per kilogram:"))

##caculate shipping cost
shipping_cost=weight*rate

##disply the result
print(f"shipping cost:{shipping_cost} USD")
