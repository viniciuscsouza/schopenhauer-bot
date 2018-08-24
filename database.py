import sqlite3

def selecionaDados(id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT frase FROM frases WHERE ID = ?", (id,))

    for linha in cursor.fetchall():
        print(linha[0])

    conn.close()
    return str(linha[0])


def contaRegistros():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) AS frase FROM frases")

    for quantidade in cursor.fetchone():
        print("Total de registros:", quantidade)
    
    conn.close()
    return quantidade