# 이진 트리의 4가지 순회 방식

# 1. 전위순회
def preorder(self,n):
    if n!= None:
        print(n.item,'',end="") # 노드 방문
        if n.left:
            self.preorder(n.left) # 왼쪽 서브트리 순회
        if n.right:
            self.preorder(n.right) # 오른쪽 서브트리 순회

# 2. 중위순회
def inorder(self,n):
    if n!= None:
        if n.left:
            self.preorder(n.left) # 왼쪽 서브트리 순회
        print(n.item,'',end="") # 노드 방문
        if n.right:
            self.preorder(n.right) # 오른쪽 서브트리 순회

# 3. 후위순회
def postorder(self,n):
    if n!= None:
        if n.left:
            self.preorder(n.left) # 왼쪽 서브트리 순회
        if n.right:
            self.preorder(n.right) # 오른쪽 서브트리 순회
        print(n.item,'',end="") # 노드 방문

# 4. 레벨 순회
def levelorder(self,root):
    q = [] # 리스트 구현(큐로 사용하기 위해)
    q.append(root)
    while q:
        t = q.pop(0)
        print(t.item,'',end="") # 큐에서 첫 항목 삭제하고 삭제한 노드 방문
        if t.left != None:
            q.append(t.left) # 왼족 자식 큐에 삽입
        if t.right != None:
            q.append(t.right) # 오른쪽 자식 큐에 삽입 