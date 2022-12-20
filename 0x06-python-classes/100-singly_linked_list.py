#!/usr/bin/python3
"""
No modules imported
"""


class Node:
    """
    class that generates the next new node instance
    """
    def __init__(self, data, next_node=None):
        """
        method that helps us define the properties of object summary
        Args:
            data (int): the new data attributes
            next_node (int): the next new node of the data attributes
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        method that retrieves the new instance
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        method that sets the new instance
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        method that retrieves the new instance
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        methods that sets the new instance
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    class that generate a instace of singlylinked list
    """
    def __init__(self):
        """
        initialize a new singlylinked list
        """
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while current_node.next_node is not None and current_node.next_node.data < value:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        current_node = self.__head
        result = []
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(result)
