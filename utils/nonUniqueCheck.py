import maya.cmds as mc

def check():
	'''
	Non-Unique Checker looks for non unique node names.
	It will separate shape, dag and dep nodes when reporting.
	'''

	# Create variables
	dagErrors=[] 	# hold all the nonunique DAG items
	shapeErrors=[] 	# hold all the nonunique Shape items
	depErrors=[] 	# hold all the nonunique DG items

	dag = mc.ls(dag=True)
	shapes = mc.ls(geometry=True)
	dep = mc.ls(dep=True)

	for item in shapes:
		while dag.count(item):
			dag.remove(item)

	for item in shapes:
		while dep.count(item):
			dep.remove(item)

	for item in dag:
		while dep.count(item):
			dep.remove(item)

	# Print header statement

	print 'Non-Unique Checker'
	print '==========================================\n'

	print 'DAG NODES'
	print '------------'
	for item in dag:
		if item.count('|'): dagErrors.append(item)
	print '\n'.join(sorted(dagErrors)) + '\n'

	print 'DEP NODES'
	print '------------'
	for item in dep:
		if item.count('|'): depErrors.append(item)
	print '\n'.join(sorted(depErrors)) + '\n'

	print 'SHAPE NODES'
	print '------------'
	for item in shapes:
		if item.count('|'): shapeErrors.append(item)
	print '\n'.join(sorted(shapeErrors)) + '\n'

	del dep
	del dag
	del shapes

	mc.select(cl=True)

	print '=========================================='
	print ('Non-Unique Check located ' + str(len(dagErrors) + len(depErrors) + len(shapeErrors)) + ' errors.')
