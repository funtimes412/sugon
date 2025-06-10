from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    if request.is_json:
        data = request.get_json() 
        print("\n--- Received POST request (JSON) ---")
        print(f"Received JSON data: {data}")

        if 'test' in data: 
            print(f"Value of 'test' key: {data['test']}")
            return data['test']
        else:
            print("JSON data does not contain a 'test' key.")
            return "a"
        return data

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
#a
