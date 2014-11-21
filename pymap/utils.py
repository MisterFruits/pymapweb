import string, random

class Tree(dict):
    """Tree structure definition"""
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

    def branch(self, elements):
        if elements:
            branch(elements[1:], self[elements[0]])

    def walk(self):
        """ iterate tree in pre-order depth-first search order """
        for key, value in self.items():
            yield key
            for child in self[key].walk():
                yield child

def branch(elements, tree):
    """Fill a tree branch from a list"""
    if elements:
        branch(elements[1:], tree[elements[0]])

def gentext(length=8, chars=string.ascii_letters + string.digits):
    """Generate random text"""
    if length < 0:
        return ''
    return ''.join([random.choice(chars) for i in range(length)])

