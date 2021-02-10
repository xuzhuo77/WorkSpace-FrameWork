import networkx as nx


class SkillTechMapper():
    _skill_tech = {}

    def __init__(self):
        pass

    def set_skill_tech(self, skill_name, tech_name):
        self._skill_tech[skill_name] = tech_name


class TechState():
    DEFALT = 0
    READY = 1
    USING = 2


class Tech():
    def __init__(self, name):
        self.tech_name = name
        self.tech_state = TechState.DEFALT

    def light_node(self):
        self.tech_state = TechState.USING

    def ready_node(self):
        self.tech_state = TechState.READY

    def can_use(self):
        return self.tech_state == TechState.USING


class TechNode(Tech):
    def __init__(self, name):
        super(TechNode, self).__init__(name)


class TechNodeBuild(TechNode):
    def __init__(self):
        super(TechNode, self).__init__("build")


class TechNodeLayEgg(TechNode):
    def __init__(self):
        super(TechNode, self).__init__("layEgg")


class TechNodeResearch(TechNode):
    def __init__(self):
        super(TechNode, self).__init__("research")


class TechTree(nx.DiGraph, SkillTechMapper):
    _node_id = {}
    _name_node = {}

    def __init__(self):
        super(TechTree, self).__init__()

    def get_node_by_skill_name(self, skill_name):
        return self._name_node[self._skill_tech[skill_name]]

    def add_relation(self, node1, node2):
        id1 = self.get_node_id(node1)
        id2 = self.get_node_id(node2)
        self.add_edge(id1, id2)

    def get_node_id(self, node1):
        # new_dict = {v: k for k, v in self._id_nodes.items()}
        if node1 in self._node_id.keys():
            return self._node_id[node1]
        else:
            self._node_id[node1] = len(self._node_id)
            self._name_node[node1.tech_name] = node1
            return len(self._node_id) - 1

    # 使技能可用
    def ligth_node(self, node):
        node.light_node()
        node_id = self.get_node_id(node)
        neighbors = self.neighbors(node_id)
        id_node = self.get_id_node_dict()
        for id in neighbors:
            id_node[id].ready_node()

    def get_id_node_dict(self):
        return {id: node for node, id in self._node_id.items()}

    def show_state(self):
        id_node = self.get_id_node_dict()
        print("list tech state", list([id_node[id].tech_state for id in self.nodes()]))

    def traverse(self):
        for n, nbrs in self.adjacency():
            for nbr, edict in nbrs.items():
                print(self.get_id_node_dict()[nbr].tech_state, edict)  #


class TechTreeSkill(TechTree):
    pass

# tt = TechTreeSkill()
# t1 = TechNodeBuild()
# t2 = TechNodeLayEgg()
# t3 = TechNode("None")
# tt.add_relation(t1, t2)
# tt.add_relation(t1, t2)
# tt.add_relation(t2, t3)
#
# print(tt.edges())
#
# # tt.ligth_node(t1)
# tt.ligth_node(t1)
# tt.ligth_node(t2)
# # tt.show_state()
# tt.traverse()
#
# nx.dfs_tree(tt)
