#   Product Database Creation

category = ['Phone','Phone','Phone','Phone','Phone','Phone','Tablet','Tablet','Tablet','Tablet','SIM card','SIM card','Case','Case','Charger','Charger']
description = ['Compact','Clam Shell','RoboPhone – 5-inch screen and 64GB memory','RoboPhone – 6-inch screen and 256GB memory','Y-Phone Standard – 6-inch screen and 64GB memory','Y-Phone Deluxe – 6-inch screen and 256GB memory','RoboTab – 8-inch screen and 64GB memory','RoboTab – 10-inch screen and 128GB memory','Y-Tab Standard – 10-inch screen and 128GB memory','Y-Tab Deluxe – 10-inch screen and 256GB memory','SIM Free (no SIM card purchased)','Pay As You Go (SIM card purchased)','Standard','Luxury','Car','Home']
price = [29.99,49.99,199.99,499.99,549.99,649.99,149.99,299.99,499.99,599.99,0.00,9.99,0.00,50.00,19.99,15.99]
products = ["BPCM", "BPSH", "RPSS", "RPLL", "YPLS","YPLL", "RTMS", "RTLM", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM"]

#   Function Creation

def outputProductRange(frange1,frange2):    #   Output a range of products
    for x in range(frange1,frange2):
        print(category[x])
        print(description[x])
        print(price[x])
        print(products[x])
        print(' ')

def outputProduct(a):   #   Output a single product
    print(category[a])
    print(description[a])
    print(price[a])
    print(products[a])

def purchaseProduct(prange1,prange2):   #   Get input from the user and validate it
    validID = False
    while validID == False:
        print('Please enter the ID of the product you would like to purchase:')
        choice = input().upper()
        for x in range(prange1,prange2):
            if products[x] == choice:
                choice = x
                validID = True
                return(choice)
            else:
                continue
        print('Input not valid.')
        input('Press ENTER to try again...')
    # Old version
    
#    validID = False
#    while validID == False:
#        try:
#            print('Please enter the ID of the product you would like to purchase:')
#            choice = input().upper()
#            choice = products.index(choice)
#        except ValueError as e:
#            print('Please choose a valid ID...')
#            input('Press ENTER to continue')
#        else:
#            valid = True
#            return choice

def chargerOutput():
    y=1
    for x in range(14,16):
        print(category[x])
        print(description[x])
        print(price[x])
        print('Number: ',y)
        y=y+1
        print('')

#   Var Creation
cost = 0.00
#   Output phones and tablets: Descriptions & Prices & IDs
outputProductRange(0,10)
#   Allow user to pick
choicePhoneTablet = purchaseProduct(0,10)
cost = cost+price[choicePhoneTablet]

if choicePhoneTablet<=5:
    print('''
Now pick a SIM for your device. 
Here are some options:

''')
    outputProductRange(10,12)

    choiceSIM = purchaseProduct(10,12)
    cost = cost+price[choiceSIM]
else:
    print('''
No sim needed

''')
print('''
Now pick a case for your device. 
Here are some options:

''')
outputProductRange(12,14)
choiceCase = purchaseProduct(12,14)
cost = cost+price[choiceCase]

#   Charger

print('''
Now pick charger(s) for your device. 
Here are some options:

''')
chargerOutput()

validCharger = False
while validCharger == False:
    choiceCharger = input('Please enter the number of the charger you would like to purchase, if you would like both type both: ').upper()
    if choiceCharger == '1': 
        choiceCharger = 14
        cost = cost+price[choiceCharger]
        both = False
        validCharger = True
    elif choiceCharger == '2':
        choiceCharger = 15
        cost = cost+price[choiceCharger] 
        both = False
        validCharger = True  
    elif choiceCharger == 'BOTH':
        choiceCharger = 14
        cost = cost+price[14]
        choiceCharger2 = 15
        cost = cost+price[15]
        both = True
        validCharger = True
    else:
        input('Not Valid Press ENTER to try again, please type 1, 2 or both')
        continue
print('''Thank you for shopping with us!

Here is your Recipt


''')

outputProduct(choicePhoneTablet)
purchasedPhoneTablets = [choicePhoneTablet]
print('')
if choicePhoneTablet<=5:
    outputProduct(choiceSIM)
    purchasedSIMs = [choiceSIM]
    print('')
outputProduct(choiceCase)
purchasedCases = [choiceCase]
print('')
if both==True:
    outputProduct(choiceCharger)
    purchasedChargers = [choiceCharger]
    print('')
    outputProduct(choiceCharger2)
    purchasedChargers2 = [choiceCharger2]
    print('')
else:
    outputProduct(choiceCharger)
    purchasedChargers = [choiceCharger]
    print('')
print('Your total is: $',cost)

valid1 = False
valid2 = False
moreThanOne = False
while valid2 == False:
    anotherOne = input('Would you like to purchase another device? y/n  ').lower()
    while valid1 == False:
        if anotherOne == 'y':
            moreThanOne = True
            #   Phones / Tablets
            outputProductRange(0,10)
            choicePhoneTablet = purchaseProduct(0,10)
            cost = cost+price[choicePhoneTablet]
            purchasedPhoneTablets.append(choicePhoneTablet)
            #   SIM
            if choicePhoneTablet<=5:
                print('''
Now pick a SIM for your device. 
Here are some options:

''')
                outputProductRange(10,12)

                choiceSIM = purchaseProduct(10,12)
                cost = cost+price[choiceSIM]
                purchasedSIMs.append(choiceSIM)
            else:
                print('''
No sim needed

''')
            #   Case
            print('''
Now pick a case for your device. 
Here are some options:

''')
            outputProductRange(12,14)
            choiceCase = purchaseProduct()
            cost = cost+price[choiceCase]
            purchasedCases.append(choiceCase)
            #   Charger
            print('''
Now pick charger(s) for your device. 
Here are some options:

''')
            chargerOutput()
            valid3 = False
            while valid3 == False:
                choiceCharger = input('Please enter the number of the charger you would like to purchase, if you would like both type both: ').upper()
                if choiceCharger == '1': 
                    choiceCharger = 14
                    cost = cost+price[choiceCharger]
                    purchasedChargers.append(choiceCharger)
                    valid3 = True
                elif choiceCharger == '2':
                    choiceCharger = 15
                    cost = cost+price[choiceCharger] 
                    purchasedChargers.append(choiceCharger)
                    valid3 = True  
                elif choiceCharger == 'BOTH':
                    choiceCharger = 14
                    purchasedChargers.append(choiceCharger)
                    cost = cost+price[14]
                    choiceCharger2 = 15
                    purchasedChargers2.append(choiceCharger2)
                    cost = cost+price[15]
                    both = True
                    valid3 = True
                else:
                    input('Not Valid Press ENTER to try again, please type 1, 2 or both')
                    continue
            print(' ')
            print('Your total is: $',cost)
            anotherOne = input('Would you like to purchase another device? y/n  ').lower()
            continue
        elif anotherOne == 'n':
            if moreThanOne == True:
                print('''Thank you for shopping with us!

                Here is your Recipt


                ''')
                for e in choicePhoneTablet:
                    outputProduct(choicePhoneTablet)
                    purchasedPhoneTablets = [choicePhoneTablet]
                    print('')
                    if choicePhoneTablet<=5:
                        outputProduct(choiceSIM)
                        purchasedSIMs = [choiceSIM]
                        print('')
                    outputProduct(choiceCase)
                    purchasedCases = [choiceCase]
                    if both==True:
                        outputProduct(choiceCharger)
                        purchasedChargers = [choiceCharger]
                        print('')
                        outputProduct(choiceCharger2)
                        purchasedChargers2 = [choiceCharger2]
                        print('')
                    else:
                        outputProduct(choiceCharger)
                        purchasedChargers = [choiceCharger]
                        print('')
                    valid2 = True
                    valid1 = True
                print('Your total is: $',cost)
            else:
                print('See you soon!')
                valid2 = True
                valid1 = True
        else:
            print('Not valid input, please enter y or n')
            input('Press ENTER to continue...')
            continue
            


