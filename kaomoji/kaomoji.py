# -*- coding: utf-8 -*-

import yaml
import random
import os
from data import load_kaomojis


class Kaomoji(object):
    def __init__(self):
        self.kaomoji_dict = load_kaomojis.load_kaomojis()
        self._all_kaomoji_list = self.all_kaomoji(as_list=True)

    def __call__(self, n=1):
        return self.random_kaomoji(n)

    def kaomoji(self, nihongo, all=False):
        _k = self.kaomoji_dict[nihongo]
        if isinstance(_k, list):
            return _k if all else random.choice(_k)
        return _k

    def random_kaomoji(self, n=1, as_list=False):
        _rk = random.sample(self._all_kaomoji_list, n)
        return _rk if as_list else " ".join(_rk)

    def get_kao_list(self):
        return list(self.kaomoji_dict.keys())

    def add_kao(self, key, value):
        if key in self.kaomoji_dict.keys():
            if isinstance(self.kaomoji_dict[key], str):
                _t = [self.kaomoji_dict[key]]
                _t.append(value)
                self.kaomoji_dict[key] = _t
            else:
                self.kaomoji_dict[key].append(value)
        else:
            self.kaomoji_dict[key] = value

    def all_kaomoji(self, as_list=False):
        _kaomojis = []
        for v in self.kaomoji_dict.values():
            if isinstance(v, list):
                _kaomojis.extend(v)
            else:
                _kaomojis.append(v)
        return _kaomojis if as_list else " ".join(_kaomojis)

    def super_kaomoji(self, as_list=False):
        n = random.randint(1, len(self._all_kaomoji_list))
        return self.random_kaomoji(n, as_list=as_list)


def main():
    kao = Kaomoji()
    print(kao(n=1))