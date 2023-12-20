# import networkx as nx
# import matplotlib.pyplot as plt


# def draw_graph(G, u2u, u2a):
#     edge_colors = ["blue" for _ in u2u] + [
#         "red" for _ in u2a
#     ]  # Assign colors for edges
#     pos = nx.circular_layout(G)  # Layout for the nodes
#     nx.draw(
#         G,
#         pos,
#         edgelist=u2u + u2a,
#         edge_color=edge_colors,
#         with_labels=True,
#         node_size=200,
#         node_color=[
#             "red" if G.nodes[node]["bipartite"] == 1 else "blue" for node in G.nodes
#         ],
#         font_size=10,
#         font_color="black",
#     )
#     plt.show()


def compare_dictionaries(solution, answer):
    true_count = 0
    false_count = 0
    miss_count = 0

    for key in solution.keys():
        if key in answer:
            if solution[key] == answer[key]:
                true_count += 1
            else:
                false_count += 1
        else:
            miss_count += 1

    for key in answer.keys():
        if key not in solution:
            miss_count += 1

    accuracy = true_count / len(solution)

    metrics = [true_count, false_count, miss_count, accuracy]

    return metrics
