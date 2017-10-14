import Constant


class Tree:
    
    def __init__(self):
        self.child_counts=0
        self.child_nodes=[]
        self.tag=''
        self.value=''
        self.parent_node=None
        self.is_leaf=False
        self.is_root=False
        
    def add_child(self,child_nodes):
        self.child_nodes.append(child_nodes)
    
    def set_tag(self,tag):
        self.tag=tag
    
    def set_value(self,value):
        self.value=value
    
    def set_parent_node(self,parent_node):
        self.parent_node=parent_node
        
    def set_is_leaf(self,is_leaf):
        self.is_leaf=is_leaf
    
    def set_is_root(self,is_root):
        self.is_root=is_root
    

class Tree_Parser:
    
    def extract_children_nodes(self,value):
        left_bracket_count=0
        has_left_bracket=False
        start_index=0
        end_index=0
        children_nodes_list=[]
        for i,char in enumerate(value):
            if char == Constant.left_parentheses:
                if left_bracket_count == 0:
                    start_index=i
                has_left_bracket=True
                left_bracket_count+=1
            if char == Constant.right_parentheses:
                left_bracket_count-=1
                if left_bracket_count == 0:
                    end_index=i+1
            if (left_bracket_count == 0 and char != Constant.space 
                and has_left_bracket):
                children_nodes_list.append(value[start_index:end_index])

        return children_nodes_list,len(children_nodes_list)

    def get_tag_value(self,constituencyTree):
        tagStr=''
        valueStartIndex = 0
        valueEndIndex = 0
        leftBracketCount = 0
        gotTag=False
        for i,char in enumerate(constituencyTree):
            if char == Constant.left_parentheses:
                leftBracketCount+=1
                if not gotTag:
                    tag=True
                    continue
            if char == Constant.right_parentheses:
                leftBracketCount-=1
            if char == Constant.space and not gotTag:
                tag=False
                gotTag=True;
                valueStartIndex = i+1
            if leftBracketCount == 0:
                valueEndIndex = i
            if tag == True:
                tagStr+=char
        return tagStr,constituencyTree[valueStartIndex:valueEndIndex]
    
    def create_tree(self,parent_tree,constituency_tree):
        if len(constituency_tree)==0:
            return
        tree_node=Tree()
        if parent_tree is None:
            tree_node.set_is_root(True)
        tag,value=self.get_tag_value(constituency_tree)
        tree_node.set_tag(tag)
        tree_node.set_value(value)
        tree_node.set_parent_node(parent_tree)
        children_nodes_value,child_nodes_count=self.extract_children_nodes(value)
        if child_nodes_count == 0:
            tree_node.set_is_leaf(True)
        for child_value in children_nodes_value:
            tree_node.add_child((self.create_tree(tree_node,child_value)))
    
        return tree_node
        

