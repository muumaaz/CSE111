#2
class Question:
    def __init__(self, text, choices, correct_choice):
        # Initialize three instance variables
        # text(type str), choices(type list), correct_choice(type int)
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

class Quiz:
    # Initialize a static variable for counting the number of Quizzes
    # or, to count the number of Quiz class objects
    total_quizzes = 0

    def __init__(self, quiz_name):
      # Initialize instance variable name (type str)
      # Initialize instance variable question (type list)
      # Initialize instance variable score (type int)
      self.name = quiz_name
      self.questions = []
      self.score = 0
      Quiz.total_quizzes += 1


    def add_question(self, *questions):
      # Append the question objects in the question list
      for q in questions:
        self.questions.append(q)

    @classmethod
    def create_from_data(cls, quiz_name, question_data_list):
      # Firstly, make a Quiz class object by passing the quiz_name parameter in the constructor
      quiz = cls(quiz_name)

      # From the question_data_list extract the Question data
      for q in question_data_list:
        text = q['text']
        choices = q['choices']
        correct_choice = q['correct_choice']
      # After that, make the Question class objects passing the extracted data in the constructor
        #question = Question(q['text'], q['choices'], q['correct_choice'])
        question = Question(text, choices, correct_choice)
      # Append those in the question list of the Quiz class object
        quiz.add_question(question)
      # Finally, return the Quiz class object
      return quiz


    def attempt(self):
      '''
      Sample printing format for attempt method.
      let's say we are calling quiz1.attempt() from the driver code.
      output:

      --- Math Quiz ---
      What is the result of 2 + 2?
      1. 3
      2. 4
      3. 5
      Your answer (enter the choice number): 2
      Correct answer! 1 point for you.
      What is the result of 3 * 6?
      1. 15
      2. 18
      3. 20
      Your answer (enter the choice number): 1
      Wrong answer!
      Your total score: 1/2
      '''
      print(f"--- {self.name} ---")

      for question in self.questions:
        print(f"{question.text}") # will print the question as shown in the output.
        for index in range(len(question.choices)):# this loop will print the choices as shown in the output.
            print(f"{index+1}. {question.choices[index]}")

        user_choice = int(input("Your answer (enter the choice number): ")) # takes the choice number from the user

        if user_choice == question.correct_choice: # calculate the quiz score
            self.score += 1
            print("Correct answer! 1 point for you.")
        else:
          print("Wrong answer!")
      print(f"Your total score: {self.score}/{len(self.questions)}") # total score gained in a quiz

# Test the Quiz Maker

# We are creating a Quiz object for the Math Quiz
quiz1 = Quiz("Math Quiz")
# Now creating two quiz question objects
# The Question class constructor takes three parameters: (Question, choices, correct answer)
# The correct answer is given as (list_index + 1)
quiz1_question1 = Question("What is the result of 2 + 2?", ["3", "4", "5"], 2)
quiz1_question2 = Question("What is the result of 3 * 6?", ["15", "18", "20"], 2)
# Adding the question objects to a question list of the Quiz class
quiz1.add_question(quiz1_question1, quiz1_question2)
# We will use this list of dictionaries to prepare the python quiz questions
python_quiz_data = [
    {
        'text': "What is the keyword to define a function in Python?",
        'choices': ["func", "def", "function"],
        'correct_choice': 2
    },
    {
        'text': "Which one is NOT a built-in data type in Python?",
        'choices': ["int", "str", "double"],
        'correct_choice': 3
    }
]
# Create another Quiz class object for the python quiz
quiz2 = Quiz.create_from_data("Python Quiz", python_quiz_data)
# Accessing static variable using the class name
print("Total no. of quizzes: ", Quiz.total_quizzes)
# Attempt Math Quiz
quiz1.attempt()
# Attempt Python Quiz
quiz2.attempt()