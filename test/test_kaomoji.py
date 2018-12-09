import pytest
from kaomoji import kaomoji
from data import load_kaomojis

def test_load_kamoji():
    kao = load_kaomojis.load_kaomojis()
    assert kao

def test_Kaomoji():
    kao = kaomoji.Kaomoji()
    assert kao

def test_get_kao_list():
    kao = kaomoji.Kaomoji()
    keys = kao.get_kao_list()
    assert keys

def test_add_kao_1():
    kao = kaomoji.Kaomoji()
    kao.add_kao(key="あ", value=":(")
    assert kao.kaomoji_dict["あ"]

def test_add_kao_2():
    kao = kaomoji.Kaomoji()
    kao.add_kao(key="あげ", value=":(")
    assert isinstance(kao.kaomoji_dict["あげ"], list)
    assert len(kao.kaomoji_dict["あげ"]) == 2

def test_add_kao_1():
    kao = kaomoji.Kaomoji()
    _len = len(kao.kaomoji_dict["あおり"])
    kao.add_kao(key="あおり", value=":(")
    assert isinstance(kao.kaomoji_dict["あおり"], list)
    assert len(kao.kaomoji_dict["あおり"]) == _len+1

def test_kaomoji():
    kao = kaomoji.Kaomoji()
    assert kao.kaomoji("あおり", all=False)
    assert kao.kaomoji("あおり", all=True)

def test_random_kaomoji_1():
    kao = kaomoji.Kaomoji()
    a = kao.random_kaomoji(1, as_list=False)
    assert a
    assert isinstance(a, str)

def test_random_kaomoji_2():
    kao = kaomoji.Kaomoji()
    a = kao.random_kaomoji(1, as_list=True)
    assert a
    assert isinstance(a, list)

def test_all_kaomoji_1():
    kao = kaomoji.Kaomoji()
    a = kao.all_kaomoji(as_list=False)
    assert a
    assert isinstance(a, str)

def test_all_kaomoji_2():
    kao = kaomoji.Kaomoji()
    a = kao.all_kaomoji(as_list=True)
    assert a
    assert isinstance(a, list)

def test_super_kaomoji_1():
    kao = kaomoji.Kaomoji()
    a = kao.super_kaomoji(as_list=False)
    assert a
    assert isinstance(a, str)

def test_super_kaomoji_2():
    kao = kaomoji.Kaomoji()
    a = kao.super_kaomoji(as_list=True)
    assert a
    assert isinstance(a, list)


