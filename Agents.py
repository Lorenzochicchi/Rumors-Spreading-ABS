import numpy as np


class Spreader:
    def __init__(self,spreader, List_rumor,Mem,L):
        self.H_max=-np.math.log(1/Mem)
        self.spreader= spreader   
        self.memory =[[]]*Mem 
        self.major_rumor=[]
        self.entropy=0.0
        self.count=[0]*pow(2,L)
        
    #to evaluate the major opinion   
    def CalMaxRumor(self,L,List_rumors):
        lista=[]    
        if self.count!= [0]*pow(2,L):        
            M=max(self.count)
            for j in range (0,len(self.count)):
                if M==self.count[j]:
                    lista.append(j)
            R=np.random.choice(lista)
            self.major_rumor=List_rumors[R].copy()
    
    
    #to evaluate the entropy
    def CalEntropy(self,L, List_rumors):
        self.count=[0]*pow(2,L)
        s=0
        for j in self.memory:
            for w in range(len(List_rumors)):
                if j==List_rumors[w]:
                    self.count[w]+=1
        if self.count != [0]*pow(2,L):
            TOT=0
            for j in self.count:
                TOT+=j
            for h in range(len(self.count)):
                f=self.count[h]/TOT
                if f!= 0:
                    s+= f*np.math.log(f,2)
            self.entropy=-s
 

    #to choose if to distort major opinion
    def ValutaDistorsioni(self,K,L):
        if self.major_rumor!=[]:
            Pdist=1/(math.exp((self.H_max-self.entropy)/self.H_max*K)+1)
            r=np.random.random()
            if r<Pdist:
                Dist=self.major_rumor.copy()
                q=np.random.randint(L)
                self.major_rumor[q]=(self.major_rumor[q]+1) % 2
              
                

    #to update memory
    def UpdateMemory(self,NewOpinion):
        self.memory[0:0]=NewOpinion.copy()
        del(self.memory[-1])
        return self.my_group
    

class repairer:
    def __init__(self,spreader,TrueOpinion):
        self.spreader= spreader   
        self.major_rumor=TrueOpinion



    
