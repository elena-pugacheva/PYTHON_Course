# СПИСКИ.
list_1 = []
list_1=list()
print(list_1)
list_1=[1, 2, 3, 8]
print(*list_1)     

# звездочка убирает скобки

for i in list_1:
    print(i)

# кажды элемент списка с новой строки

print(len(list_1)) 
# сколько элементов в списке

print(list_1[-2]) 
# нумерация с конца если -

list_1.append(8) 
print(list_1)
# добавить элемент в конец списка

list_1=[]
print(list_1)
for i in range(5):
    list_1.append(i)
    print (list_1)
# постепенное добавление элементов в список


list_1=[12, 7, -1, 21, 0]
print(list_1.pop())
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.pop())
print(list_1)

# удаление элемента
list_1=[12, 7, -1, 21, 0]
print(list_1.insert(2,11))
print(list_1)

# добавление элемента

# Кортежи
t=()
print(type(t))

t=(1, 5, 6, )
print(type(t))

v=[1,8,9]
print(type(v))

v=tuple(v)
print(v)
print(type(v))

a=1
b=2

a,b=1,2
a,b,c =v
print(a,b,c)

t=[1,2,3,5]
t[0]=2
print(t)
# замена элементов кортежа

# Словари
d={}
d=dict()
print(d)
d['q']='qwerty'
print(d['q'])

# Множества
colors={1,2,3,3,5,}
print(colors)

colors.add(8)
print(colors)
# добавить

colors.remove(3)
print(colors)
# удалить

colors.discard(3)
print(colors)
# проврить и удалить

colors.clear()
print(colors)
# очистить множество

a={1,2,3,5,8}
b={2,5,8,13,21}
c=a.copy()
print(c)
# копировать

u=a.union(b)
print(u)
# объединить два множества

i=a.intersection(b)
print(i)
# выделить несовпадения

d1=a.difference(b)
print(d1)
# разность

d2=b.difference(a)
print(d2)
# разность

a={1,8,6}
b=frozenset(a)
print(b)
# замороженое множество

# генератор списков

list1 = [3 for item in range(5)]
print(list1)

list1 = [i for i in range(1,10) if i%2==0]
print(list1)




