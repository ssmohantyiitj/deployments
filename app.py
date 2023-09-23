from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def current_datetime():
    # Get the current date and time
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # Get the current day of the week
    day_of_week = now.strftime("%A")

    return f"Current Date and Time: {date_time_str}<br>Day of the Week: {day_of_week}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
