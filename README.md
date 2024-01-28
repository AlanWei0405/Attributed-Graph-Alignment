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
In this project, we have implemented 3 different metrics/methods so fat to tackle this problem. To run experiments with 
different metric/method, please use the corresponding functions listed below in `main`, e.g., 
`results = attr_rich_cmn_nbs_hgrn(g1, g2prime, num_users)`.

### Thresholding using Common Attributes Method

In the paper [*On the Feasible Region of Efficient Algorithms for
Attributed Graph Alignment*](https://arxiv.org/pdf/2201.10106.pdf#page2), the original method using thresholds is proposed. 
In [`attr_rich.py`](attr_rich.py), the number of common attributes for each user-user node pair . There are two thresholds used in this method, 
namely `x` and `y`. `x` is used to select the anchor user nodes, then `y` is a utilized in the next step to match the 
rest of the nodes.

### Hungarian Algorithm using Common Attributes Method

In [`attr_rich_cmn_nbs_hgrn.py`](attr_rich_cmn_nbs_hgrn.py), the same cost matrix is first generated. This time, the Hungarian Algorithm is 
implemented to find the optimal matching based on the cost matrix. The equivalency between using common attributes and 
using the Hamming distance is proved [here](Proof-of-Equivalency.html).

### Hungarian Algorithm using Hamming Distance Method

An alternative of the method above is implemented in [`attr_rich_hm_ds_hgrn.py`](attr_rich_hm_ds_hgrn.py)The Hamming 
Distance between a graph pair is the number of edges that only exist in one and only one of the two graphs,
This alternative also verifies the equivalency between maximizing the common attributes and minimizing the Hamming 
Distance.

## Conclusion

From the experimental results, we can compare the pros and cons of these methods.

### Thresholding using Common Attributes Method

#### Pros

- Hyperparameters can be manually adjusted to obtain results of different precisions.
- Interim results can be utilized since there are two stages in this method.
#### Cons

- Can not perform very well in the practical implementations in the sense that low thresholds can generate less accurate
 results while high thresholds can over constrain the possible outcomes. The empirical formulas for the thresholds 
provide an general guidance for choosing the hyperparameters. However, it might not lead to the optimal results in all 
real world data sets.

### Hungarian Algorithm using Common Attributes / Hamming Distance Method

#### Pros

- The Hungarian Algorithm is known to generate the optimal solution to linear assignment problems. In this problem, 
maximizing the number of Common attributes and minimizing the Hamming Distance are all cases of linear assignment. 

#### Cons

- The algorithm is implemented in only one stage. When the accuracy is not 100%, there's no interim results for us to 
further take advantage of to achieve a higher accuracy.

Overall, through this project, I've understood the mathematical and information-theoretical proof of the algorithm. By 
further implementing the algorithm, I verified that the MAP/MLE estimator for this problem is the estimator that 
minimizes the Hamming Distance, which is proved to be equivalent to maximize the number of common attributes. Inspired 
by the fact that both of the algorithm and the estimator are already theoretically optimal in their categories 
respectively, I'm looking forward to exploring the machine learning models that can provide better solutions to this 
problem on real world datasets.

## Acknowledgement

1. On the Feasible Region of Efficient Algorithms for
Attributed Graph Alignment
https://arxiv.org/pdf/2201.10106.pdf#page2
2. Attributed Graph Alignment
https://arxiv.org/pdf/2102.00665.pdf#page1

I'd like to express my deepest appreciation to the guidance I received from Dr. Oya and Dr. Wang. I'm also thankful for 
Ph.D. student Ziao Wang for his help with theoretical proof.
