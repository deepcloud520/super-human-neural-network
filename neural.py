import random as r
import math 
def sigmoid(n):
    return float('{:.2f}'.format(1/(1+math.e**-n)))
class Neural():
    def __init__(self,other=[]):
        self.conn=other
        self.b=0#r.randint(0,3)
        self.weight=r.randint(1,9)/10
        self.act=0;
    def calc_act(self):
        ct=0
        if not self.conn:
            return
        for n in self.conn:
            ct+=n.act*n.weight
        self.act=sigmoid(ct+self.b)
        return self.act
    def back(self):
        pass
    def __str__(self):
        return '{weight:'+str(self.weight)+',act:'+str(self.act)+',b:'+str(self.b)+'}'


class neurals:
    def __init__(self,gen_nums):
        self.network=[]
        tmp=[]
        layer=0
        #this is the gen fist layer
        for dd in range(0,gen_nums[0]):
            tmp.append(Neural())
        self.network.append(tmp)
        print(tmp)
        #clean
        tmp=[]
        for d in gen_nums[1:]:
            for n in range(0,d):
                tmp.append(Neural([*self.network[layer-1]]))#[self.network[layer][i] for i in range(0,len(self.network[layer-1]))]
            self.network.append(tmp)
            tmp=[]
            layer+=1
    
    def run(self,data):
        c=0
        for i in self.network[0]:
            self.network[0][c].act=data[c]
            c+=1
        for i in self.network[1:]:
            for d in i:
                d.calc_act()
    
    
n=neurals([2,1])
n.network[0][0].weight=1
n.network[0][1].weight=-1
n.run([1,3])
print(n.network[0][0])
print(n.network[0][1])
print(n.network[1][0])