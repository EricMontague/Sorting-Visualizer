"""This module contains the class responsible for defining buttons."""

# https://inventwithpython.com/blog/2012/10/30/designing-a-button-ui-module-for-pygame/
import pygame
# Buttons: 
# "Reset"
# "Sort!"

# "Speed": button with a triangle in the middle and a number on the side
# "Array Size": button with a triangle in the middle

class Button:
    """Class to represent a button."""

    def __init__(self, label, dimensions, background_color):
        self.rectangle = pygame.Rect(dimensions)
        self.label = label
        self.background_color = background_color

    def draw(self, surface):
        """Draw the button."""
        button_surface = self._get_surface()
        surface.blit(self.rectangle, button_surface)
        self.label.draw(button_surface, self.rectangle.center)

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

    @property
    def name(self):
        """Return the button label's text."""
        return self.label.name

    def _get_surface(self):
        """Return the rectangular area of the navbar's area as
        a pygame Surface object."""
        return pygame.Surface(self.rectangle.width, self.rectangle.height)

    

# https://www.nngroup.com/articles/input-steppers/
class InputStepperButton:
    """Class to represent either a minus or plus button for
    an input stepper widget.
    """

    def __init__(self, points, background_color, line_width=0):
        self.points = points
        self.background_color = background_color
        self.line_width = line_width
        
    def draw(self, surface):
        """Draw the button onto the given surface."""
        self.triangle = pygame.draw.polygon(
            surface, 
            self.background_color, 
            self.points, 
            self.line_width
        )
        
    


    