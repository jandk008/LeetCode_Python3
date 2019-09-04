import pytest

from leetcode.word_ladder import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("begin_word, end_word, word_list, expected", [
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'], 5),
    ('dot', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'], 3),
    ('hit', 'dog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'], 4),
    ('qa', 'sq', ['si', 'go', 'se", "cm", "so', 'ph', 'mt', 'db', 'mb', 'sb',
     "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba",
     "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma",
     "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr",
     "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li",
     "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an",
     "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex",
     "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq",
     "ye"], 5),
    ('hot', 'dog', ['hot', 'dog', 'cog', 'pot', 'dot'], 3),
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'], 0)])
def test_word_ladder(solution: Solution, begin_word: str, end_word: str,
                     word_list: list, expected):
    assert solution.ladder_length(begin_word, end_word, word_list) == expected
