class TreeNode:
    pass


def in_order_tree_walk(x):
    if x is not None:
        in_order_tree_walk(x.left)
        print(x.key)
        in_order_tree_walk(x.right)


