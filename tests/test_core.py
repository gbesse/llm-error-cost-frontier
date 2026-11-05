import unittest,math
from llm_error_cost_frontier.core import run
class DomainTests(unittest.TestCase):
 def test_explicit_abstention(self):
  x=run({'review_cost':2,'wrong_cost':10,'thresholds':[0,.5,1],'cases':[dict(id='a',confidence=.9,correct=True,call_cost=1),dict(id='b',confidence=.4,correct=False,call_cost=1)]});self.assertEqual([r['total_cost']for r in x['points']],[12,4,6]);self.assertEqual(x['pareto_thresholds'],[.5])
 def test_no_acceptance_rate_unknown(self):self.assertIsNone(run({'review_cost':1,'wrong_cost':1,'thresholds':[1],'cases':[dict(id='a',confidence=0,correct=False,call_cost=0)]})['points'][0]['accepted_error_rate'])
 def test_bad_boolean(self):
  with self.assertRaises(ValueError):run({'review_cost':1,'wrong_cost':1,'thresholds':[1],'cases':[dict(id='a',confidence=0,correct=1,call_cost=0)]})
