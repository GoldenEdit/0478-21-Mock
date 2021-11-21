#imports
from tabulate import tabulate # import tabulate using "pip3 install tabulate" from terminal

#   Phones and tablets
PTCategory = ["Phone", "Phone", "Phone", "Phone", "Phone", "Phone", "Tablet", "Tablet", "Tablet", "Tablet"]
PTCodes = ["BPCM","BPSH","RPSS","RPLL","YPLS","YPLL","RTMS","RTLM","YTLM","YTLL"]
PTDescriptions = ["Compact phone","Clam Shell phone","Robophone 5 inch phone","Robophone 6 inch phone","Y-Phone Standard","Y-Phone Deluxe","RoboTab 8-inch tablet","RoboTab 10-inch tablet","Y-Tab Standard 10 inch tablet","Y-Tab Deluxe 10 inch tablet"]
PTPrices = [29.99,49.99,199.99,499.99,549.99,649.99,149.99,299.99,499.99,599.99]


# data structures

#   Cases
CaseCodes = ["CSST","CSLX"]
CaseDescriptions = ["Standard case","Luxury case"]
CasePrices = [0.00,50.00]

#   Chargers
ChargerCodes = ["CGCR","CGHM","CGBH"]
ChargerDescriptions = ["Car Charger","Home charger","Car & Home charger"]
ChargerPrices = [19.99,15.99,35.98]

#   Variables
DeviceOrder = 'N' #Lets the user decide if they would like to order a phone or tablet, stores a Y/N | String
TotalAccessoriesPrice = 0 #The price of all of the accessories (Case & Charger) added together | Float
NumDevicesOrdered = 0 #Stores the number of devices ordered to apply a discount on every +1 device ordered | Int
DeviceDiscount = 0 #Stores the discount that the user is getting, to output to them at the end | Float
TotalDeviceOrder = 0 #Cost of all of the devices that the user orderd inc discount | Float
TotalSIMPrice = 0 #Another running total variable (for the total of all of the SIMs) | Float
FirstSIMPrice = 0 #Cost of the original sim bought | Float
SIMPrice = 0 #Cost of SIM (Changes depending on which sim option is chosen) | Float


def main():
    print("") #prints an empty line
    print("----- Welcome to Mobile Phone Shop -----")
    print("") #prints an empty line

    NewOrder = ""
    
    while NewOrder == "":

    #   Phone or Tablet Order
        DeviceOrder = input("Would you like to order a phone or tablet Y/N: ").upper()  

        if DeviceOrder == "Y":
            printPTTable() # call procedure that contains code for printing the phone/tablet table

            print("") #prints an empty line
            

            #   Choose a device & validation 
            PTChoice = (input ("Enter the device code (XXXX) that you wish to purchase: ")).upper()

            
            while PTChoice not in PTCodes: #Valdation (Checks that the input is in the codes array, if not, asks for it again
                print("")
                print("Not a valid code, try again")
                PTChoice = input("Enter the device code (XXXX): ").upper()
                
                
                
            #   Get the position number in the array of the code, to find corresponding price in another array.
            DPrice = PTPrices[PTCodes.index(PTChoice)]

















            
            

            if PTChoice <7: #Checks if the users input was less than 7 (they picked a phone)
                SIMChoice = int(input("Enter 1 for a SIM free or 2 for Pay as you go SIM: "))
                while SIMChoice < 1 or SIMChoice > 2: #Valdation (Checks that the input is within constraints, if not asks for input again)
                    SIMChoice = int(input("Enter 1 for a SIM free or 2 for Pay as you go SIM: "))
            
                if SIMChoice == 1:
                    SIMCard = "SIM Free"
                    SIMPrice = 0.00 #Sets the price of the SIM
                else:
                    SIMCard = "SIM Pay as you go"
                    SIMPrice = 9.99 #Sets the price of the SIM

                TotalSIMPrice = TotalSIMPrice + SIMPrice #Running total
            print("\n")

            #   Count the number of devices ordered and apply a discount for every +1 device
            NumDevicesOrdered = NumDevicesOrdered + 1 #Adds to the running total of devices ordered
            if NumDevicesOrdered <2:
                FirstSIMPrice = SIMPrice 
                TotalDeviceOrder = DPrice + FirstSIMPrice #Running total if only 1 device is ordered
            else:
                TotalDeviceOrder = TotalDeviceOrder + (DPrice/100*90) + TotalSIMPrice - FirstSIMPrice #Device running total & prevents the SIM price being added twice
                DeviceDiscount = DeviceDiscount + (DPrice/100*10) #Discount running total
            print("\n")

        #   Cases
        CaseOrder = input("Would you like to order a Case Y/N: \n").upper()

        if CaseOrder == "Y":
            print("Choose a Case option 1 or 2: ")
            for i in range (0,2):
                print(i+1,CaseCodes[i],CaseDescriptions [i],CasePrices[i]) #Output cases
                
            CaseChoice = int(input ("Enter your choice 1 or 2: "))
            while CaseChoice < 1 or CaseChoice > 2: #Valdation (Checks that the input is within constraints, if not asks for input again)
                CaseChoice = int(input ("Enter your choice 1 or 2: "))
            CasePrice = CasePrices[CaseChoice-1] #Calculates the price of the case from the user input

            TotalAccessoriesPrice = TotalAccessoriesPrice + CasePrice #Running total for accessories to prevent the discount being taken off them
        print("\n")

        #   Chargers
        ChargerOrder = input("Would you like to order a Charger Y/N: \n").upper()

        if ChargerOrder == "Y":
            print("Choose a charger option 1 - 3")
            for i in range (0,3):
                print(i+1,ChargerCodes[i],ChargerDescriptions[i],ChargerPrices[i]) #Output chargers
                
            ChChoice = int(input ("Enter your choice 1 - 3: "))
            while ChChoice < 1 or ChChoice > 3: #Valdation (Checks that the input is within constraints, if not asks for input again)
                ChChoice = int(input ("Enter your choice 1 - 3: "))

            ChPrice = ChargerPrices[ChChoice-1] #Find price of charger


            TotalAccessoriesPrice = TotalAccessoriesPrice + ChPrice #Running total for accessories to prevent the discount being taken off them
            print("\n")


        NewOrder = input("Press enter to place another order or any other key to quit")

    #Recipt Output
    print("-==================-")
    print("Your recipt:")
    print("Total: $",round(TotalDeviceOrder+TotalAccessoriesPrice,2)) #Rounded to 2 decimal places to prevent output looking ugly & Add running totals for devices & accessories together
    print("Discount: $",round(DeviceDiscount,2)) 
    print("-==================-")








# procedure to display a table containing only phones or tablets
def printPTTable():

    data = [] # declare empty data list/array ready to be filled for displayiing table

    # populate array with only phone and tablet products
    for i in range(0, len(PTCategory)):
        data.append([PTCategory[i], PTCodes[i], PTDescriptions[i], PTPrices[i]])
       
    # print table using tabulate function. Number of headers must match length of each list element in data
    print(tabulate(data, headers=["TYPE", "CODE", "DESCRIPTION", "COST"], tablefmt = "fancy_grid", numalign="right"))

    print("") #prints an empty line





# KEEP
if __name__ == '__main__':
    main()


    
