from tkinter import *
import numpy as np
import decimal


# 将text内容转换为矩阵形式便于计算
def split(string_list):
    string_list = string_list.split(';')
    for i in range(len(string_list)):
        string_list[i] = string_list[i].split()
    string_list = np.array(string_list)
    string_list = string_list.astype(int)
    return string_list


'''
def get_input():
    global text1_input, text2_input
    text1_input = split(text1.get('0.0', 'end'))
    text2_input = split(text2.get('0.0', 'end'))
'''


# 加法
def add_function():
    text1_input = split(text1.get('0.0', 'end'))
    text2_input = split(text2.get('0.0', 'end'))
    if text1_input.shape == text2_input.shape:
        add_result = text1_input + text2_input
        print(add_result)
        vartext.set(add_result)
    else:
        vartext.set('ERROR！')


# 减法
def minus_function():
    text1_input = split(text1.get('0.0', 'end'))
    text2_input = split(text2.get('0.0', 'end'))
    if text1_input.shape == text2_input.shape:
        minus_result = text1_input - text2_input
        print(minus_result)
        vartext.set(minus_result)
    else:
        vartext.set('ERROR！')


# 两矩阵乘法
def mul_function():
    text1_input = split(text1.get('0.0', 'end'))
    text2_input = split(text2.get('0.0', 'end'))
    if text1_input.shape[1] == text2_input.shape[0]:
        mul_result = np.zeros(shape=(text1_input.shape[0], text2_input.shape[1]))
        for i in range(0, text1_input.shape[0]):
            for j in range(0, text2_input.shape[1]):
                for m in range(0, text1_input.shape[1]):
                    mul_result[i][j] = mul_result[i][j] + text1_input[i][m] * text2_input[m][j]
        print(mul_result)
        vartext.set(mul_result)
    else:
        vartext.set('ERROR！')


# 数乘
def num_mul_function():
    text1_input = split(text1.get('0.0', 'end'))
    try:
        entry1_input = float(entry1.get())
        for i in range(0, text1_input.shape[0]):
            for j in range(0, text1_input.shape[1]):
                text1_input[i][j] = text1_input[i][j] * entry1_input
        print(text1_input)
        vartext.set(text1_input)
    except ValueError:
        vartext.set('ERROR！')

# 转置
def trans_function():
    text1_input = split(text1.get('0.0', 'end'))
    trans_result = np.zeros(shape=(text1_input.shape[1], text1_input.shape[0]))
    for i in range(0, trans_result.shape[0]):
        for j in range(0, trans_result.shape[1]):
            trans_result[i][j] = text1_input[j][i]
    print(trans_result)
    vartext.set(trans_result)


# 幂运算
def exponent_function():
    text1_input = split(text1.get('0.0', 'end'))
    try:
        if float(entry1.get()) == int(entry1.get()):
            entry1_input = int(entry1.get())
            if text1_input.shape[0] == text1_input.shape[1]:  # 方阵才可以幂运算
                exponent_result = text1_input
                while entry1_input - 1 > 0:
                    exponent_result = np.dot(exponent_result, text1_input)
                    entry1_input = entry1_input - 1
                print(exponent_result)
                vartext.set(exponent_result)
            else:
                vartext.set('ERROR！')
        else:
            vartext.set('ERROR！')
    except ValueError:
        vartext.set('ERROR')


# 计算行列式
def det_function():
    text1_input = split(text1.get('0.0', 'end'))
    if text1_input.shape[0] == text1_input.shape[1]:
        det_result = np.linalg.det(text1_input)
        print(det_result)
        vartext.set(det_result)
    else:
        vartext.set('ERROR！')


# 求逆矩阵
def inv_function():
    text1_input = split(text1.get('0.0', 'end'))
    try:
        if text1_input.shape[0] == text1_input.shape[1]:
            inv_result = np.linalg.inv(text1_input)
            inv_result = np.round(inv_result, decimals=3)
            print(inv_result)
            vartext.set(inv_result)
        else:
            vartext.set('ERROR！')
    except np.linalg.linalg.LinAlgError:
        vartext.set('Singular matrix！')


# 求特征值
def eig_function():
    text1_input = split(text1.get('0.0', 'end'))
    if text1_input.shape[0] == text1_input.shape[1]:
        eig_zhi, eig_vector = np.linalg.eig(text1_input)
        eig_zhi = np.round(eig_zhi, 3)
        print(list)
        print(eig_zhi)
        print(eig_vector)
        vartext.set(eig_zhi)
    else:
        vartext.set('ERROR！')


# 初始化Tk
root = Tk()

vartext = StringVar()

# 设置窗口标题
root.title('矩阵计算器')

# 输入提示文字
Label(root, text='输入矩阵A ：').grid(row=0, column=1, columnspan=3, sticky=W)
Label(root, text='输入矩阵B ：').grid(row=0, column=4, columnspan=3, sticky=W)

# 可输入控件(A,B输入格)
text1 = Text(root, width=25, height=12)
text1.grid(row=1, rowspan=3, column=0, columnspan=3, padx=8, sticky=E)
# np_tex1 = split(text1.get('0.0', 'end'))
# print(np_tex1)
text2 = Text(root, width=25, height=12)
text2.grid(row=1, rowspan=3, column=3, columnspan=3, padx=8, sticky=E)
# np_text2 = split(text2.get('0.0', 'end'))

# 用于隔开不同控件
Label(root).grid(row=4, column=0, columnspan=3)

# 输出提示文字和数乘输入提示文字
Label(root, text='计算输出矩阵：').grid(row=6, column=0, columnspan=3, sticky=W)     # 靠左
Label(root, text='输入数字a ：').grid(row=5, column=3, sticky=E)     # 靠右

label_warn = Label(root, text='注意：1.输入矩阵用空格隔开同一行的不同元素，加英文分号表示开始下一行\n2.特征值按钮只能输出特征值不出现特征向量')
label_warn.grid(row=10, column=0, columnspan=6)

# 可输入控件(数乘输入a，x）
entry1 = Entry(root)
entry1.grid(row=5, column=4, columnspan=2)

# 设置窗口大小
root.geometry('420x500')

# 设置窗口是否可以变化长/宽
root.resizable(width=False, height=False)

# 用作输出框，内容可变
Label(root, width=24, height=10, bg='white', textvariable=vartext).grid(row=7, rowspan=3, column=0,
                                                                          columnspan=3, sticky=N)
# 生成button，功能表
buttonADD = Button(root, text='A+B', width=9, height=3, command=add_function)
buttonMINUS = Button(root, text='A-B', width=9, height=3, command=minus_function)
buttonMUL = Button(root, text='A*B', width=9, height=3, command=mul_function)
buttonAa = Button(root, text='aA', width=9, height=3, command=num_mul_function)
buttonTRANS = Button(root, text='transA', width=9, height=3, command=trans_function)
buttonEX = Button(root, text='A^x', width=9, height=3, command=exponent_function)
buttonDET = Button(root, text='|A|', width=9, height=3, command=det_function)
buttonINV = Button(root, text='invA', width=9, height=3, command=inv_function)
buttonEIG = Button(root, text='EIG', width=9, height=3, command=eig_function)
buttonADD.grid(row=7, column=3)
buttonMINUS.grid(row=7, column=4)
buttonMUL.grid(row=7, column=5)
buttonAa.grid(row=8, column=3)
buttonTRANS.grid(row=8, column=4)
buttonEX.grid(row=8, column=5)
buttonDET.grid(row=9, column=3)
buttonINV.grid(row=9, column=4)
buttonEIG.grid(row=9, column=5)

# 进入消息循环
root.mainloop()



