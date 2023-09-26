from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask("FrameAPI")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', required=True)

frames = {
    'frame1': {'title': 'Kacamata Bulat'},
    'frame2': {'title': 'Kacamata Lonjong'}
}

class Frame(Resource):

    def get(self, frame_id):
        if frame_id == "all":
            return frames
        return frames[frame_id]
    
    def put(self, frame_id):
        args = parse.parse_args()
        new_frame = 
        
        
    

api.add_resource(Frame, '/frames/<frame_id>')

if __name__ == '__main__':
    app.run()