print("Initiating Target Matching Program -- Based on a Program asked at a (supposed) Google Interview!")
## Author - Neeraj Nair
## Date - 12.11.2018
## Version 1.0

#Basic Hi-Hello stuff below to welcome the user
usr_name = input("Please enter your name!  -- ")
print("Hi {}, Welcome to the target matching program".format(usr_name))

# Setting a limit for the list depending on this the loop would iterate to capture user input to feed into the array
n = int(input("Enter the Numeral Limit, This would be the limit of the numbers you as the user would be feeding  -->  "))

#Just creating a blank list here for the processing part starts
num_list = []

#A loop that would take the inputs to feed into the above created list
for i in range(0,n):
	print("You will now need to enter the input numerals to peform further actions!")
	a=input("Add the {} postion numeral  -->  ".format(i))
	num_list.append(a)

#Just showing the user the values he has fed into the list	
print("Values entered by you {} are as below".format(usr_name))
print(num_list)

#This part would capture the desired target number the program would need to focus on
target_num=int(input("Now you need to enter the target number  --> "))
print("Target Value is set as = {}".format(target_num))

#Running multi-looping to iterate/compare between all the numbers to find a match
for i in range(len(num_list)):
	 for j in range(len(num_list)):
		 if ( ( int(num_list[i]) + int(num_list[j]) ) == target_num):
			 print("Value Matches Found!!! They are {} and {} ".format(num_list[i],num_list[j]))

			 
print("Processing Complete, Ceasing Target Matching Program")
print("Bye {}".format(usr_name))
	
