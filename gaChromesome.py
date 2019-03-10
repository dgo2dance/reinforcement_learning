
"""
染色体
有多个dna构成
"""

import  numpy as np
import pandas as pd
from gaGene import Gene


class Chromesome:

    def __init__(self,chromesomesize,genesize,require_a,require_p,require_n):

        self.chromesomesize=chromesomesize
        self.genesize=genesize
        # 各个班次对人员的需求量
        self.require_a = require_a
        self.require_p = require_p
        self.require_n = require_n
        self.chromesome =[]
        self.cost=[3,4,4,2]

    # 初始化染色体,有多个基因构成
    def initialize_chromesome(self):
        for _ in range(self.chromesomesize):
            tmp_gene = Gene()
            self.chromesome.append(tmp_gene)


    # 计算适应度
    def getfitness(self):
        fit = 0
        actual_a=[]
        actual_p=[]
        actual_n=[]

        for j in range(self.genesize):
            a_num = 0
            p_num = 0
            n_num = 0
            for i in range(self.chromesomesize):
              # print(self.chromesome[i])
              if(self.chromesome[i].dna[j]==0):
                a_num+=1
              elif(self.chromesome[i].dna[j]==1):
                p_num+=1
              elif(self.chromesome[i].dna[j]==2):
                n_num+=1
            actual_a.append(a_num)
            actual_p.append(p_num)
            actual_n.append(n_num)
        print("actual_a:")
        print(actual_a)
        print("actual_p:")
        print(actual_p)
        print("actual_n:")
        print(actual_n)
        sum_a=self.calcuteSquare(self.require_a,actual_a)
        sum_p=self.calcuteSquare(self.require_p,actual_p)
        sum_n=self.calcuteSquare(self.require_n,actual_n)
        self.fitness=sum_a+sum_p+sum_n
        print("fitness:")
        print(self.fitness)
        return self.fitness

    def calcuteSquare(self,a,b):
        sum=0
        for i in range(len(a)):
            sum+=(a[i]-b[i])**2
        return sum

    def set(self,dna,i):
        print("iiiiiii")
        print(i)
        print(dna)
        self.chromesome.append(dna)


    def __str__(self):
        return str(self.chromesome)

    def __repr__(self):
        return str(self)