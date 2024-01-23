#Loop the whole program to keep asking until user doesnt want to input an integer anymore
#print beginning statement
#ask user to input integer
#Print header for table
#loop the input to display 1 to number the user inputted, square and cube for those numbers as well
#print the loop and format in table form
#Print header for Multiplication table
#put in loop for using user input to create multiplication table
# ask the user if they want to continue or not
#if user says yes loop starts over, if user says anything than yes, ending statement is printed.


while True:
    print ("Learn your squares and cubes!")
    usernum= int(input("Please enter an integer: "))

    print("Number | Square | Cube")
    print("------------------------")
    for i in range(1, usernum + 1):
        square = i ** 2
        cube = i ** 3
        print(f"{i:6} | {square:6} | {cube:6}")

    print ("Multiplication Table")
    print("------------------------")
    for row in range(1, usernum+1):
        print(*(f"{row*col:3}" for col in range(1, usernum + 1)))


    user_choice = input("Do you want to continue? (yes/no): ").lower()
    if user_choice != 'yes':
        print("Goodbye!")
        break

