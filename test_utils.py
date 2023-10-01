import unittest

from utils import (get_word_ls,
                   get_score,
                   get_score_advanced,
                   is_cheat_at_letter
                   )


class TestMainClass(unittest.TestCase):
    # get_score(user_word:str, target_word:str) Signature for get_score

    def test_simple_scoring(self):
        _test_cases = [("LELIYL", "DFLSLD"),
                       ("DFLSLD", "LELIYL"),
                       ("ECCCC", "CRANK"),
                       ("CCCCC", "CRANK"),
                       ]
        _results = [["?", "-", "+", "-", "-", "?"],
                    ["-", "-", "+", "-", "?", "-"],
                    ["-", "?", "?", "?", "?"],
                    ["+", "?", "?", "?", "?"]
                    ]

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
                       ("ECCCC", "CRANK"),
                       ("CCCCC", "CRANK"),
                       ]

        _results = [["-", "-", "+", "-", "?", "-"],
                    ["+", "+", "-", "-", "?"],
                    ["?", "-", "+", "-", "-", "-"],
                    ["+", "-", "+", "-", "-", "+"],
                    ["+", "?", "+", "-", "-", "+"],
                    ["-", "-", "-", "?", "?", "?"],
                    ["-", "-", "+", "-", "?", "?"],
                    ["-", "?", "-", "-", "-"],
                    ["+", "-", "-", "-", "-"],
                    ]

        for t_case, res in zip(_test_cases, _results):
            self.assertEqual(get_score_advanced(*t_case), res)


class TestCheat(unittest.TestCase):
    def setUp(self) -> None:
        all_words_path = r".\word-bank\all_words.txt"
        target_words_path = r".\word-bank\target_words.txt"

        self.all_words = get_word_ls(all_words_path)
        self.target_words = get_word_ls(target_words_path)

    def test_cheat(self):
        self.assertTrue(is_cheat_at_letter("aaade", "dfaaf", "a"))
        self.assertTrue(is_cheat_at_letter("aaaaa", "asdad", "a"))

        self.assertFalse(is_cheat_at_letter("dfaaf", "aaade", "a"))
        self.assertFalse(is_cheat_at_letter("asdad", "aaaaa", "a"))
        self.assertFalse(is_cheat_at_letter("aaabbb", "aaabbb", "a"))

        self.assertTrue(is_cheat_at_letter("aaabbbb", "aabbbbb", "a"))
        self.assertFalse(is_cheat_at_letter("aaabbbb", "aabbbbb", "b"))

    def test_scoring_compare(self):  # Scoring is the same if Non-cheat scenario
        self.assertEqual(get_score("dfaaf", "aaade"), get_score_advanced("dfaaf", "aaade"))
        self.assertEqual(get_score("asdad", "aaaaa"), get_score_advanced("asdad", "aaaaa"))
        self.assertEqual(get_score("aaabbb", "aaabbb"), get_score_advanced("aaabbb", "aaabbb"))

        self.assertEqual(get_score("CRANK", "ECCCC"), get_score_advanced("CRANK", "ECCCC"))

        self.assertNotEqual(get_score("aaade", "dfaaf"), get_score_advanced("aaade", "dfaaf"))
        self.assertNotEqual(get_score("aaaaa", "asdad"), get_score_advanced("aaaaa", "asdad"))
        self.assertNotEqual(get_score("aaabbbb", "aabbbbb"), get_score_advanced("aaabbbb", "aabbbbb"))


if __name__ == "__main__":
    unittest.main()
