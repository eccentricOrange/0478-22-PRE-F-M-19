sizesAvailable = ["Small", "Medium", "Large"]
basesAvailable = ["Thick", "Thin"]
toppingsAvailable = ["Pepperoni", "Chicken", "Extra Cheese", "Mushrooms", "Spinach", "Olives"]

def inputValidate (item, available):
    print "\nYou have the following choices of " + item + " to choose from:"
    for count in range (len(available)):
        print available[count],
    variable = raw_input("\n\nPlease enter the " + item + " you want: ")
    while (variable not in available):
        variable = raw_input("Please re-enter the " + item + " from one of the options above: ")
    return variable
    
sizesCount = [0, 0, 0]
basesCount = [0, 0]
toppingsCount = [0, 0, 0, 0, 0, 0]
ordersCount = 0
while (raw_input("\n\nDo you want to take an order? ") in ["yes", "Yes", "YES", "True", "true", "TRUE", "yeah", "YEAH", "yeah"]):
    status = "Alter"
    while (status == "Alter"):
        toppings = []
        size = inputValidate("size", sizesAvailable)
        base = inputValidate("base", basesAvailable)
        toppingsNumber = int(input("\nPlease enter the number of toppings you want. You may enter any whole number between 0 and 3: "))
        while (toppingsNumber > 3) or (toppingsNumber < 0):
            toppingsNumber = int(input("\nPlease re-enter the number of toppings you want. You may enter any whole number between 0 and 3: "))
        for count in range(toppingsNumber):
            toppings.insert(count, inputValidate(("topping " + str(count + 1)), toppingsAvailable))
        status = raw_input("\nDo you want to Confirm, Alter or Not proceed? ")
    if status == "Confirm":
        ordersCount += 1
        print "Your unique order number is", ordersCount
        for count in range(toppingsNumber):
            toppingsCount[toppingsAvailable.index(toppings[count])] += 1
        sizesCount[sizesAvailable.index(size)] += 1
        basesCount[basesAvailable.index(base)] += 1
toppingsSum = 0.0
highest = 0.0
lowest = 1000.0
for count in range(len(toppingsAvailable)):
    toppingsSum += toppingsCount[count]
    if toppingsCount[count] > highest:
        highest = toppingsCount[count]
        highestIndex = count
    if (toppingsCount[count] < lowest) and (toppingsCount[count] > 0):
        lowest = toppingsCount[count]
        lowestIndex = count
print "\n\n", toppingsAvailable[highestIndex], "was the most popular topping and accounted for", ((highest/toppingsSum) * 100.0), "% of the toppings sales."
print toppingsAvailable[lowestIndex], "was the least popular topping and accounted for", ((lowest/toppingsSum) * 100.0), "% of the toppings sales."