# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:20:01 2023

@author: crown
"""
## 함수 선언부
def add_fuc(n1,n2):
    return n1 + n2

def sub_fuc(n1,n2):
    return n1 - n2

def mul_fuc(n1,n2):
    return n1 * n2

## 전역 변수부
num1, num2, res = 100,200,0

## 메인 코드부
res = add_fuc(num1,num2)
print(num1,"+",num2,'=',res)

res = sub_fuc(num1,num2)
print(num1,"-",num2,'=',res)

res = sub_fuc(num1,num2)
print(num1,"*",num2,'=',res)