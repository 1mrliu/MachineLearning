# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/16 3:33 PM'
from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005
NAME = 'TestChat'

class ChatSession(async_chat):
    """
    一个负责处理服务器和单个用户间连接的类
    """
    def __init__(self, server, sock):
        # 标准的设置任务
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []
        # 问候用户
        self.push('Welcome to %s\r\n'% self.server.name)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        """
        如果遇到结束符，就意味着读取了一整行
        因此将这行内容广播给每个人
        :return:
        """
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

class ChatServer(dispatcher):
    """
    一个接受连接并创建会话的类。它还负责向这些会话广播
    """
    def __init__(self, port, name):
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.name = name
        self.sessions = []

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line + '\r\n')

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(self, conn))

if __name__ == "__main__":
    s = ChatServer(PORT, NAME)
    try:asyncore.loop()
    except KeyboardInterrupt:
        print()