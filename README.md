# KeggSearch
Bioinformatics Project for ABE 141: Creating a search engine and optimizer for biochemical reactions. 
Reads the reactions dataset from the BRITE heirarchy on kegg.jp
Parses the data's many layers and converts it into multiple lists of reactions by enzyme category
Using the NetworkX library, the reaction lists are used as feeders for nodes in a graph
The graph can now be used to find the shortest distance [if any] between two compounds via enzyme-based biochemical reactions
The final part of the code is the basic user interactivity with the program. 
