# coding: utf_8
  
import unittest
  
import apriori
import fptree
  
small_trans = [
    (100, [1,2,5]),
    (200, [2,4]),
    (300, [2,3]),
    (400, [1,2,4]),
    (500, [1,3]),
    (600, [2,3]),
    (700, [1,3]),
    (800, [1,2,3,5]),
    (900, [1,2,3]),
    ]
  
min_sup = 2
  
expected_result = {
        1: {(1,): 6, (2,): 7, (3,): 6, (4,): 2, (5,): 2},
        2: {
            (1, 2): 4, (1, 3): 4, (1, 5): 2,
            (2, 3): 4, (2, 4): 2, (2, 5): 2,
            },
        3: {(1, 2, 3): 2, (1, 2, 5): 2},
        }
  
class TestFreqPatternAlgorithms(unittest.TestCase):
    def normalize_result_dict(self, result_dict):
        ndict = {}
        for count in result_dict:
            ndict[count] = {}
            for itemset, sup_count in result_dict[count].iteritems():
                ndict[count][tuple(sorted(itemset))] = sup_count
        return ndict
    def assert_small_trans_result(self, result_dict):
        result_dict = self.normalize_result_dict(result_dict)
        for item_set_size, item_set_results in expected_result.iteritems():
            self.assertEqual(
                    len(item_set_results),
                    len(result_dict[item_set_size])
                    )
            for itemset, sup_count in item_set_results.iteritems():
                self.assertEqual(result_dict[item_set_size][itemset], sup_count)
  
        # Permit algoriths to output empty 4 or 5 item sets.
        for item_set_size in [4,5]:
            if item_set_size in result_dict:
                self.assertTrue(len(result_dict[item_set_size])==0)
  
    def test_apriori(self):
        result_dict = apriori.apriori(small_trans, min_sup)
        self.assert_small_trans_result(result_dict)
  
    def test_fpgrowth(self):
        result_dict = fptree.analyze_trans_set_group_by_size(small_trans, min_sup)
        self.assert_small_trans_result(result_dict)
  
if __name__ == '__main__':
    unittest.main()
