from flask import Flask, request, Response
#from dbManagement import db
from funcs import getQuizPage, quizNotFound, getHomePage, calculatePoint
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

# SINAV SONUCUNU KARŞILAMA:
@quizApp.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        point = calculatePoint(request.data)# Puanı
        respData = "<h3>" + str(point) + "</h3>"
        resp = Response(response=respData, status=200, mimetype='application/xml')
        return resp
    else:
        return ""

# VARSAYILAN SAYFA BULUNAMADI DÖNÜŞÜNÜN ELE ALINMASI:
@quizApp.errorhandler(404)
def pageNotFound():
    return quizNotFound()

# Uygulamayı çalıştırma:
if __name__ == "__main__":
    quizApp.run(debug=True)