"""

数组初始化 操作参考代码

"""
import  numpy as np
import pandas as pd

# 初始化 table   以0初始化

print("000-------------");
ACTIONS = ['left', 'right']
N_STATES = 20

table =  pd.DataFrame(
        np.zeros((N_STATES, len(ACTIONS))),     # q_table initial values
        columns=ACTIONS,    # actions's name
    )
print(table)


# 生成0-1之间的平均分布的随机数据


print("001-------------")
rarray=np.random.random(size=10)
rarray_t=np.random.uniform(-0.1,0.1,size=10)  #生成-0.1 到0.1之间的随机数组
print(rarray)
print(rarray_t)

rand = np.random.randint(0,4,(3,8))
print(rand)

rand_t = np.random.randint(0,4,size=10)
print(rand_t)

rand_l = np.random.randint(5,8,size=6)

print(rand_l)
#  print(rand_t+rand_l)


for i in range(2):
    print (i)
