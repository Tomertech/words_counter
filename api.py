from flask import Flask
from flask_restful import Api
from word_counter import WordsCounter
from word_statistics import Statistics

# Init app
app = Flask(__name__)

api = Api(app)

api.add_resource(WordsCounter, '/wordscounter')
api.add_resource(Statistics, '/statistics')


if __name__ == '__main__':
    app.run()
