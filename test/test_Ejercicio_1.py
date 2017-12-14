import unittest
import Ejercicio1


class Ejercicio1Test(unittest.TestCase):

    def testSiReciboUnStringVacioDevuelvoUnaListaVacia(self):
        resultado=Ejercicio1.rotacionDeUnaPalabra("")
        self.assertEqual(resultado,[])

    def testSiReciboUnStringConEspaciosDevuelvoUnaListaVacia(self):
        resultado = Ejercicio1.rotacionDeUnaPalabra("     ")
        self.assertEqual(resultado, [])

    def testSiReciboUnaLetraDevuelvoUnaListaConEsaLetra(self):
        resultado = Ejercicio1.rotacionDeUnaPalabra("a")
        self.assertEqual(resultado, ['a'])

    def testSiReciboPalabraDeDosLetrasDevuelvoUnaListaConEsaPalabraMasUnaRotacionDeEsaPalabra(self):
        resultado = Ejercicio1.rotacionDeUnaPalabra("ab")
        self.assertEqual(resultado, ['ab','ba'])

    def testSiReciboUnaPalabraDeTresLetrasDevuelvoUnaListaConEsaPalabraMasDosRotacionesDeEsaPalabra(self):
        resultado = Ejercicio1.rotacionDeUnaPalabra("paz")
        self.assertEqual(resultado, ['paz','azp','zpa'])

    def testSiReciboUnaPalabraDeCuatroLetrasDevuelvoUnaListaConEsaPalabraMasTresRotacionesDeEsaPalabra(self):
        resultado = Ejercicio1.rotacionDeUnaPalabra("so l")
        self.assertEqual(resultado, ['so l','o ls',' lso','lso '])

    def testSiReciboUnaPalabraDeCincoLetrasDevuelvoUnaListaConEsaPalabraMasCuatroRotacionesDeEsaPalabra(self):
        resultado = Ejercicio1.rotacionDeUnaPalabra("rotar")
        self.assertEqual(resultado, ['rotar','otarr','tarro','arrot','rrota'])



