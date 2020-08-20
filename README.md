# -java-python-
数据分析知识简单运用

数据集预处理**
爬取过后得到的数据集可能像这样：python1.csv python2.csv python3.csv  ...... *所以需要进行数据集的合并操作>>*
 1.导入pandas
 2.使用pandas 的合并函数  file1.append(file2,ignore_index=True)


 合并过后，里面会存在重复公司的数据: 
 

 - 1网站本身发布的职位重复数据
 - 爬虫如果崩溃从上次断点爬取也会爬取重复数据

*那么需要进行去重操作*
去重函数：pd_file.duplicated()只有当所有记录一样时去除重复

*到这一步将处理好的数据在写入到新的csv文件中*
写入函数：pd_file.to_csv(file_name,sep=",",header=True,index=False)

处理好的数据集是：java_fix_index.csv 和python_fix_index.csv其他的数据集是爬虫爬下来的数据集并没有经过合并
