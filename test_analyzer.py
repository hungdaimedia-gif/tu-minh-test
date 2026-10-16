"""Unit tests for analyzer.py (full coverage of public functions)."""

import unittest
from analyzer import count_words, count_sentences, top_words


class TestCountWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_blank_string(self):
        self.assertEqual(count_words("   \n\t  "), 0)

    def test_single_word(self):
        self.assertEqual(count_words("hello"), 1)

    def test_simple_sentence(self):
        self.assertEqual(count_words("hello world"), 2)

    def test_extra_whitespace(self):
        self.assertEqual(count_words("  hello   world \n new\tline "), 4)

    def test_punctuation_not_counted(self):
        self.assertEqual(count_words("hello, world! how's it going?"), 6)

    def test_numbers_count_as_words(self):
        self.assertEqual(count_words("I have 2 apples"), 4)


class TestCountSentences(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_sentences(""), 0)

    def test_blank_string(self):
        self.assertEqual(count_sentences("   "), 0)

    def test_single_sentence(self):
        self.assertEqual(count_sentences("Hello world."), 1)

    def test_multiple_sentences(self):
        self.assertEqual(count_sentences("Hello. How are you? Fine!"), 3)

    def test_no_terminator_counts_as_one(self):
        self.assertEqual(count_sentences("just some words"), 1)

    def test_repeated_terminators(self):
        self.assertEqual(count_sentences("Wow!! Really?? Yes."), 3)

    def test_mixed_terminators_no_spaces(self):
        self.assertEqual(count_sentences("One.Two!Three?"), 3)

    def test_trailing_terminator_only(self):
        self.assertEqual(count_sentences("..."), 0)


class TestTopWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(top_words(""), [])

    def test_basic_ranking(self):
        result = top_words("a b a c a b")
        self.assertEqual(result[0], ("a", 3))
        self.assertEqual(result[1], ("b", 2))
        self.assertEqual(result[2], ("c", 1))

    def test_default_returns_five(self):
        text = "one two three four five six seven"
        self.assertEqual(len(top_words(text)), 5)

    def test_custom_n(self):
        self.assertEqual(len(top_words("one two three", n=2)), 2)

    def test_n_larger_than_vocab(self):
        self.assertEqual(top_words("a b", n=5), [("a", 1), ("b", 1)])

    def test_case_insensitive(self):
        result = dict(top_words("Hello hello HELLO world"))
        self.assertEqual(result.get("hello"), 3)
        self.assertEqual(result.get("world"), 1)

    def test_punctuation_ignored(self):
        result = dict(top_words("hi, hi! hi?"))
        self.assertEqual(result.get("hi"), 3)

    def test_n_zero(self):
        self.assertEqual(top_words("a b c", n=0), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
