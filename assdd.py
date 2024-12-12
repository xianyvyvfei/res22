# coding = utf-8
# 爬取数据算法
from urllib.request import urlopen as uo
from bs4 import BeautifulSoup
from tkinter import *
import requests
import re as r

class Ppx:
    def __init__(self, url, root, text):
        self.url = url
        self.root = root
        self.text = text
        # 头：用户代理 操作系统 浏览器信息
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"}
        # 存储 抓取到的信息
        self.data = [0, []]

    # 获取 信息
    def get_data(self):
        data = self.data
        return data

    def main(self):
        try:
            rs = requests.get(self.url, headers=self.headers)
        except:
            self.data[0] = -1
            return -1
        html = rs.content.decode('utf-8', 'ignore')
        my_page = BeautifulSoup(html, 'lxml')

        # 正则匹配 贪心
        obj1 = r.compile(r'<a name="(?P<t1>.*?)"></a>', r.S)
        obj2 = r.compile(r'<span class=".*?" data-text="true">(?P<t2>.*?)</span>', r.S)
        obj3 = r.compile(r'<a class=".*?" data--from-module=".*?" href=".*?" target="_blank">\
                    (?P<t3>.*?)</a>', r.S)
        # 过滤
        obj_s = r.compile(r'\d+', r.S)

        data_x = 0
        # 切割HTML文件内数据
        for tag in my_page.find_all('div', class_='J-lemma-content'):
            for t1 in tag.find_all('div'):
                str_s = ""
                for t2 in t1.find_all('div'):
                    for t3 in t2.find_all('a'):
                        list1 = obj1.finditer(str(t3))
                        for i in list1:
                            txt = i.group("t1")
                            if not obj_s.findall(txt):
                                # 提取标题信息
                                data_x += 1
                                self.data[data_x].append(txt)
                for t2 in t1.find_all('span'):
                    list1 = obj2.finditer(str(t2))
                    for list2 in list1:
                        txt1 = list2.group("t2")
                        if 'a' not in txt1:
                            # 提取标签a内的数据 求掉链接
                            self.data[data_x].append(txt1)
                    for t3 in t2.find_all('a'):
                        # 提取信息-关于标题的信息
                        txt2 = t3.get_text('a')
                        self.data[data_x].append(txt2)
                self.data.append([])
if __name__ == '__main__':
    root = Tk()
    Ppx.main()