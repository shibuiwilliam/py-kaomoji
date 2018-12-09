# -*- coding: utf-8 -*-

import yaml
import random
import os
from data import load_kaomojis


class Kaomoji(object):
    """Kaomoji library
    """

    def __init__(self):
        """
        Attributes:
            kaomoji_dict(dict): a dict for kaomoji; key(kaomoji key)=value(kaomoji)
            _all_kaomoji_list(list): a list of kaomoji keys
        """

        self.kaomoji_dict = load_kaomojis.load_kaomojis()
        self._all_kaomoji_list = self.all_kaomoji(as_list=True)

    def __call__(self, n=1):
        """get a random kaomoji
        
        Keyword Arguments:
            n {int}: [number of kaomojis to get] (default: {1})
        
        Returns:
            str: [kaomoji
        """

        return self.random_kaomoji(n)

    def kaomoji(self, nihongo, all=False):
        """kaomoji
        
        Arguments:
            nihongo {[str]}: key for kaomoji; your emotion
        
        Keyword Arguments:
            all {bool}: get all kaomojis if multiple kaomojis exist in the key (default: {False})
        
        Returns:
            list if all else str: kaomoji
        """

        _k = self.kaomoji_dict[nihongo]
        if isinstance(_k, list):
            return _k if all else random.choice(_k)
        return _k

    def random_kaomoji(self, n=1, as_list=False):
        """get random kaomoji
        
        Keyword Arguments:
            n {int}: number of random kaomojis to get (default: {1})
            as_list {bool}: retrieve in list or str (default: {False})
        
        Returns:
            list if as_list else str: kaomoji
        """

        _rk = random.sample(self._all_kaomoji_list, n)
        return _rk if as_list else " ".join(_rk)

    def get_kao_list(self):
        """get a list of kaomoji keys
        
        Returns:
            list: a list kaomoji keys
        """

        return list(self.kaomoji_dict.keys())

    def add_kao(self, key, value):
        """add new kaomoij
        
        Arguments:
            key {str}: key for the new kaomoji
            value {str}: new kamoji
        """

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
        """get all kaomoji!!!
        
        Keyword Arguments:
            as_list {bool}:  retrieve in list or str (default: {False})
        
        Returns:
            list if as_list else str: kaomojis!!!
        """

        _kaomojis = []
        for v in self.kaomoji_dict.values():
            if isinstance(v, list):
                _kaomojis.extend(v)
            else:
                _kaomojis.append(v)
        return _kaomojis if as_list else " ".join(_kaomojis)

    def super_kaomoji(self, as_list=False):
        """get random number of kaomojis
        
        Keyword Arguments:
            as_list {bool}:  retrieve in list or str (default: {False})
        
        Returns:
            list if as_list else str: kaomojis!!!
        """

        n = random.randint(1, len(self._all_kaomoji_list))
        return self.random_kaomoji(n, as_list=as_list)


def main():
    kao = Kaomoji()
    print(kao(n=1))