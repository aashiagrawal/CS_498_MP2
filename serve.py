from flask import Flask
import socket
import subprocess
app = Flask(__name__)

@app.route('/',methods = ['POST'])
def stress_cpu():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return "CPU stress test", 200

@app.route('/',methods = ['GET'])
def get_ip():
    host_name = socket.gethostname()
    IP_addr = socket.gethostbyname(host_name)
    return f'Private IP Address is: {IP_addr}', 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5003)
   app.run(debug = True)