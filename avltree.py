class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.size = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.__nodesCount = 0
        self.__root = None

    def find(self, value):
        return self.__contains(self.__root, value)

    def __contains(self, node, target):
        if node is None:
            return False
        if node.value == target:
            return True
        if target > node.value:
            return self.__contains(node.right, target)
        else:
            return self.__contains(node.left, target)

    def insert(self, value):
        if value is None:
            return False
        if self.find(value):
            return False
        else:
            self.__root = self.__insert(self.__root, value)
            self.__nodesCount += 1
            return True

    def __insert(self, node, target):
        if node is None:
            return Node(target)

        if target > node.value:
            node.right = self.__insert(node.right, target)
        else:
            node.left = self.__insert(node.left, target)

        node.height = 1 + max(self.__height(node.left), self.__height(node.right))
        node.size = 1 + self.__size(node.left) + self.__size(node.right)

        return self.__balance(node)

    def __height(self, node):
        return node.height if node else 0

    def __size(self, node):
        return node.size if node else 0

    def __balance(self, node):
        if node is None:
            return node

        balance = self.__height(node.left) - self.__height(node.right)

        if balance > 1:
            if node.left and node.left.value > node.value:
                return self.__rotateRight(node)
            else:
                if node.left:
                    node.left = self.__rotateLeft(node.left)
                return self.__rotateRight(node)

        if balance < -1:
            if node.right and node.right.value < node.value:
                return self.__rotateLeft(node)
            else:
                if node.right:
                    node.right = self.__rotateRight(node.right)
                return self.__rotateLeft(node)

        return node

    def __rotateRight(self, node):
        B = node.left
        if B is None:
            return node  # No need to rotate if B is None

        node.left = B.right
        if B.right:
            B.right = node

        node.height = 1 + max(self.__height(node.left), self.__height(node.right))
        node.size = 1 + self.__size(node.left) + self.__size(node.right)

        B.height = 1 + max(self.__height(B.left), self.__height(B.right))
        B.size = 1 + self.__size(B.left) + self.__size(B.right)

        return B

    def __rotateLeft(self, node):
        B = node.right
        if B is None:
            return node  # No need to rotate if B is None

        node.right = B.left
        if B.left:
            B.left = node

        node.height = 1 + max(self.__height(node.left), self.__height(node.right))
        node.size = 1 + self.__size(node.left) + self.__size(node.right)

        B.height = 1 + max(self.__height(B.left), self.__height(B.right))
        B.size = 1 + self.__size(B.left) + self.__size(B.right)

        return B

    def __minNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, value):
        if self.find(value):
            self.__root = self.__remove(self.__root, value)
            self.__nodesCount -= 1
            return True
        return False

    def __remove(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.__remove(node.left, value)
        elif value > node.value:
            node.right = self.__remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.__minNode(node.right)
            node.value = temp.value
            node.right = self.__remove(node.right, temp.value)

        node.height = 1 + max(self.__height(node.left), self.__height(node.right))
        node.size = 1 + self.__size(node.left) + self.__size(node.right)

        return self.__balance(node)

    def order_of_key(self, value):
        return self.__orderOfKey(self.__root, value)

    def __orderOfKey(self, node, value):
        if node is None:
            return 0
        if value <= node.value:
            return self.__orderOfKey(node.left, value)
        else:
            return self.__size(node.left) + 1 + self.__orderOfKey(node.right, value)

    def get_by_order(self, k):
        return self.__getByOrder(self.__root, k)

    def __getByOrder(self, node, k):
        if node is None:
            return -1
        left_size = self.__size(node.left)
        if k <= left_size:
            return self.__getByOrder(node.left, k)
        elif k == left_size + 1:
            return node.value
        else:
            return self.__getByOrder(node.right, k - left_size - 1)


avl = AVLTree()
avl.insert(10)
avl.insert(20)
avl.insert(30)
print(avl.find(10))  # True
avl.remove(10)
print(avl.find(10))  # False
print(avl.order_of_key(20))  # 1
print(avl.get_by_order(2))  # 30
