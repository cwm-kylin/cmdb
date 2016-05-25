#_*_coding:utf-8_*_
__author__ = 'kylin'
import os,sys,platform
# linux，windows平台检查，将程序路径添加到环境变量中
if platform.system() == "Windows":
    #如果是winodes平台，获取当前程序文件路径，
    BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
else:
    #如果是linux平台，获取当前程序文件路径，
    BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])

#将程序路径加入到系统环境变量中
sys.path.append(BASE_DIR)

#从内核中HouseStark导入模块，将用户输入参数传入HouseStark模块中ArgvHandler类
from core import HouseStark

if __name__ == '__main__':

    HouseStark.ArgvHandler(sys.argv)