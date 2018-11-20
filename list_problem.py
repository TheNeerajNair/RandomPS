## Objective - A list with 5 elements must always possess 5 elements, when one element is added, one must be removed.
## Author - Neeraj Nair
## Date - 20.11.2018
## Version - 1.0

my_list = [ "cat" , "dog" , "horse" , "lion" , "tiger" ]


def process_unit(my_list):
    print(my_list)
    new_val = str(input("Enter the new Value which must be inserted into the list above -  "))
    del my_list[0]
    my_list.append(new_val)
    a = int(len(my_list))
    if a == 5:
        print("Still has 5 elements")
    else:
        print("Something's not right")
	
    return my_list

    
			
			
process_unit(my_list)
print("new List - ")
print(my_list)
