import unittest
import keyring, logging
from pymap.utils import gentext, branch, Tree

class UtilsTest(unittest.TestCase):
    """Test for package methods"""
    def test_gentext(self):
        self.assertEqual('', gentext(0))
        self.assertEqual(10, len(gentext(10)))
        self.assertEqual('', gentext(-1))

    def test_branch(self):
        tree = Tree()
        expectedtree = Tree()
        tree[1][2][3]
        expectedtree[1][2][3]
        self.assertEqual(expectedtree, tree)
        branch([], tree)
        self.assertEqual(expectedtree, tree)
        branch([1,2,3], tree)
        self.assertEqual(expectedtree, tree)

    def test_keyring(self):
        """Testing keyring module"""
        self.assertEqual(None,
                keyring.get_password("zoubzoub", "blbablalb"))

        keyring.set_password("system", "username", "password")
        self.assertEqual('password',
            keyring.get_password('system', 'username'))

        self.assertTrue(keyring.get_password('imap.free.fr',
                                 'vic.toad.tor'))

class TreeTest(unittest.TestCase):
    """Test for Tree class"""
    def test_Tree(self):
        self.assertEqual(Tree(), {})
        tree = Tree()
        tree[40]
        self.assertEqual({40:{}}, tree)
        tree[40]
        self.assertEqual({40:{}}, tree)
        tree[30]
        self.assertEqual({40:{}, 30:{}}, tree)
        tree[40][3]
        self.assertEqual({40:{3:{}}, 30:{}}, tree)

    def test_branch(self):
        expectedtree = Tree()
        actualtree = Tree()

        expectedtree['path']
        actualtree.branch(['path'])
        self.assertEqual(expectedtree, actualtree)

        expectedtree['poth']
        actualtree.branch(['poth'])
        self.assertEqual(expectedtree, actualtree)

        expectedtree['path']['to']['dir']
        actualtree.branch(['path','to','dir'])
        self.assertEqual(expectedtree, actualtree)

        expectedtree = Tree()
        actualtree = Tree()
        expectedtree[1]['A']['i']
        expectedtree[1]['A']['ii']
        expectedtree[1]['B']
        expectedtree[2]['A']['i']
        actualtree.branch([1, 'A', 'i'])
        actualtree.branch([1, 'A', 'ii'])
        actualtree.branch([1, 'B'])
        actualtree.branch([2, 'A', 'i'])
        self.assertEqual(expectedtree, actualtree)

    def test_walk(self):
        tree = Tree()
        treedef = (1, 'A', 'ii')
        tree.branch(treedef)
        self.assertEqual(treedef, list(zip(*tree.walk()))[1])

    def test_includes(self):
        tree = Tree()
        self.assertTrue(tree.includes({}))
        self.assertFalse(tree.includes({10:{}}))
        tree[10]
        tree[20][30]
        self.assertTrue(tree.includes({10:{}}))
        self.assertTrue(tree.includes({20:{}}))
        self.assertTrue(tree.includes({20:{30:{}}}))


    def test_contains(self):
        tree = Tree()
        self.assertFalse([10] in tree)
        tree[10]
        self.assertTrue([10] in tree)
        self.assertFalse(10 in tree)
        self.assertFalse('bla' in tree)

if __name__ == '__main__':
    unittest.main()
