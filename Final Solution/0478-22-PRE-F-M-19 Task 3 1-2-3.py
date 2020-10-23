# **   DECLARE CONSTANTS

# These are the options of the various properties of the pizza available
sizesAvailable = ["Small", "Medium", "Large"]  # The size of the pizza
basesAvailable = ["Thick", "Thin"]  # The type of base of the pizza
toppingsAvailable = ["Pepperoni", "Chicken", "Extra Cheese", "Mushrooms", "Spinach", "Olives"]  # The toppings available

maxToppings = 3  # The maximum number of toppings that can be taken

# **   DECLARE VARIABLES
CurrentID = 0  # The running unique ID of the order
ordersCount = 0  # The running total of the number of confirmed orders
close = False  # status of more orders

highest = 0.0
highestIndex = 0
lowest = 1000.0
lowestIndex = 0
toppingsSum = 0.0

orderData = []  # Running tracker of all the items of one order

# Initialize the array with all values 0
totalSizes = [0, 0, 0]  # Set values for 3 sizes
totalBases = [0, 0]  # Set values for 2 bases
totalToppings = [0, 0, 0, 0, 0, 0]  # Set values for 6 toppings

# **   TASK 1
# Use a default status "Alter" to customize the pizza
# Input the values of each attribute for count in range( validate them
# Give the customer a choice to alter the order, confirm it OR cancel it
# If they choose to alter, re-input the values
# If they confirm it, provide them with a new order number.

# **   TASK 2
# Increment a counter of number of pizzas if an order is confirmed
# Add the value of the Counters[] to the TotalCounters[]
# Output the number of pizzas ordered.

while (close != True):

    status = "Alter"  # Default status to input values

    # Input for count in range( validate the values
    while status == "Alter":  # As long as the status is "Alter"
    
        # Reset the running tracker
        orderData = []  # Initialize to have 0 toppings

        # Output the available options
        
        # Output the sizes
        print "\nThe following sizes are available to choose from:"
        for count in range(3):  # Iterate 3 times for 3 sizes
            print sizesAvailable[count] + ',',  # Output the available sizes
        
        # Output the bases
        print "\n\nThe following bases are available to choose from:"
        for count in range(2):  # Iterate 2 times for 2 pizza bases
            print basesAvailable[count] + ',',  # Output the available bases
        
        # Output the toppings
        print "\n\nThe following toppings are available to choose from:"
        for count in range(6):  # Iterate 6 times for 6 toppings
            print toppingsAvailable[count] + ',',  # Output the available toppings
        
        size = ""  # Enable the while loop to run by making the size invalid
        
        # Input and validate the size of the pizza
        while (size != "Small") and (size != "Medium") and (size != "Large"):  # Validation loop
            size = raw_input("\n\nPlease enter the size of the pizza you would like: ")  # Input the size
            
            if (size != "Small") and (size != "Medium") and (size != "Large"):  # If the size is invalid        
                print "The size you have entered is invalid. Please re-enter the size from one of the options above."  # Print error message and ask for correction
        
        # Unless the size is invalid, break out of the loop
        
        # Input and validate the base of the pizza
        
        base = ""  # Enable the while loop to run by making the base invalid
        
        while (base != "Thick") and (base != "Thin"):  # Validation loop
            base = raw_input("\nPlease enter the pizza base you would like: ")  # Input the base
            
            if (base != "Thick") and (base != "Thin"):  # If the base is invalid
                print "The base you have entered is invalid. Please re-enter the base from one of the options above."  # Print error message and ask for correction
            
        # Unless the base is invalid, break out of the loop
        
        # Input and validate the number of toppings the customer wants
        print   # Input prompt
        
        toppingChoice = 100  # Enable the while loop to run by making the number of toppings invalid
        
        while not ((toppingChoice <= 3) and (toppingChoice >= 0)):  # Validation loop
            toppingChoice = int(input("How many toppings do you want on your pizza? You may enter any whole number between 0 and 3: "))  # Input the number of toppings the user wants
            
            if not ((toppingChoice <= 3) and (toppingChoice >= 0)): # If the number of toppings is invalid
                print "You have entered an invalid number of toppings. Please re-enter any whole number between 0 and 3."  # Throw error message and ask for correction
            
        # Unless the number of toppings is greater than 3, break out of the loop
        
        numberOfItems = 3 + toppingChoice  # Calculate the total number of items based on the number of toppings
        
        orderData = range(numberOfItems)  # Declare an array with as many elements as in the order
        
        # Store the data acquired so far
        orderData[0] = size  # Store the size
        orderData[1] = base  # Store the base
        orderData[2] = numberOfItems  # Store the total number of items
        
        for outsideCount in range(toppingChoice):  # Iterate as many times as the toppings taken
        
            # Input for count in and validate the topping of the pizza
            
            topping = ""  # Enable the while loop to run by making the topping invalid
            
            while (topping != "Pepperoni") and (topping != "Chicken") and (topping != "Extra Cheese") and (topping != "Mushrooms") and (topping != "Spinach") and (topping != "Olives"):  # Validation loop
                topping = raw_input("Please enter topping " + str(outsideCount + 1) + " of the pizza you would like: ")  # Input the topping
                
                if (topping != "Pepperoni") and (topping != "Chicken") and (topping != "Extra Cheese") and (topping != "Mushrooms") and (topping != "Spinach") and (topping != "Olives"):  # If the topping is invalid
                    print "The topping you have entered is invalid. Please re-enter the topping from one of the options above."  # Print error message and ask for correction
                
            # Unless the topping is invalid, break out of the loop
            
            orderData[2 + outsideCount] = topping  # Store the validated topping in the array
        
        # Move on to the next topping
        
        status = raw_input("\nDo you want to Alter your order, Confirm or Not proceed? ")  # Input whether the customer wants to alter their order, confirm it or cancel it
        
    # Unless they want to alter their order, break out of the loop

    # Give the customer a unique order ID if they have confirmed it
    if status == "Confirm":  # If the customer has confirmed their order
    
        print "\nYour unique order number is: ", CurrentID  # Print out the unique ID
        CurrentID = CurrentID + 1  # Increment the ID for the next confirmed order
        ordersCount = ordersCount + 1  # Increment the counter for confirmed orders
        
        # Record how many of each size has been ordered
        for count in range(3):  # Iterate 3 times for 3 sizes
            if orderData[0] == sizesAvailable[count]:  # If a size is recorded
                totalSizes[count] = totalSizes[count] + 1  # Increment the counter
        
        # Record how many of each pizza base has been ordered
        for count in range(2):  # Iterate 2 times for 2 pizza bases
            if orderData[1] == basesAvailable[count]:  # If a pizza base is recorded
                totalBases[count] = totalBases[count] + 1  # Increment the counter
        
        # Record how many of each topping has been ordered
        for outsideCount in range(toppingChoice):  # Run as many times as the number of toppings taken
            for insideCount in range(6):  # Iterate 6 times for 6 toppings
                if orderData[2 + outsideCount] == toppingsAvailable[insideCount]:  # If a topping has been ordered
                    totalToppings[insideCount] = totalToppings[insideCount] + 1  # Increment the counter
    
    close = input("\nDo you want to exit the program? ")  # Ask the staff if all orders are done

# Break out of the loop unless more pizzas are to be ordered

print "\n\n", ordersCount, "pizzas were ordered."  # Output how many pizzas were ordered

# **   TASK 3
# Calculate the total number of toppings ordered
# Calculate the highest ordered toppings
# Calculate the lowest ordered toppings
# Express both values as a percentage of the total orders

for count in range(6):  # Iterate 6 times for 6 toppings
    toppingsSum = toppingsSum + totalToppings[count]  # Add to the running total to calculate the sum
    
    # Calculate the highest sales
    if totalToppings[count] > highest:  # If the current topping sold more than the running most popular topping
        highest = totalToppings[count]  # Update the running most popular topping
        highestIndex = count  # Record the array index of the topping
    
    # Calculate the lowest sales
    if (totalToppings[count] < lowest) and (totalToppings[count] > 0):  # If the current topping sold less than the running least popular topping for count in range( it sold in the first place
        lowest = totalToppings[count]  # Update the running least popular topping
        lowestIndex = count  # Record the array index of the topping

print toppingsAvailable[highestIndex], "was the most popular topping and accounted for", ((highest/toppingsSum) * 100), "% of the toppings sales."  # Output the most popular toppings
print toppingsAvailable[lowestIndex], "was the least popular topping and accounted for", ((lowest/toppingsSum) * 100), "% of the toppings sales."  # Output the least popular toppings

# This is the end of the program
# All required tasks have been completed.
