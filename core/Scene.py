import pyglet

class Scene:
    """A `Scene` is the viewable content at any given time."""
    
    def draw(self):
        """Draws the Scene every frame."""
        pass
    
    def on_key_press(self, symbol, modifiers):
        """A handler for responding to keystrokes."""
        pass
    
    def exit(self):
        """Escape handler to exit the application."""
        print("\n[BASE Scene] Exiting application...")
        pyglet.app.exit()