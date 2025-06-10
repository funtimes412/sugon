from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    try:
        data = request.get_json()
        print("testing")
        print(f"Received log data: {data['test']}")
        return "work"
    except Exception as e:
        return "error"

if __name__ == "__main__":
    app.run(host="https://kl2232.onrender.com",port=8000,debug=True)

