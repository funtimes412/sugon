from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    print(request.data) 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)

