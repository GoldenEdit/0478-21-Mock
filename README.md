I have made a few changes that you may/may not wish to keep.

You will need to import the tabular library .

Firstly, I have organised your code into procedures. All your main code goes into main. You then need to begin organising your code into appropriate procedures (maybe some functions). The first one I have done for you - it is a procedure that is responsible for printing out the phone/ tablets table. Instead of putting the code for printing out the table in the main procedure, it is best practice to section it into its own procedure. To use the procedure (run its code), you simply call its name - printPTTable(). Whenever you call that name, that code will run.

I have also added another list, called PTCategories​, to store the type of device (phone or tablet). 

I have changed the way your table is displayed - this makes use of the tabular library.

It is better practice to enter the code of the item (eg BPCM), as opposed to a number (0-10). I have begun to implement the validation checks for this. It is much simpler, as you can just write

while x not in list
     keep asking for user input
