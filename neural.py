import random as r
import math,sys
import pygame as pg
from pygame.locals import *
# the action funtion
def sigmoid(x):
    return float('{:.2f}'.format(x if x>0 else 0.01*(math.e**x-1)))
class neuron():
    def add_weight(self,neur,num):
        self.weight.update({neur:num})
    def get_weight(self,neur):
        return self.weight[neur]
    def set_weight(self,neur,num):
        self.add_weight(neur,num)
    def calc_weight(self,neur,num):
        self.set_weight(neur,self.get_weight(neur)+num)
    def __init__(self,other=[]):
        self.conn=other
        self.b=0#r.randint(0,3)
        # init weight
        self.weight={}
        # the weight is connect weight
        for n in self.conn:
            
            self.add_weight(n,r.randint(-10,10)/10)
        self.act=0;
    def calc_act(self):
        ct=0
        if not self.conn:
            return
        for n in self.conn:
            ct+=n.act*self.get_weight(n)
        self.act=sigmoid(ct+self.b)
        return self.act
    def back(self,dream):# 未完成，正在施工
        # haha!
        ret=[]
        bigs=[]
        actsum=0
        temp=[]
        # -------------------#
        cost=(dream-self.act)**2
        rund=0.01
        # if is the first layer
        if not self.conn:
            return []
        # calc pingjunzhi
        for neu in self.conn:
            actsum+=neu.act
        # start!!
        actsum/=len(self.conn)
        for neu in self.conn:
            if neu.act>=actsum:
                temp.append(neu)
                # calc
                noww=self.get_weight(neu)
                zw=neu.act
                az=self.act*noww
                ca=2*(zw)
                cw=zw*az*ca
                temp.append(cw)
            ret.append(temp)
            temp=[]
        return ret
        
    def __str__(self):
        return '{weight:'+str(self.weight)+',act:'+str(self.act)+',b:'+str(self.b)+'}'


class neuwork:
    def __init__(self,gen_nums):
        self.network=[]
        tmp=[]
        layer=1
        # this is the gen fist layer
        for dd in range(0,gen_nums[0]):
            tmp.append(neuron())
        self.network.append(tmp)
        print(tmp)
        # clean
        tmp=[]
        for d in gen_nums[1:]:
            for n in range(0,d):
                tmp.append(neuron([*self.network[layer-1]]))#[self.network[layer][i] for i in range(0,len(self.network[layer-1]))]
            self.network.append(tmp)
            tmp=[]
            layer+=1
    
    def run(self,data):# run the network
        c=0
        for i in self.network[0]:
            self.network[0][c].act=data[c]
            c+=1
        for i in self.network[1:]:# start!!
            for d in i:
                d.calc_act()
    def back(self,data):
        '''炒鸡无敌反向传播'''
        t=[]
        down=data
        i=0
        thislayer=len(self.network)
        for layer in self.network[:0:-1]:
            for neur in layer:
                t.append(neur.back(down[i])[0])
                i+=1
            i=0
            # change
            for neur in layer:
                for y in range(0,len(neur.weight)):
                    sum=0
                    for s in range(0,len(t)):
                        sum+=t[y][1]
                    for downn in self.network[thislayer-2]:
                        print(downn)
                        neur.calc_weight(downn,-sum)
                    
            t=[]
            thislayer-=1

class neural_vis:
    def __init__(self,net):
        pg.init()
        self.net=net
        window=(600,500)
        self.scr=pg.display.set_mode(window)
        pg.display.set_caption('这是标题')
    def sig(self,num):
        return float('{:.2f}'.format(1/(1+math.e**-num)))
    def draw(self):
        cx=50
        cy=50
        last_cx=cx
        last_cy=cy
        last_layer=[]
        for layer in self.net.network:
            for neu in layer:
                pg.draw.circle(self.scr,(0,self.sig(neu.act)*255,0),(cx,cy),10,10)
                if not last_layer:
                    cy+=30
                    continue
                else:
                    for n in last_layer:
                        pass
                        #pg.draw.line(self.scr,(self.sig(neu.get_weight(n))*255,0,0),(cx,cy),(last_cx,last_cy),2)
                cy+=30
            last_layer=layer.copy()
            cy=50
            cx+=30
            last_cx=50
            last_cy=cy
    def mainloop(self):
        while True:
            for e in pg.event.get():
                if e.type==12:
                    sys.exit()
            keys=pg.key.get_pressed()
            if keys[K_r]:
                self.net.run([1,3,5,6,8,3,7,2,1,5])
            self.draw()
            pg.display.update()
            
#test code
n=neuwork([10,9,9,6,5])
print(n.network[2][0])
n.network[1][0].set_weight(n.network[0][0],10)
n.network[1][1].set_weight(n.network[0][0],-1)
v=neural_vis(n)
v.mainloop()
'''
n.run([1])
print(n.network[1][0])
print(n.network[1][1])
print(n.network[0][0])
print()
n.back([0,1])
print(n.network[1][0])
print(n.network[1][1])
print(n.network[0][0])
print()
n.run([1])
print(n.network[1][0])
print(n.network[1][1])
print(n.network[0][0])
'''
