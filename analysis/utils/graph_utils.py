def show_graph_from_adjmtx(A,B=None):
	import matplotlib.pyplot as plt
	import networkx as nx
	import numpy as np

	gr = nx.DiGraph()
	nodes=range(1,A.shape[0])
	gr.add_nodes_from(nodes)

	rows, cols = np.where(A == 1)
	edges_A = zip(cols.tolist(), rows.tolist())
	gr.add_edges_from(edges_A)
	if not B==None:
		rows, cols = np.where(B == 1)
		edges_B = zip(cols.tolist(), rows.tolist())
		gr.add_edges_from(edges_B)
	else:
		edges_B=None

	pos=nx.circular_layout(gr)
	mylabels={i:'%d'%i for i in gr.nodes()} # {(gr.nodes(),['%d'%i for i in gr.nodes()])
	nx.draw_networkx_nodes(gr, node_size=500, pos=pos,labels=mylabels, with_labels=True)
	nx.draw_networkx_labels(gr,pos=pos,labels=mylabels)
	nx.draw_networkx_edges(gr,pos,edgelist=edges_A,edge_color='r')
	print 'Red: unmodulated'
	if edges_B:
		nx.draw_networkx_edges(gr,pos,edgelist=edges_B,edge_color='b')
		print 'Blue: modulated'
	plt.show()
	return gr

def show_graph_from_pattern(pattern_file):
	import matplotlib.pyplot as plt
	import networkx as nx
	import numpy as np
	pf=[i.strip().replace('"','') for i in open(pattern_file).readlines()]
	if not pf[0].find('digraph')>-1:
		raise RuntimeError('input is not a valid dot file')
		
	gr = nx.DiGraph()
	nodes=[]
	edges=[]
	for l in pf[1:]:
		l_s=l.split(' ')
		print l_s
		if len(l_s)>1:
			nodes.append(int(l_s[0]))
			nodes.append(int(l_s[2]))
			edges.append((int(l_s[0]),int(l_s[2])))
			assert l_s[4].find('arrowhead')>-1
			if l_s[4].find('none')>-1:
				edges.append((int(l_s[2]),int(l_s[0])))
				
	nodes=list(set(nodes))
	gr.add_nodes_from(nodes)
	gr.add_edges_from(edges)

	pos=nx.circular_layout(gr)
	mylabels={i:'%d'%i for i in gr.nodes()} # {(gr.nodes(),['%d'%i for i in gr.nodes()])
	nx.draw_networkx_nodes(gr, node_size=500, pos=pos,labels=mylabels, with_labels=True)
	nx.draw_networkx_labels(gr,pos=pos,labels=mylabels)
	nx.draw_networkx_edges(gr,pos,edge_color='r')
	print 'Red: unmodulated'
	plt.show()
	return gr
