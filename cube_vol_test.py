import unittest
import cube_vol

class testCaseCubeVolume(unittest.TestCase):
        def test_normal_input(self):
                self.assertEqual(cube_vol.vol(4), 64)
        def test_neg_input(self):
                self.assertEqual(cube_vol.vol(-1), "Can not be negative") #input cannot be negative
        def test_type_error(self):
                self.assertRaises(TypeError, cube_vol.vol, "dog") #invalid type of input

if __name__ == '__main__':
        unittest.main()

