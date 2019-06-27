# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/3/21 8:07 PM'
"""
强化学习用到的小例子。使用Q-learning的例子进行处理
在一条直线上，右边的是宝藏，左边是人，当在右边获得宝藏的时候，会记录宝藏的位置，并最终提高找到宝藏的概率。

Q-learning 是一种记录行为值 (Q value) 的方法, 每种在一定状态的行为都会有一个值 Q(s, a), 就是说 行为 a 在 s 状态的值是 Q(s, a).
 s 在上面的探索者游戏中, 就是 o 所在的地点了. 而每一个地点探索者都能做出两个行为 left/right, 这就是探索者的所有可行的 a 啦.

如果在某个地点 s1, 探索者计算了他能有的两个行为, a1/a2=left/right, 计算结果是 Q(s1, a1) > Q(s1, a2), 
那么探索者就会选择 left 这个行为. 这就是 Q learning 的行为选择简单规则.
"""
import time

import numpy as np
import pandas as pd

np.random.seed(2)

N_STATES = 6 # 直线的长度
ACTIONS = ['left','right']
EPSILON = 0.9 # greedy policy
ALPHA = 0.1 # learning rate
GAMMA = 0.9 # discount factor
MAX_EPISODES = 13 # 最大回合数
FRESH_TIME = 0.3 # fresh time for one move

def build_q_table(n_states, actions):
    """
    :param n_states: 地点或者状态 
    :param actions: 采取的行为
    :return: 
    """
    table = pd.DataFrame(np.zeros((n_states,len(actions))),columns=actions)
    return table

def choose_action(state, q_table):
    # 选择action
    state_actions = q_table.iloc[state,:] # 选出station中的所有的action值
    if(np.random.uniform() > EPSILON) or ((state_actions.all() == 0)):
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.idxmax()
    return action_name


def get_env_feedback(S,A):
    # agent 和客户端进行交互
    if A == 'right':
        if S == N_STATES - 2: # 中断
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:
        R = 0
        if S == 0:
            S_ = S  # reach the wall
        else:
            S_ = S - 1
    return S_, R

def update_env(S, episode, step_counter):
    # 更新环境
    env_list = ['-']*(N_STATES-1) + ['T']  # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode : total_steps = {}'.format(episode+1,step_counter)
        print('\r{}'.format(interaction),end="")
        time.sleep(2)
        print('\r',end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction),end='')
        time.sleep(FRESH_TIME)

def rl():
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:
            A = choose_action(S,q_table)
            S_, R = get_env_feedback(S,A) # 采取措施并获得下一个状态和奖励
            q_predict = q_table.loc[S,A]
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_,:].max()
            else:
                q_target = R
                is_terminated =True

            q_table.loc[S,A] += ALPHA *(q_target - q_predict) # 更新
            S = S_ # 移动到下一个状态

            update_env(S, episode,step_counter+1)
    return q_table

if __name__ == "__main__":
    q_table = rl()
    print('/r')
    print(q_table)


