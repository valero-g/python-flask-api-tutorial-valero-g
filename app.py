from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label" : "Ir a comprar a Lidl", "done": False},
    {"label": "Preparar la cena", "done": False}
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print(request_body)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>',methods= ['DELETE'])
def delete_todo(position):
    print("This is the position to delete", position)
    del(todos[position])
    return jsonify(todos)


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=3245, debug= True)