from dao import connection


# CONSULTAR TODAS AS CONVIVÊNCIAS
def consultar_convivencias():
    query = """
            select * from convivencias
            """
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    retorno = cursor.fetchall()
    cursor.close()
    conn.close()
    return retorno

# CONSULTAR AVISOS

def consultar_avisos():
    query = """
            select * from avisos
            """
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    retorno = cursor.fetchall()
    cursor.close()
    conn.close()
    return retorno
