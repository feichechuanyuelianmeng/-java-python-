import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# import pandas.core.indexes.base.Index
plt.rcParams['font.sans-serif'] = ['SimHei']

def lagou_data_java():
    java1_data = pd.read_csv("lagou_java.csv")
    java2_data = pd.read_csv("lagou_java1.csv")
    print(java1_data.info())
    print("*"*100)
    print(java2_data.info())
    print("*" * 100)
    java_data = java1_data.append(java2_data, ignore_index=True)
    print(java_data.info)
    print("*" * 100)
    # 去除重复
    # company_list = java_data["company_name"].tolist()
    # print(company_list)
    # print(len(company_list))
    # company_list = list(set([i for i in company_list]))
    # print(len(company_list))
    is_duplictate = java_data.duplicated()
    # print(is_duplictate)
    # duplicate_list = is_duplictate.tolist()
    # num = 0
    # for dup in duplicate_list:
    #     if dup == True:
    #         num = num + 1
    # print(num)
    java_data = java_data.drop_duplicates()
    print(java_data.info())
    java_data.to_csv("java_fix_index.csv", sep=",",header=True,index=False)

def lagou_data_python():
    python1_data = pd.read_csv("lagou_python.csv")
    python2_data = pd.read_csv("lagou_python1.csv")
    python3_data = pd.read_csv("lagou_python2.csv")
    # print(java1_data.info())
    # print("*"*100)
    # print(java2_data.info())
    # print("*" * 100)
    python_data = python1_data.append([python2_data,python3_data], ignore_index=True)
    print(python_data.info)
    print("*" * 100)
    # 去除重复
    # company_list = java_data["company_name"].tolist()
    # print(company_list)
    # print(len(company_list))
    # company_list = list(set([i for i in company_list]))
    # print(len(company_list))
    is_duplictate = python_data.duplicated()
    print(is_duplictate)
    duplicate_list = is_duplictate.tolist()
    num = 0
    for dup in duplicate_list:
        if dup == True:
            num = num + 1
    print(num)
    python_data = python_data.drop_duplicates()
    print(python_data.info())
    python_data.to_csv("python_fix_index.csv", sep=",",header=True,index=False)

def data_preprocess(file_path):
    python = pd.read_csv(file_path)
    python_salary_list = python['job_salary'].tolist()
    print(python_salary_list)
    python_min_sal = []
    python_max_sal = []
    python_aver_sal = []
    for salary in python_salary_list:
        min = salary.split("-")[0].split("k")[0]
        max = salary.split("-")[-1].split("k")[0]
        print(max)
        aver = (int(max) + int(min)) / 2
        python_min_sal.append(int(min))
        python_max_sal.append(int(max))
        python_aver_sal.append(aver)

    # 添加3个工资指标
    python_salary_min = np.array(python_min_sal)
    python_salary_average = np.array(python_aver_sal)
    python_salary_max = np.array(python_max_sal)
    python["min_salary"] = python_min_sal
    python["average_salary"] = python_aver_sal
    python["max_salary"] = python_max_sal
    return python
    # python.apply(pd.to_numeric(),errors="ignore")

def country_picture(python,i,name=None):
    y1 = python["min_salary"].values
    y2 = python["average_salary"].values
    y3 = python["max_salary"].values
    # min直方图
    # plt.subplot(2,1,i)
    # group = 15
    # # dist = (y1.max()-y1.min())//2
    # plt.xticks(range(3, 30, 2))
    # plt.xlabel("最低工资",fontsize=20)
    # plt.ylabel("公司数量",fontsize=20)
    # # plt.title("公司给出的最低工资",fontsize=20)
    # plt.tick_params(axis='both', labelsize=20)
    #
    # _xticks = ["{}K".format(i) for i in range(y1.min(), 30, 2)]
    # plt.grid(alpha=0.4)
    # plt.xticks(range(y1.min(), 30, 2), _xticks)
    # plt.hist(y1, group, facecolor="lime", edgecolor="red", alpha=0.7,label=name+"公司给出的最低工资分布")
    # plt.legend(loc="best", fontsize=30)

    # # avg直方图
    # plt.subplot(2, 1, i)
    # group = 15
    # dist = (y2.max()-y2.min())//2
    # # print(dist)
    #
    # plt.xlabel("平均工资",fontsize=20)
    # plt.ylabel("公司数量",fontsize=20)
    # plt.title("公司给出的平均工资",fontsize=20)
    # _xticks = ["{}K".format(i) for i in range(int(y2.min()), 35, 2)]
    # plt.tick_params(axis='both', labelsize=20)
    # plt.xticks(range(int(y2.min()), 35, 2), _xticks)
    #
    # plt.grid(alpha=0.5)
    # plt.hist(y2, group,facecolor="orange", edgecolor="lime", alpha=0.7,label=name+"公司给出的平均工资分布")
    # plt.legend(loc="best", fontsize=30)

    # max直方图
    plt.subplot(2, 1, i)
    group = 10
    dist = (y3.max()-y3.min())//2
    # print(dist)

    plt.xlabel("最高工资",fontsize=20)
    plt.ylabel("公司数量",fontsize=20)
    plt.title("公司给出的最高工资",fontsize=20)
    _xticks = ["{}K".format(i) for i in range(int(y2.min()), 45, 2)]
    plt.tick_params(axis='both', labelsize=20)
    plt.xticks(range(int(y3.min()), 45, 2), _xticks)

    plt.grid(alpha=0.5)
    plt.hist(y3, group,facecolor="blue", edgecolor="red", alpha=0.7,label=name+"公司给出的最高工资分布")
    plt.legend(loc="best", fontsize=30)

def city_num(python,i,name=None):
    jobloc_list = python["job_location"].tolist()
    print(jobloc_list)
    city_list = []
    for city in jobloc_list:
        city_list.append(city.strip().split("-")[0])
    python["city"] = pd.Series(city_list)
    print(python["city"].values)
    city_count = python.groupby(by="city")["city"].count().sort_values(ascending=False)

    # 画图 城市分布图
    plt.subplot(2, 1, i)
    len_city = len(city_count.index)
    x_data = [i for i in range(len_city)]
    y_data = city_count
    plt.xlabel("公司数量",fontsize=20)
    plt.tick_params(axis='both', labelsize=18)

    _xticks = city_count.index
    plt.yticks(x_data, _xticks)
    plt.barh(x_data, y_data,color = "orange",label=name+"公司全国分布地区")
    plt.grid(alpha=0.5)
    plt.legend(loc="best", fontsize=30)

def averae_salary(python,i,name=None):
    jobloc_list = python["job_location"].tolist()
    print(jobloc_list)
    city_list = []
    for city in jobloc_list:
        city_list.append(city.strip().split("-")[0])
    python["city"] = pd.Series(city_list)
    print(python["city"].values)
    city_min = python.groupby(by="city")["min_salary"].mean().sort_values(ascending=False)
    city_average = python.groupby(by="city")["average_salary"].mean().sort_values(ascending=False)
    city_max = python.groupby(by="city")["max_salary"].mean().sort_values(ascending=False)

    # 画图 城市分布图
    plt.subplot(2, 1, i)



    plt.xlabel("城市", fontsize=20)
    plt.ylabel("平均工资(K)", fontsize=20)
    plt.tick_params(axis='both', labelsize=18)

    width = 0.5
    len_city = len(city_min.index)
    # x1_data = [i + width for i in range(len_city)]
    # y1_data = city_min
    x2_data = [i for i in range(len_city)]
    y2_data = city_average
    # x3_data = [i - width for i in range(len_city)]
    # y3_data = city_max

    _xticks = city_average.index

    _yticks = [i * 2 for i in range(len_city)]
    plt.xticks(x2_data, _xticks,rotation=90)
    plt.yticks(_yticks)

    # plt.bar(x3_data, y3_data, width=width)
    plt.bar(x2_data, y2_data, width=width, label = "各城市{}平均工资".format(name), color="m",edgecolor="lightcyan",alpha=0.6)
    plt.grid(alpha=0.5)
    plt.legend(loc="best", fontsize=45)
    # plt.bar(x1_data, y1_data, width=width)

def exprience_salray(python,i,name):
    # 经验与工资的关系
    python_exper_list = python['job_overlook'].tolist()
    experience_list = []

    for exper in python_exper_list:
        experience = exper.strip().split("/")[2].strip()[2:]
        experience_list.append(experience)
    print(experience_list)

    # for exper in python_exper_list:
    #     work_age = exper.strip().split("/")[2].strip().split("经验")[1]
    #     print(work_age)
    #     if work_age[-1] == '年' :
    #         work_age = work_age[:-1]
    #     elif "上" in work_age.split(" "):
    #         work_age = "5-10"
    #     else:
    #         work_age = "应届"
    #     # print(work_age)
    #     exper_list.append(work_age)
    # num = 0
    # for exper in exper_list:
    #     if exper == "应届":
    #         num = num + 1
    # print(num)
    #
    python["experience_age"] = pd.Series(experience_list)
    print(python[python["experience_age"]=="10年以上"]["min_salary"].values)
    # print(python.info())
    exper_age = python.groupby(by='experience_age')[["min_salary","average_salary","max_salary"]].mean().sort_values(by="average_salary",ascending=True)

    print(exper_age)

    plt.subplot(2, 1, i)
    width = 0.2

    x1 = [i-width for i in range(len(exper_age.index))]
    x2 = [i for i in  range(len(exper_age.index))]
    x3 = [i + width for i in  range(len(exper_age.index))]
    y1 = exper_age["min_salary"].values
    y2 = exper_age["average_salary"].values
    y3 = exper_age["max_salary"].values

    plt.xlabel("经验", fontsize=20)
    plt.ylabel("工资（K）", fontsize=20)
    plt.tick_params(axis='both', labelsize=18)
    plt.xticks(x2,exper_age.index)
    plt.yticks([i for i in range(35)])
    if name == "java":
        plt.text(-0.4,18,"这里10年以上数据就只有一条而且工资较低",fontsize=25,color="red")

    plt.bar(x1,y1,width=width,label="{}最低工资".format(name))
    plt.bar(x2,y2,width=width,label="{}平均工资".format(name))
    plt.bar(x3,y3,width=width,label="{}最高工资".format(name))
    plt.grid(alpha=0.5)
    plt.legend(loc="best", fontsize=45)

def siez_salary(python,i,name):
    # print(python.info())
    # size_count = python[python["company_size"]=="少于15人"]["min_salary"]
    # print(size_count)
    # size_count = python.groupby(by="company_size")["average_salary"].mean().sort_values("average_salary")
    # print(size_count.values)
    company_size = python.groupby(by="company_size").mean().sort_values("average_salary")

    print(company_size)
    width = 0.2
    plt.subplot(2, 1, i)
    # x1 = [i - width for i in range(len(company_size.index))]
    x2 = [i for i in range(len(company_size.index))]
    # x3 = [i + width for i in range(len(company_size.index))]
    # y1 = company_size["min_salary"].values
    y2 = company_size["average_salary"].values
    # y3 = company_size["max_salary"].values


    plt.xlabel("公司规模", fontsize=20)
    plt.ylabel("工资（K）", fontsize=20)
    plt.tick_params(axis='both', labelsize=20)
    plt.xticks(x2, company_size.index)
    plt.yticks([i for i in range(25)])
    if name == "java":
        plt.text(0.7,17.5,"少于15人的公司共有4家其中3家给的工资偏高",color="green",fontsize=20)
    # plt.bar(x1, y1, width=width)
    plt.plot(x2, y2,'r-*',linewidth=20 ,alpha=0.5, label=name+"公司规模对应平均工资变化")
    # plt.bar(x3, y3, width=width)
    plt.grid(alpha=0.5)
    plt.legend(loc="best", fontsize=45)

def java_python_compare():
    # 数据的预处理
    python = data_preprocess("python_fix_index.csv")
    java = data_preprocess("java_fix_index.csv")

    # # 画图全国范围
    # plt.figure(figsize=(20, 20), dpi=100)
    # country_picture(python,1,name="python")
    # country_picture(java,2,name="java")
    # plt.savefig("picture/country_max.svg")
    # plt.show()

    # 分析各城市职业人数
    # plt.figure(figsize=(20, 20), dpi=100)
    # city_num(python,1,name="python")
    # city_num(java,2,name="java")
    # plt.savefig("picture/city_num.svg")
    # plt.show()

    #
    # 各城市平均工资
    # 画图全国范围
    # plt.figure(figsize=(20, 20), dpi=100)
    # averae_salary(python,1,name="python")
    # averae_salary(java,2,name="java")
    # plt.savefig("picture/city_average.svg")
    # plt.show()

    # 经验与工资
    # 画图全国范围
    # plt.figure(figsize=(20, 20), dpi=100)
    # exprience_salray(python,1,name="python")
    # exprience_salray(java,2,name="java")
    # plt.savefig("picture/experience_salary.svg")
    # plt.show()


    # 公司规模与工资的关系
    plt.figure(figsize=(20, 20), dpi=100)
    siez_salary(python,1,name="python")
    siez_salary(java,2,name="java")
    plt.savefig("picture/size_salary.svg")
    plt.show()


    #
    # company_size = python.groupby("company_size").mean().sort_values("average_salary")
    # print(company_size)
    # width = 0.2
    #
    # x1 = [i - width for i in range(len(company_size.index))]
    # x2 = [i for i in range(len(company_size.index))]
    # x3 = [i + width for i in range(len(company_size.index))]
    # y1 = company_size["min_salary"].values
    # y2 = company_size["average_salary"].values
    # y3 = company_size["max_salary"].values
    #
    # plt.xticks(x2, company_size.index)
    # plt.yticks([i * 2 for i in range(35)])
    #
    # plt.bar(x1, y1, width=width)
    # plt.bar(x2, y2, width=width)
    # plt.bar(x3, y3, width=width)
    # plt.grid(alpha=0.5)
    # plt.show()

if __name__ == '__main__':
    # lagou_data_java()
    # lagou_data_python()
    java_python_compare()