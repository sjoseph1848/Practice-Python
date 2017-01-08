tip = float(input("How much was your bill? "))

tip_15_percent = float(tip * .15) 
tip_18_percent = float(tip * .18)
tip_20_percent = float(tip * .20)

print("Your tip at 15 percent is $%s \n Your tip at 18 percent is $%s \n Your tip at 20 percent is $%s "
 %(tip_15_percent, tip_18_percent, tip_20_percent))