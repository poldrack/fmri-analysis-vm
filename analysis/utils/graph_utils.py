def show_graph_from_adjmtx(A,B,C,title=''):
	import matplotlib.pyplot as plt
	import networkx as nx
	import numpy as np

	gr = nx.DiGraph()
	nodes=list(range(1,A.shape[0]))
	gr.add_nodes_from(nodes)
	gr.add_node('u')
	rows, cols = np.where(A == 1)
	edges_A = list(zip(cols.tolist(), rows.tolist()))
	gr.add_edges_from(edges_A)
	rows, cols = np.where(B == 1)
	edges_B = list(zip(cols.tolist(), rows.tolist()))
	gr.add_edges_from(edges_B)
	mylabels={i:'%d'%i for i in gr.nodes() if not i=='u'} # {(gr.nodes(),['%d'%i for i in gr.nodes()])
	rows=np.where(C==1)[0]
	edges_C=[]
	for r in rows:
		edges_C.append(('u',r))
	gr.add_edges_from(edges_C)
	mylabels['u']='u'
	pos=nx.circular_layout(gr)
	print(gr.edges())
	nx.draw_networkx_nodes(gr, node_size=500, pos=pos,labels=mylabels, with_labels=True)
	nx.draw_networkx_labels(gr,pos=pos,labels=mylabels)
	nx.draw_networkx_edges(gr,pos,edgelist=edges_C,edge_color='k')
	print('Black: input')
	nx.draw_networkx_edges(gr,pos,edgelist=edges_A,edge_color='r')
	print('Red: unmodulated')
	if edges_B:
		nx.draw_networkx_edges(gr,pos,edgelist=edges_B,edge_color='b')
		print('Blue: modulated')
	plt.title(title)
	plt.show()
	return gr

def show_graph_from_pattern(pattern_file,nnodes=5):
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
		print(l_s)
		if len(l_s)>1:
			# if it's a numeric node, add to the list
			try:
				nodes.append(int(l_s[0]))
				n1=int(l_s[0])
			except:
				n1=l_s[0]
			try:
				nodes.append(int(l_s[2]))
				n2=int(l_s[2])
			except:
				n2=l_s[2]
			edges.append((n1,n2))
			assert l_s[4].find('arrowhead')>-1
			if l_s[4].find('none')>-1:
				edges.append((n2,n1))

	nodes=list(range(0,nnodes)) # include any nodes that had no connnections
	mylabels={i:'%d'%i for i in nodes} # {(gr.nodes(),['%d'%i for i in gr.nodes()])
	mylabels['u']='u'
	nodes.append('u')
	gr.add_nodes_from(nodes)
	gr.add_edges_from(edges)

	pos=nx.circular_layout(gr)
	nx.draw_networkx_nodes(gr, node_size=500, pos=pos,labels=mylabels, with_labels=True)
	nx.draw_networkx_labels(gr,pos=pos,labels=mylabels)
	nx.draw_networkx_edges(gr,pos,edge_color='r')
	print('Red: unmodulated')
	plt.show()
	return gr
