# Network Optimzation Implementation of Maximum Bandwidth Path
### Setup Instructions
- Install and run code on Python 3.7.0

### Running Algorithms
The ```main.py``` has two arguments:
- Menu Options:
  - 1 for Sparse graph generation
  - 2 for Dense graph generation
- Trial Numbers: Insert an integer value for the number of source-destination vertex pairs to create

- Run the following command in order to create a single sparse graph with 5 pairs of source-destination vertices:
  ```
  python src/main.py 1 5
  ```
- Run the following command in order to create a single dense graph with 5 pairs of source-destination vertices:
  ```
  python src/main.py 2 5
  ```

### Overall Code Structure
- ```graph.py```: Contains the class of Graph, Vertex, and Edge
- ```krsukalAlgo.py```: Contains the implementation of Kruskal’s algorithm with the use of functions such as heapSort, DFS, and path. 
  - ```MakeUnionFind.py```: Contains the functions of Make, Set, and Union which help the Kruskal implementation in path compression
- ```dijkstraAlgo.py```: Contains the implementation of Dijkstra’s algorithm with and without the use of the heap structure.
  - ```heapStruct.py```: Contains the functions Maximum, Insert, and Delete in order to implement the maximum heap structure
- ```main.py```: Returns the running time of all three routing algorithms based on a sparse or dense graph and a specified number of trials.
