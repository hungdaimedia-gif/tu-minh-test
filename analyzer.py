"""Simple text analyzer: word count, sentence count, top-N frequent words."""

import re
from collections import Counter


def _words(text):
    """Split text into lowercase words, ignoring punctuation."""
    return re.findall(r"\b\w+\b", text.lower())


def count_words(text):
    """Return the number of words in text."""
    return len(_words(text))


def count_sentences(text):
    """Return the number of sentences in text.

    Sentences are split on '.', '!' and '?' (one or more in a row).
    Text without a terminator counts as one sentence if non-blank.
    """
    parts = re.split(r"[.!?]+", text)
    sentences = [p.strip() for p in parts if p.strip()]
    return len(sentences)


def top_words(text, n=5):
    """Return the n most frequent words as a list of (word, count) tuples.

    Words are matched case-insensitively. Ties keep first-seen order.
    """
    return Counter(_words(text)).most_common(n)


if __name__ == "__main__":
    sample = "Hello world! Hello again. This is a test, a simple test."
    print("words:", count_words(sample))
    print("sentences:", count_sentences(sample))
    print("top 5:", top_words(sample))
