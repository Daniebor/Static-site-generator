class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        string = ""
        if self.props == None:
            return string
        
        for key, value in self.props.items():
            string += f'{key}="{value}" '

        return string[:-1]
    
    def __repr__(self):
        return f"HTLMNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("All leaf nodes require a value!")
        
        if self.tag == None or self.tag == "":
            return self.value
        
        props_html = self.props_to_html()

        if props_html == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
