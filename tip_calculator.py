from optparse import OptionParser   #import the OptionParser object from this module

parser = OptionParser()     #create an instance of OptionParser

parser.add_option("-m", "--meal", dest="meal_arg", help="Meal Cost")
parser.add_option("-x", "--tax", dest="tax_arg", help="Tax for meal", default="8")
parser.add_option("-t", "--tip", dest="tip_arg", help="Tip percentage",
                    default="20")


(options, args) = parser.parse_args() 
if not (options.meal_arg): 
    parser.error("You need to supply an argument for meal cost!")
# if you want to require one or more of your arguments, you can add an if
# statement that raises an error if a required argumnt is missing


meal_cost = float(options.meal_arg)
taxRate = float(options.tax_arg)
tipRate = float(options.tip_arg)

tax = meal_cost * taxRate/100
meal_w_tax = meal_cost + tax

# you should tip on pre-taxed meal! 
tip = meal_cost * tipRate/100
total = meal_w_tax + tip

print "The base cost of of your meal was $%.2f" % meal_cost
print "You need to pay $%.2f for tax" % tax
print "Tipping at a rate of %d%% you should leave $%.2f for a tip" % (tipRate, tip)
print "The grand total of your meal is $%.2f" % total