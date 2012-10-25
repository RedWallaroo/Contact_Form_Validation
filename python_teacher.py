''' Python Teacher explorer a variety of Python coding best practices'''

import logging
import io
import time
import pdb
from Tkinter import *


#Creates a textbox field
class Textbox(Frame):

    def __init__(self, parent, msg):
        #initializes the frame
        Frame.__init__(self,parent)

        #create the Textbox label on the left side
        self.the_label = Label(self, text = msg)
        self.the_label.pack(side = LEFT, fill = X, expand = True)

        #create the inpput field on the right side
        self.the_input_field = Entry(self)
        self.the_input_field.pack(side = LEFT, fill = X, expand = True)

        #pack the frame
        self.pack(fill = X, anchor = NW, expand = True)

    def text(self):
        #retrieve textbox value
        return self.the_input_field.get()

class Textfield(Frame):

    def __init__(self, parent, msg):
        #initializes the frame
        Frame.__init__(self,parent)

        #create the Textbox label on the left side
        self.the_label = Label(self, text = msg)
        self.the_label.pack(side = LEFT, fill = X, expand = True)

        #pack the frame
        self.pack(fill = X, anchor = NW, expand = True)

def retrieve_text():

    print (app_entry.get())

def is_not_null(the_input):

    the_input = the_input.strip()
    if the_input:
        return True
    else:
        return False

def validate_name(student_name):

    if validate_input(student_name):
        student_name = capitalize_name(student_name)
        print 'Ah, your name is: ' + student_name
    else:
        print 'Wait a minute! You did not enter your name properly.'
    

def is_a_number(the_input):

    # the isdigit() function in python does not handle negative signs or decimal points. therefore
    # a different approach will be to attempt to convert the input to a float. 
    # also, we are using a try/except block to catch the specified exceptions.
    
    try:
        the_input = float(the_input)
        return True
    except ValueError:
        return False

def is_a_single_char(entry):

    if len(entry) == 1:
        return True
    else:
        return False

def is_a_date(entry):
    #date should be submitted in short date format.
    try:
        valid_date = time.strptime(entry, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def is_po_box_address(entry):

    if entry.find("p.o. box") >= 0 or entry.find("po box") >= 0:
        print("This looks like a P.O. box address...")
        capitalized_address = capitalize_name(entry)
        capitalized_address = capitalized_address.replace('P.o.','P.O.').replace('Po','P.O.')
        print("The P.O. box address is: " + capitalized_address)
        prompt
        return True
    else:
        return False

def is_apt_or_suite(entry):

    if entry.find("apt") >= 0 or entry.find("suite") >= 0:
        return True
    else:
        return False

def is_city_state_zip(entry):


    US_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    

def is_parsed_address(entry):
    
    # we will try to 'parse' the entry and see if we can come up with a mailing
    # address that makes sense.
    # Ideally, we should be able to identify a House number, Street name, Apt/Suite number
    # City, State, Zip will be part of a different parsing function
    
    # let's lowercase everything.
    entry = entry.lower()
   
    # P.O. box address are easy to identify so no need to continue parsing if a string 
    # contains 'P.O.'
    if not is_po_box_address(entry):
        # If it is not a P.O. Box address, let's split the words first and then check them one by one
        entry = entry.split(' ')

        # Need to declare a few variables including a dictionary which we'll use to store the parsed 
        # address

        check_word = entry[0]
        next_word_counter = 0
        address_dictionary = {}

        for y in range (len(entry)):

            check_word = entry[y]
            go_to_next_word = False
            pdb.set_trace()
            # Check word for House Number
            # if it contains numbers, we'll let it be a 'House Number'.
            for x in range(len(check_word)):
                if is_a_number(check_word[x]):
                    key,value = "House Number", check_word
                    if not any(d[key] for d in address_dictionary):
                        address_dictionary[key] = value
                        go_to_next_word = True
                    break
                    
            if go_to_next_word: continue

            # Check for Apt/Suite

            if is_apt_or_suite(check_word):
                key,value = "Apt or Suite", check_word
                if not any(d[key] for d in address_dictionary):
                    address_dictionary[key] = value
                    go_to_next_word = True
               

            if go_to_next_word: continue

            # Check for Street name
            # If it is not a House number and not Apt or Suite then it is Street name

            if not is_apt_or_suite(check_word):
                key,value = "Street Name", check_word
                if not any(d[key] for d in address_dictionary):
                    address_dictionary[key] = value
                    go_to_next_word = True
                
            if go_to_next_word: continue
            
        return address_dictionary
            

    


    









def capitalize_name(the_name):

    #take any input of type name and capitalize accordingly.
    #already checked for empty input.
    #convert each word to lowercase first in case user provided it in uppercase.
    #loops through input and counts number of words, then capitalizes first letter of each word.
    
    words_in_name = the_name.split(' ')
    capitalized_words = []
    for word in words_in_name:
        word = word.lower()
        capitalized_word = word[0].upper() + word[1:]
        capitalized_words.append(capitalized_word)
    result = ' '.join(capitalized_words)
    return result

def name_selection():

    print ("""Here are some examples of 'names' users may enter:\n
    - 'joe smith' or 'Joe smith' or 'jOe SmITH' or 'joe'
    - '' or ' ' (space or nothing)
    - '123' or '1.0' (a number)
    - 'a' or '1' or '+' (a single character)\n""")

    entry = raw_input("Enter a name here ---> ")
    print("Cool. First, we'll check for nulls...")
    if is_not_null(entry):
        print ("OK, we've got something to work with.")
        if is_a_number(entry):
            print("Oh wait, I found a number. Names cannot contain numbers!")
            prompt()
        else:
            print("Whew, not a number. Is it a single character?...")
            if is_a_single_char(entry):
                print("Really? A single character?. Sorry, this is not valid.")
                prompt()
            else:
                print("Looks like we have a winner...")
                print("Let's format that correctly and print it out...")
                capitalized_name = capitalize_name(entry)
                print("You passed validation. Your name is: " + capitalized_name)
                prompt()
    else:
        print("Wait a minute, you did not provide a name.")
        prompt()

def dob_selection():

    print ("""Here are some examples of valid and invalid 'date of birth' entries:\n
    - '09/13/1975' or '09/13/75' - US Format
    - '13/09/1975' or '13/09/75' - EU Format
    - '' or ' ' (space or nothing)
    - '123' or '2.0' (a number that is not a DOB)
    - 'a' or '1' or '+' (a single character)\n""")
    entry = raw_input("Enter a 'Date of Birth' here  in mm/dd/yyy format ---> ")
    print("Cool. First, we'll check for nulls...")
    if is_not_null(entry):
        print ("OK, we've got something to work with.")
        if is_a_date(entry):
            print("After checking, I believe you provided an actual Date...")
            print("Your DOB is: " + entry)
            prompt()
        else:
            print("Sorry. What you submitted was not in the correct format.")
            prompt()       
    else:
        print("Wait a minute, you did not provide a Date of Birth.")
        prompt()

def address_selection():
    
    print ("""Here are some examples of 'address' entries:\n
    - '123 main st' or '123 main st apt 3' or '123 main st apt 3'
    - '1/2 main street' 
    - 'main street suite #3'
    - ' ' or '' (space or nothing)\n""")
    entry = raw_input("Enter a US Mailing Address here ---> ")
    print("Cool. First, we'll check for nulls...")
    if is_not_null(entry):
        print ("OK, we've got something to work with.")
        print ("Let me check if you provided enough elements to parse...")
        if len(entry) >= 2:
            print ("Cool! I can now try and parse this address...")
            if is_parsed_address(entry):
                print("Success, Looks like we were able to parse your address correctly ...")
                print("Your DOB is: " + entry)
                prompt()
            else:
                print("Sorry. Something just didn't make sense. I have failed to parse the address.")
                prompt()
        else:
            print("I can't really parse a one-word address. Sorry! ")
            prompt()       
    else:
        print("Wait a minute, you did not provide a Mailing Address.")
        prompt()

def city_state_zip_selection():
    pass
def ph_selection():
    pass
def email_selection():
    pass
def prompt():

    what_to_do = raw_input("Choose one of these options: [M] Main Menu, [Q] Quit ---> ")
    if is_not_null:
        if what_to_do == 'm':
            main_menu()
        else:
            pass


def process_selection(selection):
    
    if is_not_null:
        option_list = ["1","2","3","4","5"]
        if selection in option_list:
            if selection == "1":
                print("\nNAME: A name may contain words, even some symbols but not numbers")
                name_selection()
            if selection == "2":
                print("\nDATE OF BIRTH: A DOB contains numbers and '/' or '-' ")
                dob_selection()
            if selection == "3":
                print("\nADDRESS: Addresses contains letters, numbers and symbols")
                address_selection()
            if selection == "4":
                print("\nCITY,STATE,ZIP: City/State contains letters, Zip contains numbers")
                city_state_zip_selection()
            if selection == "5":
                print("\nPHONE NUMBER: A phone number contains numbers and '-' or '()'")
                ph_selection()
            if selection == "6":
                print("\nEMAIL ADDRESS: An email address contains letters, numbers and '@'")
                email_selection()
        else:
            print "Invalid selection. Exiting..."
#win = Tk()
#win.title("The Contact Form")
# find a way to center window
#win.geometry("900x600+500+100")
#Textfield(win,"THE CONTACT FORM")
#Textfield(win,"This purpose of this exercise is to fill out a typical contact form with arbitraty /n input and validate it accordingly")
#Textfield(win,"User may supply name or not. So we check for both. We also need to check for a valid name based")
#student_name = Textbox(win, "Name:")

def main_menu():
    
    print (""" \nTHE CONTACT FORM\n
This exercise will guide you through different examples of input validation
by using a typical contact form. Select an input field from the list below:

        [1] Name
        [2] Date of Birth
        [3] Mailing Address
        [4] City, State, Zip 
        [5] Phone number
        [6] Email Address\n""")

    selection = raw_input("Enter a number from the menu here ---> ")
    process_selection(selection)


main_menu()
# name input cases handled properly.



