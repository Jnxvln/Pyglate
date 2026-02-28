import pyglet
from core.Scene import Scene

class DefaultScene(Scene):
    """A fallback Scene if the intended Scene fails to render. Okay to alter, but DO NOT REMOVE!"""
    
    def __init__(self, scene_manager, text: str = "Default Scene - Press ENTER to continue, ESC to exit"):
        self.scene_manager = scene_manager
        self.label = pyglet.text.Label(
            text,
            font_name="monospace", 
            font_size=18,
            color=(0, 255, 0, 255),
            x=400, y=300,
            anchor_x="center",
            anchor_y="center"
        )
    
    def draw(self):
        """Draws the Scene every frame"""
        self.label.draw()
