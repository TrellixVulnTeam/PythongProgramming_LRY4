#class  Terran:
#    def __init__(self, name):
#        self.name = name

#class Tank(Terran):
#    def __init__(self,name,damage):
#        super().__init__(self, name)
#        self.damage = damage

#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(self, name)
#        self.hp = hp

#t1 = Tank("tank",0)
#t2 = Marine("marine",100)

#------------------TerranŬ������ �߻�Ŭ������ ������
#Terran���κ��� �Ļ��� �ֵ����״� ���� ����� �ְ� ����. �׷� �θ�Ŭ������ �־������ ��
#Terran�� body�� ������ �� ����. �׶� abstract�޼ҵ�� �����ϸ� ��
#from abc import ABCMeta, abstractmethod
#class Terran(metaclass=ABCMeta):#class�� ���� �ΰ����� ���� �־���. metaclass�� ���� ������ ABCMeta��� 
#    def __init__(self, name):
#        self.name = name

#    @abstractmethod
#    def attack(self):
#        pass

#class Tank(Terran):
#    def __init__(self,name,damage):
#        super().__init__(name)
#        self.damage = damage

#    def attack(self):
#        print("��ũ�� ���ϴ�")
#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(name)
#        self.hp = hp

#    def attack(self):
#        print("���� ���ϴ�")

#def Attack(terran):
#    terran.attck()

#t1 = Tank("tank",0)
#t2 = Marine("marine",100)

#tlist = [Tank("tank1",0),Marine("marine1",100)]
#for item in tlist:
#    Attack(item)
#Attack(t1)
#Attack(t2)
#-------------
#class MyList(list):#list�κ��� �Ļ��Ǿ��� Ŭ������ ����� ����
#    name=""
#    def __init__(self, name):#����Ʈ��ɵ� ������ �ְ� �̸��� �ִ°� ��������
#        super().__init__([])#�� ����Ʈ �ϳ� ��������
#        self.name = name

#list1=MyList("greenjoa")
#list1.append(10)#list�� �߰���Ű�°�
#list1.append(50)
#list1.append(60)
#list1.append(80)
#list1.append(100)
#print(list1)#�̸��� ���� ����� �Ǿ����� �������� ������ �����Ǹ� ���ؼ� �ذ��� �� ����
#print(dir(list1))#����Ʈ�� �ִ� ��ɵ� �� �� ���� list���� ���� �� �ִ� ������� ǥ������
#                    #����Ʈ�� ������ name�ۿ� ����. name�̶�� ����� �߰��� �Ǿ�������.

#------------------print�Ҷ� ����ϴ°� string�Լ��� ���ؼ� ����� ��. string�Լ��� ������ �Ұ���.
class MyList(list):#list�κ��� �Ļ��Ǿ��� Ŭ������ ����� ����
    name=""
    def __init__(self, name):#����Ʈ��ɵ� ������ �ְ� �̸��� �ִ°� ��������
        super().__init__([])#�� ����Ʈ �ϳ� ��������
        self.name = name
    def __str__(self):
        return self.name+":"+super().__str__()#list�� str�Լ��� ȣ���. 

list1=MyList("greenjoa")
list1.append(10)#list�� �߰���Ű�°�
list1.append(50)
list1.append(60)
list1.append(80)
list1.append(100)
print(list1)#�̸��� ���� ����� �Ǿ����� �������� ������ �����Ǹ� ���ؼ� �ذ��� �� ����

