import os
import socket
import json
import yaml


"""使用python中的os模块测试目标ip网络是否可达，返回Trun或False"""
def ping_network(network_ip):
    #result = os.system("ping %s -w 3 -c 3" % (network_ip))     #在windows下不适用，-c 参数被封；
    result = os.system("ping %s -w 3" % (network_ip))
    if result == 0:
        print("本机至 %s 网络通畅;" % (network_ip))
        return True
    else:
        print("本机至 %s 网络不通;" % (network_ip))
        return False


"""使用python中的socket模块检测ip的端口是否开通"""
def socket_port(network_ip, port):
    # global socket_port_number  # 定义一个全局参数，返回ip目标端口的连通性：0 为连通，1 为阻塞；

    print("正在检测目标ip端口......别慌，稍作等待......")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    try:
        s.connect((network_ip, int(port)))
        s.shutdown(2)
        socket_port_number = 0
    except:
        socket_port_number = 1
        pass
    if socket_port_number == 0:
        print("检测 %s %s 端口[正常]." % (network_ip, port))
        return True
    else:
        print("检测 %s %s 端口[关闭]." % (network_ip, port))
        return False


"""判断文件是否存在，进行json、yaml格式的解析"""
#用法：在 file_format_analysis() 内传入参数，file_path为文件的绝对路径，format为[json、yaml]两个字段。
def file_format_analysis(file_path,format):     #format只能为 json、yaml。
    if os.path.exists(file_path) == True:
        if format == "json":
            print("%s 文件存在，进行json解析。" % (file_path))
            with open(file_path, 'rb') as f:
                file_json = json.load(f)
            return file_json
        elif format == "yaml":
            print("%s 文件存在，进行yaml解析。" % (file_path))
            with open(file_path, 'rb') as files:
                file_yaml = yaml.load(files,Loader=yaml.FullLoader)
            return file_yaml
        else:
            print("%s 文件存在，只进行判断，不进行解析。" % (file_path))
            return True
    elif os.path.exists(file_path) == False:
        print("%s 文件不存在。" % (file_path))
        return False
    else:
        print("判断 %s 文件是否存在时出现异常。" % (file_path))
        exit()


#判断两个数组内的数据是否相同的，不相同的话输出不同的数据；
#返回一个字典---dic_list：
#   dic_lsit['list_same'] = ["两个数组交集"]
#   dic_lsit['list_different_a'] = ["list_a中不同的数值"]
#   dic_lsit['list_different_b'] = ["list_b中不同的数值"]
def list_contrast(list_a,list_b):
    if len(list_a) == 0 or len(list_b) == 0:    #判断传入的数字是否为空
        print("传入数组不可都为空")
        exit()

    list_1 = list_a[:]
    list_2 = list_b[:]
    dic_list = {}   #定义一个字典，里面存放：1、两个数组相同的数值；2、list_a数组不同的数值；3、list_b数组不同的数值；
    list_same = []    #定义一个列表，存储相同的数值
    for i in range(0,len(list_1)):  #在数据量相同的情况下，遍历一个数组，
        if list_1[i] in list_2:
            list_same.append(list_1[i])   #将相同的数值存储到一个列表中；
        else:
            pass
    dic_list['list_same'] = list_same   #将相同的数值存入字典；

    for i in range(0,len(list_same)):   #遍历存放两个数组交集的列表；
        list_1.remove(list_same[i])     #删除list_a中相同的数值，剩下不同的数值；
        list_2.remove(list_same[i])     #删除list_b中相同的数值，剩下不同的数值；
    dic_list['list_different_a'] = list_1   #将list_a中不同的数值存入字典
    dic_list['list_different_b'] = list_2   #将list_b中不同的数值存入字典

    return dic_list

"""判断两个字典内容的方法"""
#   dic_all["same"] = {两个字典的交集}
#   dic_all["diff_a"] = {第一个参数中不同的键值}
#   dic_all["diff_a"] = {第一个参数中不同的键值}
def dic_contrast(dic_a,dic_b):
    dic_all = {}
    dic_same = {}      #定义一个字典，存储两个字典中相同的键值；
    dic_diff_a = {}     #定义一个字典，存储第一个参数中不同的键值；
    dic_diff_b = {}     #定义一个字典，第一个参数中不同的键值；

    if len(dic_a) == 0 and len(dic_b) == 0:
        print("传入字典参数不可都为空")
        exit()

    if len(dic_a) >= len(dic_b):    #对比两个字典内的数量，遍历多的去和少的对比；
        for i in dic_a.keys():      #遍历dic_a的键；
            if i in dic_b.keys():   #如果dic_a中的键在dic_b中存在
                if dic_a[i] == dic_b[i]:    #则判断值是否相等；
                    dic_same[i] = dic_a[i]
                else:
                    dic_diff_a[i] = dic_a[i]
                    dic_diff_b[i] = dic_b[i]
            else:    #如果dic_a中的键在dic_b中不存在
                dic_diff_a[i] = dic_a[i]
    else:
        for i in dic_b.keys():      #遍历dic_b的键；
            if i in dic_a.keys():   #如果dic_b中的键在dic_a中存在
                if dic_b[i] == dic_a[i]:    #则判断值是否相等；
                    dic_same[i] = dic_b[i]
                else:
                    dic_diff_a[i] = dic_a[i]
                    dic_diff_b[i] = dic_b[i]
            else:       #如果dic_b中的键在dic_a中不存在
                dic_diff_b[i] = dic_b[i]

    dic_all["same"] = dic_same
    dic_all["diff_a"] = dic_diff_a
    dic_all["diff_b"] = dic_diff_b

    return dic_all

