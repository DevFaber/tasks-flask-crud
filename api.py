from flask import Flask


app = Flask(__name__)

tasks = []

if __name__ == "__main__" :
  app.run(debug=True)