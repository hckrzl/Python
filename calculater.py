#!/usr/bin/python
#coding=utf8

"""
This is a simple calculator program.
You can perform "add","minus","multiple","divide" in this program.
"""

import wx
import re

app = wx.App()
win = wx.Frame(None)
reg = r"[\+\-\*\/]"

panel = wx.Panel(win)

btn_dot = wx.Button(panel,label=".")
btn_1 = wx.Button(panel,label="1")
btn_2 = wx.Button(panel,label="2")
btn_3 = wx.Button(panel,label="3")
btn_4 = wx.Button(panel,label="4")
btn_5 = wx.Button(panel,label="5")
btn_6 = wx.Button(panel,label="6")
btn_7 = wx.Button(panel,label="7")
btn_8 = wx.Button(panel,label="8")
btn_9 = wx.Button(panel,label="9")
btn_0 = wx.Button(panel,label="0")
btn_add = wx.Button(panel,label="+")
btn_minus = wx.Button(panel,label="-")
btn_multiple = wx.Button(panel,label="*")
btn_divide = wx.Button(panel,label="/")
btn_clear = wx.Button(panel,label="C")
btn_result = wx.Button(panel,label="=")
text_content = wx.TextCtrl(panel)

def b1(evt):
    buff = text_content.GetValue()
    buff  = buff + '1'
    text_content.SetValue(buff)
def b2(evt):
    buff = text_content.GetValue()
    buff  = buff + '2'
    text_content.SetValue(buff)
def b3(evt):
    buff = text_content.GetValue()
    buff  = buff + '3'
    text_content.SetValue(buff)
def b4(evt):
    buff = text_content.GetValue()
    buff  = buff + '4'
    text_content.SetValue(buff)
def b5(evt):
    buff = text_content.GetValue()
    buff  = buff + '5'
    text_content.SetValue(buff)
def b6(evt):
    buff = text_content.GetValue()
    buff  = buff + '6'
    text_content.SetValue(buff)
def b7(evt):
    buff = text_content.GetValue()
    buff  = buff + '7'
    text_content.SetValue(buff)
def b8(evt):
    buff = text_content.GetValue()
    buff  = buff + '8'
    text_content.SetValue(buff)    
def b9(evt):
    buff = text_content.GetValue()
    buff  = buff + '9'
    text_content.SetValue(buff)
def b0(evt):
    buff = text_content.GetValue()
    buff  = buff + '0'
    text_content.SetValue(buff)
def b_add(evt):
    buff = text_content.GetValue()
    if "+" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 + operand2) + '+'
        text_content.SetValue(buff)
    elif "-" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 - operand2) + "+"
        text_content.SetValue(buff)
    elif "*" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 * operand2) + "+" 
        text_content.SetValue(buff)
    elif "/" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(float(operand1) / operand2) + "+"
        text_content.SetValue(buff)
    else :
        buff = buff + "+"
        text_content.SetValue(buff)



def b_minus(evt):
    buff = text_content.GetValue()
    if "+" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 + operand2) + '-'
        text_content.SetValue(buff)
    elif "-" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 - operand2) + "-"
        text_content.SetValue(buff)
    elif "*" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 * operand2) + "-" 
        text_content.SetValue(buff)
    elif "/" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(float(operand1) / operand2) + "-"
        text_content.SetValue(buff)
    else :
        buff = buff + "-"
        text_content.SetValue(buff)



def b_multiple(evt):
    buff = text_content.GetValue()
    if "+" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 + operand2) + '*'
        text_content.SetValue(buff)
    elif "-" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 - operand2) + "*"
        text_content.SetValue(buff)
    elif "*" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 * operand2) + "*" 
        text_content.SetValue(buff)
    elif "/" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(float(operand1) / operand2) + "*"
        text_content.SetValue(buff)
    else :
        buff = buff + "*"
        text_content.SetValue(buff)



def b_divide(evt):
    buff = text_content.GetValue()
    if "+" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 + operand2) + '/'
        text_content.SetValue(buff)
    elif "-" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 - operand2) + "/"
        text_content.SetValue(buff)
    elif "*" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 * operand2) + "/" 
        text_content.SetValue(buff)
    elif "/" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(float(operand1) / operand2) + "/"
        text_content.SetValue(buff)
    else :
        buff = buff + "/"
        text_content.SetValue(buff)



def b_result(evt):
    buff = text_content.GetValue()
    if "+" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 + operand2)
        text_content.SetValue(buff)
    elif "-" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 - operand2)
        text_content.SetValue(buff)
    elif "*" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(operand1 * operand2)
        text_content.SetValue(buff)
    elif "/" in buff:
        operand1 = re.split(reg,buff)[0]
        operand2 = re.split(reg,buff)[1]
        if '.' in operand1:
            operand1 = float(operand1)
        else:
            operand1 = int(operand1)
        if '.' in operand2:
            operand2 = float(operand2)
        else:
            operand2 = int(operand2)
        buff = str(float(operand1) / operand2)
        text_content.SetValue(buff)
    else :
        pass

def b_clear(evt):
    text_content.SetValue("")



line1 = wx.BoxSizer(wx.HORIZONTAL)
line2 = wx.BoxSizer(wx.HORIZONTAL)
line3 = wx.BoxSizer(wx.HORIZONTAL)
line4 = wx.BoxSizer(wx.HORIZONTAL)
cal = wx.BoxSizer(wx.VERTICAL)

line1.Add(btn_add,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line1.Add(btn_minus,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line1.Add(btn_multiple,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line1.Add(btn_divide,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)

line2.Add(btn_1,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line2.Add(btn_2,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line2.Add(btn_3,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line2.Add(btn_4,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)

line3.Add(btn_5,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line3.Add(btn_6,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line3.Add(btn_7,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line3.Add(btn_8,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)

line4.Add(btn_9,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line4.Add(btn_0,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line4.Add(btn_clear,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
line4.Add(btn_result,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)

cal.Add(text_content,proportion=1,flag=wx.EXPAND|wx.ALL,border=20)
cal.Add(line1,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
cal.Add(line2,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
cal.Add(line3,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
cal.Add(line4,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)

panel.SetSizer(cal)


btn_1.Bind(wx.EVT_BUTTON,b1)
btn_2.Bind(wx.EVT_BUTTON,b2)
btn_3.Bind(wx.EVT_BUTTON,b3)
btn_4.Bind(wx.EVT_BUTTON,b4)
btn_5.Bind(wx.EVT_BUTTON,b5)
btn_6.Bind(wx.EVT_BUTTON,b6)
btn_7.Bind(wx.EVT_BUTTON,b7)
btn_8.Bind(wx.EVT_BUTTON,b8)
btn_9.Bind(wx.EVT_BUTTON,b9)
btn_0.Bind(wx.EVT_BUTTON,b0)
btn_add.Bind(wx.EVT_BUTTON,b_add)
btn_minus.Bind(wx.EVT_BUTTON,b_minus)
btn_multiple.Bind(wx.EVT_BUTTON,b_multiple)
btn_divide.Bind(wx.EVT_BUTTON,b_divide)
btn_result.Bind(wx.EVT_BUTTON,b_result)
btn_clear.Bind(wx.EVT_BUTTON,b_clear)



win.Show()
app.MainLoop()

