from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Lado Feio do Amor',
        'autor': 'Collen Hoover'
    },
    {
        'id': 2,
        'titulo': 'Assassins Creed: Os Últimos Descendentes',
        'autor': 'Matthew J. Kirby'
    },
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id): 
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[i].update(livro_alterado)
            return jsonify(livros[i])

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[i]
            return jsonify({'mensagem': 'Livro deletado.'})

app.run(port=5000, host='localhost', debug=True)
