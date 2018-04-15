# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx, wx.xrc, wx.richtext
import re, math, clipboard


###########################################################################
## Class ConfigFrame
###########################################################################


class ConfigFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Step7 StlCreator V0.1", pos=wx.DefaultPosition,
                          size=wx.Size(601, 434), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        g_sizer1 = wx.GridSizer(0, 3, 0, 0)

        self.firstcontext = wx.StaticText(self, wx.ID_ANY, u"第一行循环文本", wx.DefaultPosition, wx.DefaultSize, 0)
        self.firstcontext.Wrap(-1)
        g_sizer1.Add(self.firstcontext, 0, wx.ALL, 5)

        self.firstlinetxt = wx.TextCtrl(self, wx.ID_ANY, u"A    L    20.0", wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer1.Add(self.firstlinetxt, 0, wx.ALL, 5)

        g_sizer1.AddSpacer(1)

        self.sencondcontext = wx.StaticText(self, wx.ID_ANY, u"报警位符号模版", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sencondcontext.Wrap(-1)
        g_sizer1.Add(self.sencondcontext, 0, wx.ALL, 5)

        self.errorbitsymbol = wx.TextCtrl(self, wx.ID_ANY, u"D_CONV_STATUS_ZONE_A.Status[1].INFO.Jam",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer1.Add(self.errorbitsymbol, 0, wx.ALL, 5)

        bittype_choices = [u"常开点", u"常闭点"]
        self.bittype = wx.ComboBox(self, wx.ID_ANY, u"常开点", wx.DefaultPosition, wx.DefaultSize, bittype_choices, 0)
        self.bittype.SetSelection(0)
        g_sizer1.Add(self.bittype, 0, wx.ALL, 5)

        self.thirdcontext = wx.StaticText(self, wx.ID_ANY, u"输送线起止序号(逗号分割)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.thirdcontext.Wrap(-1)
        g_sizer1.Add(self.thirdcontext, 0, wx.ALL, 5)

        self.seqnumberbeginandend = wx.TextCtrl(self, wx.ID_ANY, u"1,30", wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer1.Add(self.seqnumberbeginandend, 0, wx.ALL, 5)

        g_sizer1.AddSpacer(1)

        self.forthcontext = wx.StaticText(self, wx.ID_ANY, u"输送线序号步长", wx.DefaultPosition, wx.DefaultSize, 0)
        self.forthcontext.Wrap(-1)
        g_sizer1.Add(self.forthcontext, 0, wx.ALL, 5)

        self.seqnumberstep = wx.TextCtrl(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer1.Add(self.seqnumberstep, 0, wx.ALL, 5)

        g_sizer1.AddSpacer(1)

        self.fifthcontext = wx.StaticText(self, wx.ID_ANY, u"拆分正则表达式", wx.DefaultPosition, wx.DefaultSize, 0)
        self.fifthcontext.Wrap(-1)
        g_sizer1.Add(self.fifthcontext, 0, wx.ALL, 5)

        self.regextxt = wx.TextCtrl(self, wx.ID_ANY, u"(.+\\[).+(\\].+)", wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer1.Add(self.regextxt, 0, wx.ALL, 5)

        self.testregex = wx.Button(self, wx.ID_ANY, u"测试正则", wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer1.Add(self.testregex, 0, wx.ALL, 5)

        self.sixthcontext = wx.StaticText(self, wx.ID_ANY, u"目标DB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sixthcontext.Wrap(-1)
        g_sizer1.Add(self.sixthcontext, 0, wx.ALL, 5)

        self.destdbnumber = wx.TextCtrl(self, wx.ID_ANY, u"300", wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer1.Add(self.destdbnumber, 0, wx.ALL, 5)

        g_sizer1.AddSpacer(1)

        self.seventhcontext = wx.StaticText(self, wx.ID_ANY, u"目标开始位", wx.DefaultPosition, wx.DefaultSize, 0)
        self.seventhcontext.Wrap(-1)
        g_sizer1.Add(self.seventhcontext, 0, wx.ALL, 5)

        self.deststartbit = wx.TextCtrl(self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer1.Add(self.deststartbit, 0, wx.ALL, 5)

        g_sizer1.AddSpacer(1)
        g_sizer1.AddSpacer(1)

        button = wx.StdDialogButtonSizer()
        self.buttonApply = wx.Button(self, wx.ID_APPLY)
        button.AddButton(self.buttonApply)
        self.buttonHelp = wx.Button(self, wx.ID_HELP)
        button.AddButton(self.buttonHelp)
        button.Realize()

        g_sizer1.Add(button, 1, wx.EXPAND, 5)

        self.SetSizer(g_sizer1)
        self.Layout()
        self.m_menu = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem2 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"save", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem2)

        self.m_menuItem3 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"quit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem3)

        self.m_menu.Append(self.m_menu1, u"File")

        self.SetMenuBar(self.m_menu)

        self.Centre(wx.BOTH)

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
        run(self)
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
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Result", pos=wx.DefaultPosition, size=wx.Size(571, 417),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.VSCROLL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        b_sizer2 = wx.BoxSizer(wx.VERTICAL)

        self.resultcontext = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                      wx.DefaultSize,
                                                      0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        b_sizer2.Add(self.resultcontext, 1, wx.EXPAND | wx.ALL, 5)

        self.savetoclipboard = wx.Button(self, wx.ID_ANY, u"保存到剪切板", wx.DefaultPosition, wx.DefaultSize, 0)
        self.savetoclipboard.SetDefault()
        b_sizer2.Add(self.savetoclipboard, 0, wx.ALL, 5)

        self.SetSizer(b_sizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.savetoclipboard.Bind(wx.EVT_BUTTON, self.cilcksave2clipboard)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
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


def run(myframe):
    try:
        string = ''
        symbol1, symbol2 = testregexisok(myframe)
        firstlinetxt = myframe.firstlinetxt.Value
        bittype = 'A' if myframe.bittype.Value == u'常开点' else 'AN'
        seqnumberbegin, seqnumberend = map(int, str(myframe.seqnumberbeginandend.Value).split(','))
        seqnumberstep = int(myframe.seqnumberstep.Value)
        destdbnumber = myframe.destdbnumber.Value
        destbit = float(myframe.deststartbit.Value)
        i = seqnumberbegin
        while i <= seqnumberend:
            # plc位为8进制，此处因为浮点数精度问题，只要大于0.7就认为到0.8了
            if destbit - math.floor(destbit) >= 0.71:
                destbit = math.ceil(destbit)
            string += '%s\n%s\t%s%s%s\n=\tDB%s.DBX%.1f\n' % (firstlinetxt, bittype, symbol1, i, symbol2,
                                                             destdbnumber, destbit)
            destbit += 0.1
            i += seqnumberstep
        myframe.deststartbit.Value = '%.1f' % destbit
        resultframe = ResultFrame(None)
        resultframe.resultcontext.Clear()
        resultframe.resultcontext.SetValue(string)
        resultframe.Show()
    except Exception as e:
        wx.MessageBox('输入值有误:' + e.__str__(), style=wx.OK)


if __name__ == '__main__':
    app = wx.App()
    frame = ConfigFrame(None)
    frame.Show()
    app.MainLoop()
