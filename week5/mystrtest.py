import unittest
import mystr


class TestStrSlice(unittest.TestCase):
    def test_str(self):
        n = 2
        str1 = "I have a pen I have an apple"
        str2 = "Pen pineapple apple pen"
        lowercase, upperCount, alphaCount, strLongest = mystr.str_slicing(n, str1, str2)
        self.assertEqual(lowercase, "haveapenhaveanappleenpineappleapplepen")
        self.assertEqual(upperCount, 3)
        self.assertEqual(alphaCount, 51)
        self.assertEqual(strLongest, "pineapple")

        n2 = 2
        str3 = "THE END OF THE WORLD"
        str4 = "FINALE OF THE SHOW"
        lowercase2, upperCount2, alphaCount2, strLongest2 = mystr.str_slicing(n2, str3, str4)
        self.assertEqual(lowercase2, "No lowercase letters")
        self.assertEqual(upperCount2, 31)
        self.assertEqual(alphaCount2, 38)
        self.assertEqual(strLongest2, "FINALE")

        n3 = 2
        str5 = "There's a growing trend among teenagers"
        str6 = "A dead duck does not fly backward"
        lowercase3, upperCount3, alphaCount3, strLongest3 = mystr.str_slicing(n3, str5, str6)
        self.assertEqual(lowercase3, "heresagrowingtrendamongteenagersdeadduckdoesnotflybackward")
        self.assertEqual(upperCount3, 2)
        self.assertEqual(alphaCount3, 72)
        self.assertEqual(strLongest3, "teenagers")
