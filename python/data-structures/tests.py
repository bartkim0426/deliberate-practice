from unittest import TestCase

from union_set import DisjointSet


class DisjointSetTestCase(TestCase):
    def test_disjoint_set(self):
        '''
        union(1, 2)
        union(1, 3)
        union(4, 5)
        -> (0), (1, 2, 3), (4, 5)
        '''
        ds = DisjointSet(n=6)
        ds.union(1, 2)
        ds.union(1, 3)
        ds.union(4, 5)

        # test union method works
        self.assertEqual(
            ds.sets[3].parent.value,
            1
        )

        # test find_parent method works
        self.assertEqual(
            ds.find_parent(3).value,
            1
        )
        self.assertEqual(ds.find_parent(1).value, 1)

        # test isConnect method works
        self.assertTrue(ds.isConnect(1, 2))
        self.assertTrue(ds.isConnect(4, 5))
        self.assertFalse(ds.isConnect(1, 5))

        # test isCycle method works
        self.assertFalse(ds.isCycle())
