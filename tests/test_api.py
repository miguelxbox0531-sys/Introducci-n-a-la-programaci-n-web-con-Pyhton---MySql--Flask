import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bd import obtener_conexion 
import controlador_juegos

class TestControlador(unittest.TestCase):
    def setUp(self):
        self.conexion = obtener_conexion()
        self.cursor = self.conexion.cursor()
        
        
        self.cursor.execute("DELETE FROM juegos WHERE nombre = 'Juego Test'")
        self.conexion.commit()

    def tearDown(self):
        
        self.cursor.execute("DELETE FROM juegos WHERE nombre = 'Juego Test'")
        self.conexion.commit()
        self.cursor.close()
        self.conexion.close()

    def test_insertar_juego(self):
       
        controlador_juegos.insertar_juego('Juego Test', 'Descripcion Test', 99.99)

        
        self.cursor.execute("SELECT * FROM juegos WHERE nombre = 'Juego Test'")
        resultado = self.cursor.fetchone()
        
        
        self.assertIsNotNone(resultado, "El juego no se insertó en la base de datos")
        self.assertEqual(resultado[1], 'Juego Test')
        self.assertEqual(resultado[3], 99.99)