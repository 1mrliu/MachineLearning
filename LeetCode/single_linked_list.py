# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/10/14 2:42 PM'
'''
单链表
 1.Insert、 delete 、 search  of single-linked list
 2.int type in list node
'''

from typing import Optional

class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self._next = next

class SinglyLinkedList:

    def __init__(self):
        self._head = None

    def find_by_value(self, value:int) -> Optional[Node]:
        p = self._head
        while p and p.data != value:
            p = p._next
        return p

    def find_by_index(self, index: int) -> Optional[Node]:
        p = self._head
        position = 0
        while p and position != index:
            p = p._next
            position += 1
        return p

    def insert_value_to_head(self, value: int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: Node):
        if new_node:
            new_node._next = self._head
            self._head = new_node

    def insert_value_after(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_after(self, node: Node, new_node: Node):
        if not node or not new_node:
            return
        new_node._next = node._next
        node._next = new_node

    def insert_value_before(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        if not self._head or not node or not new_node:
             return
        if self._head == node:
            self.insert_node_to_head(new_node)
            return
        current = self._head
        while current._next and current._next != node:
            current = current._next
        if not current._next:
            return
        new_node._next = node
        current._next = new_node

    def delete_by_node(self, node: Node):
        if not self._head or not node:
            return
        if node._next:
            node.data = node._next.data
            node._next = node._next._next
            return
        current  = self._head
        while current and current._next != node:
            current = current._next
        if not current: # node not in the list
            return
        current._next = None

    def delete_by_value(self, value:int):
        if not self._head or not value:
            return
        fake_head = Node(value + 1)
        fake_head._next = self._head
        prev, current = fake_head, self._head
        while current:
            if current.data != value:
                prev._next = current
                prev = prev._next
            current = current._next
        if prev._next:
            prev._next = None
        self._head = fake_head._next

    '''
    __repr__方法是属于__str__的
    输出对象的时候，输出的是__repr__中的数据
    如果有__str__的时候，先输出__str__的数据
    
    '''
    def __repr__(self) -> str:
        nums = []
        current = self._head
        while current:
            nums.append(current.data)
            current = current._next
        if len(nums) > 0:
            return "->".join(str(num) for num in nums)
        else:
            return ""

    def print_all(self):
        current = self._head
        if current:
            print(f"{current.data}", end="")
            current = current._next
        while current:
            print(f"->{current.data}", end="")
            current = current._next
        print("\n", flush=True)

if __name__ == "__main__":
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_value_to_head(i)
    node9 = l.find_by_value(9)
    l.insert_value_before(node9,20)
    l.insert_value_before(node9,16)
    l.insert_value_before(node9,16)
    l.delete_by_value(16)
    node11 = l.find_by_index(3)
    l.delete_by_node(node11)
    l.delete_by_node(l._head)
    l.delete_by_value(13)
    print(l)