#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:37:11 2024

@author: asma
"""

#we are going to devolop a game called jumbled word
import random

def choose():
    word=['asma','anjana','milajoseph','computer','rainbow']
    pick=random.choice(word)
    return pick

def jumbled(words):
    jumble="".join(random.sample(words,len(words)))
    return jumble

def thanks(point1,point2,p1name,p2name):
    print('player 1',p1name,'your score is :',point1,'see you soon buddy')
    print('player 2',p2name,'your score is :',point2,'see you soon buddy')
    
    
    

def play():
    p1name=input('player 1 : Enter your name :')
    p2name=input('player 2 : Enter your name :')
    point1=0
    point2=0
    turn=0
    while(1):
        picked_one=choose()
        question=jumbled(picked_one)
        print(question)
        if turn%2==0:
            print(p1name,'your turn ')
            ans=input('bro what is on your mind ? ')
            if ans==picked_one:
                point1=point1+1
                print('ha ha hurre you got it buddy')
                print('your score is :',point1)
            else:
                print('oops buddy ,its wrong answer ,i thought : ',picked_one)
            c=input('if you want to play with me again print 1 :')
            if c=='0':
                print('ok see you soon !!!!')
                thanks(point1,point2,p1name,p2name)
                break
        else:
            print(p2name,'your turn ')
            ans=input('bro what is in your mind ??')
            if ans==picked_one:
                point2=point2+1
                print('hip hip hurre you got it !!')
                print('your score :',point2)
            else:
                print('oops buddy ,its wrong answer ,i thought : ',picked_one)
                c=input('if you want to play with me again print 1 :')
                if c=='0':
                    print('ok see you soon !!!!')
                    thanks(point1,point2,p1name,p2name)
                    break
        turn=turn+1
        
play()