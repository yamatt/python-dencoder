import unittest
from dencoder import Dencoder

class TestDencoder(unittest.TestCase):
    def setUp(self):
        self.sb64 = Dencoder(Dencoder.BASE64)
        self.shex = Dencoder(Dencoder.HEX)
        self.urls = Dencoder(Dencoder.URL_SAFE)
        
    def test_encode(self):
        result0 = self.sb64.encode(0)
        result1 = self.sb64.encode(1)
        result35 = self.sb64.encode(35)
        result120 = self.sb64.encode(120)
        result1024 = self.sb64.encode(1024)
        self.assertEquals(result0, 'a')
        self.assertEquals(result1, 'b')
        self.assertEquals(result35, 'J')
        self.assertEquals(result120, 'b4')
        self.assertEquals(result1024, 'qa')
        
    def test_decode(self):
        result0 = self.sb64.decode('a')
        result1 = self.sb64.decode('b')
        result35 = self.sb64.decode('J')
        result120 = self.sb64.decode('b4')
        result1024 = self.sb64.decode('qa')
        result_abc = self.sb64.decode('abc')
        result_xyz = self.sb64.decode('xyz')
        self.assertEquals(result0, 0)
        self.assertEquals(result1, 1)
        self.assertEquals(result35, 35)
        self.assertEquals(result120, 120)
        self.assertEquals(result1024, 1024)
        self.assertEquals(result_abc, 66)
        self.assertEquals(result_xyz, 95769)
        
    def test_matching(self):
        shex = "12AB"
        shexe = self.shex.decode(shex)
        shexd = self.shex.encode(shexe)
        self.assertEquals(shex, shexd)
        urls = "xyz"
        urlse = self.urls.decode(urls)
        urlsd = self.urls.encode(urlse)
        self.assertEquals(urls, urlsd)
        urls2 = "abc"
        urlse2 = self.urls.decode(urls2)
        urlsd2 = self.urls.encode(urlse)
        self.assertNotEquals(urls2, urlsd2) # because starting with a means it begins with 0
        
    def test_check(self):
        self.assertTrue(self.sb64.in_alphabet("abc"))
        self.assertTrue(self.sb64.in_alphabet("xyz"))
        self.assertTrue(self.sb64.in_alphabet("123"))
        self.assertTrue(self.sb64.in_alphabet("+/"))
        self.assertFalse(self.sb64.in_alphabet("-_"))
        self.assertFalse(self.sb64.in_alphabet("!~"))

if __name__ == '__main__':
    unittest.main()
