from flask import Flask, jsonify, request

app = Flask(__name__)


disciplinas = []

@app.route('/disciplinas', methods=['POST'])
def criar():
    dados = request.get_json()
    campos = ("titulo", "data_inicio", "data_termino", "vagas", "eh_verao")
    if not all(k in dados for k in campos):
        return jsonify({"erro": "Dados incompletos"}), 400
    
    
    dados['id'] = len(disciplinas) + 1
    disciplinas.append(dados)
    return jsonify(dados), 201

@app.route('/disciplinas', methods=['GET'])
def listar():
    return jsonify(disciplinas), 200

@app.route('/disciplinas/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    for d in disciplinas:
        if d['id'] == id:
            d.update(dados)
            return jsonify(d), 200
    return jsonify({"erro": "Disciplina nao encontrada"}), 404

@app.route('/disciplinas/<int:id>', methods=['DELETE'])
def excluir(id):
    global disciplinas
    for d in disciplinas:
        if d['id'] == id:
            disciplinas = [item for item in disciplinas if item['id'] != id]
            return jsonify({"mensagem": "Excluido com sucesso"}), 200
    return jsonify({"erro": "Disciplina nao encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
