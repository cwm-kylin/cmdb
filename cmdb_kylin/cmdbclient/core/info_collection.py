#_*_coding:utf-8_*_
__author__ = 'kylin'

from plugins import plugin_api
import json,platform,sys

"""
资产信息收集类
"""
class InfoCollection(object):
    def __init__(self):
        pass

    """
    获取平台信息
    """
    def get_platform(self):

        os_platform = platform.system()

        return os_platform

    """
    资产类收集方法：数据收集前先判断平台是windows还是linux，其它平台不支持，并做异常处理。通过相关平台API插件收集系统信息。
    """
    def collect(self):
        os_platform = self.get_platform()
        try:
            func = getattr(self,os_platform)
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError,e:
            sys.exit("Error:MadKing doens't support os [%s]! " % os_platform)

    """
    linux平台收集方式：调用linux平台API插件
    """
    def Linux(self):
        sys_info = plugin_api.LinuxSysInfo()

        return sys_info


    """
    windows平台收集方式：调用windows平台API插件
    """
    def Windows(self):
        sys_info = plugin_api.WindowsSysInfo()
        print sys_info
        #f = file('data_tmp.txt','wb')
        #f.write(json.dumps(sys_info))
        #f.close()
        return sys_info


    """
    生成汇报数据
    """
    def build_report_data(self,data):

        #add token info in here before send

        return data
