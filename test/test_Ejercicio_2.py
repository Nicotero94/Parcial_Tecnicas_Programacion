import unittest
import Ejercicio2

class Ejercicio2Test(unittest.TestCase):

    posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

    def test_siReciboUnaListaVaciaDevuelvoUnaListaVacia(self):
        resultado = Ejercicio2.batallaDeBotes([], self.posicionesDeDisparosDePrueba)
        self.assertEqual(resultado, [])

    def test_siReciboUnaListaConUnStringVacioDevuelvoUnaListaVacia(self):
        resultado = Ejercicio2.batallaDeBotes([""], self.posicionesDeDisparosDePrueba)
        self.assertEqual(resultado, [])

    def test_siReciboUnaListaConUnMapaInvalidosDevuelvoUnaListaVacia(self):
        resultado = Ejercicio2.batallaDeBotes(["      "], self.posicionesDeDisparosDePrueba)
        self.assertEqual(resultado, [])

    def test_siReciboUnaListaConUnMapaInvalidoDevuelvoUnaListaVacia(self):
        resultado = Ejercicio2.batallaDeBotes(["soy NO valido"], self.posicionesDeDisparosDePrueba)
        self.assertEqual(resultado, [])

    def test_siReciboUnaListaConOtroMapaInvalidoDevuelvoUnaListaVacia(self):
        resultado = Ejercicio2.batallaDeBotes(["yo","tambien","soy","invalido"], self.posicionesDeDisparosDePrueba)
        self.assertEqual(resultado, [])

    def test_siReciboUnaListaConUnMapaValidoPeroSusFilasNoSonIgualesDevuelvoUnaListaVacia(self):
            resultado = Ejercicio2.batallaDeBotes(["b.b.","....","..bb","b.b"], self.posicionesDeDisparosDePrueba)
            self.assertEqual(resultado, [])

    def test_siReciboUnaListaConUnMapaValidoUnaListaDeTuplasConPosicionesDeDisparoDevuelvoUnaListaDeTuplaConLasPosicionesDeLosBotesNoHundidos(self):
        resultado = Ejercicio2.batallaDeBotes(["b.b..","b...b",".....","....b"], self.posicionesDeDisparosDePrueba)
        self.assertEqual(resultado, [(2,1),(2,5)])

    def test_siReciboUnaListaConUnMapaValidoSinPosicionesDeDDeDisparoDevuelvoUnaListaDeTuplasConLasPosicionesDeLosBotes(self):
        resultado = Ejercicio2.batallaDeBotes(["b..","...","..b"], [])
        self.assertEqual(resultado, [(1,1),(3,3)])
