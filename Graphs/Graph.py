class Graph(object):
	def __init__(self, graph_dict={}):
		self.__graph_dict = graph_dict
	
	def __str__(self):
		res = "vertices"
		for k in self.__graph_dict:
			res+=str(k)+" "
		res+="\nedges:"
		for edge in self.__generate_edges():
			res+=str(edge)+" "
		return res

	def edges(self):
		return self.__generate_edges()

	def __generate_edges(self):
		edges = []  
		for vertex in self.__graph_dict:
			for neighbor in self.__graph_dict[vertex]:
				edges.append({vertex, neighbor})
		return edges

	#edge could be of type list, tuple, or set
	def addEdge(self, edge):
		edge = set(edge)
		(node1, node2) = tuple(edge)

		if node1 in self.__graph_dict:
			__graph_dict[node1].append(node2)
		else:
			__graph_dict[node1] = node2

	def add_vertex(self, vertex):
		if vertex not in __graph_dict:
			graph_dict[vertex] = []

	##BFS
	def contains(self, data):
		visited = {}

		firstKey = self.__graph_dict.iter().next()
		bfsQueue.add(firstKey)

		foundNode = False
		self.__visit(firstKey, visited)

		while len(bfsQueue)!=0:
			for neighbor in self.__graph_dict[bfsQueue[0]]:
				if neighbor not in visited:
					bfsQueue.append(neighbor)
			self.__visit(bfsQueue[0], visited)
			del(bfsQueue[0])

		return foundNode

	def __visit(self, vertex, visited):
		visited.add(vertex)
		return

	def clone(self, graph):
		return

def main():
    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }
    graph  = Graph(g)
    print(str(graph))
    print(graph.contains("b"))

if __name__=="__main__":
	main()
