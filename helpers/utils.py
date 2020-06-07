import os
import random
import string

from os.path import join, dirname


class Utils(object):
    """Python Utility functions"""

    @staticmethod
    def identical_elements(lst):
        """ Parametre olarak verilen listenin elemanlarının eşit olup olmadığı kontrol edilir """
        return not lst or lst.count(lst[0]) == len(lst)

    @staticmethod
    def create_dir_if_not_exist(path):
        if not os.path.isdir(path):
            os.mkdir(path)

    @staticmethod
    def trim_special_unicode_characters(text):
        if text is None:
            return text

        text = text.replace('\xa0', "")
        return text

    @staticmethod
    def trim_multiple_spaces(text):
        if text is None:
            return text

        after_split = text.strip().split()
        return " ".join(after_split)

    @staticmethod
    def get_without_special_characters(text):
        words = text.split()
        new_words = []
        for word in words:
            new_word = ""
            for ch in word:
                if Utils.is_character_latin_or_number(ch):
                    new_word += ch
                else:
                    new_word += " "
            new_words.append(new_word)
        return " ".join(new_words)

    @staticmethod
    def replace_with_universal_universal_characters(text):
        if text is None:
            return text

        text = text.replace('ğ', 'g')
        text = text.replace('ü', 'u')
        text = text.replace('ş', 's')
        text = text.replace('ı', 'i')
        text = text.replace('ç', 'c')
        text = text.replace('ö', 'o')
        return text

    @staticmethod
    def rand_string(length=10, char_set=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(char_set) for _ in range(length))

    @staticmethod
    def get_current_dir():
        return dirname(dirname(__file__))

    @staticmethod
    def get_full_path(*path):
        return join(dirname(dirname(__file__)), *path)

    @staticmethod
    def is_sorted(list, sort_type="asc"):
        """Listenin belirtilen sort tipine göre sekilde sıralı olup olmadigi kontrol edilir"""

        if sort_type.lower() == "asc":
            return True if all(list[i] <= list[i + 1] for i in range(len(list) - 1)) else False
        elif sort_type.lower() == "desc":
            return True if all(list[i] >= list[i + 1] for i in range(len(list) - 1)) else False
        else:
            raise ValueError('Sort type should be asc and desc')

    @staticmethod
    def search_items_in_list(list, items_list):
        """Search all items in list and return boolean"""
        return all([item in list for item in items_list])

    @staticmethod
    def to_bool(value):
        valid = {'true': True, 't': True, '1': True,
                 'false': False, 'f': False, '0': False,
                 }

        if isinstance(value, bool):
            return value

        if not isinstance(value, str):
            raise ValueError('invalid literal for boolean. Not a string.')

        lower_value = value.lower()
        if lower_value in valid:
            return valid[lower_value]
        else:
            raise ValueError('invalid literal for boolean: "%s"' % value)

    @staticmethod
    def compare_lists(list1, list2):
        return list1.sort() is list2.sort()

    @staticmethod
    def compare_lists2(list1, list2):
        if len(list1) != len(list2):
            return False
        for item in list1:
            if item not in list2:
                return False
        return True
