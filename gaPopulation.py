"""

种群迭代   进化

"""

import  numpy as np
import pandas as pd
from gaChromesome import  Chromesome
from gaGene import Gene
from math import ceil



class Population:


    def __init__(self,populationsize,chromesomesize,genesize,require_a,require_p,require_n,mutation_rate):

        self.populationsize=populationsize
        self.chromesomesize=chromesomesize
        self.genesize=genesize
        self.mutation_rate=mutation_rate

        self.random_counter = 0
        self.random_number_array=[0.06,0.32,0.87,0.02,0.15,0.47,0.36,0.53,0.32,0.39,0.39,0.26,0.27,0.21,0.73,0.42,0.69,0.32,0.3]

        # 各个班次对护士的需求量
        self.require_a=require_a
        self.require_p=require_p
        self.require_n=require_n

        self.pop=[]


    #初始化种群
    def  initPopulation(self):
        #生成第一代 种群，
        for _ in range(self.populationsize):

            tmp_chromesome = Chromesome(self.chromesomesize,self.genesize,self.require_a,self.require_p,self.require_n)
            tmp_chromesome.initialize_chromesome()
            tmp_chromesome.getfitness()
            self.pop.append(tmp_chromesome)





    def select_parents(self, tournament_size):
        """Selects and returns two parents from pool.

        Keyword arguments:
        tournament_size -- Integer size of the pool.

        选择  进入交配池

        1.
        在一定编码方案下，随机产生一个初始群组
        用相应的编码方法，将编码后的个体转换成问题空间的决策变量，并求出个体的适应值
        按照一定选择方式（即适者生存的原则），从中选择部分个体构成交配池
        由交叉和变异这两个遗传算子对交配池中随机两两配对的个体进行操作，并形成新一代的种群
        从所有的目前现存的父代与子代中选取最为优良的某些个体作为新的父代，反复执行步骤2
        ~4，使之逐代进化，直至满足收敛判断依据

        """
        pool = self.create_pool(tournament_size)
        pool.sort(key = lambda x: x.fitness(), reverse=True)
        return (pool[0], pool[1])


    def select_parent(self, tournament_size):
        """Selects and returns a parent from pool.

        Keyword arguments:
        tournament_size -- Integer size of the pool.
        """
        pool = self.create_pool(tournament_size)
        pool.sort(key = lambda x: x.getfitness(), reverse=True)
        return pool[0]


    def create_pool(self, tournament_size):
        """Creates and returns a pool from random Dna objects for tournament selection algorithm.

        Keyword arguments:
        tournament_size -- Integer size of the pool.
        """
        pool = []
        for _ in range(tournament_size):
            pool.append(self.pop[self.get_index_by_random(self.populationsize)])
        return pool

    def get_index_by_random(self, array_len):
        """Calculates and returns the index of random element using random list.

        Keyword arguments:
        array_len -- Element number of the list.
        """
        return (ceil(array_len * self.get_next_random()) - 1)

    def get_next_random(self):
        """Returns next random number from the random list.
        """
        randm = self.random_number_array[self.random_counter]
        self.increase_counter()
        return randm

    def increase_counter(self):
        """Increases the counter for random list.
        Sets counter the zero to not get index out of bounds.
        """
        self.random_counter += 1
        if self.random_counter == len(self.random_number_array):
            self.random_counter = 0


    #交叉
    def crossover(self, parent1, parent2, crossover_point):
        """Applies one point crossover operation to between two Dna objects.
        Returns the results of the crossover by two Dna object.

        Keyword Arguments:
        parent1 -- Dna object that represents firs parent of crossover.
        parent2 -- Dna object that represents second parent of crossover.
        crossover_point -- Integer index of the crossover point.
        """
        crossover_point += 1
        print('Applying Crossover:\t at', crossover_point)
        print('Parents: ', (parent1, parent2))

        child1 = Chromesome(self.chromesomesize,self.genesize,self.require_a,self.require_p,self.require_n)
        child2 = Chromesome(self.chromesomesize,self.genesize,self.require_a,self.require_p,self.require_n)
        for i in range(self.chromesomesize):
            print(parent1.chromesome[i].dna[:crossover_point])
            print(parent2.chromesome[i].dna[crossover_point:])

            ch1 = np.array(list(parent1.chromesome[i].dna[:crossover_point])+list(parent2.chromesome[i].dna[crossover_point:]))

            print("ch1")
            print(ch1)
            ch2 = np.array(list(parent2.chromesome[i].dna[:crossover_point].flatten()) + list(parent1.chromesome[i].dna[crossover_point:].flatten()))
            print("ch2")
            print(ch2)
            dna1 = Gene()
            dna1.set(ch1)
            dna2 = Gene()
            dna2.set(ch2)
            child1.set(dna1,i)
            child2.set(dna2,i)
        return child1, child2


    def recombine(self, parents, single=False):
        """Applies crossover to each parent duo from the list.
        Returns the childen list.

        Keyword arguments:
        parents -- List of Dna objects that represents parents.
        single -- Represents if parent list contains single parents or zipped two parents tuples.
        """
        if single:
            #  dna_len = len(parents[0].bits)
            children = []
            for i in range(0, len(parents), 2):
                p1 = parents[i]
                if (i + 1) >= len(parents):
                    p2 = parents[0]
                else:
                    p2 = parents[i + 1]
                #crossover_point = self.get_index_by_random(self.genesize-1)

                crossover_point =np.random.randint(0, 7)
                child1, child2 = self.crossover(p1, p2, crossover_point)
                children.append(child1)
                children.append(child2)
            return children
        else:
            #dna_len = len(parents[0][0].bits)
            children = []
            for p1, p2 in parents:
                # crossover_point = self.get_index_by_random(self.genesize-1)
                crossover_point = np.random.randint(0, 7)
                child1, child2 = self.crossover(p1, p2, crossover_point)
                children.append(child1)
                children.append(child2)
            return children



    #变异
    def mutate_children(self, children, mutation_rate=None):
        """Applies mutation operation the giving list of chromesome objects.

        Keyword arguemnts:
        children -- List of Dna objects reprents children to get mutated.
        """
        mutation_rate = mutation_rate if mutation_rate is not None else self.mutation_rate
        print('Applying mutation to:', children)
        for child in children:
            self.mutate_individual(child)

        print('Mutated offspring:', children)

    def mutate_individual(self, individual):
        """Applies mutation operation the giving individual chormesome object.

        Keyword arguments:
        individual -- Single Dna object that will get mutated.
        """
        mutation_rate = self.mutation_rate

        for i in range(self.chromesomesize):
            for j in range(self.genesize):
                if self.get_next_random() <= mutation_rate:
                    individual.chromesome[i].dna[j] =np.random.randint(0, 4)





    def survivor_select(self, mating_pool):
        """Eliminates the worse Dna objects by their fitness value.

        Keyword arguemnts:
        mating_pool -- Pool of all Dna objets.
        """
        sorted_pool = sorted(mating_pool, key=lambda x: x.getfitness(), reverse=True)
        return sorted_pool[:self.populationsize]

    def pop_summary(self):
        """Keeps track of populations numbers.
        Returns best Dna's fitness, average fitness and worst Dna's fitness value of the population.
        """
        best_individual = max(self.pop, key=lambda x: x.getfitness())
        worst_individual = min(self.pop, key=lambda x: x.getfitness())
        avg_fitness = sum(i.getfitness() for i in self.pop) / float(len(self.pop))

        return (best_individual.getfitness(), avg_fitness, worst_individual.getfitness())


    def __str__(self):
        return str(self.pop)

    def __repr__(self):
        return str(self)


