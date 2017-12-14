import unittest
import Ejercicio3

class Ejercicio3Test(unittest.TestCase):

    def siReciboUnaListaVaciaDevuelvoUnStringVacio(self):
        resultado = Ejercicio3.calculadorDelEquipoGanadorDeLaLiga([])
        self.assertEqual(resultado, "")

    def siReciboUnaListaDeTuplaConUnPartidoDevuelvoAlEquipoGanador(self):
        resultado = Ejercicio3.calculadorDelEquipoGanadorDeLaLiga([("a", 1, "b", 0)])
        self.assertEqual(resultado, "a")

    def siReciboUnaListaDeTuplaConTresPartidosDevuelvoAlEquipoGanador(self):
        resultado = Ejercicio3.calculadorDelEquipoGanadorDeLaLiga([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)])
        self.assertEqual(resultado, "c")

    def siReciboUnaListaDeTuplaConTresPartidosPeroTodosTieneLosMismosPuntosDevuelvoAlEquipoGanadorAlfabeticamente(self):
        resultado = Ejercicio3.calculadorDelEquipoGanadorDeLaLiga([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)])
        self.assertEqual(resultado, "Almagro")

    def siReciboUnaListaDeTuplaConCuatroPartidosDevuelvoAlEquipoGanador(self):
        resultado = Ejercicio3.calculadorDelEquipoGanadorDeLaLiga([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)])
        self.assertEqual(resultado, "a")