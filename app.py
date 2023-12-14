from flask import Flask, render_template
import threading
from PC_control.PC_handler import send_ping_to_main_pc

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ping')
def ping():
    data = {"status": "ON", "ip": "192.168.1.1"}  # Replace with your actual data
    return data
    return send_ping_to_main_pc()

if __name__ == '__main__':
    app.run()