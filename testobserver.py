import unittest
from Observer import Subject
from Observer import Observer

class test_subject(unittest.TestCase):
    #----------------------------------------------------------------------
    def test_create(self):
        """"""
        s= Subject()
        self.assertEqual(s.data, 23)
        self.assertIsInstance(s.observers, list)
        
    #----------------------------------------------------------------------
    def test_subscribe(self):
        """"""
        s = Subject()
        o = Observer('Harold')
        s.subscribe(o)
        self.assertIn(o, s.observers)
    
    #----------------------------------------------------------------------
    def test_unsubscribe(self):
        """"""
        s = Subject()
        o = Observer('name')
        s.subscribe(o)
        s.unsubscribe(o)
        self.assertNotIn(o, s.observers)
        