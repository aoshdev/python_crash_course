"""
Ch11: testing code
"""

# using this sample function
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")


# testing a function
import unittest

# create a class which contains a series of unit tests for a function
# it must inherit from another class: unittest.TestCase
class NamesTestCase(unittest.TestCase):
    """"Tests for get_formatted_names"""

    #methods MUST start with test_
    #methods starting with test_ will run automatically
    def test_first_last_name(self): 
        """Test 1 case"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') #expected result
    
if __name__ == '__main__':
    unittest.main()

# the above code would be run as it's being imported (don't need to call)


# testing a class
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """Show the survey question."""
        print(self.question)
        
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


question = "What language do you speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time you wish to quit. \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

my_survey.show_results()

import unittest

class TestAnonymouseSurvey(unittest.TestCase):
    """Test AnonymousSurvey class"""

    def test_store_single_response(self):
        """Test single response stored properly"""
        question = "example question"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    
    def test_three_responses(self):
        """Test 3 responses stored properly"""
        question = "example question"
        my_survey = AnonymousSurvey(question)
        responses = ['a','b','c']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()



# using the setUp() method
# allows you to create obejcts once and use them in each test method

class TestAnonymouseSurvey(unittest.TestCase):
    """Test AnonymousSurvey class"""

    # this method is from unittest.TestCase()
    # this is run before the test_ methods
    # objects created here can then be used in each test method
    def setUp(self): 
        """create survey and set of responses to be used in test"""
        question = "Example question"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['a','b','c']

    def test_store_single_response(self):
        """Test single response stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_three_responses(self):
        """Test 3 responses stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()











