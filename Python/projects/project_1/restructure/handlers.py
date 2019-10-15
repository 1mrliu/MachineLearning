# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/15 7:01 PM'
# 处理程序
class Handler:
    """
    对Parser发起的使用方法调用进行处理的对象

    Parser将对每个文本块调用方法start()和end()，并将合适的文本名称作为参数。
    方法sub()将用于正则表达式替换，使用诸如'emphasis'等名称调用时，这个方法将返回相应的额替换函数
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
            return result
        return substitution

class HTMLRender(Handler):
    """
    用于渲染HTML的具体处理程序

    HTMLRender的方法可通过超类Handler的方法start() end() sub()来访问
    这些方法实现了HTML文档使用的基本标记
    """
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))
    def sub_url(self, match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1), match.group(1))
    def feed(self, data):
        print(data)

