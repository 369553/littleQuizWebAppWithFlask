from flask import render_template, make_response
from dbManagement import getQuizQuestions, getAnswerOfQuestions, getQuizNamesFromDB
import json

# Anasayfa:
def getHomePage():
    return render_template("index.html", redirectList=["ai", "nlp"])

# Gelen sınav ismine göre sınav şablon dosyasına gerekli veritabanı
# tablo ismi parametre olarak gönderilir; gelen sonuç geri döndürülür
def getQuizPage(name):
    response = make_response(render_template("quizPage.html", quizName=name, questions=getQuestions(name), maxPoint=0))
    #response.set_cookie("maxPoint",0)
    return response

# İlgili sınavın bulunamadığına dâir sayfa:
def quizNotFound():
    return "<h3>Sınav bulunamadı</h3>"

# Sınav sorularını nesne olarak getir:
def getQuestions(quizName):
    questions = getQuizQuestions(quizName=quizName)
    return questions

def calculatePoint(data):
    asJson = json.loads(data.decode('utf-8'))
    quizName = asJson["quizName"]
    answers = asJson["answers"]
    realAnswers = getAnswerOfQuestions(quizName)
    trueAnswersCount = 0
    for i in range(0, len(realAnswers)):
        if realAnswers[i] == answers[i]:
            trueAnswersCount += 1
    #print(trueAnswersCount)
    point = (trueAnswersCount / len(realAnswers) * 100)
    #print(point)
    return point

def getQuizNames():
    return getQuizNamesFromDB()