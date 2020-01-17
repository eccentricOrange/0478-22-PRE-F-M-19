# **   IMPORT LIBRARY
import array  # Add the array library to the program


# **   DECLARE CONSTANTS

# These are the options of the various properties of the pizza available
sizesAvailable = ["Small", "Medium", "Large"]  # The size of the pizza
basesAvailable = ["Thick", "Thin"]  # The type of base of the pizza
toppingsAvailable = ["Pepperoni", "Chicken", "Extra Cheese", "Mushrooms", "Spinach", "Olives"]  # The toppings available

maxToppings = 3  # The maximum number of toppings that can be taken


# **   DECLARE VARIABLES
currentID = 0  # The running unique ID of the order
ordersCount = 0  # The running total of the number of confirmed orders
close = False  # status of more orders

highest = 0.0
highestIndex = 0
lowest = 1000.0
lowestIndex = 0
toppingsSum = 0.0

sizes = [False, False, False]  # Running tracker of the size taken in an order
bases = [False, False]  # Running tracker of the pizza base taken in an order
toppings = [False, False, False, False, False, False]  # Running tracker of the toppings taken in an order

totalSizes = array.array('i', range(3))  # Running counter of the sizes taken
totalBases = array.array('i', range(2))  # Running counter of the pizza bases taken
totalToppings = array.array('i', range(6))  # Running counter of the toppings taken


# **   TASK 1
# Use a default status "Alter" to customize the pizza
# Input the values of each attribute and validate them
# Give the customer a choice to alter the order, confirm it or cancel it
# If they choose to alter, re-input the values
# If they confirm it, provide them with a new order number.

# **   TASK 2
# Increment a counter of number of pizzas if an order is confirmed
# Add the value of the Counters[] to the TotalCounters[]
# Output the number of pizzas ordered.


while (not close):

    status = "Alter"  # Default status to input values

    # Input and validate the values
    while(status == "Alter"):  # As long as the status is "Alter"
    
        # Reset the running trackers
        sizes = [False, False, False]
        bases = [False, False]
        toppings = [False, False, False, False, False, False]
        
        # Output the available options
        
        # Output the sizes
        print "The following sizes are available to choose from:"
        for count in range(3):  # Iterate 3 times for 3 sizes
            print (sizesAvailable[count] + ','),  # Output the available sizes
        
        # Output the bases
        print "\n\nThe following bases are available to choose from:"
        for count in range(2):  # Iterate 2 times for 2 pizza bases
            print (basesAvailable[count] + ','),  # Output the available bases
        
        # Output the toppings
        print "\n\nThe following toppings are available to choose from:"
        for count in range(6):  # Iterate 6 times for 6 toppings
            print (toppingsAvailable[count] + ','),  # Output the available toppings
        
        #Input and validate the size of the pizza
        sizeValid = False  # Set flag as invalid
        
        while (not sizeValid):  # Validation loop
            size = raw_input("\n\nPlease enter the size of the pizza you would like: ")  # Input prompt

            # Check if the size is valid
            for count in range(3):  # Iterate 3 times for 3 sizes
                if size == sizesAvailable[count]:  # If a match is found from the available sizes
                    sizeValid = True  # Set flag as valid
                    sizes[count] = True  # Set flag as selected
        
        # Unless the size is invalid, break out of the loop
        
        # Input and validate the type of pizza base
        baseValid = False  # Set flag as invalid
        
        while (not baseValid):  # Validation loop
            base = raw_input("\nPlease enter the type base of the pizza you would like: ")  # Input prompt
            
            for count in range(2):  # Iterate 2 times for two sizes
                if base == basesAvailable[count]:  # If a match is found from the available pizza bases
                    baseValid = True  # Set flag as valid
                    bases[count] = True  # Set flag as selected
                    
        # Unless the type of pizza base is invalid, break out of the loop
        
        # Input and validate the number of toppings the customer wants
        toppingChoice = 100  # Initialize topping choice to be invalid
        
        while (not toppingChoice <= maxToppings):  # Validation loop
        
            toppingChoice = input("\nHow many toppings do you want on your pizza? You may enter any whole number 0 and 3: ")  # Input prompt
            
        # Unless the number of toppings is greater than 3, break out of the loop
        
        for countO in range(toppingChoice):  # Iterate as many times as the toppings taken
        
            # Input and validate the topping
            toppingValid = False  # Set flag as invalid
            
            while (not toppingValid):  # Validation loop
                topping = raw_input("\nPlease enter topping " + str(countO + 1) + " on the pizza you would like: ")  # Input prompt
                
                for countI in range(6):  # Iterate 6 times for 6 toppings
                    if topping == toppingsAvailable[countI]:  # If a match is found from the available toppings
                    
                        toppingValid = True  # Set flag as valid
                        toppings[countI] = True  # Set flag as selected
                        
            # Unless the topping is invalid, break out of the loop
        
        # Move on to the next topping
        
        # Allow the customer to choose whether they want to alter their order, confirm it or cancel it
        status = raw_input("\nDo you want to Alter your order, Confirm or Not proceed? Enter your choice: ")  # Input prompt
        
    # Unless they want to alter their order, break out of the loop

    # Give the customer a unique order ID if they have confirmed it
    if status == "Confirm":  # If the customer has confirmed their order
    
        print "\nYour unique order number is:", currentID  # Print out the unique ID
        currentID = currentID + 1  # Increment the ID for the next confirmed order
        ordersCount = ordersCount + 1  # Increment the counter for confirmed orders
        
        # Record how many of each size has been ordered
        for count in range(3):  # Iterate 3 times for 3 sizes
            if sizes[count] == True:  # If a size is recorded
                totalSizes[count] = totalSizes[count] + 1  # Increment the counter
            
        # Record how many of each pizza base has been ordered
        for count in range(2):  # Iterate 2 times for 2 pizza bases
            if bases[count] == True:  # If a pizza base is recorded
                totalBases[count] = totalBases[count] + 1  # Increment the counter
            
        # Record how many of each topping has been ordered
        for count in range(6):  # Iterate 6 times for 6 toppings
            if toppings[count] == True:  # If a topping has been ordered
                totalToppings[count] = totalToppings[count] + 1  # Increment the counter
            
    close = input("\nDo you want to exit the program? Enter your choice: ")  # Input prompt

# Break out of the loop unless more pizzas are to be ordered

print '\n', ordersCount, "pizzas were ordered."  # Output how many pizzas were ordered


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
    if totalToppings[count] < lowest:  # If the current topping sold less than the running least popular topping
        lowest = totalToppings[count]  # Update the running least popular topping
        lowestIndex = count  # Record the array index of the topping
    
print toppingsAvailable[highestIndex], "was the most popular topping and accounted for", ((highest/toppingsSum) * 100.0), "% of the toppings sales."  # Output the most popular toppings
print toppingsAvailable[lowestIndex], "was the least popular topping and accounted for", ((lowest/toppingsSum) * 100.0), "% of the toppings sales."  # Output the least popular toppings

# This is the end of the program
# All required tasks have been completed.
