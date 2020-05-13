"""This module contains the class responsible for defining a label."""


class Label:
    """Class to represent a label."""

    def __init__(self, font, text, color, center, antialias=True, background=None):
        self.font = font
        self.center = center
        self.text = self.font.render(text, antialias, color, background=background)
        
    def draw(self, surface, center=None):
        """Draw the label on the given surface."""
        text_surface = self._get_surface(center or self.center)
        surface.blit(self.text, text_surface)

    def undraw(self):
        """Undraw the label."""
        pass

    @property
    def name(self):
        """Return the label's text."""
        pass
    
    def _get_surface(self, center):
        """Return the rectangular area of the label's surface as a pygame Surface object."""
        return self.font.get_rect(center=center)
        
        
