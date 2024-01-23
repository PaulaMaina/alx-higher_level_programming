#!/usr/bin/python3
"""Definition of a Node class for a linked list"""


class Node:
    """Defines a node"""
    def __init__(self, data, next_node=None):
        """Initiates the node with data and next_node"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not (next_node is None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data with a value

            Args:
                value: value to be assigned to data
            Raise:
                TypeError: the value is not an integer
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of the node

            Args:
                value: value to be assigned to the next node
        """
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Definition of a singly linked list"""
    def __init__(self):
        """Initializes the singly linked list"""
        self.__head = None

    def __str__(self):
        """Returns a string with all data in the list"""
        temp = self.__head
        data_n = []
        while (temp is not None):
            data_n.append("{}".format(temp.data))
            temp = temp.next_node
        return "\n".join(data_n)

    def sorted_insert(self, value):
        """Insert a new node"""
        temp = self.__head
        new_node = Node(value)
        if temp is None:
            self.__head = new_node
            return
        if value < temp.data:
            new_node.next_node = temp
            self.__head = new_node
            return
        while (temp.next_node is not None and value > temp.next_node.data):
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
