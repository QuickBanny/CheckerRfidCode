import unittest
import checker


class CheckerTestCase(unittest.TestCase):
    def test_checker(self):
        path_to_file = 'test_codes.txt'
        list_test_element = [
            ['844881920480', '84481920480']
        ]
        for i in list_test_element:
            self.assertEqual(
                checker.checker(i[0],
                                path_to_file,
                                len_true_code=11,
                                n_changed=3),
                i[1])

    def test_get_code_list(self):
        path_to_file = 'test_codes.txt'
        result_list = ['844881920480', '84481920480', ]
        self.assertEqual(checker.get_true_codes(path_to_file), result_list)

    def test_distance(self):
        list_test_elements = [
            ['123321', '123321', 0],
            ['321321', '3213222', 2],
            ['123321', '000000', 6],
            ['123321', '0000000000', 10],
            ['123321', '', 6],
            ['', '', 0],
            ['123321', '111111', 4],
        ]
        for i in list_test_elements:
            self.assertEqual(checker.distance(i[0], i[1]), i[2])


if __name__ == '__main__':
    unittest.main()
