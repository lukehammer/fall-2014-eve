__author__ = 'student'

value = 10

while value >= 0:
    #print(value)
    value = value -1

people = ["kevin", "alice","paul", "bob","carol"]

index = 0
found = False
while not found:
   # print(people [index])
    if people[index]=="alice":
        found = True
    else:
        index = index + 1

    #print ("found at index 1" + str(index))





raw_data = [
    {"name":"Kevin", "age":16},
    {"name":"Carol", "age":42},
    {"name":"Ted", "age":43},
    ]
index = 0
age = 0
total = 0
# how to loop through all the people in raw_data until the sum of there ages totals > 30
while total <= 30:
    person = raw_data[index]
    total = total + person["age"]
    #print total

#print person

# how to loop through all the people in raw_data until the sum of there ages totals > 30
# using the less amount of lines

def print_name_and_age(raw):

    for person in raw:

        age = person["age"]
        name = person["name"]
        #print "This is "+ name + " that person is " + " years old " + str(age)
        templete =  "This is %s that person is %s years old "
        print templete % (name, age)

"somthing here"

print_name_and_age(raw_data)

# break up the code above in to 2 functions one for printing and one for looping

def print_name_an_age2(name,age):
        templete =  "This is %s that person is %s years old "
        print templete % (name, age)

def print_all(raw_data):
        print "start"
        for person in raw_data:
            age = person["age"]
            name = person["name"]
            print_name_an_age2(name,age)
        print "end"


"quick change"