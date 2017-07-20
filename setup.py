# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
LONGDOC = """
chop
=====

中文分词

完整文档见

GitHub: https://github.com/samurais/chop

特点
====

* 使用简单

```python
for x in t.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"): print(x)
```

* 代码通俗易懂，方便掌握算法

-  MIT 授权协议

安装说明
========

代码对 Python 3 兼容

-  全自动安装： ``easy_install chop`` 或者 ``pip install chop`` / ``pip3 install chop``
-  通过 ``import chop`` 来引用

"""

setup(name='chop',
      version='0.6',
      description='Chinese Words Segementation Utilities',
      long_description=LONGDOC,
      author='Hai Liang Wang',
      author_email='hailiang.hl.wang@gmail.com',
      url='https://github.com/samurais/chop',
      license="MIT",
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='NLP,tokenizing,Chinese word segementation',
      packages= ['chop'],
      package_dir={'chop':'chop'},
      package_data={'chop':['*.txt']}
)
