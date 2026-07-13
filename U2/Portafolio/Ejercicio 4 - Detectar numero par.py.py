price = 150
# children year < 12 =30%
#students 12 <year<25= 20%
#adults 26-64= no discount
#seniors>= 65 = 40%
age= int(input("Insert your age: "))
id= input("Do you have ID?, Yes/No: ").lower()
if age < 12:
    rate= .30
elif age <= 25 and id == "yes":
    rate=.20
elif age <= 64:
    rate= 0.00
else:
    rate=0.40
n_price= price* (1-rate)
print(f"price $: {n_price}")
