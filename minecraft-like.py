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
build_sound = Audio("assets/sounds/Build_Sound.wav", loop=False, autoplay=False)

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

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=sky_bg,
            scale=150,
            double_sided=True
        )

for z in range(20):
    for x in range(20):
        block = Block(position=(x,0,z))
        bedrock = Block(position=(x,-1,z), texture=textures[5], breakable=False)



def update():
    if held_keys["escape"]:
        application.quit()



player = FirstPersonController(position=(10,10,10))
player.cursor.visible = False
sky = Sky()





if __name__ == "__main__":
    app.run()