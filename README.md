# Rumors-Spreading-ABS

This model simulate the spreading of different types of opinions in a scale-free network. The opinions are represented by binary strings and they are spread by agents called spreaders. The spreaders have a memory of capacity M, where they store the opinions that they receive. Moreover, the spreaders can also distort an opinion before to pass it.

This model can be used also to evaluate the effect of the entrance of some "incorruptible" agents (repairers). It is possible to evaluate three different strategies to enter them: random (the repairers are inserted randomly in the network ), preferential attachment by degree (repairers are inserted in the most connected nodes) and preferential attachment by betweenness (repairers are inserted in the nodes with highest betweenness centrality). 

At the beginning, the model ask to enter the parameters of the simulation:

-The size of network

-The length of the binary strings

-The memory capacity of the spreaders

-The resistance to distortions

-The confidence in the most connected nodes

-The number of time steps

-The number of repairers inserted in the network

-The time when repairers are inserted

-The entering strategy

You can use the model at the link: https://mybinder.org/v2/gh/Lorenzochicchi/Rumors-Spreading-ABS/master
