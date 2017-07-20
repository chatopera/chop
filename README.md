# chop
Python 中文分词工具包

## 欢迎

GitHub: https://github.com/samurais/chop

Pypi: https://pypi.python.org/pypi/chop

## 依赖

Python3

## 安装说明

代码对 Python 3 兼容

*  全自动安装： ``easy_install chop`` 或者 ``pip install chop`` / ``pip3 install chop``

* 接口

```
import chop
import os

# 使用chop内部词典初始化
T = chop.Tokenizer(dict_path=os.path.join(chop.__path__[0], 'dict.txt'))

# 切词
print(' '.join(T.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")))

```

## 特点

* 使用简单

```
for x in t.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"): print(x)
```

* 代码通俗易懂，方便掌握算法

## 算法

* MMSEG: 
A Word Identification System for Mandarin Chinese Text Based on Two
Variants of the Maximum Matching Algorithm
http://technology.chtsai.org/mmseg/

Other references:
http://blog.csdn.net/nciaebupt/article/details/8114460
http://www.codes51.com/itwd/1802849.html

* HMM & Viterbi:

[基于层叠隐马尔可夫模型的中文命名实体识别](http://xueshu.baidu.com/s?wd=%E5%9F%BA%E4%BA%8E%E5%B1%82%E5%8F%A0%E9%9A%90%E9%A9%AC%E5%B0%94%E5%8F%AF%E5%A4%AB%E6%A8%A1%E5%9E%8B%E7%9A%84%E4%B8%AD%E6%96%87%E5%91%BD%E5%90%8D%E5%AE%9E%E4%BD%93%E8%AF%86%E5%88%AB&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_hit=1)

## 词典

Dict:
https://github.com/Samurais/jieba/blob/master/jieba/dict.txt

## 授权协议
[MIT](./LICENSE)