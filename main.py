from flask import Flask, request, Response
#from dbManagement import db
from funcs import getQuizPage, quizNotFound, getHomePage, calculatePoint, getQuizNames
quizApp = Flask(__name__)

# GELEN ANASAYFA İSTEĞİNİ KARŞILAMA:
@quizApp.route("/")
def home():
    return getHomePage()

# GELEN SINAV LİNKLERİNİ KARŞILAMA:
@quizApp.route("/<quizName>")
def quiz(quizName):
    keepGo = False
    for element in getQuizNames():
        if quizName == element:
            keepGo = True
            break
    if keepGo:
        return getQuizPage(quizName)
    else:
        return quizNotFound()

# SINAV SONUCUNU KARŞILAMA:
@quizApp.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        point = calculatePoint(request.data)# Puanı
        respData = "<h3>" + str(point) + "</h3>"
        try:
            resp = Response(response=respData, status=200, mimetype='application/xml')
            return resp
        except:
            return "Response oluşturulurken bir hata oluştu"
    else:
        return ""

# VARSAYILAN SAYFA BULUNAMADI DÖNÜŞÜNÜN ELE ALINMASI:
@quizApp.errorhandler(404)
def pageNotFound():
    return quizNotFound()

# Uygulamayı çalıştırma:
if __name__ == "__main__":
    quizApp.run(debug=False)