# -*- coding: utf-8 -*-

import yaml
import random
import os
from data import load_kaomojis

class Kaomoji(object):
    def __init__(self):
        self.kaomoji_dict = load_kaomojis.load_kaomojis()
        self._all_kaomoji = self.all_kaomoji()
        
    def __call__(self, n=1):
        return self.random_kaomoji(n)
        
    def kaomoji(self, nihongo):
        _k = self.kaomoji_dict[nihongo]
        if isinstance(_k, list):
            return random.choice(_k)
        return _k
    
    def random_kaomoji(self, n=1):
        return random.sample(self._all_kaomoji, n)

    def all_kaomoji(self):
        _kaomojis = []
        for v in self.kaomoji_dict.values():
            if isinstance(v, list):
                _kaomojis.extend(v)
            else:
                _kaomojis.append(v)
        return _kaomojis
    
    def super_kaomoji(self):
        n = random.randint(1, len(self._all_kaomoji))
        _rk = self.random_kaomoji(n)
        return " ".join(_rk)

def __main__():
    kao = Kaomoji()
    print(kao()[0])

if __name__ == "__main__":
    __main__()