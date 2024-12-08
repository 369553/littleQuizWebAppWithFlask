import pymysql.cursors
from Question import Question


def getNewConnection():
    connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "LINQSE.1177",
    db = 'quizs',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def getQuizQuestions(quizName):
    keepGo = False
    for element in getQuizNamesFromDB():
        if quizName == element:
            keepGo = True
            break
    if keepGo:
        sql = "SELECT * FROM " + quizName
        questions = []
        connection=getNewConnection()
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
            connection.close()
        return questions
    else:
        return None

def getAnswerOfQuestions(quizName):
    keepGo = False
    for element in getQuizNamesFromDB():
        if quizName == element:
            keepGo = True
            break
    if keepGo:
        sql = "SELECT answer FROM " + quizName
        answers = []
        connection=getNewConnection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                for row in cursor.fetchall():
                    answer = str(row["answer"])
                    answers.append(answer)
        finally:
            connection.close()
        return answers
    else:
        return None

def getQuizNamesFromDB():
    sql = "SHOW TABLES;"
    tableNames = []
    connection=getNewConnection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            for row in cursor.fetchall():
                table = str(row["Tables_in_quizs"])
                tableNames.append(table)
    finally:
        connection.close()
    return tableNames