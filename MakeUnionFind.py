V = 5000  

class MakeUnionFind:
	def __init__(self):
		self.rank = [1 for i in range(0,V)]
		self.parent = [i for i in range(0,V)]
		self.max_size = V
	
	def __init__(self, size):
		self.rank = [1 for i in range(0,V)]
		self.parent = [i for i in range(0,V)]
		self.max_size = size

	def Make(self, i):
		self.parent[i] = i
		self.rank[i] = 1

	def Find(self, i):
		w = i
		tempList = list()
		while self.parent[w] != w:
			tempList.append(w)
			w = self.parent[w]
		while len(tempList)>0:
			i = tempList[len(tempList)-1]
			tempList.pop()
			self.parent[i] = w
		return w

	def Union(self, i, j):
		if self.rank[i] > self.rank[j]:
			self.parent[j] = i
		elif self.rank[i] < self.rank[j]:
			self.parent[i] = j
		else:
			self.parent[j] = i
			self.rank[i] += 1

	