from flask import Flask, request

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def echo_server():
    data = request.data.decode('utf-8')
    response = data.upper()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, threaded=True)
