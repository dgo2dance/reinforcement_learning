"""
入口类
"""

import matplotlib.pyplot as plt
from gaPopulation import Population

if __name__ == "__main__":

    maxgenerations = 150 # 最大进化代数
    populationsize =150  # 种群大小，含有多少个个体
    chromosomesize = 30  #染色体中 基因个数， 一个染色体含有多少基因
    genesize = 7 #基因大小，一个基因中含有多少数据位
    tournamentsize =20 #锦标赛策略选择个数
    mutation_rate =0.07
    require_a=[9,8,9,8,9,10,10]
    require_p=[6,5,6,5,7,7,7]
    require_n=[4,3,3,3,4,7,7]

    file_name="TEST"

    pop = Population(populationsize,chromosomesize,genesize,require_a,require_p,require_n,mutation_rate)


    #初始化种群
    pop.initPopulation()

    print(pop)
    summary = []
    for i in range(maxgenerations):
        print('Generation', i, '\n', pop)

        summary.append(pop.pop_summary())
        parents = []
        """
        for _ in range(int(params.get('pop_size') / 2)):
            pars = pop.select_parents(params.get('tournament_size'))
            parents.append(pars)
        """

        """
        Tournament Selection  锦标赛策略

        由于算法执行的效率以及易实现的的特点，锦标赛选择算法是遗传算法中最流行的选择策略
        
        我们再整个种群中抽取n个个体，让他们进行竞争(锦标赛)，抽取其中的最优的个体。参加锦标赛的个体个数成为tournament size。通常当n=2便是最常使用的大小，
        也称作Binary Tournament Selection.
    
        """
        for _ in range(int(populationsize)):
            par = pop.select_parent(tournamentsize)
            print("par")
            print(par)
            parents.append(par)

        children = pop.recombine(parents, single=True)
        pop.mutate_children(children)
        print("------------")
        print(pop.pop)
        print(children)
        mating_pool = pop.pop.copy()
        print("2222")
        print(mating_pool)

        mating_pool += children
        #for s in range(len(children)):
        #    mating_pool.append(children[s])
        #mating_pool = mating_pool.extend(children)
        #print("mating_pool")
        #print(mating_pool)
        pop.pop = pop.survivor_select(mating_pool)

    print('Final Population:', pop)


    """Creating the summaries for graph.
    """
    best_vals = [s[0] for s in summary]
    avg_vals = [s[1] for s in summary]
    worst_vals = [s[2] for s in summary]

    """Plotting the graph
    """
    range_ = range(0, maxgenerations)
    plt.plot(range_, best_vals, 'go--', label='Best')
    plt.plot(range_, avg_vals, 'rs--', label='Average')
    plt.plot(range_, worst_vals, 'bo--', label='Worst')
    plt.grid()
    plt.legend(loc='lower right')
    plt.xlabel('Iteration')
    plt.ylabel('Fitness')
    title = 'Fitness values for '
    title += str(maxgenerations)
    plt.title(title)
    fig = plt.gcf()
    fig.canvas.set_window_title(file_name)
    plt.show()