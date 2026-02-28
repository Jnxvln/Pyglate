# Pyglate

A minimal, opinionated Pyglet application template designed for quick project setup. Clone it, rename your scenes, and start building! The scaffolding is already done.

---

## What's Included

- A `Window` with configurable title, width, and height
- A `SceneManager` that handles rendering and input delegation
- A base `Scene` class all scenes inherit from
- Two example scenes (`Scene1`, `Scene2`) to demo and experiment with
- A `DefaultScene` fallback that renders if no scene is explicitly set
- Built-in ESCAPE-to-exit on all scenes
- Clean separation between core engine files and scene content

---

## Project Structure

```
Pyglate/
├── core/
│   ├── Scene.py          # Base class for all scenes
│   └── SceneManager.py   # Manages rendering and input delegation
├── scenes/
│   ├── DefaultScene.py   # ⚠️ DO NOT REMOVE (see below)
│   ├── Scene1.py         # Example scene,  safe to edit or delete
│   └── Scene2.py         # Example scene,  safe to edit or delete
└── main.py               # Entry point,  configure your app here
```

---

## Getting Started

### 1. Clone and set up your environment

```bash
git clone <your-repo-url> my-new-project
cd my-new-project
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install pyglet
```

### 2. Configure your app in `main.py`

```python
APP_TITLE: str = "My App"
APP_WIDTH: int = 800
APP_HEIGHT: int = 600
```

### 3. Set your initial scene

```python
scene_manager.set_scene(Scene1(scene_manager))
```

### 4. Run it

```bash
python main.py
```

---

## Core Concepts

### Scenes

A `Scene` is whatever the user sees at any given moment: a main menu, a game screen, a settings page, etc. Every scene inherits from the base `Scene` class in `core/Scene.py` and can override:

- `draw()`, called every frame, put your rendering logic here
- `on_key_press(symbol, modifiers)`, handle keyboard input
- `exit()`, called when ESCAPE is pressed, exits the app by default

### Creating a New Scene

```python
import pyglet
from core.Scene import Scene

class MyScene(Scene):
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        self.label = pyglet.text.Label("Hello!", x=400, y=300,
                                        anchor_x="center", anchor_y="center")

    def draw(self):
        self.label.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self.exit()
```

### Switching Scenes

From within any scene, switch to another <u>**using a local import to avoid circular dependencies**</u>:

```python
def on_key_press(self, symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        from scenes.MyOtherScene import MyOtherScene
        self.scene_manager.set_scene(MyOtherScene(self.scene_manager))
```

### SceneManager

The `SceneManager` is the glue between `main.py` and your scenes. It:

- Holds a reference to the active scene
- Calls `draw()` on the active scene every frame
- Delegates keypresses to the active scene via `on_key_press()`
- Falls back to `DefaultScene` if no scene is provided at startup

You generally won't need to modify `SceneManager` unless you're extending the engine itself.

---

## ⚠️ DefaultScene, Do Not Remove

`scenes/DefaultScene.py` is the fallback scene loaded automatically if `SceneManager` is initialized without an explicit scene. It acts as a safety net and prevents a blank/crashed window if something goes wrong during startup.

**It is safe to edit**, change the text, colors, or behavior to suit your project.

**Do not delete it**, `SceneManager` imports it directly and will break without it.

---

## Example Scenes

`Scene1.py` and `Scene2.py` are placeholder scenes included to demonstrate scene switching out of the box. They are fully safe to edit, rename, or delete once you're ready to build your own scenes.

- `Scene1`, press ENTER to go to `Scene2`
- `Scene2`, press ENTER to go back to `Scene1`
- Either scene, press ESCAPE to exit

---

## Coordinate System

Pyglet uses a **bottom-left origin** coordinate system. `(0, 0)` is the bottom-left corner of the window, and `y` increases upward. This is the opposite of CSS/HTML but matches standard Cartesian coordinates.

---

## Key Constants

Use `pyglet.window.key` for readable key comparisons:

```python
pyglet.window.key.ENTER
pyglet.window.key.NUM_ENTER  # Numpad Enter, check both!
pyglet.window.key.ESCAPE
pyglet.window.key.SPACE
pyglet.window.key.LEFT, .RIGHT, .UP, .DOWN
```

---

## Requirements

- Python 3.10+
- pyglet

```bash
pip install pyglet
```

---

## License

Do whatever you want with this, it's just a template. Go build something cool.
