import networkx as nx
from numpy import *
from matplotlib import *
from Agents import *



#Create a Barabasi-Albert graph of size n

def CreateGraphBarabasi(n):
    G=nx.barabasi_albert_graph(n,2)
    G.agent={}
    return(G)

#this function convert  a decimal number into a binary number.The list is completed utill it have length L (Zeros are inserted at the left)

def ConvertiInBinario(d,Len):
    a=[]
    while d > 0:
        if d%2==0:
            a.append(0)
        else:
            a.append(1)
        d = d // 2
    while len(a)<Len:
        a.append(0)
    return(a[::-1])

#This function take as input an integer L and return a list of all the binary strings with lenght L.

def MakeListRumors(Len):
    List_of_rumors=[]
    V=pow(2,Len)
    for i in range(V):
        b=ConvertiInBinario(i,Len)
        List_of_rumors.append(b)
    return(List_of_rumors)

#to initialize the network

def InitGraph(G,List,Mem, L):
    G.agent={}
    for i in G.nodes():
        G.agent[i]=Spreader(True, List, Mem ,L)   
    p= np.random.randint(len(G.nodes()))
    G.agent[p].memory[0:0]=[List[0].copy()]
    del G.agent[p].memory[-1]
    
#to insert repairers into the network (three different entering rules)
    
def InsertRepairersRandom(G,Rep,TrueOpinion):
    N=len(G.nodes())
    for i in range(0,Rep):
        q=np.random.randint(N)
        G.agent[q]=repairer(False,TrueOpinion)

    
def InsertRepairersPref(G,Rep,TrueOpinion):
    N=len(G.nodes())
    Hubs=[]
    degrees=dict(G.degree()).values()
    OrdDegr=sorted(list(degrees))[::-1]
    R=0
    for grad in OrdDegr:
        for j in G.nodes():
            if G.degree[j]==grad and G.agent[j].spreader==True:
                if R == Rep:
                    break
                G.agent[j]=repairer(False,TrueOpinion)
                R+=1
                if R == Rep:
                    break
        if R == Rep:
            break
            
def InsertRepairersBetw(G,Rep,TrueOpinion):
    N=len(G.nodes())
    Hubs=[]
    Betw=nx.algorithms.centrality.betweenness_centrality(G)
    degrees=dict(Betw).values()
    OrdDegr=sorted(list(degrees))[::-1]
    R=0
    for grad in OrdDegr:
        for j in G.nodes():
            if Betw[j]==grad and G.agent[j].spreader==True:
                if R == Rep:
                    break
                G.agent[j]=repairer(False,TrueOpinion)
                R+=1
                if R == Rep:
                    break
        if R == Rep:
            break
    
            

            
            
# The Agents spread opinions each other
def Interaction(G,beta):
    Nodes=[]
    for i in G.nodes():
        Nodes.append(i)
    random.shuffle(Nodes)
    for i in Nodes:
        if G.agent[i].major_rumor !=[]:
            for j in G.neighbors(i):
                if G.agent[j].spreader==True:
                    gradi=[]
                    for w in G.neighbors(j):
                        gradi.append(pow(G.degree[w],beta))
                    eta=pow(G.degree[i],beta)/max(gradi)
                    r=np.random.random()
                    if r < eta:
                        G.agent[j].memory[0:0]=[G.agent[i].major_rumor]
                        del(G.agent[j].memory[-1]) 


#Save opinions concentrations
                         
def MemorizzaConcentrazioni(G,F, List_of_rumors):    
    temp=[]
    NumSpread=len(G)-F
    for j in range(len(List_of_rumors)):
        a=0
        for i in G.nodes():
            if G.agent[i].spreader==True:
                if List_of_rumors[j]==G.agent[i].major_rumor:
                    a+=1
        temp.append(a/NumSpread)

    return(temp)

#Save average entropy

def MemorizzaEntropiaMedia(G,H,L):       
    NumbInfect=0
    for i in G.nodes():
        if G.agent[i].major_rumor!=[] and G.agent[i].spreader==True:
            NumbInfect+=1

    s=0
    for k in G.nodes():
        if G.agent[k].spreader==True:
            if G.agent[k].count != [0]*pow(2,L):
                s+=G.agent[k].entropy
    if s==0:
        H.append(s)
    else:
        H.append(s/NumbInfect)
