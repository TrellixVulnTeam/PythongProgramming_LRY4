#coding:cp949
#def sum_and_mul(a,b):
#    return a+b, a*b

#sum, mul  = sum_and_mul(10,30)
#print(sum,mul)
#-------------

#def printData(data):
#    for item in data:
#        if isinstance(item,list): #item�� list�̸�
#            for items in item:
#                print(items)
#        else:
#            print(item)

#data = ["ȫ�浿",["���׶�","�ϻ�"],"��浿",["���׶�","��","��"],"��浿",["��","��","��"]]

#printData(data)
#-------------����Ʈ�ȿ� ����Ʈ�ȿ� ����Ʈ�� ���ִ� ��� ���� ������ ����Լ��� ����
#�Լ����ڿ� �鿩���� �� Ƚ���� �־���
#def printData(data,level=0):
#    for item in data:
#        if isinstance(item,list): #item�� list�̸�
#            printData(item,level+1)
#        else:
#            for i in range(level):
#                print('\t',end='')
#            print(item)

#data = ["ȫ�浿",["���׶�",["���¿�","Ȳ����","������"]],"��浿",["���׶�","��","��"],"��浿",["��","��","��"]]

#printData(data)
#--------------------������� �����ϵ��� printData�Լ��� ���� ���Ϸ� ���� ���⼭�� import�ؼ� ��
#import printData #printData: ����̸�

#data = ["ȫ�浿",["���׶�",["���¿�","Ȳ����","������"]],"��浿",["���׶�","��","��"],"��浿",["��","��","��"]]
#printData.printData(data)#����̸�, �Լ��̸� ���� ��
#---------------
#import os

#help(os.mkdir)
import os

print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
#print(os.getcwd())
#os.system("python setup.py sdist")
os.system("python setup.py install")