# This program reads a file of account numbers into a list, then prompts the user
# for an account number and compares that number to the numbers on the list
# to determine if the account number is valid or invalid.
# Chris Blaylock
# 11/13/2019

# Add exception handling: try/except
try:
    
    # Open the charge_accounts.txt file and read the content into a list
    # then close the file
    accounts = open("charge_accounts.txt","r")
    accounts_list = accounts.readlines()
    accounts.close()

    # Strip  off the new line character from each list item
    number_of_list_item = 0
    while number_of_list_item < len(accounts_list):
        accounts_list[number_of_list_item] = accounts_list[number_of_list_item].rstrip('\n')
        number_of_list_item = number_of_list_item + 1
    
    # Prompt the user to enter an account number
    account_number = input("Please enter an account number: ")

    # Use the Python "in" operator to search for the account number in the list
    # Display a message indicating whether an account number is
    # valid or invalid depending on whether it is found in the list
    if account_number in accounts_list:
        print(account_number, 'is valid')
    else:
        print(account_number, 'is invalid')
# Exception handling: print the default error message if an error is found.        
except Exception as err:
    print(err)


    





