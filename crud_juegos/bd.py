import pymysql

def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='22MORANbay',
        db='juegos',
        port=3306,
        charset='utf8mb4'
    )