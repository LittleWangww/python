#!/usr/bin/env python3

from tkinter import *

#定义框架
#布局学习参照 https://www.jianshu.com/p/8731df25602c
def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

#统一按钮样式和风格
def button(root, side, text, command = None):
    w = Button(root, text=text, font=('aril',12), command=command)
    w.pack(side = side, expand = YES, fill = BOTH)
    return w



#继承Frame类，初始化程序界面的布局
class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        # self.oprion_add('*Font', 'Verdana 12 bold')
        self.option_add('*Font', 'Verdana 12 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('简易计算器')
        self.master.iconname('calc1')

        display = StringVar()
        # 定义显示数字结果的文本框
        Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)
        # 添加横条型框架以及里面的按钮
        for key in ('123', '456', '789', '+0.'):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w=display, c=char: w.set(w.get() + c))
        opsF = frame(self, TOP)

        for char in '-*/=':
            if char == '=':
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, LEFT, char, lambda w=display, s='%s ' % char: w.set(w.get() + s))

        # 定义清除按钮
        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, '清除', lambda w=display: w.set(''))


    # 调用eval函数计算表达式的值
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set('ERROR')

#程序入口
if __name__ == '__main__':
    Calculator().mainloop()
