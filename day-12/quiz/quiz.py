general_questions = 'general Questions'
computer_questions = 'computer Questions'
python_questions = 'python Questions'

questions = [general_questions, computer_questions, python_questions]

quiz = {general_questions: [("Amartya Sen was awarded the Nobel prize for his contribution to Welfare Economics.", True),
                        ("The Headquarters of the Southern Naval Command of the India Navy is located at Thiruvananthapuram.", False),
                        ("The Captain Roop Singh stadium is named after a former Indian cricketer.", False)],

        computer_questions: [("Whaling / Whaling attack is a kind of phishing attacks that target senior executives and other high profile to access valuable information.", True),
                         ("IPv6 Internet Protocol address is represented as eight groups of four Octal digits.", False),
                         ("CPU controls only input data of computer", False)],

        python_questions: [("A function cannot be defined inside another function", False),
                     ("None is a Python type whose value indicates that no value exists.", True),
                     ("Regular expression processing is built into the Python language.", False)]
}

result = {"Correct": 0, "Incorrect": 0}

def get_quiz_choice():
    while True:
        try:
            quiz_number = int(input('Choose the quiz you like\n1 for {}\n2 for {}\n3 for {}\nYour choice:'.format(general_questions,
                                                                                          computer_questions,
                                                                                          python_questions)))
        except ValueError:
            print ("Not a number, please try again\n")
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print ("Invalid value, please try again\n")
            else:
                return quiz_number


def get_answer(question, correct_answer):
    while True:
        try:
            print ("Q: {}".format(question))
            answer = int(input("1 for True\n0 for False\nYour answer: "))
        except ValueError:
            print ("Not a number, please try again\n")
        else:
            if answer is not 0 and answer is not 1:
                print ("Invalid value, please try again\n")
            elif bool(answer) is correct_answer:
                result["Correct"] += 1
                return True
            else:
                result["Incorrect"] += 1
                return False


choice = get_quiz_choice()
quiz_name = questions[choice - 1]
print ("\nYou chose the {}\n".format(quiz_name))
quiz_questions = quiz[quiz_name]
for q in (quiz_questions):
    print ("Your answer is: {}\n".format(str(get_answer(q[0], q[1]))))
