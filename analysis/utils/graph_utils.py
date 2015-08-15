def show_graph_with_labels(A,B):
    import matplotlib.pyplot as plt
    import networkx as nx
    import numpy as np
    rows, cols = np.where(A == 1)
    edges_A = zip(cols.tolist(), rows.tolist())
    rows, cols = np.where(B == 1)
    edges_B = zip(cols.tolist(), rows.tolist())
    gr = nx.DiGraph()
    nodes=range(1,A.shape[0])
    gr.add_nodes_from(nodes)
    gr.add_edges_from(edges_A)
    gr.add_edges_from(edges_B)
    pos=nx.circular_layout(gr)
    mylabels={i:'%d'%i for i in gr.nodes()} # {(gr.nodes(),['%d'%i for i in gr.nodes()])
    nx.draw_networkx_nodes(gr, node_size=500, pos=pos,labels=mylabels, with_labels=True)
    nx.draw_networkx_labels(gr,pos=pos,labels=mylabels)
    nx.draw_networkx_edges(gr,pos,edgelist=edges_A,edge_color='r')
    print 'Red: unmodulated (A)'
    nx.draw_networkx_edges(gr,pos,edgelist=edges_B,edge_color='b')
    print 'Blue: modulated (B)'
    plt.show()
    return gr
