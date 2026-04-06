from flask import Flask, jsonify, request

app = Flask(__name__)
disciplinas = []

@app.route('/disciplinas', methods=['POST'])
def criar():
    dados = request.get_json()
    # Validação simples para os campos obrigatórios
    if not all(k in dados for k in ("titulo", "vagas", "eh_verao")):
        return jsonify({"erro": "Dados incompletos"}), 400
    disciplinas.append(dados)
    return jsonify(dados), 201

@app.route('/disciplinas', methods=['GET'])
def listar():
    return jsonify(disciplinas), 200

if __name__ == '__main__':
    app.run(debug=True)


# Versão final para entrega da atividade
# Testando a esteira do GitHub Actions com 75% de cobertura