import sys

meal_cost = float(sys.argv[1])
taxRate = float(sys.argv[2])
tipRate = float(sys.argv[3])

tax = meal_cost * taxRate/100
meal_w_tax = meal_cost + tax

# you should tip on pre-taxed meal! 
tip = meal_cost * tipRate/100
total = meal_w_tax + tip

print "The base cost of of your meal was $%.2f" % meal_cost
print "You need to pay $%.2f for tax" % tax
print "Tipping at a rate of %d%% you should leave $%.2f for a tip" % (tipRate, tip)
print "The grand total of your meal is $%.2f" % total