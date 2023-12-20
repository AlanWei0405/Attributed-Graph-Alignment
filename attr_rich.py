import random


def attr_rich(g1, g2prime, num_users, x, y):

    # Set thresholds
    x = x
    y = y
    # Find anchor
    # Initialize a dictionary to store the number of common neighbors for each pair
    common_neighbors_dict = {}
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
            common_neighbors_dict[(node_i, node_j)] = common_neighbors
    # print(common_neighbors_dict)
    filtered_dict = {
        key: value for key, value in common_neighbors_dict.items() if value > x
    }
    # Step 2: Group keys by the same i values
    i_groups = {}
    for key, value in filtered_dict.items():
        i = key[0]
        if i not in i_groups:
            i_groups[i] = []
        i_groups[i].append((key, value))
    # Step 3: Keep only the entry with the largest value for each i group
    for i, group in i_groups.items():
        max_value = max(group, key=lambda x: x[1])[1]
        i_groups[i] = [(key, value) for key, value in group if value == max_value]
    temp_data = {}
    for i, group in i_groups.items():
        for key, value in group:
            temp_data[key] = value
    filtered_dict = temp_data
    # Step 4: Group keys by the same j values
    j_groups = {}
    for key, value in filtered_dict.items():
        j = key[1]
        if j not in j_groups:
            j_groups[j] = []
        j_groups[j].append((key, value))
    # Step 5: Keep only the entry with the largest value for each i group
    for j, group in j_groups.items():
        max_value = max(group, key=lambda x: x[1])[1]
        j_groups[j] = [(key, value) for key, value in group if value == max_value]
    temp_data = {}
    for j, group in j_groups.items():
        for key, value in group:
            temp_data[key] = value
    filtered_dict = temp_data
    # Step 6: Randomly keep only one entry for each i group
    i_groups = {}
    for key, value in filtered_dict.items():
        i = key[0]
        if i not in i_groups:
            i_groups[i] = []
        i_groups[i].append((key, value))
    for i, group in i_groups.items():
        keep_key, _ = random.choice(group)
        for key, _ in group:
            if key != keep_key:
                del filtered_dict[key]
    j_groups = {}
    for key, value in filtered_dict.items():
        j = key[1]
        if j not in j_groups:
            j_groups[j] = []
        j_groups[j].append((key, value))
    for j, group in j_groups.items():
        keep_key, _ = random.choice(group)
        for key, _ in group:
            if key != keep_key:
                del filtered_dict[key]
    # Get the keys from the filtered dictionary
    anchors = list(filtered_dict.keys())
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
    # Calculate Wij
    w_dict = {}
    for i in unmatched_u1:
        for j in unmatched_u2:
            w_dict[(i, j)] = len(
                [
                    (node_k, node_l)
                    for node_k in g1.neighbors(i)
                    for node_l in g2prime.neighbors(j)
                    if (node_k, node_l) in anchors
                ]
            )
    matched_pairs = {
        key: value for key, value in w_dict.items() if value > y * len(anchors)
    }
    pairs = matched_pairs
    # Step 2: Group keys by the same i values
    i_groups = {}
    for key, value in pairs.items():
        i = key[0]
        if i not in i_groups:
            i_groups[i] = []
        i_groups[i].append((key, value))
    # Step 3: Keep only the entry with the largest value for each i group
    for i, group in i_groups.items():
        max_value = max(group, key=lambda x: x[1])[1]
        i_groups[i] = [(key, value) for key, value in group if value == max_value]
    temp_data = {}
    for i, group in i_groups.items():
        for key, value in group:
            temp_data[key] = value
    pairs = temp_data
    # Step 4: Group keys by the same j values
    j_groups = {}
    for key, value in pairs.items():
        j = key[1]
        if j not in j_groups:
            j_groups[j] = []
        j_groups[j].append((key, value))
    # Step 5: Keep only the entry with the largest value for each i group
    for j, group in j_groups.items():
        max_value = max(group, key=lambda x: x[1])[1]
        j_groups[j] = [(key, value) for key, value in group if value == max_value]
    temp_data = {}
    for j, group in j_groups.items():
        for key, value in group:
            temp_data[key] = value
    pairs = temp_data
    # Step 6: Randomly keep only one entry for each i group
    i_groups = {}
    for key, value in pairs.items():
        i = key[0]
        if i not in i_groups:
            i_groups[i] = []
        i_groups[i].append((key, value))
    for i, group in i_groups.items():
        keep_key, _ = random.choice(group)
        for key, _ in group:
            if key != keep_key:
                del pairs[key]
    j_groups = {}
    for key, value in pairs.items():
        j = key[1]
        if j not in j_groups:
            j_groups[j] = []
        j_groups[j].append((key, value))
    for j, group in j_groups.items():
        keep_key, _ = random.choice(group)
        for key, _ in group:
            if key != keep_key:
                del pairs[key]
    # Print the updated dictionary
    results = anchors + list(pairs.keys())

    results = {i: j for i, j in results}

    return results
