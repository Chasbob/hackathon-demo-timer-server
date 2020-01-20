from flask import Flask, request, jsonify
import datetime

time_limit = 3 # 1 minute is the default time limit
end_time = 0

def main():
    app = Flask(__name__)

    @app.route('/get_countdown', methods=['GET'])
    def countdown():

        now = datetime.datetime.now()
        endtime = now + datetime.timedelta(0,0,0,0, time_limit)

        return jsonify({'time' : endtime})

    app.run(port=3001)

    @app.route('/set_time_limit', methods=['GET', 'POST'])
    def set_time(time):
        try:
            if request.method == "POST":
                time_limit = request.data['time_limit']
        except Exception as e:
            print(e)
