import pickle
import json
import pandas as pd
import copy

TDAT2     = pickle.load(open('TDAT2.pickle.dump', 'rb'))

TDAT_df   = pd.DataFrame(TDAT2)
TDAT_dict = TDAT_df.to_dict(orient="list")

#print sorted(list(TDAT2))
#print sorted(list(TDAT_dict))

for key in  sorted(list(TDAT2)):
	print "------------------------------------"
	print key
	#print sorted(TDAT2[key])
	#print sorted(TDAT_dict[key])
	assert(len(TDAT2[key]) == len(TDAT_dict[key]))
	if not (sorted(TDAT2[key]) == sorted(TDAT_dict[key])):
		print "not equal !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	before = copy.deepcopy(TDAT2)
	after = copy.deepcopy(TDAT_dict)
	#print before[key]
	del before[key]
	del after[key]
	try:
		json.dumps(before)     ## works
		json.dumps(after) ## failes
	except:
		print key, "fails drop"

	before = copy.deepcopy(TDAT2[key])
	after = copy.deepcopy(TDAT_dict[key])
	try:
		json.dumps({key:before})     ## works
	except:
		print key, "fails solo before"
		print "solo", key, before
	try:
		json.dumps({key:after}) ## failes
	except:
		print key, "fails solo after"
		#print "solo-after", key, after
		#print "solo-before", key, before
		if before == after:
			print "one of these two lists cannot be json serialized but they are identical according to python!?!?"
			print map(type, before)[0]
			print map(type, after)[0]
		else:
			print "well at least they are different"
