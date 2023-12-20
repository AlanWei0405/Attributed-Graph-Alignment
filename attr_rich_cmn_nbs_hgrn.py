import numpy as np
from scipy.optimize import linear_sum_assignment


def attr_rich_cmn_nbs_hgrn(g1, g2prime, num_users):

    # Find anchor
    # Initialize a dictionary to store the number of common neighbors for each pair
    common_neighbors_dict = np.zeros([num_users, num_users])
    # Iterate through all pairs of user nodes
    for node_i in [node for node in g1.nodes() if g1.nodes[node]["bipartite"] == 0]:
        for node_j in [
            node for node in g2prime.nodes() if g2prime.nodes[node]["bipartite"] == 0
        ]:
            # Calculate the number of common neighbors between node_A and node_B
            common_neighbors = len(
                set(
                    set(g1.neighbors(node_i))
                    & set(
                        [
                            node
                            for node in g1.nodes()
                            if g1.nodes[node]["bipartite"] == 1
                        ]
                    )
                )
                & set(
                    set(g2prime.neighbors(node_j))
                    & set(
                        [
                            node
                            for node in g2prime.nodes()
                            if g2prime.nodes[node]["bipartite"] == 1
                        ]
                    )
                )
            )

            # Store the count in the dictionary
            common_neighbors_dict[node_i][node_j] = common_neighbors
    # print(common_neighbors_dict)
    row_ind, col_ind = linear_sum_assignment(
        np.max(common_neighbors_dict) - common_neighbors_dict
    )

    # Get the keys from the filtered dictionary
    anchors = [(g1_node, g2p_node) for g1_node, g2p_node in zip(row_ind, col_ind)]
    # print(f"Anchors: {anchors}")

    # Align Users
    # Unmatched nodes
    unmatched_u1 = [
        node_i
        for node_i in [node for node in g1.nodes() if g1.nodes[node]["bipartite"] == 0]
    ]
    unmatched_u2 = [
        node_j
        for node_j in [
            node for node in g2prime.nodes() if g2prime.nodes[node]["bipartite"] == 0
        ]
    ]
    for (i, j) in anchors:
        if i in unmatched_u1:
            unmatched_u1.remove(i)
        if j in unmatched_u2:
            unmatched_u2.remove(j)

    pairs = []
    if len(unmatched_u1) != 0:
        # Calculate Wij
        w_dict = np.zeros([len(unmatched_u1), len(unmatched_u2)])
        for i in unmatched_u1:
            for j in unmatched_u2:
                w_dict[i][j] = len(
                    [
                        (node_k, node_l)
                        for node_k in g1.neighbors(i)
                        for node_l in g2prime.neighbors(j)
                        if (node_k, node_l) in anchors
                    ]
                )

        row_ind2, col_ind2 = linear_sum_assignment(np.max(w_dict) - w_dict)
        pairs = [(g1_node, g2p_node) for g1_node, g2p_node in zip(row_ind2, col_ind2)]

    # Print the updated dictionary
    results = anchors + pairs

    results = {i: j for i, j in results}

    return results
