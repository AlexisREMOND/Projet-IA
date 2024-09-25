from flask import Flask, request, render_template
import requests, urllib
from deep_translator import GoogleTranslator

app = Flask(__name__, template_folder="templates")

id_app = "7549WP-T6WUWE3U7X"
host = "api.wolframalpha.com"
con_id = ""
s = ""

qr = []

@app.route("/")
def home():
    return render_template("home.html", data=qr)

@app.route("/", methods=["POST"])
def activerSiri(con_id=None):
    global can_id, host, s

    qrtemp = []

    question = request.form["question"]
    qrtemp.append(question)
    question = GoogleTranslator(source="fr", target="en").translate(question)

    if con_id:
        query = f"http://{host}/v1/conversation.jsp?appid={id_app}&conversationid={con_id}&i={urllib.parse.quote_plus(question)}"
    else:
        query = f"http://{host}/v1/conversation.jsp?appid={id_app}&i={urllib.parse.quote_plus(question)}"
    if s:
        query += f"&s={s}"
        s = ""

    reponse = requests.get(query).json()

    if reponse.get('error', 0):
        qrtemp.append("Erreur")
        qr.append(qrtemp)
        #qr.append([question, "Erreur"])
        return home()

    con_id = reponse["conversationID"]
    host = reponse["host"] + "/api"
    s = reponse.get("s", "")

    reponse = GoogleTranslator(source="en", target="fr").translate(reponse["result"])
    qrtemp.append(reponse)
    qr.append(qrtemp)
    #qr.append([question, reponse["result"]])

    return home()

if __name__ == "__main__":
    app.run()


