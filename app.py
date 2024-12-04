from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'root',
    'password': 'root',
    'database': 'teste_web_developer'
}
def db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/verbas', methods=['GET'])
def listar_verbas():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT a.id, t.nome_acao AS acao, a.investimento, a.data_prevista
        FROM acao a JOIN tipo_acao t ON a.codigo_acao = t.codigo_acao
    """)
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)

@app.route('/verbas', methods=['POST'])
def adicionar_verba():
    data = request.json
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT codigo_acao FROM tipo_acao WHERE nome_acao = %s", (data['acao'],))
    codigo_acao = cursor.fetchone()
    if not codigo_acao:
        return jsonify({'error': 'Tipo de ação não encontrado'}), 400
    cursor.execute("""
        INSERT INTO acao (codigo_acao, investimento, data_prevista, data_cadastro)
        VALUES (%s, %s, %s, NOW())
    """, (codigo_acao[0], data['investimento'], data['dataPrevista']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Verba adicionada com sucesso!'})

@app.route('/verbas/<int:id>', methods=['PUT'])
def editar_verba(id):
    data = request.json
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE acao SET investimento = %s, data_prevista = %s WHERE id = %s
    """, (data['investimento'], data['dataPrevista'], id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Verba editada com sucesso!'})

@app.route('/verbas/<int:id>', methods=['DELETE'])
def excluir_verba(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM acao WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Verba excluída com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
