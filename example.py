from TreeParser import TreeParser

sentence='(ROOT (NP (NP (NP (NP (NN Power)) (CC and) (NP (NN elegance))) (ADVP (RB together))) (. .)))'
tree_parser=TreeParser()
Tree=tree_parser.create_tree(None,sentence)	
print (sentence)
print ('root\'s tag', Tree.tag)
print ('root\'s tag', Tree.value)
for child in Tree.children_nodes:
    print ('child\'s tag: ',child.tag)
    print ('child\'s value: ',child.value)
