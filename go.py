import networkx as nx
import pickle
from Agents import *
from Functions import *

n=int(input("What is the network size? "))
L=int(input("How long are the binary sequences representing the rumors? "))
Mem=int(input("What is the memory capacity of the agents?"))
K=float(input("What is the value of k (resistance to distortions)?"))
beta=float(input("What is the value of Beta (Confidende in the most connected nodes)?"))
item=int(input("How many time steps?"))
Rep=int(input("How many repairers?"))
Tstar=int(input("When the repairers are entered the network?"))
Pref=int(input("What is the entering rule? random (0), preferential attachment (1), betweenness (2)"))
Rumors=[]
H=[]



List_of_rumors=MakeListRumors(L)

#create network and initialize it
G=CreateGraphBarabasi(n)
InitGraph(G,List_of_rumors,Mem, L)
cont=item//20
F=0
for t in range (0,item):
    
    if t==Tstar:
        print("The repairers are entering the network...")
        F=Rep
        if Pref==0:
            InsertRepairersRandom(G,Rep,List_of_rumors[-1])
        if Pref==1:
            InsertRepairersPref(G,Rep,List_of_rumors[-1])
        if Pref==2:
            InsertRepairersBetw(G,Rep,List_of_rumors[-1])

    for i in G.nodes():
        if G.agent[i].spreader == True:
            G.agent[i].CalMaxRumor(L,List_of_rumors)
            G.agent[i].CalEntropy(L,List_of_rumors)
            G.agent[i].ValutaDistorsioni(K,L)

    Interaction(G,beta)

    #Save data    

    temp=MemorizzaConcentrazioni(G,F,List_of_rumors)
    Rumors.append(temp)
    MemorizzaEntropiaMedia(G,H,L)
    
    if t%cont ==0:
        dada=t/item
        print("(", round(dada,2), "of simulation completed) The concentration of the wrong opinion is:", temp[0] )


print("Simulation completed")