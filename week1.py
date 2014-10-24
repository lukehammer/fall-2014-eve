__author__ = 'student'


def print_name():
    age = 33
    first_name = "Luke"

    # this is a comment
    # print and str are built in functions
    print(first_name + " is " + str(age))


raw_data = {"name": "Luke", "age": 33, "last": "Hammer"}


def get_response(data):
    template = "Hello %s %s, how are you?"
    name = data["name"]
    last = data["last"]
    result = template % (name, data["last"])
    return result

def get_response2(data):
    return "Hello %s %s, how are you? you are %s" % (data["name"], data["last"],data["age"])


print(get_response(raw_data))

response = get_response2(raw_data)
print(response)