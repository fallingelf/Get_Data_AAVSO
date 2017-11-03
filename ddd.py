# coding(utf-8)
# 获取整个网站的数据
import urllib.request                   #Urllib模块提供了读取web页面数据的接口，我们可以像读取本地文件一样读取www和ftp上的数据。
import re                               #正则表达式模块
import os                               #文件操作模块



def getHtml(url):
    page = urllib.request.urlopen(url)  # urllib.urlopen()方法用于打开一个URL地址
    html = page.read()                  # read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来。
    return html                         # 执行程序返回网页整个内容。

def getdata_V(html):
    html = html.decode('utf-8')         #html内容编码
    reg =r'<td>(DQ HER|DQ Her)</td>\n  <td>([0-9]{7}.[0-9]+)</td>[\S\s]{250}[\S]*[\s]*>([0-9]{2}.[0-9]+)[\S\s]{19}([0-9]{1}.[0-9]+)[\S\s]{12}(CV)'
                                                        #正则表达式用于筛选数据
    datre = re.compile(reg)              #把正则表达式编译成一个正则表达式对象.
    datlist = re.findall(datre, html)    #读取html中包含正则表达式的数据。
    for dat in datlist:
        dat = str(dat)
        dat = dat.replace("'", '')
        dat = dat.replace("(", '')
        dat = dat.replace(")", '')        #将数据去除符号。
        file_CV.write(dat + "\n")       #每个list元素一行保存。

file_CV = open('C:\\Users\\wqs\\PycharmProjects\\Get_Data_AAVSO\\DQHer_CV.txt','w+')      #初始化用于数据保存的文件

urlmode='https://www.aavso.org/apps/webobs/results/?star=DQ+HER&num_results=200&page='       #url模板
x=300        #870
html = getHtml(urlmode+str(x))
getdata_V(html)
print(urlmode+str(x))                                                 #输出请求的url

#关闭数据文件
file_CV.close()