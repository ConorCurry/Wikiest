#Create data structure for popularity keyed prefix search
from collections import defaultdict

def Tree():
	return defaultdict(Tree)

def addWord(tree, word, score):
	#_traverse(tree, word, add=True)['score'] = score
	cur = tree
	for lev, let in enumerate(word.lower()):
		cur = cur.__getitem__(let)
		if 'top' not in cur: cur['top'] = []
		_computeTop(cur['top'], (score,word[lev+1:]))
	cur['score'] = score
	return cur

def _computeTop(top, scorePair, topSize=3):
	for i in range(topSize):
		if i >= len(top) - 1:
			top.append(scorePair)
			return True
		if scorePair[0] > top[i][0]:
			top.insert(i, scorePair)
			if(len(top)) > 3: top.pop()
			return True
	return False

def getWord(tree, word):
	#return _traverse(tree, word)
	cur = tree
	for let in word.lower():
		if let not in cur: return False
		cur = cur.__getitem__(let)
	return cur['top'], cur

# def _traverse(tree, word, add=False):
# 	cur = tree
# 	for let in word.lower():
# 		if (not add) and let not in cur:
# 			return False
# 		cur = cur.__getitem__(let)
# 	return cur

# class Node(letter, score):
# 	self.letter = letter
# 	self.score = score
# 	self.topChildren = []
# 	self.children = []
#
