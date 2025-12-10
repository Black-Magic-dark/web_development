class Trienode:
   def __init__(self):
      self.children={}
      self.is_end=False


class Trie:
   def __init__(self):
       self.root=Trienode()
#    Insert word into trie
    
   def insert(self,word:str):
      node=self.root
      for char in word :
         if char not in node.children:
            node.children[char]=Trienode()
         node=node.children[char]
      node.is_end=True
      
    #   search
   def search(self,word:str) -> bool:
      node=self.root
      for char in word :
         if char not in node.children:
            return False
         node=node.children[char]
      return node.is_end
   
# search for prefix
   def startswith(self,word:str) -> bool:
      node=self.root
      for char in word :
         if char not in node.children:
            return False
         node=node.children[char]
      return True

trie=Trie()
trie.insert("apple")
trie.insert("apps")
print(trie.search("app"))
print(trie.search("asp"))
print(trie.startswith("pl"))
          
   
       

