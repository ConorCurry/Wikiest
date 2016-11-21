#Create data structure for popularity keyed prefix search
from collections import defaultdict

def Tree():
	return defaultdict(Tree)

def addWord(tree, word, score):
	#_traverse(tree, word, add=True)['score'] = score
	cur = tree
	for let in word.lower():
		cur = cur.__getitem__(let)
	return cur

def getWord(tree, word):
	#return _traverse(tree, word)
	cur = tree
	for let in word.lower():
		if let not in cur: return False
		cur = cur.__getitem__(let)
	return cur

def _traverse(tree, word, add=False):
	cur = tree
	for let in word.lower():
		if (not add) and let not in cur:
			return False
		cur = cur.__getitem__(let)
	return cur

# class Node(letter, score):
# 	self.letter = letter
# 	self.score = score
# 	self.topChildren = []
# 	self.children = []
#
