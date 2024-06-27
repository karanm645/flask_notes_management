from flask import Flask

def create_app():
  app = Flask(__name__) #name of the file that was ran
  # secure cookies and session data
  app.config['SECRET_KEY'] = "jiofepwaj fioepwjfiopwea" # in production never share
  
  return app