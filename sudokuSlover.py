__author__ = 'student'
def enterpuzzle ():
    while True:
        puzzle = raw_input('please enter your 81 digit puzzle use "." for blank spots :\n')
        #Validate that user input is len = 81
        if not len(puzzle)== 81:
            print "please enter a value that is equal to 81 charactors long. Please try again"
            continue
        #Validate that user input only has numbers or .
        valid = [ "1","2","3","4","5","6","7","8","9","0","."]
        for char in puzzle:
            if not char in valid:
                print char + " is not a valid value please reenter puzzle without using " + char





enterpuzzle()
