import unittest
import seventeen


class Test(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = seventeen.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUEN DIA")


if __name__ == "__main__":
    unittest.main()
