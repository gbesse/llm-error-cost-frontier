import math,itertools
from .common import number,integer,identifier,unique_ids
def run(d):
 rows=d['cases'];unique_ids(rows);thresholds=[number(v,0,1)for v in d['thresholds']];review=number(d['review_cost'],0,1e9);wrong=number(d['wrong_cost'],0,1e9)
 if not 1<=len(rows)<=10000 or not 1<=len(thresholds)<=1000:raise ValueError('size')
 for r in rows:
  number(r['confidence'],0,1);number(r['call_cost'],0,1e9)
  if type(r['correct'])is not bool:raise ValueError('judgment')
 out=[]
 for t in sorted(set(thresholds)):
  accepted=[r for r in rows if r['confidence']>=t];errors=sum(not r['correct']for r in accepted);abstain=len(rows)-len(accepted);cost=sum(r['call_cost']for r in rows)+review*abstain+wrong*errors;out.append(dict(threshold=t,accepted=len(accepted),abstained=abstain,errors=errors,coverage=len(accepted)/len(rows),accepted_error_rate=errors/len(accepted)if accepted else None,total_cost=cost))
 frontier=[]
 for i,a in enumerate(out):
  if not any(b['total_cost']<=a['total_cost']and b['errors']<=a['errors']and(b['total_cost']<a['total_cost']or b['errors']<a['errors'])for j,b in enumerate(out)if j!=i):frontier.append(a['threshold'])
 return dict(points=out,pareto_thresholds=frontier,review_outcome_assumed_perfect_for_cost_only=True)
