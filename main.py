from flask import Flask, request, redirect
from flask_cors import CORS
from pull import pullPrimary, pullSecondary
import translators as ts
import translators.server as tss
app = Flask('')
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
  return redirect('https://info.classtranslate.com')

@app.route('/getprimary/<lang>')
def getPrimary(lang):
  return pullPrimary(lang)

@app.route('/getsecondary/<lang>')
def getSecondary(lang):
  return pullSecondary(lang)

@app.route('/<lang1>/<lang2>')
def translate(lang1, lang2):
  if lang1 != lang2:
    try: 
      request.args.get("content")
    except NameError: 
      var_exists = False
    else: 
      var_exists = True
    if var_exists:
      translated = tss.google(request.args.get("content"), from_language=lang1, to_language=lang2)
      clarification = tss.google(translated, from_language=lang2, to_language=lang1)
      return({"translated": translated, "clarification": clarification})
  else: 
    return({"translated": request.args.get("content"), "clarification": request.args.get("content")})

app.run('0.0.0.0')
