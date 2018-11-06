#!/usr/bin/env python3
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)
print(list1[1])
list1.extend(['juniper','ciena'])
print(list1)
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)
print("first of second list is: " + list1[5][0] + " and third of the second list is: " + list1[5][2]) 
print(list1[5][1])
list2 = ['fox', 'ant', 'bee','cat','dog']
print(list2)
