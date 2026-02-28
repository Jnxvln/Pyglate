import pyglet
from core.Scene import Scene

class Scene1(Scene):
    def __init__(self, scene_manager, text: str = "Scene 1 - Press ENTER to continue, ESC to exit"):
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
        """Draws the Scene every frame."""
        self.label.draw()
    
    def on_key_press(self, symbol, modifiers):
        """Responds to keypress events."""
        if symbol in (pyglet.window.key.ENTER, pyglet.window.key.NUM_ENTER):
            from scenes.Scene2 import Scene2
            self.scene_manager.set_scene(Scene2(self.scene_manager))
        elif symbol == pyglet.window.key.ESCAPE:
            print("\n[Scene1] Exiting application...")
            self.exit()
