"""This module contains the class responsible for defining a label."""


from visualizer.widget_types import WidgetType


class Label:
    """Class to represent a label."""

    def __init__(self, font, text, font_color, antialias=True, background=None):
        self.font = font
        self.font_color = font_color
        self.text = self.font.render(text, antialias, font_color, background)
        self.type = WidgetType.LABEL

    def draw(self, surface, center):
        """Draw the label on the given surface."""
        self.center = center
        text_surface = self._get_surface(self.center)
        surface.blit(self.text, text_surface)

    def undraw(self):
        """Undraw the label."""
        pass

    def clicked(self, mouse_position):
        """Return True if the label was clicked, else return False."""
        text_surface = self._get_surface(self.center)
        return text_surface.collidepoint(mouse_position)
        

    @property
    def name(self):
        """Return the label's text."""
        pass

    def _get_surface(self, center):
        """Return the rectangular area of the label's surface as a pygame Surface object."""
        return self.text.get_rect(center=center)
