import pytest

from leetcode.linked_list import ListNode
from leetcode.rotate_linked_list import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("head, k, expected", [
    (ListNode.fromlist([1, 2, 3, 4]), 2, ListNode.fromlist([3, 4, 1, 2])),
    (ListNode.fromlist([1, 2, 3, 4]), 1, ListNode.fromlist([4, 1, 2, 3])),
    (ListNode.fromlist([1, 2, 3, 4]), 3, ListNode.fromlist([2, 3, 4, 1])),
    (ListNode.fromlist([1, 2, 3]), 5, ListNode.fromlist([2, 3, 1])),
    (ListNode.fromlist([1, 2, 3, 4]), 0, ListNode.fromlist([1, 2, 3, 4]))])
def test_rotate_linked_list(solution: Solution, head: ListNode, k: int,
                            expected: ListNode):
    assert solution.rotateRight(head, k) == expected
