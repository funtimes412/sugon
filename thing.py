from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    print(request.data) 

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)

