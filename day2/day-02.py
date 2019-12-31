# -*-coding: UTF-8 -*-
from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston

if __name__ == '__main__':
    li = load_iris()
    print("获取特征值")
    print(li.data)
    print("目标值")
    print("----------------------------target---------------------------")
    print(li.target)
    print("--------------------------------descr------------------------")
    print(li.DESCR)
    print("-----------------------------fetch_20newsgroups----------------------------------")
    news = fetch_20newsgroups(subset='all')

    print(news.data)
    print(news.target)
    lb = load_boston()

    print("获取特征值")
    print(lb.data)
    print("目标值")
    print(lb.target)
    print(lb.DESCR)