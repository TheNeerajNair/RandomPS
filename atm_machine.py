###############################################################################################
#Author - Neeraj Nair
#Version - v1.0
#Date - 6th Feb - 2019
#Subject - Basic ATM machine code
###############################################################################################

###### This Section will basically replicate a Database style structured Data Store ##########
user_list = {'user1': '0000', 'user2': '1002' , 'user3' : '0022'}
user_amt_list = {'user1': '1000', 'user2': '1500' , 'user3': '2000'}	
##############################################################################################


def welcome_console():
		print('Hello! Welcome to the ATM machine program')
		print('This program is designed to simulate the real workings of an ATM machine')
		print('This is the first available version of the code so far - New Features will come soon!')

def main_console():
		print('Choose your Required Function')
		print('Press 1 and Hit Enter for Cash Withdrawl')
		print('Press 2 and Hit Enter for Checking Available Balance')
		print('Press 3 and Hit Enter for Changing Pin for existing account')
		print('Press 4 and Hit Enter for Generating Mini-Statement -- Feature Currently NOT AVAILABLE')
		num = input(' USER INPUT REQUIRED: Please ENTER an INPUT -->  ')
		if num == '1':
			cash_withdrawl()
		elif num == '2':
			check_avail_bal()
		elif num == '3':
			change_user_pin()
		elif num == '4':
			gen_mini_statement()
		else:
		    print('Invalid Choice Made, aborting instance try again!') 
		    main_console()
			
def cash_withdrawl():
		print('You have selected the choice to withdraw cash')
		username = input('ENTER YOUR USERNAME PLEASE -- Since this code wont be able to support Magnetic Strip ATM card style authentication check we directly use username and PIN -- ')
		if (username in user_list.keys()) == True:
				print('Welcome {}'.format(username))
				password = input('Please Enter your four digit PIN -- ')
				if (password) == (user_list.get(username,0)):
					print('{} PIN Match Made'.format(username))
					amt = input('Choose the Amount which you wish to withdraw -- ')
					withdraw_amt = int(amt)
					bal = (user_amt_list.get(username,0))
					current_bal = int(bal)
					if withdraw_amt < current_bal or (withdraw_amt == current_bal):
						print('You have withdrawn Rs {}'.format(withdraw_amt))
						final_bal = (current_bal - withdraw_amt) 
						user_amt_list.pop(username)
						user_amt_list[username] = final_bal
						print('Database Updated for {}'.format(username))
						print('Transaction Process Completed, Thank You for using this ATM machine! Have a nice day!')
						print(user_amt_list)
					else:
						print('Invalid Amount Entered, Please check your amount limit, Amount entered is more than amount present in {} account'.format(username))
						cash_withdrawl()
				else:
					print('Incorrect PIN Issued, Aborting instance')
					cash_withdrawl()
		else:
				print('User does not exist, Aborting the instance')
				cash_withdrawl()

def check_avail_bal():
		print('You have selected the choice to Check your Available Balance')
		username = input('ENTER YOUR USERNAME PLEASE -- ')
		if (username in user_list.keys()) == True:
				print('Welcome {}'.format(username))
				password = input('Please Enter your four digit PIN -- ')
				if (password) == (user_list.get(username,0)):
					print('{} PIN Match Made'.format(username))
					bal = (user_amt_list.get(username,0))
					print('Your Available Balance is Rupees = {}'.format(bal))
					print('Process Completed, Thank You for using this ATM machine! Have a nice day!')
				else:
					print('Incorrect PIN Issued, Aborting instance')
					check_avail_bal()
		else:
				print('User does not exist, Aborting the instance')
				check_avail_bal()

def change_user_pin():
		print('You have selected the choice to Change Your User Pin')
		username = input('ENTER YOUR USERNAME PLEASE -- ')
		if (username in user_list.keys()) == True:
				print('Welcome {}'.format(username))
				password = input('Please Enter your current four digit PIN -- ')
				if (password) == (user_list.get(username,0)):
					print('{} PIN Match Made'.format(username))
					new_pin = input('Please enter your NEW four digit PIN number')
					if len(new_pin) is not 4:
						print('You have not entered a NEW valid pin - Please ensure your PIN digit is 4 digits')
						change_user_pin()
					else:
						print('PIN update is in process, Please wait!')
						user_list.pop(username)
						user_list[username] = new_pin
						print('New PIN has been successfully updated')
						print(user_list)
						print('Process Completed, Thank You for using this ATM machine! Have a nice day!')
				else:
					print('Incorrect PIN Issued, Aborting instance')
					change_user_pin()
		else:
				print('User does not exist, Aborting the instance')	
				change_user_pin()				

				
def gen_mini_statement():
			print('Hello, Thanks for trying to check if this feature works')
			print('But unfortunately this specific feature is still in development')
				
## My Program Calling Starts from here - 

welcome_console()
main_console()
####################################################################################################################################				
####################################################################################################################################
######################################## THATS ALL FOLKS!!! ########################################################################
####################################################################################################################################				
