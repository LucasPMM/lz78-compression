from typing import Union, Tuple

class Trie:
    def __init__(self, value='', numeric_value=None, parent=None, empty=True):
        self.value = value
        self.empty = empty
        self.numeric_value = numeric_value
        self.parent = parent
        self.children = {}

    def _get_prefix(self, word):
        res: Tuple[int, Union[str, None]] = (-1, None)
        for key in self.children.keys():
            last = len(key)
            while last > 0:
                if key[:last] == word[:last]:
                    return (last, key)
                last -= 1
        return res

    def contains(self, word):
        # if word == '' and '' in self.children.keys():
        #     return self.children[''].numeric_value

        if word == self.value and self.numeric_value != None:
            return self.numeric_value

        index, key = self._get_prefix(word)
        if key == None:
            return -1
        return self.children[key].contains(word[index:])

    def add(self, word, value):
        self._add(word, value)

    def _add(self, word, value):
        index, key = self._get_prefix(word)

        if key == None:
            self._add_node(word, Trie(empty=False, numeric_value=value))
            if not self.empty and self.numeric_value != 0:
                self._add_node('', Trie(empty=False, numeric_value=self.numeric_value))
                self.numeric_value = None
                self.empty = True   
        elif index == len(key):
            self.children[key].add(word[index:], value)
        else:
            prefix = word[:index]
            temp = self.children.pop(key)
            temp.value = key[index:]
            self._add_node(prefix, None)
            self.children[prefix]._add_node(word[index:], Trie(empty=False, numeric_value=value))
            self.children[prefix]._add_node(key[index:], temp)

    def _add_node(self, value, node):
        if (node == None):
            node = Trie()
        node.parent = self
        node.value = value
        self.children[value] = node