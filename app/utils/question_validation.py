def question_validation(question_given,questions):

    for question in questions:
        if question_given.question == question[5] and question_given.answers == question[1] and question_given.right_answer == question[6] and question_given.image == question[2]:
            return True

    return False