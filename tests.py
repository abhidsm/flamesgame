import flames 
import unittest


class TestFlamesMethods(unittest.TestCase):
    
    def test_flames_count(self):
        self.assertEqual(flames.flames_count('abhi','abhi'),0)
        self.assertEqual(flames.flames_count('abhi','a'),3)
        self.assertEqual(flames.flames_count('abhi','asd'),5)

    def test_flames_result(self):
        self.assertEqual(flames.flames_result(1),'S')
        self.assertEqual(flames.flames_result(2),'E')
        self.assertEqual(flames.flames_result(3),'F')
        self.assertEqual(flames.flames_result(7),'E')
        self.assertEqual(flames.flames_result(10),'L')
        self.assertEqual(flames.flames_result(15),'M')
        self.assertEqual(flames.flames_result(21),'F')
        self.assertEqual(flames.flames_result(28),'A')
        self.assertEqual(flames.flames_result(30),'A')

    def test_calculate(self):
        self.assertEqual(flames.calculate('abhi','abhil'),'S')
        self.assertEqual(flames.calculate('abhi','abhila'),'E')
        self.assertEqual(flames.calculate('abhi','abhilas'),'F')
        self.assertEqual(flames.calculate('abhi','abhilashdsm'),'E')
        self.assertEqual(flames.calculate('Abhi',' abHil '),'S')
        self.assertEqual(flames.calculate('abhi','abhi.l'),'S')

        
        

if __name__ == '__main__':
    unittest.main()

