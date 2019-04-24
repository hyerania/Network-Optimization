import math
from graph import Vertex

V = 5000
class Heap:
	def __init__(self):
		self.heap = list() #Represents H vector
		self.pos = [-1 for i in range(V)] #Represents D vector

	def maximum(self):
		return self.heap[0].dst
	
	def insert(self, v, bw):
		if len(self.heap) == V:
			return

		node = Vertex(v, bw)
		self.heap.append(node)
		i = len(self.heap) - 1
		self.pos[v] = i
		while (i != 0 and self.heap[self.parent(i)].bw < self.heap[i].bw):
			self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
			self.pos[self.heap[i].dst] = i
			self.pos[self.heap[self.parent(i)].dst] = self.parent(i)
			i = self.parent(i)

	def delete(self, v):
		posHeap = self.pos[v]
		if posHeap > V:
			return

		i = len(self.heap)-1
		self.heap[i], self.heap[posHeap] = self.heap[posHeap], self.heap[i]
		self.pos[self.heap[posHeap].dst] = posHeap
		self.heap.pop()
		self.pos[v] = -1
		self.heapify(posHeap)
		return

	def parent(self, i):
		return math.ceil((i/2)-1)

	def heapify(self, i):
		maxVal = i
		left = 2*i+1
		right = 2*i+2

		if (left < len(self.heap) and self.heap[left].bw > self.heap[maxVal].bw):
			maxVal = left
		if (right < len(self.heap) and self.heap[right].bw > self.heap[maxVal].bw):
			maxVal = right
		if (maxVal != i):
			self.heap[maxVal], self.heap[i] = self.heap[i], self.heap[maxVal]
			self.pos[self.heap[i].dst] = i
			self.pos[self.heap[maxVal].dst] = maxVal
			self.heapify(maxVal)
