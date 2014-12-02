import string, random, logging

class Tree(dict):
    """Tree structure definition"""
    def __init__(self, elements=None):
        super(Tree, self).__init__()
        if elements:
            self.branch(elements)

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

    def branch(self, elements):
        """Fill this tree branch from a list"""
        if elements:
            branch(elements[1:], self[elements[0]])

    def walk(self, level=0):
        """ iterate tree in pre-order depth-first search order """
        for key in self.keys():
            yield (level, key)
            for child in self[key].walk(level+1):
                yield child

    def __repr__(self, level=0):
        return '\n'.join(['\t'*el[0]+repr(el[1]) for el in self.walk()])

    def __contains__(self, item):
        if type(item) is list:
            return self.includes(Tree(item))
        elif type(item) is Tree:
            return self.includes(item)
        logging.debug('Type %s is not handled, try a list or a dict/Tree',
                        type(item))
        return False

    def includes(self, tree):
        res = True
        for key in tree.keys():
            if not super(Tree, self).__contains__(key):
                return False
            res = res and self[key].includes(tree[key])
        return res

def branch(elements, tree):
    """Fill a tree branch from a list"""
    if elements:
        branch(elements[1:], tree[elements[0]])

def gentext(length=8, chars=string.ascii_letters + string.digits):
    """Generate random text"""
    if length < 0:
        return ''
    return ''.join([random.choice(chars) for i in range(length)])

