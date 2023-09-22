import unittest

from utils import get_score, get_score_advanced


class TestMainClass(unittest.TestCase):
    # get_score(user_word:str, target_word:str) Signature for get_score

    def test_simple_scoring(self):
        _test_cases = [("LELIYL", "DFLSLD"), ("DFLSLD", "LELIYL")]
        _results = [["?", "-", "+", "-", "-", "?"], ["-", "-", "+", "-", "?", "-"]]

        for t_case, res in zip(_test_cases, _results):
            self.assertEqual(get_score(*t_case), res)

    def test_advanced_scoring(self):
        # Note: get_score_advanced(user_word, target_word) Signature
        _test_cases = [("DFLSLD", "LELIYL"),
                       ("LLOIL", "LLLLP"),
                       ("LELIYL", "DFLSLD"),
                       ("LLLLLL", "LELIYL"),
                       ("LLLLUL", "LELILL"),
                       ("TGULLL", "LLLRFO"),
                       ("TGLULL", "LLLRFO"),
                       ]

        _results = [["-", "-", "+", "-", "?", "-"],
                    ["+", "+", "-", "-", "?"],
                    ["?", "-", "+", "-", "-", "-"],
                    ["+", "-", "+", "-", "-", "+"],
                    ["+", "?", "+", "-", "-", "+"],
                    ["-", "-", "-", "?", "?", "?"],
                    ["-", "-", "+", "-", "?", "?"],
                    ]

        for t_case, res in zip(_test_cases, _results):
            self.assertEqual(get_score_advanced(*t_case), res)
