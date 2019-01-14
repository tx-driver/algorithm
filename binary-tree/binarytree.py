from collections import deque

def make_binarytree(depth):
	tree = []
	for i in range(1, 2**(depth+1)-2, 2):
		tree.append([i, i+1])
	return tree

class DFS():
	def __init__(self, tree):
		self.tree = tree
	
	def preorder_wi_recursive(self, parent):
		def _inner(parent):
			print(parent, '', end='')
			if parent > len(self.tree) - 1: return
			_inner(self.tree[parent][0])
			_inner(self.tree[parent][1])
		_inner(parent)
		print()

	def inorder_wi_recursive(self, parent):
		def _inner(parent):
			if parent > len(self.tree) - 1:
				print(parent, '', end='')
				return
			_inner(self.tree[parent][0])
			print(parent, '', end='')
			_inner(self.tree[parent][1])
		_inner(parent)
		print()

	def postorder_wi_recursive(self, parent):
		def _inner(parent):
			if parent > len(self.tree) - 1:
				print(parent, '', end='')
				return
			_inner(self.tree[parent][0])
			_inner(self.tree[parent][1])
			print(parent, '', end='')
		_inner(parent)
		print()
	
	def preorder_wo_recursive(self, parent):
		stack = deque()
		stack.append(parent)
		while len(stack) is not 0:
			parent = stack[-1]
			stack.pop()
			print(parent, '', end='')
			if parent < len(self.tree):
				stack.append(self.tree[parent][1])
				stack.append(self.tree[parent][0])
		print()

	def inorder_wo_recursive(self, parent):
		stack = deque()
		prev = deque()
		stack.append(parent)
		while len(stack) is not 0:
			parent = stack[-1]
			stack.pop()
			if parent < len(self.tree):
				prev.append(parent)
				stack.append(self.tree[parent][1])
				stack.append(self.tree[parent][0])
			else:
				print(parent, '', end='')
				if len(prev):
					print(prev.pop(), '', end='')
		print()

	def postorder_wo_recursive(self, parent):
		stack = deque()
		prev = deque()
		stack.append(parent)
		while len(stack) is not 0:
			parent = stack[-1]
			stack.pop()
			if parent < len(self.tree):
				left = self.tree[parent][0]
				right = self.tree[parent][1]
				prev.append(parent)
				prev.append(right)
				stack.append(right)
				stack.append(left)
			else:
				print(parent, '', end='')
				if len(prev):
					if parent == prev[-1]:
						prev.pop()
						print(prev.pop(), '', end='')
		print(prev[-2], '', end='')
		print()

if __name__ == '__main__':
	depth = 2
	dfs = DFS(make_binarytree(depth))
	print(dfs.tree)
	dfs.preorder_wi_recursive(0)
	dfs.inorder_wi_recursive(0)
	dfs.postorder_wi_recursive(0)
	dfs.preorder_wo_recursive(0)
	dfs.inorder_wo_recursive(0)
	dfs.postorder_wo_recursive(0)