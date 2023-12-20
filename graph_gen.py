import networkx as nx
import random


def graph_gen(n, p, su, m, q, sa):

    # Create an empty graph
    g = nx.Graph()

    # Number of nodes
    num_users = n  # n
    num_attrs = m  # m

    # Probability of an edge between any pair of nodes
    u2u_gen_p = p
    u2a_gen_q = q

    # Add nodes to the graph
    g.add_nodes_from(range(num_users), bipartite=0)  # First set of nodes (bipartite=0)
    g.add_nodes_from(
        range(num_users, num_users + num_attrs), bipartite=1
    )  # Second set of nodes (bipartite=1)
    u2u_edges = [
        (i, j)
        for i in range(num_users)
        for j in range(i + 1, num_users)
        if random.random() < u2u_gen_p
    ]
    u2a_edges = [
        (i, j)
        for i in range(num_users)
        for j in range(num_users, num_users + num_attrs)
        if random.random() < u2a_gen_q
    ]

    # Add user-user edges based on the given probability
    g.add_edges_from(u2u_edges)
    # Add user-attr edges based on the given probability
    g.add_edges_from(u2a_edges)

    # Draw the graph (optional, requires matplotlib)
    # draw_graph(g, u2u_edges, u2a_edges)
    # # Print the edges in the graph
    # print("Edges in the graph:")
    # for edge in G.edges():
    #     print(edge)

    # Generate G1 and G2
    g1 = g.copy()
    g2 = g.copy()
    s_u = su
    s_a = sa

    # Randon sample from the edges
    G1_u2u = [edge for edge in u2u_edges if random.random() < s_u]
    G1_u2a = [edge for edge in u2a_edges if random.random() < s_a]
    g1.remove_edges_from(
        list(filter(lambda edge: edge not in G1_u2u + G1_u2a, g.edges))
    )
    G2_u2u = [edge for edge in u2u_edges if random.random() < s_u]
    G2_u2a = [edge for edge in u2a_edges if random.random() < s_a]
    g2.remove_edges_from(
        list(filter(lambda edge: edge not in G2_u2u + G2_u2a, g.edges))
    )
    # draw_graph(g1, G1_u2u, G1_u2a)
    # draw_graph(g2, G2_u2u, G2_u2a)

    # Generate G2'
    # Apply a permutation
    # Generate a random permutation of the nodes
    user_nodes = list(g2.nodes())[:num_users]
    # print(user_nodes)
    random.shuffle(user_nodes)
    # print(user_nodes)

    # Create a mapping from the original nodes to the shuffled nodes
    node_mapping = {
        original_node: shuffled_node
        for original_node, shuffled_node in zip(g2.nodes(), user_nodes)
    }
    # print(node_mapping)
    # G2prime_nodes = user_nodes + list(g2.nodes())[num_users:]
    # print(G2prime_nodes)

    # Relabel the nodes in the graph using the random permutation
    g2prime = nx.relabel_nodes(g2, node_mapping)
    # shuffled_G2_u2u = [(i, j) for (i, j) in g2prime.edges if j < num_users]
    # shuffled_G2_u2a = [(i, j) for (i, j) in g2prime.edges if j >= num_users]
    # draw_graph(g2prime, shuffled_G2_u2u, shuffled_G2_u2a)
    return g1, g2prime, node_mapping, num_users
