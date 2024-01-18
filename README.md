<script type="text/javascript"
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$'], ['\\(','\\)']],
      processEscapes: true},
      jax: ["input/TeX","input/MathML","input/AsciiMath","output/CommonHTML"],
      extensions: ["tex2jax.js","mml2jax.js","asciimath2jax.js","MathMenu.js","MathZoom.js","AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
      TeX: {
      extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"],
      equationNumbers: {
      autoNumber: "AMS"
      }
    }
  });
</script>

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
edges with probability `sa`. By doing this twice, we obtain the $ G_1 $

### [main.py](main.py)
Firstly, by running `main`, we can set values to the hyperparameters required to initialize a simulation of the problem 
setting. There are 7 hyperparameters required to do so, namely `iteration`, `n`, `p`, `su`, `m`, `q`, and `sa`.

### [graph_gen.py](graph_gen.py)
`graph_gen.py` contains the functions required to set up the algorithm.

## Algorithm

### Thresholding Method

### Hamming Distance Method

### Common Attribute Method

## Comparison

## Conclusion

## Acknowledgement

### [attr_rich_cmn_nbs_hgrn.py](attr_rich_cmn_nbs_hgrn.py)
In `attr_rich_cmn_nbs_hgrn.py`, a cost matrix of common attributes is first generated. Then, the Hungarian Algorithm is 
implemented to find the optimal matching based on the cost matrix. The equivalency between using common attributes and 
using the Hamming distance is proved [here](Proof-of-Equivalency.html).

