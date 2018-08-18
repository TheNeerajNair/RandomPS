print("Amount Input Program")

net_amount = 0

while True:
    user_op = input("Enter txn sequence as D or W space Amount")
    print(user_op)
    operation = user_op.split(' ')
    print(operation)


    if operation[0] == "D":
        net_amount = int(operation[1]) + net_amount
    elif operation[0] == "W":
        net_amount = int(operation[1]) - net_amount
    else:
        print("Processing Final AMount")
        break
        
    

print("Your Final Value = {}".format(net_amount))
