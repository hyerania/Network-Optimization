import math
import sys

from graph import Graph, Vertex
from heapStruct import Heap
V = 5000

# Algorithm status codes:
# In-Tree = 0
# Fringe = 1
# Unseen = 2

def dijkstra(G, s, t):
	bw = [0]*V
	parent = [-1]*V
	status = [2]*V
	
	status[s] = 0
	bw[s] = sys.maxsize
	for v in G.findNeighbor(s):
		bw[v.dst] = v.bw
		parent[v.dst] = s
		status[v.dst] = 1

	while status[t] != 0:
		v = maxfringe(bw, status)
		status[v] = 0
		n = G.findNeighbor(v)
		for i in range(len(n)):
			w = n[i].dst
			if (status[w] == 2):
				bw[w] = min(bw[v], n[i].bw)
				parent[w] = v
				status[w] = 1
			elif (status[w] == 1 and bw[w] < min(bw[v], n[i].bw)):
				bw[w] = min(bw[v], n[i].bw)
				parent[w] = v
	return bw[t]


def maxfringe(bw, status):
	bwTemp = 0
	statusTemp = 0

	for i in range(V):
		if status[i] == 1 and bwTemp < bw[i]:
			bwTemp = bw[i]
			statusTemp = i

	return statusTemp


def dijkstraHeap(G, s, t):
	hp = Heap()
	bw = [0]*V
	parent = [-1]*V
	status = [2]*V
	
	status[s] = 0
	bw[s] = sys.maxsize
	for v in G.findNeighbor(s):
		bw[v.dst] = v.bw
		parent[v.dst] = s
		status[v.dst] = 1
		hp.insert(v.dst, bw[v.dst])

	while status[t] != 0:
		v = hp.maximum()
		hp.delete(hp.maximum())
		status[v] = 0
		n = G.findNeighbor(v)
		for i in range(len(n)):
			w = n[i].dst
			if (status[w] == 2):
				bw[w] = min(bw[v], n[i].bw)
				parent[w] = v
				status[w] = 1
				hp.insert(w, bw[w])
			elif (status[w] == 1 and bw[w] < min(bw[v], n[i].bw)):
				hp.delete(w)
				bw[w] = min(bw[v], n[i].bw)
				parent[w] = v
				hp.insert(w,bw[w])
	return bw[t]