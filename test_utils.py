import unittest

from utils import get_score


class TestMainClass(unittest.TestCase):
    # get_score(user_word:str, target_word:str) Signature for get_score
    _test_cases = [("LELIYL", "DFLSLD"), ("DFLSLD", "LELIYL")]
    _results = [["?", "-", "+", "-", "-", "?"], ["-", "-", "+", "-", "?", "-"]]

    def test_scoring(self):
        for t_case, res in zip(self._test_cases, self._results):
            self.assertEqual(get_score(*t_case), res)