# encoding:utf-8

import random
def generate_code(codelen):
    allcnt  = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_pos = len(allcnt) - 1
    rlt     = ''
    for _ in range(0,codelen):
        idx = random.randint(0,max_pos)
        rlt += allcnt[idx]
    print('random code:')
    print(rlt)

if __name__ == '__main__':
    generate_code(6)
