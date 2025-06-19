from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

textures = {
    1: load_texture("assets/textures/Grass.png"),
    2: load_texture("assets/textures/Dirt.png"),
    3: load_texture("assets/textures/Brick.png"),
    4: load_texture("assets/textures/Wood.png"),
    5: load_texture("assets/textures/Stone.png"),
}

sky_bg = load_texture("assets/textures/Sky.png")
build_sound = Audio("assets/sfx/Build_Sound.wav", loop=False, autoplay=False)

block_pick = 1

class Block(Button):
    def __init__(self, position=(0,0,0), texture=textures[1], breakable=True):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/models/Block.obj",
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.light_gray,
            scale=0.5
        )
        self.breakable = breakable

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                build_sound.play()
                new_block = Block(position=self.position + mouse.normal, texture=textures[block_pick])
            elif key == "right mouse down" and self.breakable:
                build_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=sky_bg,
            scale=150,
            double_sided=True
        )

class Tree(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/models/Lowpoly_tree_sample.obj",
            scale=(0.6,0.6,0.6),
            collider="mesh",
        )

def generate_trees(num_trees=3, terrain_size=20):
    for _ in range(num_trees):
        x = random.randint(0, terrain_size-1)
        y = 3
        z = random.randint(0, terrain_size-1)
        Tree(position=(x,y,z))

def generate_terrain():
    height = 5

    for z in range(20):
        for x in range(20):

            for y in range(height):
                if y == height-1:
                    Block(position=(x,y,z), texture=textures[1])
                elif y >= height-3:
                    Block(position=(x,y,z), texture=textures[2])
                else:
                    Block(position=(x,y,z), texture=textures[5])

            Block(position=(x,-1,z), texture=textures[5], breakable=False)

def update():
    global block_pick

    for i in range(1,6):
        if held_keys[str(i)]:
            block_pick = i
            break

    if held_keys["escape"]:
        application.quit()

    if player.y <= -5:
        player.position = (10,10,10)



player = FirstPersonController(position=(10,10,10))
player.cursor.visible = False
sky = Sky()
generate_trees()
generate_terrain()


if __name__ == "__main__":
    app.run()