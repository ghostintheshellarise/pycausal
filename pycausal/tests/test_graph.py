from unittest import TestCase

import pycausal
import networkx as nx

class TestGraph(TestCase):
    
    def get_smoking_dag(self):
        edgelist = [('class', 'smoking'), 
                    ('class', 'job'), 
                    ('class', 'dental care'),
                    ('smoking', 'tar in lungs'),
                    ('job', 'asbestos'),
                    ('job', 'dental care'),
                    ('tar in lungs', 'cell damage'),
                    ('asbestos', 'cell damage'),
                    ('dental care', 'yellow teeth'),
                    ('cell damage', 'cancer')]
        
        dag = nx.DiGraph(edgelist)
        return dag
        
    def test_backdoor(self):
        dag = self.get_smoking_dag()
        
        s = pycausal.backdoor(dag, ['smoking'], ['cancer'])
        self.assertEqual(s, ['class'])
        
        s = pycausal.backdoor(dag, ['tar in lungs', 'asbestos'], ['dental care'])
        self.assertEqual(set(s), set(['smoking', 'job']))
        
    def test_check_backdoor(self):
        dag = self.get_smoking_dag()
    
        self.assertFalse(pycausal.check_backdoor(dag, ['smoking', 'asbestos'], ['yellow teeth'], ['cancer']))
        self.assertTrue(pycausal.check_backdoor(dag, ['cell damage'], ['dental care'], ['tar in lungs', 'asbestos']))
        self.assertFalse(pycausal.check_backdoor(dag, ['cell damage'], ['dental care'], ['tar in lungs']))