from lib.toy_storage import *
"""
Given a new instance of ToyStorage
It comes with an empty list (self.toy_list)
"""
def test_instantiates_with_toy_list():
    toy_storage = ToyStorage()
    actual = toy_storage.toy_list
    expected = []
    assert actual == expected