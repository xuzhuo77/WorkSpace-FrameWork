import json
from zhak_projects.agame.map_editor.YamlUtils import read_default, write_default
from zhak_projects.agame.elements.SpriteActor import SpriteActor
import numpy as np
class FileAccessMap():
    def __init__(self,parent,map_name):
        self.map_name=map_name
        self.data = {"map_name": map_name}
        self.parent=parent

    def read(self,sprite_dict,screen,scene):
        self.data = read_default(self.map_name + ".yaml")
        self.update_map_data(scene)
        self.update_sprite_group(sprite_dict,screen,scene)

    def update_map_data(self,scene):
        scene.map.map_data = np.array(json.loads(self.data["map_data"]))

    def update_sprite_group(self,sprite_dict,screen,scene):
        for j_sprite in self.data["sprite_group"]:
            spritedata = json.loads(j_sprite)
            if spritedata["sprite_type"] in sprite_dict.keys():
                sprite =sprite_dict[spritedata["sprite_type"]](screen)
                sprite.pos = np.array(spritedata["pos"])
                if scene.sprite_group is not None:
                    scene.sprite_group.add(sprite)
#--------------------------------------------------------------------------------------------------
    def write(self,scene):
        self.write_map(scene)
        self.write_sprite_group(scene)
        try:
            write_default(self.map_name + ".yaml", self.data)
        except:
            open(self.map_name + ".yaml", 'w')
            write_default(self.map_name + ".yaml", self.data)

    def write_map(self,scene):
        self.data.update({"map_data": json.dumps(scene.map.map_data.tolist())})

    def write_sprite_group(self,scene):
        list = [sprite.map_editor_serialize() for sprite in scene.sprite_group if isinstance(sprite,SpriteActor)]
        self.data["sprite_group"] = list



