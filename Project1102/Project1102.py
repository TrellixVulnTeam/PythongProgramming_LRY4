﻿from bs4 import BeautifulSoup
import html.parser
#f = open('test.xml')
#xml = f.read()
#soup = BeautifulSoup(xml,"html.parser")
#for node in soup.findAll('node'):
#    print("Node:"+node.string)
#    print("Attr1:"+node['attr1'])
#------
#f = open('song.xml',encoding='utf-8')
#xml = f.read()
#soup = BeautifulSoup(xml,"html.parser")
#for nodes in soup.test('song'):
#    for node in nodes:
#        print(node.string)
##=-------
#f = open('alcohol.xml',encoding='utf-8')
#xml = f.read()
#soup = BeautifulSoup(xml,"html.parser")
#for nodes in soup.alcohol('cate1'):
#    if(nodes['tt']=='안주'):
#        print('Cate1:'+nodes['tt'])
#    for node in nodes('cate2'):
#        print('\tCate2:'+node['tt'])
#        for item in node('item'):
#            print('\w\w'+item.string)
#-------
#import json
#data={1:'a',2:'b'}
#data2 = json.dumps(data)
#data3 = json.loads(data2)
#print(type(data2))
#print(type(data3))
#data = {1:'우리',2:'나라'}
#data2 = json.dumps(data,ensure_ascii=False)
#print(data2)
#------
#import json
#s= """
#{
#"name":"cybaek",
#"detail":{"last":"baek"},
#"emails":["cybaek@xxx.com","cybaek@yyy.com"]
#}
#"""
#data = json.loads(s)
#print(data['name'])#cybaek
#print(data['detail'])#('last':'baek')
#print(data['detail']['last'])#baek
#-----
import json
s= """
{
    "name":"cybaek"
    "detail":{"last":"baek"},
    "emails":["cybaek@xxx.com","cybaek@yyy.com"]
}
"""
class JsonObject:
    def __init__(self,d):
        self.__dict__=d
    data = json.loads(s,object_hook=JsonObject)
print(data.name)
print(data.detail)
print(data.detail.last)
for email in data.emails:
    print(email)
