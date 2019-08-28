import pytest

from leetcode.linked_list import ListNode


@pytest.mark.parametrize("nums", [(1, 2, 3, 4)])
def test_none_empty_list_node_creation(nums: list):
    node4 = ListNode(nums[3], None)
    node3 = ListNode(nums[2], node4)
    node2 = ListNode(nums[1], node3)
    head = ListNode(nums[0], node2)

    generated_list = ListNode.fromlist(nums)
    assert generated_list == head
    assert len(generated_list) == len(nums)


def test_empty_list_node_creation():
    assert ListNode.fromlist([]) is None
