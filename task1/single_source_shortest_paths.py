def initialize_single_source(G, s):
	"""Initialize distance and predecessor values for vertices in graph.

	Arguments:
	G -- a graph
	s -- index of the source vertex for shortest paths
	"""
	# Initialize d and pred.
	card_V = G.get_card_V()
	# d[v] is an upper bound on the weight of a shortest path from source s to v.
	d = [float('inf')] * card_V
	pi = [None] * card_V
	d[s] = 0
	return d, pi


def relax(u, v, w, d, pi, relax_func=None):
	"""Improve the shortest path to v found so far.

	Arguments:
	u, v -- relaxing the edge (u, v))
	w -- weight of the edge (u, v)
	d -- upper bound on the weight of a shortest path from source s to v
	pi -- list of predecessors
	relax_func -- function called after relaxing an edge, default is to do nothing
	"""
	if d[v] > d[u] + w:
		d[v] = d[u] + w  # reduce v's shortest path weight
		pi[v] = u        # update v's predecessor predecessor
		if relax_func is not None:
			relax_func(v)
