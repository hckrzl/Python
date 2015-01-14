#!/usr/bin/python
#coding=utf8

import wx

app = wx.App()
win = wx.Frame(None)
panel = wx.Panel(win)

def openfile(evt):
    filepath = text_filename.GetValue()
    fopen = open(filepath,'r')
    text_content.SetValue(fopen.read())
    fopen.close()


def savefile(evt):
    contents = text_content.GetValue()
    filepath = text_filename.GetValue()
    fopen = open(filepath,'a+')
    fopen.writelines(contents + '\n')
    fopen.close()

text_filename = wx.TextCtrl(panel)
btn_open = wx.Button(panel, label = "Open")
btn_save = wx.Button(panel,label =  "Save" )
text_content = wx.TextCtrl(panel,style=wx.TE_MULTILINE|wx.HSCROLL)

btn_open.Bind(wx.EVT_BUTTON,openfile) #bind a built-in event binding 
btn_save.Bind(wx.EVT_BUTTON,savefile) 

hbox = wx.BoxSizer(orient = wx.HORIZONTAL)
hbox.Add(text_filename,proportion=1,flag=wx.EXPAND)
hbox.Add(btn_open,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(btn_save,proportion=0,flag=wx.LEFT,border=5)

vbox = wx.BoxSizer(orient = wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND,border=5)
vbox.Add(text_content,proportion=1,flag=wx.ALL|wx.EXPAND,border=5)


panel.SetSizer(vbox)
win.Show()
app.MainLoop()
    
