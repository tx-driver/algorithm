from collections import deque

def make_binarytree(depth):
	tree = []
	for i in range(1, 2**depth-2, 2):
		tree.append([i, i+1])
	return tree

class DFS():
	def __init__(self, tree):
		self.tree = tree
	
	def preorder_wi_recursive(self):
		def _inner(parent):
			print(parent, '', end='')
			if parent > len(self.tree) - 1: return
			_inner(self.tree[parent][0])
			_inner(self.tree[parent][1])
		_inner(0)
		print()

	def inorder_wi_recursive(self):
		def _inner(parent):
			if parent > len(self.tree) - 1:
				print(parent, '', end='')
				return
			_inner(self.tree[parent][0])
			print(parent, '', end='')
			_inner(self.tree[parent][1])
		_inner(0)
		print()

	def postorder_wi_recursive(self):
		def _inner(parent):
			if parent > len(self.tree) - 1:
				print(parent, '', end='')
				return
			_inner(self.tree[parent][0])
			_inner(self.tree[parent][1])
			print(parent, '', end='')
		_inner(0)
		print()
	
	def preorder_wo_recursive(self):
		stack = deque()
		stack.append(0)
		while len(stack) is not 0:
			parent = stack[-1]
			stack.pop()
			print(parent, '', end='')
			if parent < len(self.tree):
				stack.append(self.tree[parent][1])
				stack.append(self.tree[parent][0])
		print()

	def inorder_wo_recursive(self):
		stack = deque()
		prev = deque()
		stack.append(0)
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

	def postorder_wo_recursive(self):
		stack = deque()
		prev = deque()
		stack.append(0)
		while len(stack) is not 0:
			prev.append(stack[-1])
			parent = stack.pop()
			if parent < len(self.tree):
				stack.append(self.tree[parent][0])
				stack.append(self.tree[parent][1])
		prev = list(prev)
		prev.reverse()
		print(' '.join(list(map(str, prev))))

if __name__ == '__main__':
	depth = int(input())
	dfs = DFS(make_binarytree(depth))
	dfs.preorder_wi_recursive()
	dfs.inorder_wi_recursive()
	dfs.postorder_wi_recursive()
	dfs.preorder_wo_recursive()
	dfs.inorder_wo_recursive()
	dfs.postorder_wo_recursive()