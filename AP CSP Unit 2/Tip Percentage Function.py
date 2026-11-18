bill_amount = int(input("Enter the amount of your dinner bill: "))
default_percentage = 0.18
question = input("The default percentage tipped is 18%. Did you tip above or below that? Answer "ABOVE" or "BELOW."")
tipChanged = False
if question = "ABOVE" or question = "BELOW":
    tipChanged = True
    custom = float(input("Enter your custom tip percentage, but as a WHOLE number: "))
    tippercentage = custom / 100
tipamount = bill_amount * tippercentage
finalpercentage = bill_amount + tip_amount
print("Total Amount: ", finalpercentage)