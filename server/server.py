from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
api = Api(app)



# REST API FUNCTIONS
class getRequest(Resource):
    def get(self):
        success = {"response": 1}
        failure = {"response": 0}
        sendSMS()
        return success


api.add_resource(getRequest, '/sms/')



def sendSMS():
    print("test")


if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0')
