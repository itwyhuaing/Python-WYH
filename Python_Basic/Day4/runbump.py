# encoding:utf-8
import os
import time


def fmain():
    print('11')
    content = '0123456789A___'
    while True:
        # 清理屏幕上的输出
        os.system('clear') # os.system('cls')
        print(content)
        # 休眠200毫秒
        time.sleep(.1)
        content = content[1:] + content[0]


if __name__ == '__main__':
    print('00')
    fmain()
