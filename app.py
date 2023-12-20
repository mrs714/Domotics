from flask import Flask, render_template
from PC_control.PC_handler import send_ping_to_main_pc, send_WOL_to_main_pc
from NAS_control.NAS_handler import get_nas_info

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ping')
def ping():
    return send_ping_to_main_pc()

@app.route('/wol')
def wol():
    return send_WOL_to_main_pc()

@app.route('/nas')
def nas():
    return get_nas_info()

if __name__ == '__main__':
    app.run()