# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:

# If the person is 1 year old or less, it should display "infant" (without quotes).
# If the person is older than 1 year, but younger than 13 years, it should display "child".
# If the person is at least 13 years old, but less than 20 years old, it should display "teenager".
# If the person is at least 20 year old, it should display "adult".

# Here is my Pseudocode for #1 Age Classifier 
# the start 
    #promt the user to enter a person's age
    #get age

    #if age less than or equal to 1 then
        #display "The person is an infant."
    #else if age less than 13 THEN
        #display "The person is a child."
    #else if age less than 20 then
        #display "The person is a teenager."
    #else
        #display "The person is an adult."
   # end if
# the end

age = int(input("Enter a person's age: "))
if age <= 1:
    print("The person is an infant.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
else:
    print("The person is an adult.")
    
    


