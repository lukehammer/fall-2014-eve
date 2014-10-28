__author__ = 'student'

class Person(object):
    def __init__(self, first_name, last_name, phone_number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

def printPerson(self):
    print (self.first_name)
    print (self.last_name)
    print (self.address)
    print (self.phone_number)

def return_first_name(self):
    return self.first_name

def add_person(phonebook):
    first = raw_input("What is your first name ? ")
    last = raw_input("What is your last name ? ")
    phone_number = raw_input("What is your Phone Number? ")
    address = raw_input("What is your address ? ")
    new_person = Person(first,last,phone_number,address)
    phonebook.append(new_person)

def search_by_first_name(phonebook, first_name):
    for x in phonebook:
        if return_first_name(x)== first_name:
            print "you have found a match"
            printPerson(x)
            return True
    print "sorry no match"
    return False

def delete_by_first_name(phonebook, first_name):
    for x in phonebook:
        if return_first_name(x)== first_name:
            print "you have found a match"
            pop(x)
            return True
    print "sorry no match"
    return False
def print_all(phonebook):
    for x in phonebook:
        printPerson(x)
       # search functinon
        # Add function
        #  Remove function
phonebook = []
cont = True
while cont == True:
    next =
    aw_input("What would you like do next?\n 'add' person \n  'search'  by first name \n  'delete'  by first name\n  'print':  "))
    if next == "add":
        add_person(phonebook)
    elif next == "search":
        first_name = raw_input("what is the persons first name? ")
        search_by_first_name(phonebook, first_name)
    elif next == "quit":
        cont = False
    elif next == "delete":
        first_name = raw_input("what is the persons first name? ")
        delete_by_first_name(phonebook, first_name)
    elif next == "print":
        first_name = raw_input("what is the persons first name? ")
        print_all(phonebook)
    else:
        print "not a vaild option"




#add_person(phonebook)
#printPerson(phonebook[0])
#phonebook.append(Person("Luke","Hammer", 5035053651,"Vancouver"))
#phonebook.append(Person("John","Hammer1", 5039641653003,"Portland"))
#phonebook.append(Person("sam","Hammer2", 94651003,"Vancouver"))
#phonebook.append(Person("Dave","Hammer3", 5016553003,"Vancouver"))
#phonebook.append(Person("Test","Hammer4", 503896403,"Vancouver"))
#phonebook.append(Person("banana","Hammer5", 5035940903,"Vancouver"))



#search_by_first_name(phonebook,"pual")

#print search_by_first_name(phonebook,"pual")
#print search_by_first_name(phonebook,"banana")

#printPerson(phonebook[0])
#print (return_first_name(phonebook[0]))
#phonebook.append(add_person())
#phonebook.append(add_person())


























#print (phonebook)

#luke = Person("Luke","Hammer", 5035053003,"Vancouver")
#print luke
#printPerson(luke)
# search functinon
# Add function
# Remove function