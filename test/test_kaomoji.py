import pytest
from kaomoji import kaomoji
from data import load_kaomojis

def test_load_kamoji():
    kao = load_kaomojis.load_kaomojis()
    assert kao

def test_kaomoji():
    kao = kaomoji.Kaomoji()
    assert kao
