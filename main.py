# 这是一个示例 Python 脚本。
# import itchat

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import urllib3
from urllib3.exceptions import ProtocolError
import itchat

# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

import itchat
from itchat.content import *
import tkinter as tk
from tkinter import messagebox


# 定义一个处理文本消息的函数
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def print_received_message(msg):
    print("收到一条消息：")
    print("发送者昵称：", msg['User']['NickName'])
    print("消息内容：", msg['Text'])
    # 关注某好友的信息，当该好友发信息时，直接在当前页面弹出消息窗口
    if msg['User']['NickName'] == 'xxxxx':
        # 初始化Tkinter
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        # 弹出消息窗口
        messagebox.showinfo(f"{msg['User']['NickName']}发来消息", msg['Text'])
        # 启动事件循环
        root.mainloop()


@itchat.msg_register(TEXT, isGroupChat=True)
def print_received_message(msg):
    print("收到一条群消息：")
    print("发送者昵称：", msg.actualNickName)
    print("消息内容：", msg['Text'])


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def print_recording(msg):
    # 下载文件
    msg.download(msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


http = urllib3.PoolManager()

try:
    # 尝试连接到服务器
    response = http.request('GET', 'http://www.baidu.com')
except ProtocolError as e:
    print(f"An error occurred: {e}")
else:
    # 如果连接成功，使用 itchat 发送消息
    itchat.auto_login(hotReload=True)
    itchat.send('Hello, friend!', toUserName='xxxxxxx')
    itchat.run()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
