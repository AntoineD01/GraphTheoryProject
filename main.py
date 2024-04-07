import Myfunctions
import networkx as nx
import matplotlib as plt

def main():
    file_path = "Constraint Table Test.txt"  
    tasks, durations, predecessors = Myfunctions.read_constraint_table(file_path)
    Myfunctions.display_table(tasks, durations, predecessors)
    successors = Myfunctions.successors(tasks, predecessors)
    nb_edges = Myfunctions.count_edges(successors)

    edges = Myfunctions.generate_edges(tasks, predecessors)
    print(edges)
    
    G = nx.DiGraph()
    G.add_nodes_from(tasks)
    G.add_edges_from(edges)

    edge_labels = {}
    for i in range (nb_edges):
        edge_labels[edges[i]] = durations[i]
    
    #edge_labels = {('A', 'B'): '3', ('A', 'C'): '3', ('B', 'D'): '2', ('C', 'D'): '4', ('C', 'F'): '3', ('D', 'E'): '5'}
    
    pos = nx.spring_layout(G)  # Define the layout for the graph
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=12, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')  # Add edge labels
    
    
    plt.pyplot.show()

if __name__ == "__main__":
    main()
