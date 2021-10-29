import pytest

from leetcode.kmp_search import Solution


@pytest.mark.parametrize("s, p, expected",
                         [("abc", "bc", 1), ("aaab", "aab", 1),
                          ("ababcabcabababd", "ababd", 10), ("baaaa", "aaa", 1),
                          ("aadaab", "aab", 3), ("abc", "bcd", -1),
                          ("aaacaaaa", "aaacaaaa", 0), ("aaab", "aabc", -1),
                          ("ababdabacdababcabab", "ababcabab", 10),
                          ("abcdefaababa", "ababa", 7), ("efabcbc", "abcbc", 2),
                          ("ajbiabaabce", "abaabc", 4),
                          ("aabaabac", "aabac", 3),
                          ("aaaaaaaaaaabe", "aabf", -1), ('bca', 'a', 2)])
def test_kmp_true(s: str, p: str, expected: int):
    assert Solution.kmp_search(s, p) == expected
