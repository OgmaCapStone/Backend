from app.utils.question_validation import question_validation
from app.utils.Classes import Questions

new_valid_question = Questions(
        answers = ["wrong answer 1","wrong answer 2","new right answer","wrong answer 4"],
        image = "",
        level = 1,
        technology = 1,
        question =  "New question",
        right_answer = "new right answer",
        password = "password"
    )

new_invalid_question = Questions(
        answers = ["wrong answer 1","wrong answer 2","right_answer","wrong answer 4"],
        image = "",
        level = 1,
        technology = 1,
        question =  "question",
        right_answer = "right answer",
        password = "password"
    )




db_questions = [[
    "id",
    ["wrong answer 1","wrong answer 2","right_answer","wrong answer 4"],
    "",
    1,
    1,
    "question",
    "right answer",
    ]
    ]

def test_should_pass():
    assert question_validation(new_invalid_question,db_questions) == True

def test_should_not_pass():
    assert question_validation(new_valid_question,db_questions) == False