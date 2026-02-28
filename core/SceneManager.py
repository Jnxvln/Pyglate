import sys
from core.Scene import Scene
from pyglet.window import Window
from scenes.DefaultScene import DefaultScene

class SceneManager():
    """Manages which scene is being rendered and delegates key press events to the individual Scenes."""
    current_scene: Scene = None
    
    def __init__(self, window: Window, scene: Scene = None):
        """Initializes the SceneManager instance. It expects a `Window` instance to render to, and a `Scene` to render."""
        
        if not window:
            print("[SceneManager init] ERROR: Missing reference to a target Window", file=sys.stderr)
            return
        self.window = window
        
        if not scene:
            self.current_scene = DefaultScene(self)
            return
        self.current_scene = scene
    
    def set_scene(self, scene: Scene) -> None:
        """Updates the currently rendered scene to be the target scene."""
        self.current_scene = scene
    
    def on_key_press(self, symbol, modifiers):
        """Responds to keypress events."""
        if self.current_scene:
            self.current_scene.on_key_press(symbol, modifiers)
    
    def draw(self):
        """Draws the Scene every frame."""
        self.window.clear()
        if self.current_scene:
            self.current_scene.draw()