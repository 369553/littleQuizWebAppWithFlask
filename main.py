from flask import Flask, request
#from dbManagement import db
from funcs import getQuizPage, quizNotFound, getHomePage
quizApp = Flask(__name__)

# GELEN ANASAYFA İSTEĞİNİ KARŞILAMA:
@quizApp.route("/")
def home():
    return getHomePage()

# GELEN SINAV LİNKLERİNİ KARŞILAMA:
@quizApp.route("/<quizName>")
def quiz(quizName):
    match(quizName):
        case "nlp":
            return getQuizPage("nlp")
        case "ai":
            return getQuizPage("ai")
        case _:
            return quizNotFound()
    content = "AA"
    return f"<p>{content}</p>"

# VARSAYILAN SAYFA BULUNAMADI DÖNÜŞÜNÜN ELE ALINMASI:
@quizApp.errorhandler(404)
def pageNotFound():
    return quizNotFound()

# Uygulamayı çalıştırma:
if __name__ == "__main__":
    quizApp.run(debug=True)