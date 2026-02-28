import pyglet
from pyglet.window import Window
from core.SceneManager import SceneManager
from scenes.Scene1 import Scene1

#region Application State
APP_TITLE: str = "Pyglet Base Application"
APP_WIDTH: int = 800
APP_HEIGHT: int = 600
window: Window = Window(width=APP_WIDTH, height=APP_HEIGHT, caption=APP_TITLE)
scene_manager = SceneManager(window)
#endregion


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# SET THE INITIAL SCENE
scene_manager.set_scene(Scene1(scene_manager))
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#region EVENT HANDLERS
@window.event
def on_draw():
    """Delegates drawing to the SceneManager in order to render a specific Scene. (E.g. `scene_manager.set_scene(DefaultScene(scene_manager))`)"""
    scene_manager.draw()

@window.event
def on_key_press(symbol, modifiers):
    """Delegates response of Scene-specific keystrokes to the SceneManager"""
    scene_manager.on_key_press(symbol, modifiers)
#endregion

# Start the app
pyglet.app.run()