import unittest
from question_c import execute
__author__ = "Uğurkan Hoşgör"
__version__ = "1.0.0"
class TestMain(unittest.TestCase):

    def test_Empty(self):
        str = ""
        expect = ("", 0)
        self.assertEqual(execute(str), expect)

    def test_ABCD(self):
        str = "ABCD"
        expect = ("ABCD", 4)
        self.assertEqual(execute(str), expect)

    def test_ABBCDDEFGHII(self):
        str = "ABBCDDEFGHII"
        expect = ("DEFGHI", 6)
        self.assertEqual(execute(str), expect)

    def test_AABBCCD(self):
        str = "AABBCCD"
        expect = [("AB", 2), ("BC", 2), ("CD", 2)]
        self.assertIn(execute(str), expect)
        
    def test_LongestAtStart(self):
        str = "abcdefghijkkBCD"
        expect = ("abcdefghijk", 11)
        self.assertEqual(execute(str), expect)

    def test_LongestAtEnd(self):
        str = "ABCDaabcdefghijk"
        expect = ("abcdefghijk", 11)
        self.assertEqual(execute(str), expect)

    def test_LongestInMiddle(self):
        str = "cdAABCDDef"
        expect = ("ABCD", 4)
        self.assertEqual(execute(str), expect)

    def test_UnicodeCharacters(self):
        str = "aÖÖÇŞİÜĞ"
        expect = ("ÖÇŞİÜĞ", 6)
        self.assertEqual(execute(str), expect)

    def test_LargeString(self):
        str = "A" * 100000 + "B" * 100000 + "C" * 100000
        expect = [("AB", 2), ("BC", 2)]
        self.assertIn(execute(str), expect)


if __name__ == '__main__':
    unittest.main()