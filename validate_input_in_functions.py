
    """
    Program:  validate_input_in_functions.py
    author:  Lisa Kilmer
    last date modified:  6/17/2020
    The purpose of this program is to take input for the test score and to make sure it is in range 0-100.
    print test_name:test_score
    :param prompt: test_score, input score
    :param retries: 3
    :param test_name: =Math mandatory
    :param test_score: default = 0 user input for test score
    :param invalid_message: Invalid test score, try again!
    :return: test_name:test_score
    """
def score_input(prompt, retries=3, test_name='Math', test_score=0, invalid_message='Invalid test score, try again!'):
    while True:
        test_score = input(prompt)
        if test_score in range(0, 101):
            #return test_name:test_score
            return test_name,test_score
            return pass
        if test_score not in range(0, 101):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError(invalid_message)

        if retries < 0:
            raise ValueError(invalid_message)



if __name__ == '__main__':
    test_score = int(score_input("What is your score? "))
    print('test_name', ':', test_score)
