from counter_utils.counter_utils import load_counter_from_file, delete_counter
from flask_restful import Resource, reqparse
from flask import Response


class Statistics(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('word', required=True, type=str)
        args = parser.parse_args()
        word = args.word.lower()
        try:
            counter = load_counter_from_file()
            return Response(response=f'The word "{word}" appeared so far {counter[word]} times', status=401)
        except OSError:
            Response(response="ERROR: could not load counter file", status=401)

    def delete(self):
        try:
            delete_counter()
            return Response(response="Counter was reset", status=200)
        except OSError:
            Response(response="ERROR: could not reset counter", status=401)

