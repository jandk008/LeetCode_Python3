import pytest

from leetcode.binary_tree import TreeNode
from leetcode.heap_sorting import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize('nums, expected',
                         [([2, 2, 1], [1, 2, 2]), ([1], [1]), ([1, 2], [1, 2]),
                          ([4, 3, 2, 1], [1, 2, 3, 4]), ([33, 22], [22, 33]),
                          ([2, 3, 4, 3, 5, 2, 7], [2, 2, 3, 3, 4, 5, 7]),
                          ([1, 2, 1, 2, 1], [1, 1, 1, 2, 2]),
                          ([1, 2, 3], [1, 2, 3]), (
                              [1, 2324, 14, 21, 12, 132, 34, 512, 5, 24],
                              [1, 5, 12, 14, 21, 24, 34, 132, 512, 2324])])
def test_quick_sorting(solution: Solution, nums: list, expected: list):
    solution.sort(nums)
    assert nums == expected


@pytest.mark.parametrize('root, expected', [
    (TreeNode.fromlist([1, 2, 3, 4, 5, 6]), [1, 2, 4, 5, 3, 6]),
    (TreeNode.fromlist([1, 2, 3, 6, None, 4, 5]), [1, 2, 6, 3, 4, 5])])
def test_preorder(root: TreeNode, expected: list):
    assert preOrder(root) == expected


@pytest.mark.parametrize('root, expected', [
    (TreeNode.fromlist([1, 2, 3, 4, 5, 6]), [4, 2, 5, 1, 6, 3]),
    (TreeNode.fromlist([1, 2, 3, 6, None, 4, 5]), [6, 2, 1, 4, 3, 5])])
def test_inorder(root: TreeNode, expected: list):
    assert inOrder(root) == expected


@pytest.mark.parametrize('root, expected', [
    (TreeNode.fromlist([1, 2, 3, 4, 5, 6]), [4, 5, 2, 6, 3, 1]),
    (TreeNode.fromlist([1, 2, 3, 6, None, 4, 5]), [6, 2, 4, 5, 3, 1])])
def test_inorder(root: TreeNode, expected: list):
    assert postOrder(root) == expected


def plus(x, y):
    return plus(x ^ y, (x & y) << 1) if y else x


def test():
    print(plus(-1,2))
    s = "catsanddog"
    s.strip()
    w = ["This", "is", "an", "example", "of", "text", "justification."]
    a = [[1,2], [3,4], [5,6]]
    b = [x + [0] for x in a]
