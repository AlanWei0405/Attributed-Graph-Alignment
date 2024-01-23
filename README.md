# Attributed Graph Alignment
This is a research project supervised by Dr. Lele Wang and Dr. Simon Oya. 
The goal of this project is to match two labeled user graphs with high accuracy. 
The previous work was done by Dr. Wang's Ph.D. student Ziao Wang and this repository is created and maintained 
by Alan Wei. 

## Problem Setting
A graph is used represent a user network:

- The user nodes represent the users in the network;
- The attribute nodes represent the attributes in the network;
- A user-user edge indicates a connection between the two users;
- A user-attribute edge indicates that the user is labeled with the attribute.

Given a pair of graphs such that the user node names are different but the attribute node names are the same, and the 
sets of user-user edges and user-attribute edges are also different respectively, the goal is to identify the optimal 
correspondence of the user nodes in the graph pair.

## Initialization

Firstly, we are going to generate a **base graph** to get such a graph pair. Let `G(n,p,su,m,q,sa)` denote the base graph 
where `n` is the number of user nodes, `p` is the generating probability of a user-user edge, `m` is the number of 
attributes, and `q` is generating probability of a user-attribute edge. 

After getting our base graph, we can move on to generate the graph pair. Notice that there are still two hyperparameters
 unused, namely `su` and `sa`. Now, we are going to select the user-user edges with probability `su` and user-attribute 
edges with probability `sa`. By doing this twice, we obtain a graph pair of `G1` and `G2`. In the last step of this 
initialization process, a random permutation will be applied to the user nodes in `G2` leading us to the final graph 
pair of `G1` and `G2'`.

By running `main`, we can set values of the hyperparameters required to initialize a simulation of the problem 
setting. There are 7 hyperparameters required to do so, namely `iteration`, `n`, `p`, `su`, `m`, `q`, and `sa`. In 
addition to the 6 hyperparameters mentioned, `iteration` is the number of experiments conducted using the same set of 
hyperparameters.

[graph_gen.py](graph_gen.py) contains the functions required by the initialization process and will return `G1`, `G2'`, 
the true permutation `node_mapping` and the number of users `num_users`.

## Algorithm

### Thresholding Method

### Hamming Distance Method

### Common Attribute Method

In `attr_rich_cmn_nbs_hgrn.py`, a cost matrix of common attributes is first generated. Then, the Hungarian Algorithm is 
implemented to find the optimal matching based on the cost matrix. The equivalency between using common attributes and 
using the Hamming distance is proved [here](Proof-of-Equivalency.html).

## Comparison

## Conclusion

## Acknowledgement

