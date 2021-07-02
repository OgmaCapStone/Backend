import random

def questions_formating(questions,number_of_questions):
    
    random.shuffle(questions)
    json_response = dict()
    json_response['questions'] = list()
    for question in questions[:number_of_questions]:
        json = dict()
        json['question'] = question[0]
        correct_answer = question[3]
        random.shuffle(question[1])
        json['answers'] = check_values(question[1])
        json['correct_answer_index'] = json['answers'].index(correct_answer)
        json['image'] = question[2]
        json_response['questions'].append(json)
    return json_response

def check_question(questions):

    for question in questions['questions']:

        for i in range(0,len(question['answers'])):
            question['answers'][i] = question['answers'][i].replace("''","'")

        question["question"]= question["question"].replace("''","'")

        

    return questions

def check_values(values):

    arr = list()

    for value in values:

        arr.append(value.replace("''","'"))

    return arr