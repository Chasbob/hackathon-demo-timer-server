from flask import Flask, request, jsonify
import datetime

time_limit = 1 # 1 minute is the default time limit

def main():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def get_time_limit():

        now = datetime.datetime.now()
        end = now + datetime.timedelta(0,0,0,0, time_limit)

        return jsonify({'time' : end})

    app.run(port=3001)