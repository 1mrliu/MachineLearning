# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/16 2:59 PM'
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'Hello World!', textAnchor= 'middle')
d.add(s)
renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file.')