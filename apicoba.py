from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi objek flask
app = Flask (__name__)

# inisiasi ibjek flask_restful
api = Api(app)

#inisiasi objek flask_cors
CORS(app)

# buat class resource
class ContohResource(Resource):
    def get(self):
        response = {"message" : "Haii"}
        return response
