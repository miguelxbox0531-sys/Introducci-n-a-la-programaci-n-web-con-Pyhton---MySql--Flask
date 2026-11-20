import unittest
from bd import obtener_conexion  
class TestBaseDeDatos(unittest.TestCase):
    def setUp(self):
        self.conexion = obtener_conexion()
        self.cursor = self.conexion.cursor()

    def tearDown(self):
        self.cursor.close()
        self.conexion.close()

    def test_conexion_exitosa(self):
        self.assertIsNotNone(self.conexion)

    def test_consulta_juegos(self):
        self.cursor.execute("SELECT * FROM juegos")
        resultados = self.cursor.fetchall()
        self.assertIsInstance(resultados, tuple)