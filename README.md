# Attributed Graph Alignment
This is a research project supervised by Dr. Lele Wang and Dr. Simon Oya. 
The goal of this project is to match two labeled user graphs with high accuracy. 
The previous work was done by Dr. Wang's Ph.D. student Ziao Wang and this repository is created and maintained 
by Alan Wei. 

## [main.py](main.py)


## [graph_gen.py](graph_gen.py)
`graph_gen.py` contains the functions required to set up the algorithm.

## [attr_rich_cmn_nbs_hgrn.py](attr_rich_cmn_nbs_hgrn.py)
In `attr_rich_cmn_nbs_hgrn.py`, a cost matrix of common attributes is first generated. Then, the Hungarian Algorithm is 
implemented to find the optimal matching based on the cost matrix. The equivalency between using common attributes and 
using the Hamming distance is proved [here](Proof-of-Equivalency.html).

