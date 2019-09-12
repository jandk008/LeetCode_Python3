import pytest

from leetcode.design_hashset import DesignHashSet


@pytest.fixture
def hash_set():
    return DesignHashSet()


def test_my_hash_set(hash_set: DesignHashSet):
    hash_set.add(1)
    hash_set.add(2)
    assert hash_set.contains(1)
    assert hash_set.contains(2)
    assert not hash_set.contains(3)
    hash_set.add(2)
    assert hash_set.contains(2)
    hash_set.remove(2)
    assert not hash_set.contains(2)
