#bas#Basic get input from user and add into a list program

my_list = []

while True:
    print('Enter Your Value For Slot  ' + str(len(my_list)) + '  --> ' + 'Or hit enter to stop!')
    name = input()
    if name == '':
        break
    my_list = my_list + [name]


for i in range(len(my_list)):
    print('Slot Number ' + str(i) + '--->  ' +  my_list[i] )

print(my_list)

    
