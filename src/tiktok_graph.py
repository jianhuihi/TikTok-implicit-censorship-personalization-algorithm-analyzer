class TikTokNode():
    def __init__(self, tiktok, subtitles):
        self.tiktok = tiktok
        self.subtitles = subtitles

class TikTokGraph():
    def __init__(self):
        self.edges = []
        self.nodes = []
    
    def add_node(self, node: TikTokNode):
        self.nodes.append(node)

    def add_edge(self, src: TikTokNode, dst: TikTokNode):
        self.edges.append([src, dst])
    