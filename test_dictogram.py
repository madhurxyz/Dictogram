#!python


from __future__ import division, print_function
from histograms import Dictogram#, Listogram
import unittest


class DictogramTest(unittest.TestCase):

    # test fixtures
    text_str = 'one fish two fish red fish blue fish'
    text_list = text_str.split()
    hist_list = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    hist_dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

    def test_items(self):
        hist_dict = Dictogram(self.text_list)
        assert len(hist_dict) == 5
        assert hist_dict == self.hist_dict
        self.assertItemsEqual(hist_dict, self.hist_dict)

        hist_list = hist_dict.items()
        assert len(hist_list) == 5
        self.assertItemsEqual(hist_list, self.hist_list)

    def test_count(self):
        hist_dict = Dictogram(self.text_list)
        assert hist_dict.types == 5
        assert hist_dict.tokens == 8
        assert hist_dict.count('one') == 1
        assert hist_dict.count('two') == 1
        assert hist_dict.count('red') == 1
        assert hist_dict.count('blue') == 1
        assert hist_dict.count('fish') == 4
        assert hist_dict.count('food') == 0

    def test_update(self):
        hist_dict = Dictogram(self.text_list)
        hist_dict.update(['two', 'blue', 'fish', 'food'])
        assert hist_dict.types == 6
        assert hist_dict.tokens == 12
        assert hist_dict.count('one') == 1
        assert hist_dict.count('two') == 2
        assert hist_dict.count('red') == 1
        assert hist_dict.count('blue') == 2
        assert hist_dict.count('fish') == 5
        assert hist_dict.count('food') == 1

    def test_contains(self):
        hist_dict = Dictogram(self.text_list)
        for word in self.text_list:
            assert word in hist_dict
        for word in ['fishy', 'food']:
            assert word not in hist_dict

if __name__ == '__main__':
    unittest.main()
