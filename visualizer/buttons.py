"""This module contains the class responsible for defining buttons."""

# Buttons: 
# "Reset"
# "Sort!"

# "Speed": button with a triangle in the middle and a number on the side
# "Array Size": button with a triangle in the middle

class Button:
    """Class to represent a button."""

    def __init__(self, surface, label, rectangle):
        self.rectangle = rectangle
        self.rectangle.draw(surface)
        self.label = label
        self.label.draw(surface)
        self.deactivate() # buttons will be deactivated by default

    def draw(self):
        """Draw the button."""
        pass

    def undraw(self):
        """Undraw the button."""
        pass

    def clicked(self):
        """Return True if the user clicked the button."""
        pass

    def activate(self):
        """Highlight this button to show that it has been
        selected.
        """
        pass

    def deactivate(self):
        """Unhighlight this button to show that it is not selected."""
        pass

    def get_label(self):
        """Return the text label for the button."""
        pass

    def _get_surface(self):
        """Return the rectangular area of the navbar's area as
        a pygame Surface object."""
        return pygame.Surface(self.rectangle.width, self.rectangle.height)

    
    