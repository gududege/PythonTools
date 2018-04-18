# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext
import re, math, clipboard


###########################################################################
## Class ConfigFrame
###########################################################################

class ConfigFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Step7 StlCreator V1.0", pos=wx.DefaultPosition,
                          size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.menbar = wx.MenuBar(0)
        self.filemenu = wx.Menu()
        self.savemenuitem = wx.MenuItem(self.filemenu, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL)
        self.filemenu.Append(self.savemenuitem)

        self.filemenu.AppendSeparator()

        self.quitmenuitem = wx.MenuItem(self.filemenu, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL)
        self.filemenu.Append(self.quitmenuitem)

        self.menbar.Append(self.filemenu, u"File")

        self.windowsmenu = wx.Menu()
        self.autocreatemenu = wx.MenuItem(self.windowsmenu, wx.ID_ANY, u"AutoCreate", wx.EmptyString, wx.ITEM_NORMAL)
        self.windowsmenu.Append(self.autocreatemenu)

        self.fromfilemenu = wx.MenuItem(self.windowsmenu, wx.ID_ANY, u"FromFile", wx.EmptyString, wx.ITEM_NORMAL)
        self.windowsmenu.Append(self.fromfilemenu)

        self.menbar.Append(self.windowsmenu, u"Windows")

        self.SetMenuBar(self.menbar)

        self.statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        # 创造两个panel并设置panel1为默认显示
        self.autocreatepanel = autoCreatePanel(self)
        self.fromfilepanel = readFromFilePanel(self)
        self.fromfilepanel.Hide()
        self.bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.bSizer2.Add(self.autocreatepanel)
        self.bSizer2.Add(self.fromfilepanel)

        self.SetSizer(self.bSizer2)

        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.clickclosewindow)
        self.Bind(wx.EVT_MENU, self.clicksavemenu, id=self.savemenuitem.GetId())
        self.Bind(wx.EVT_MENU, self.clickquitmenu, id=self.quitmenuitem.GetId())
        self.Bind(wx.EVT_MENU, self.cilckswitchautocreatemenu, id=self.autocreatemenu.GetId())
        self.Bind(wx.EVT_MENU, self.clickswitchfilemenu, id=self.fromfilemenu.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def clickclosewindow(self, event):
        self.Destroy()
        event.Skip()

    def clicksavemenu(self, event):
        event.Skip()

    def clickquitmenu(self, event):
        self.Destroy()
        event.Skip()

    def cilckswitchautocreatemenu(self, event):
        self.fromfilepanel.Hide()
        self.autocreatepanel.Show()
        event.Skip()

    def clickswitchfilemenu(self, event):
        self.autocreatepanel.Hide()
        self.fromfilepanel.Show()
        event.Skip()


###########################################################################
## Class autocreatepanel
###########################################################################

class autoCreatePanel(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=(screen_width, screen_height),
                         style=wx.TAB_TRAVERSAL)

        gSizer1 = wx.GridSizer(0, 3, 0, 0)

        self.firstcontext = wx.StaticText(self, wx.ID_ANY, u"第一行循环文本", wx.DefaultPosition, wx.DefaultSize, 0)
        self.firstcontext.Wrap(-1)
        gSizer1.Add(self.firstcontext, 0, wx.ALL, 5)

        self.firstlinetxt = wx.TextCtrl(self, wx.ID_ANY, u"A    L    20.0", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.firstlinetxt, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.sencondcontext = wx.StaticText(self, wx.ID_ANY, u"报警位符号模版", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sencondcontext.Wrap(-1)
        gSizer1.Add(self.sencondcontext, 0, wx.ALL, 5)

        self.errorbitsymbol = wx.TextCtrl(self, wx.ID_ANY, u"D_CONV_Action.Action[1,1].Jam", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        gSizer1.Add(self.errorbitsymbol, 0, wx.ALL, 5)

        bittypeChoices = [u"常开点", u"常闭点"]
        self.bittype = wx.ComboBox(self, wx.ID_ANY, u"常开点", wx.DefaultPosition, wx.DefaultSize, bittypeChoices, 0)
        self.bittype.SetSelection(0)
        gSizer1.Add(self.bittype, 0, wx.ALL, 5)

        self.thirdcontext = wx.StaticText(self, wx.ID_ANY, u"输送线起止序号(逗号分割)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.thirdcontext.Wrap(-1)
        gSizer1.Add(self.thirdcontext, 0, wx.ALL, 5)

        self.seqnumberbeginandend = wx.TextCtrl(self, wx.ID_ANY, u"1,30", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.seqnumberbeginandend, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.forthcontext = wx.StaticText(self, wx.ID_ANY, u"输送线序号步长", wx.DefaultPosition, wx.DefaultSize, 0)
        self.forthcontext.Wrap(-1)
        gSizer1.Add(self.forthcontext, 0, wx.ALL, 5)

        self.seqnumberstep = wx.TextCtrl(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.seqnumberstep, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.fifthcontext = wx.StaticText(self, wx.ID_ANY, u"拆分正则表达式", wx.DefaultPosition, wx.DefaultSize, 0)
        self.fifthcontext.Wrap(-1)
        gSizer1.Add(self.fifthcontext, 0, wx.ALL, 5)

        self.regextxt = wx.TextCtrl(self, wx.ID_ANY, u"(.+\\[).+(\\].+)", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.regextxt, 0, wx.ALL, 5)

        self.testregex = wx.Button(self, wx.ID_ANY, u"测试正则", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.testregex, 0, wx.ALL, 5)

        self.sixthcontext = wx.StaticText(self, wx.ID_ANY, u"目标DB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sixthcontext.Wrap(-1)
        gSizer1.Add(self.sixthcontext, 0, wx.ALL, 5)

        self.destdbnumber = wx.TextCtrl(self, wx.ID_ANY, u"300", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.destdbnumber, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.seventhcontext = wx.StaticText(self, wx.ID_ANY, u"目标开始位", wx.DefaultPosition, wx.DefaultSize, 0)
        self.seventhcontext.Wrap(-1)
        gSizer1.Add(self.seventhcontext, 0, wx.ALL, 5)

        self.deststartbit = wx.TextCtrl(self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.deststartbit, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        button = wx.StdDialogButtonSizer()
        self.buttonApply = wx.Button(self, wx.ID_APPLY)
        button.AddButton(self.buttonApply)
        self.buttonHelp = wx.Button(self, wx.ID_HELP)
        button.AddButton(self.buttonHelp)
        button.Realize()

        gSizer1.Add(button, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        # Connect Events
        self.testregex.Bind(wx.EVT_BUTTON, self.testregexbutton)
        self.buttonApply.Bind(wx.EVT_BUTTON, self.clickrunbutton)
        self.buttonHelp.Bind(wx.EVT_BUTTON, self.clickhelpbutton)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def testregexbutton(self, event):
        try:
            testregexisok(self)
        except Exception as e:
            wx.MessageBox(u'正则或符号模版错误:' + e.__str__(), style=wx.OK)
        else:
            wx.MessageBox(u'该正则可用于该符号模版', style=wx.OK)
        event.Skip()

    def clickrunbutton(self, event):
        runautocreate(self)
        event.Skip()

    def clickhelpbutton(self, event):
        wx.MessageBox(u'本工具可生成形如:\nA\tL\t20.0\nA\tD_CONV_STATUS_ZONE_A.Status[1].INFO.Jam\n=\tDB300.DBX0.0\n'
                      u'的STL语句,其中输送线序号和bit位会自动叠加\n'
                      u'默认符号模版的正则表达式为:\n(.+\\[).+(\\].+)', style=wx.OK)
        event.Skip()


###########################################################################
## Class readfromfilepanel
###########################################################################

class readFromFilePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=(screen_width, screen_height),
                          style=wx.TAB_TRAVERSAL)

        gSizer1 = wx.GridSizer(0, 3, 0, 0)

        self.firstcontext = wx.StaticText(self, wx.ID_ANY, u"第一行循环文本", wx.DefaultPosition, wx.DefaultSize, 0)
        self.firstcontext.Wrap(-1)
        gSizer1.Add(self.firstcontext, 0, wx.ALL, 5)

        self.firstlinetxt = wx.TextCtrl(self, wx.ID_ANY, u"A    L    20.0", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.firstlinetxt, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.errorbitsymbol = wx.StaticText(self, wx.ID_ANY, u"报警位符号模版", wx.DefaultPosition, wx.DefaultSize, 0)
        self.errorbitsymbol.Wrap(-1)
        gSizer1.Add(self.errorbitsymbol, 0, wx.ALL, 5)

        self.errorbitsymbol = wx.TextCtrl(self, wx.ID_ANY, u"D_CONV_Action.Action[1,1].Jam", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        gSizer1.Add(self.errorbitsymbol, 0, wx.ALL, 5)

        bittypeChoices = [u"常开点", u"常闭点"]
        self.bittype = wx.ComboBox(self, wx.ID_ANY, u"常开点", wx.DefaultPosition, wx.DefaultSize, bittypeChoices, 0)
        self.bittype.SetSelection(0)
        gSizer1.Add(self.bittype, 0, wx.ALL, 5)

        self.thirdcontext = wx.StaticText(self, wx.ID_ANY, u"从文件中读取序号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.thirdcontext.Wrap(-1)
        gSizer1.Add(self.thirdcontext, 0, wx.ALL, 5)

        self.filepicker = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"选择读取文件", u"*.*", wx.DefaultPosition,
                                            wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        gSizer1.Add(self.filepicker, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.fifthcontext = wx.StaticText(self, wx.ID_ANY, u"拆分正则表达式", wx.DefaultPosition, wx.DefaultSize, 0)
        self.fifthcontext.Wrap(-1)
        gSizer1.Add(self.fifthcontext, 0, wx.ALL, 5)

        self.regextxt = wx.TextCtrl(self, wx.ID_ANY, u"(.+\\[).+(\\].+)", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.regextxt, 0, wx.ALL, 5)

        self.testregex = wx.Button(self, wx.ID_ANY, u"测试正则", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.testregex, 0, wx.ALL, 5)

        self.sixthcontext = wx.StaticText(self, wx.ID_ANY, u"目标DB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sixthcontext.Wrap(-1)
        gSizer1.Add(self.sixthcontext, 0, wx.ALL, 5)

        self.destdbnumber = wx.TextCtrl(self, wx.ID_ANY, u"300", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.destdbnumber, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.seventhcontext = wx.StaticText(self, wx.ID_ANY, u"目标开始位", wx.DefaultPosition, wx.DefaultSize, 0)
        self.seventhcontext.Wrap(-1)
        gSizer1.Add(self.seventhcontext, 0, wx.ALL, 5)

        self.deststartbit = wx.TextCtrl(self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.deststartbit, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        button = wx.StdDialogButtonSizer()
        self.buttonApply = wx.Button(self, wx.ID_APPLY)
        button.AddButton(self.buttonApply)
        self.buttonHelp = wx.Button(self, wx.ID_HELP)
        button.AddButton(self.buttonHelp)
        button.Realize()

        gSizer1.Add(button, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        # Connect Events
        self.testregex.Bind(wx.EVT_BUTTON, self.testregexbutton)
        self.buttonApply.Bind(wx.EVT_BUTTON, self.clickrunbutton)
        self.buttonHelp.Bind(wx.EVT_BUTTON, self.clickhelpbutton)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def testregexbutton(self, event):
        try:
            testregexisok(self)
        except Exception as e:
            wx.MessageBox(u'正则或符号模版错误:' + e.__str__(), style=wx.OK)
        else:
            wx.MessageBox(u'该正则可用于该符号模版', style=wx.OK)
        event.Skip()

    def clickrunbutton(self, event):
        runcreatefromfile(self)
        event.Skip()

    def clickhelpbutton(self, event):
        wx.MessageBox(u'本工具可生成形如:\nA\tL\t20.0\nA\tD_CONV_STATUS_ZONE_A.Status[1].INFO.Jam\n=\tDB300.DBX0.0\n'
                      u'的STL语句,其中输送线序号和bit位会自动叠加\n'
                      u'默认符号模版的正则表达式为:\n(.+\\[).+(\\].+)', style=wx.OK)
        event.Skip()


###########################################################################
## Class ResultFrame
###########################################################################

class ResultFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Result", pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.VSCROLL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.resultcontext = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                      wx.DefaultSize,
                                                      0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        bSizer2.Add(self.resultcontext, 1, wx.EXPAND | wx.ALL, 5)

        self.savetoclipboard = wx.Button(self, wx.ID_ANY, u"保存到剪切板", wx.DefaultPosition, wx.DefaultSize, 0)
        self.savetoclipboard.SetDefault()
        bSizer2.Add(self.savetoclipboard, 0, wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.clickclosewindow)
        self.savetoclipboard.Bind(wx.EVT_BUTTON, self.cilcksave2clipboard)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def clickclosewindow(self, event):
        self.Destroy()
        event.Skip()

    def cilcksave2clipboard(self, event):
        copy2clipboard(self)
        event.Skip()


def copy2clipboard(myframe):
    clipboard.copy(myframe.resultcontext.GetValue())
    wx.MessageBox('复制成功', style=wx.OK)
    pass


def testregexisok(myframe):
    errorbitsymbol = myframe.errorbitsymbol.Value
    regex = re.compile(myframe.regextxt.Value)
    symbol1 = re.match(regex, errorbitsymbol).group(1)
    symbol2 = re.match(regex, errorbitsymbol).group(2)
    return symbol1, symbol2


def runautocreate(mypanel):
    try:
        string = ''
        symbol1, symbol2 = testregexisok(mypanel)
        firstlinetxt = mypanel.firstlinetxt.Value
        bittype = 'A' if mypanel.bittype.Value == u'常开点' else 'AN'
        seqnumberbegin, seqnumberend = map(int, str(mypanel.seqnumberbeginandend.Value).split(','))
        seqnumberstep = int(mypanel.seqnumberstep.Value)
        destdbnumber = mypanel.destdbnumber.Value
        destbit = float(mypanel.deststartbit.Value)
        if destbit - math.floor(destbit) >= 0.71:
            raise Exception('初始位输入值超范围!')
        i = seqnumberbegin
        while i <= seqnumberend:
            string += '%s\n%s\t%s%s%s\n=\tDB%s.DBX%.1f\n' % (firstlinetxt, bittype, symbol1, i, symbol2,
                                                             destdbnumber, destbit)
            destbit += 0.1
            # plc位为8进制，此处因为浮点数精度问题，只要大于0.7就认为到0.8了
            if destbit - math.floor(destbit) >= 0.71:
                destbit = math.ceil(destbit)
            i += seqnumberstep
        mypanel.deststartbit.Value = '%.1f' % destbit
        resultframe = ResultFrame(mypanel)
        resultframe.resultcontext.Clear()
        resultframe.resultcontext.SetValue(string)
        resultframe.Show()
    except Exception as e:
        wx.MessageBox('输入值有误:' + e.__str__(), style=wx.OK)


def runcreatefromfile(mypanel):
    try:
        with open(mypanel.filepicker.GetPath(), 'r') as file:
            string = ''
            symbol1, symbol2 = testregexisok(mypanel)
            firstlinetxt = mypanel.firstlinetxt.Value
            bittype = 'A' if mypanel.bittype.Value == u'常开点' else 'AN'
            destdbnumber = mypanel.destdbnumber.Value
            destbit = float(mypanel.deststartbit.Value)
            if destbit - math.floor(destbit) >= 0.71:
                raise Exception('初始位输入值超范围!')
            while True:
                i = file.readline().strip()
                if i == '':
                    break
                string += '%s\n%s\t%s%s%s\n=\tDB%s.DBX%.1f\n' % (firstlinetxt, bittype, symbol1, i, symbol2,
                                                                 destdbnumber, destbit)
                destbit += 0.1
                # plc位为8进制，此处因为浮点数精度问题，只要大于0.7就认为到0.8了
                if destbit - math.floor(destbit) >= 0.71:
                    destbit = math.ceil(destbit)
            mypanel.deststartbit.Value = '%.1f' % destbit
            resultframe = ResultFrame(mypanel)
            resultframe.resultcontext.Clear()
            resultframe.resultcontext.SetValue(string)
            resultframe.Show()
    except Exception as e:
        wx.MessageBox('输入值有误:' + e.__str__(), style=wx.OK)


if __name__ == '__main__':
    app = wx.App()
    screen_width = wx.DisplaySize()[0]
    screen_height = wx.DisplaySize()[1]
    frame = ConfigFrame(None)
    frame.Show()
    app.MainLoop()
