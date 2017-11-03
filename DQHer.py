# coding(utf-8)
# 获取整个网站的数据
import urllib.request                   #Urllib模块提供了读取web页面数据的接口，我们可以像读取本地文件一样读取www和ftp上的数据。
import re                               #正则表达式模块
import os                               #文件操作模块



def getHtml(url):
    page = urllib.request.urlopen(url)  # urllib.urlopen()方法用于打开一个URL地址
    html = page.read()                  # read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来。
    return html                         # 执行程序返回网页整个内容。

def getdata_Vis(html):
    html = html.decode('utf-8')         #html内容编码
    reg =r'<td>(DQ HER|DQ Her)</td>\n  <td>([0-9]{7}.[0-9]+)</td>\
[\s]*[\S]*[\s]*[\S]*[\s]*[\S]*[\s]*[\S]*[\s]*[\S]*[\s]*[\S]*[\s]*>([0-9]{2}.[0-9]+)</a></td>\n  \n  <td>&mdash;</td>\n  <td>(Vis.)</td>'
                                        #正则表达式用于筛选数据
    datre = re.compile(reg)             #把正则表达式编译成一个正则表达式对象.
    datlist = re.findall(datre, html)   #读取html中包含正则表达式的数据。
    for dat in datlist:
        dat = str(dat)
        dat = dat.replace("'", '')
        dat = dat.replace("(", '')
        dat = dat.replace(")", '')        #将数据去除符号。
        file_Vis.write(dat + "\n")       #每个list元素一行保存。

def getdata_V(html):
    html = html.decode('utf-8')         #html内容编码
    reg =r'<td>(DQ HER|DQ Her)</td>\n  <td>([0-9]{7}.[0-9]+)</td>[\S\s]{250}[\S]*[\s]*>([0-9]{2}.[0-9]+)[\S\s]{19}([0-9]{1}.[0-9]+)[\S\s]{12}(V)'
                                                       #正则表达式用于筛选数据
    datre = re.compile(reg)             #把正则表达式编译成一个正则表达式对象.
    datlist = re.findall(datre, html)   #读取html中包含正则表达式的数据。
    for dat in datlist:
        dat = str(dat)
        dat = dat.replace("'", '')
        dat = dat.replace("(", '')
        dat = dat.replace(")", '')      #将数据去除符号。
        file_V.write(dat + "\n")       #每个list元素一行保存。

def getdata_CV(html):
    html = html.decode('utf-8')         #html内容编码
    reg =r'<td>(DQ HER|DQ Her)</td>\n  <td>([0-9]{7}.[0-9]+)</td>[\S\s]{250}[\S]*[\s]*>([0-9]{2}.[0-9]+)[\S\s]{19}([0-9]{1}.[0-9]+)[\S\s]{12}(CV)'
                                        #正则表达式用于筛选数据
    datre = re.compile(reg)             #把正则表达式编译成一个正则表达式对象.
    datlist = re.findall(datre, html)   #读取html中包含正则表达式的数据。
    for dat in datlist:
        dat = str(dat)
        dat = dat.replace("'", '')
        dat = dat.replace("(", '')
        dat = dat.replace(")", '')      #将数据去除符号。
        file_CV.write(dat + "\n")       #每个list元素一行保存。


file_Vis = open('C:\\Users\\wqs\\PycharmProjects\\Get_Data_AAVSO\\DQHer_Vis.txt','w+')      #初始化用于数据保存的文件
file_V    = open('C:\\Users\\wqs\\PycharmProjects\\Get_Data_AAVSO\\DQHer_V.txt','w+')
file_CV = open('C:\\Users\\wqs\\PycharmProjects\\Get_Data_AAVSO\\DQHer_CV.txt','w+')

urlmode='https://www.aavso.org/apps/webobs/results/?star=DQ+HER&num_results=200&page='       #url模板
for x in range(1,870):  #870
    html = getHtml(urlmode+str(x))
    getdata_Vis(html)
    getdata_V(html)
    getdata_CV(html)
    print(urlmode+str(x))                                                 #输出请求的url

#关闭数据文件
file_Vis.close()
file_V.close()
file_CV.close()


#----------------------------------------------------------------------------
# Note1
# 正则表达式的通用流程是为查找的数据写一个模块，然后添加小括号来提取目标数据。
# 正则表达式是死的，对于重复的pattem最好字符串刻画。
# [\s]*用于识别连续的非文字；[\S]*用于识别连续的文字
#[\S\s]{n}用于识别n个字符(包括非文字)
# 括号()用于目标数据记录；[]表示匹配里面的元素
# Note2
# urllib.urlretrieve(image_url,input_file)   直接将远程数据下载到本地。





