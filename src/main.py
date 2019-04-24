import math
import random
import sys
import time

from graph import Graph, Vertex, Edge
from dijkstraAlgo import dijkstra, dijkstraHeap
from kruskalAlgo import kruskal

def main():
	if(len(sys.argv) != 3):
		print("Arg1: Contains 1 for sparse graph testing or 2 for dense graph gesting")
		print("Arg2: Contains numeric int value for number of trials testing") 
		return

	menu = int(sys.argv[1])
	trials = int(sys.argv[2])
	V = 5000

	if (menu == 1):
		print("Sparse Graph Testing")
		G = Graph()

		start = time.time()
		G.createSparseG()
		end = time.time()
		elapsedTimeG = end-start
		print("Time_SparseG: ", elapsedTimeG)

		for i in range(trials):
			srcV = random.randint(0, V-1)
			dstV = random.randint(0, V-1)

			if srcV == dstV:
				continue

			# Print source and destination pair
			print(srcV, " : ", dstV)

			#Testing Dijkstra's Algorithm without Heap structure
			start = time.time()
			max_D = dijkstra(G, srcV, dstV)
			end = time.time()
			elapsedTimeD = end-start
			print("Time_D: ", elapsedTimeD)

			#Testing Dijkstra's Algorithm with Heap structure
			start = time.time()
			max_DH = dijkstraHeap(G, srcV, dstV)
			end = time.time()
			elapsedTimeDH = end-start
			print("Time_DH: ", elapsedTimeDH)

			#Testing Kruskal's Algorithm  with Heapsort
			start = time.time()
			max_K = kruskal(G, srcV, dstV)
			end = time.time()
			elapsedTimeK = end-start
			print("Time_K: ", elapsedTimeK)

			# Prints Maximum Bandwidth Path for each algorithm
			# print("Max_D: ", max_D)
			# print("Max_DH: ", max_DH)
			# print("Max_K: ", max_K)

			print("TRIAL: ", i+1, " DONE")


	elif (menu == 2):
		print("Dense Graph Testing")
		G = Graph()

		start = time.time()
		G.createDenseG()
		end = time.time()
		elapsedTimeG = end-start
		print("Time_DenseG: ", elapsedTimeG)

		for i in range(trials):
			srcV = random.randint(0, V-1)
			dstV = random.randint(0, V-1)

			if srcV == dstV:
				continue

			#Print source and destination pair
			print(srcV, " : ", dstV)

			#Testing Dijkstra's Algorithm without Heap structure
			start = time.time()
			max_D = dijkstra(G, srcV, dstV)
			end = time.time()
			elapsedTimeD = end-start
			print("Time_D: ", elapsedTimeD)

			#Testing Dijkstra's Algorithm with Heap structure
			start = time.time()
			max_DH = dijkstraHeap(G, srcV, dstV)
			end = time.time()
			elapsedTimeDH = end-start
			print("Time_DH: ", elapsedTimeDH)

			# Testing Kruskal's Algorithm  with Heapsort
			start = time.time()
			max_K = kruskal(G, srcV, dstV)
			end = time.time()
			elapsedTimeK = end-start
			print("Time_K: ", elapsedTimeK)

			# Prints Maximum Bandwidth Path for each algorithm
			# print("Max_D: ", max_D)
			# print("Max_DH: ", max_DH)
			# print("Max_K: ", max_K)

			print("TRIAL: ", i+1, " DONE")

	else:
		print("Wrong menu input")

if __name__ == "__main__":
	main()