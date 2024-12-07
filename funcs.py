from flask import render_template
from Question import Question
from dbManagement import getQuizQuestions


# Anasayfa:
def getHomePage():
    return render_template("index.html", redirectList=["ai", "nlp"])

# Gelen sınav ismine göre sınav şablon dosyasına gerekli veritabanı
# tablo ismi parametre olarak gönderilir; gelen sonuç geri döndürülür
def getQuizPage(name):
    return render_template("quizPage.html", quizName=name, questions=getQuestions(name))

# İlgili sınavın bulunamadığına dâir sayfa:
def quizNotFound():
    return "<h3>Sınav bulunamadı</h3>"

# Sınav sorularını nesne olarak getir:
def getQuestions(quizName):
    questions = getQuizQuestions(quizName=quizName)
    return questions