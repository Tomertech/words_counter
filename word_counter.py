from counter_utils.counter_utils import word_counter
from flask_restful import Resource, reqparse
from flask import Response


class WordsCounter(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('source', required=True, type=str)
        parser.add_argument('type', choices=['url', 'file', 'string'], required=True, type=str)
        args = parser.parse_args()
        try:
            word_counter(args.source, args.type)
        except (ValueError, OSError):
            return Response(response="ERROR: source is invalid", status=401)

        return Response(response="Got it!", status=200)




