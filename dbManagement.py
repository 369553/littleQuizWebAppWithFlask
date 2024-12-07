import pymysql.cursors
from Question import Question

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "LINQSE.1177",
    db = 'quizs',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def getQuizQuestions(quizName):
    keepGo = False
    match quizName:
        case "nlp":
            keepGo = True
        case "ai":
            keepGo = True
    if keepGo:
        sql = "SELECT * FROM " + quizName
        questions = []
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                for row in cursor.fetchall():
                    id = int(row["id"])
                    questionText = str(row["question"])
                    optA = str(row["optionA"])
                    optB = str(row["optionB"])
                    optC = str(row["optionC"])
                    optD = str(row["optionD"])
                    answer = str(row["answer"])
                    explanation = str(row["explanation"])
                    question = Question (id, questionText, optA, optB, optC, optD, answer, explanation)
                    questions.append(question)
        finally:
            pass
            #connection.close()
        return questions
    else:
        return None
    