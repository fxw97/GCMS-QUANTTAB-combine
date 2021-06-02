# GCMS-QUANTTAB-combine
## combine GCMS output datas
```
自动整理汇总GC-MS导出的定量文件QUANTTAB.CSV中需要的信息，包括样品名，及各个目标化合物的峰强度。
用到的库包括pandas、os和csv
使用方法：
1.将需要处理的数据文件夹放置example data目录下，假设其名为datafile1。datafile1其内部文件为GC-MS拷贝过来的数据文件，具体可参考**2019出口数据**目录中的文件。
2.将combine QUANTTAB datas.py脚本中path改为path=r'./example data/datafile1/*/QUANTTAB.CSV'，运行脚本即可，整合好的数据会自动储存在combined results.csv文件里。
```
