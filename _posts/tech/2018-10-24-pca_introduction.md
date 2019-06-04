---
layout:     post
title:      "数据科学中的二向箔-主成分分析法原理及Python实现方法"
subtitle:   "谈谈对主成分分析法原理的一些理解"
date:       2018-08-10 16:20:45
author:     "soaringsoul"
header-img: "img/posts/pca_post_zoom.jpg"
catalog: true
tags:
    - 机器学习
---


# 1 引子
> 我看到了我的爱恋
> 
> 我飞到她的身边
> 
> 我捧出给她的礼物
> 
> 那是一小块凝固的时间
> 
> 时间上有美丽的条纹
> 
> 摸出来像浅海的泥一样柔软

> 她把时间涂满全身
> 
> 然后拉起我飞向存在的边缘
> 
> 这是灵态的飞行
> 
> 我们眼中的星星像幽灵
> 
> 星星眼中的我们也像幽灵                                                           
> 　　　　　　　　　　　　　　　　　　　　　　——《三体-死神永生》

读过《三体》的人应该都对这首歌谣印象深刻，在地球文明还在大力建造各种掩体各种战舰以期抵抗外星文明时，宇宙中的一个名为歌者文明的小清理员哼唱者这首歌谣，向太阳系随手丢出了一张二向箔，便对整个太阳系实施了降唯打击，于是，整个太阳系跌落成了一幅二维巨画。

今天，不是要谈《三体》，而是想谈谈对数据科学领域中的主成分分析法的一些个人理解。

那什么是主成分分析法呢，它又是用来做什么的呢？

在我看来，主成分分析法就是数据科学界的二向箔，它的主要作用就是数据降维。

# 2 主成分分析法的用途和原理
> 主成分分析法的全称是principal component analysis，简称PCA，是一种数学变换的方法。
> 它把给定的一组相关变量通过线性变换转成另一组不相关的变量，这些新的变量按照方差依次递减的顺序排列。
> 
> 在数学变换中保持变量的总方差不变，使第一变量具有最大的方差，称为第一主成分，第二变量的方差次大，并且和第一变量不相关，称为第二主成分。依次类推，I个变量就有I个主成分。


> 进行主成分分析后，还可以根据需要进一步利用K-L变换（霍特林变换）对原数据进行投影变换，达到降维的目的。
                                  ——《百度百科》

以上是百度百科对PCA的简介说明，PCA是Pearson在1901年提出的,再后来由hotelling在1933年加以发展提出的一种多变量的统计方法，目前已经被广泛应用于机器学习领域。PCA最主要的用途在于“数据降维”，它既可以通过析取主成分显出的最大的个别差异,也可以用来削减回归分析和聚类分析中变量的数目.

举个例子，假如你要对某银行的贷款用户进行分析，通过建立逻辑回归模型预测用户是否会按时还款，银行给我们提供了包括用户性别、年龄、婚姻状况、工龄、银行流水记录、信用卡账单记录、申贷金额、申请时间、放款时间等近20项指标，你可能觉着每项指标都很重要，可是如果同时对这近20个指标进行分析，又会过于繁琐，仅数据建模前的数据清理和数据转换就要花费很长时间，这个时间可能已经远超过了工作预期，这个时候你就可以采用主成分分析的方法对这20多个数据指标进行降维了。
通过主成分分析，我们可以根据这些指标间的相互关系将近20个分析指标降唯为5~6个主成分指标，甚至更少，这些主成分指标既涵盖了所有指标中的绝大部分信息,又让你的分析得到了简化。通过主成分分析，我们简化了数据分析过程上的数据转换过程、增加了结果精度，又保证了数据分析报告的按时完成。

关于PCA的数学原理及推导过程，我们不在这里赘述，感兴趣的可以自行去查阅相关的文献资料，PCA原理简单而言，即线性变换，在数据分析的应用层面上，就是将具有一定相关性的多个指标简化为一组线性不相关的综合主成分指标，转换后的这些主成分指标方差最大的为第一主成分。

![主成分分析法图解](https://upload-images.jianshu.io/upload_images/8579659-d3f24f2f844383df.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
上图是主成分分析法的简单图解，图中的点集是由一些二维变量构成，假如我们想把这些二维变量降为一维，理想情况下这个一维变量应该最大限度的包含原始二维变量的信息。一般而言，变量方差越大，变量的差异越大，所含的信息就越多，从这个角度出发，我们应该选择Y1方向，因为Y1方向的方差最大，离散程度最大，包含的信息量越大。


# 3 主成分分析法的Python实现
以下是主成分分析法的计算流程：
* 1 数据标准化/归一化
以下是数据标准化/归一化的常用的两种方法，具体使用方法和使用场景这里不做赘述。
  * min-max标准化
  * Z-score标准化方法
* 2 计算协方差矩阵
![协方差矩阵计算公式](https://upload-images.jianshu.io/upload_images/8579659-50ee233da510e0ea.gif?imageMogr2/auto-orient/strip)

* 3 计算协方差矩阵的特征值和特征向量
* 4 将特征值排序
* 5 保留前N个最大的特征值对应的特征向量
* 6 将数据转换到上面得到的N个特征向量构建的新空间中（实现特征压缩）

了解了算法之后我们可以结合自己掌握的编程语言如python , R, Java等一步步实现PCA算法，下面是通过python实现的PCA代码示例：
```
def pca(dataMat, topNfeat=9999999):
    """pca

    Args:
        dataMat   原数据集矩阵
        topNfeat  应用的N个特征
    Returns:
        lowDDataMat  降维后数据集
        reconMat     新的数据集空间
    """

    # 数据标准化/归一化，这里未对数据归一化，只是取了平均值，实际应用时根据业务数据进行数据归一化
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals


    # cov协方差=[(x1-x均值)*(y1-y均值)+(x2-x均值)*(y2-y均值)+...+(xn-x均值)*(yn-y均值)+]/(n-1)
    '''
    方差：（一维）度量两个随机变量关系的统计量
    协方差： （二维）度量各个维度偏离其均值的程度
    协方差矩阵：（多维）度量各个维度偏离其均值的程度

    当 cov(X, Y)>0时，表明X与Y正相关；(X越大，Y也越大；X越小Y，也越小。这种情况，我们称为“正相关”。)
    当 cov(X, Y)<0时，表明X与Y负相关；
    当 cov(X, Y)=0时，表明X与Y不相关。
    '''
    covMat = cov(meanRemoved, rowvar=0)

    # eigVals为特征值， eigVects为特征向量
    eigVals, eigVects = linalg.eig(mat(covMat))
    # print 'eigVals=', eigVals
    # print 'eigVects=', eigVects
    # 对特征值，进行从小到大的排序，返回从小到大的index序号
    # 特征值的逆序就可以得到topNfeat个最大的特征向量
    '''
    >>> x = np.array([3, 1, 2])
    >>> np.argsort(x)
    array([1, 2, 0])  # index,1 = 1; index,2 = 2; index,0 = 3
    >>> y = np.argsort(x)
    >>> y[::-1]
    array([0, 2, 1])
    >>> y[:-3:-1]
    array([0, 2])  # 取出 -1, -2
    >>> y[:-6:-1]
    array([0, 2, 1])
    '''
    eigValInd = argsort(eigVals)
    # print 'eigValInd1=', eigValInd

    # -1表示倒序，返回topN的特征值[-1 到 -(topNfeat+1) 但是不包括-(topNfeat+1)本身的倒叙]
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    # print 'eigValInd2=', eigValInd
    # 重组 eigVects 最大到最小
    redEigVects = eigVects[:, eigValInd]
    # print 'redEigVects=', redEigVects.T
    # 将数据转换到新空间
    # print "---", shape(meanRemoved), shape(redEigVects)
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    # print 'lowDDataMat=', lowDDataMat
    # print 'reconMat=', reconMat
    return lowDDataMat, reconMat

```
在机器学习领域目前已经有一部分相当成熟和完善的机器学习算法库，如sklearn、tensorflow等，这些算法库里也几乎都集成了PCA算法，实际在应用时，直接从这些算法库里调用就可以了。下面是使用sklearn中PCA算法的例子,可以发现，相比手动写代码实现要方便快捷很多。
```
import numpy as np
from sklearn.decomposition import PCA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
'''创建一个PCA对象，其中参数n_components表示保留的特征数，
这里默认保存2个，如果设置成‘mle’,那么会自动确定保留的特征数'''
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_)
```

# 结语

关于PCA算法，今天就写到这里，后续打算继续以具体的数据为例，深入探索PCA算法。