"""This module contains the class responsible for defining a label."""


from visualizer.widget_types import WidgetType


class Label:
    """Class to represent a label."""

    def __init__(self, font, text, font_color, antialias=True):
        self.font = font
        self.actual_text = text
        self.font_color = font_color
        self.text = self.font.render(text, antialias, font_color)
        self.type = WidgetType.LABEL
        self.center = None

    def draw(self, surface, center=None):
        """Draw the label on the given surface."""
        if center:
            self.center = center
        text_surface = self._get_surface(self.center)
        surface.blit(self.text, text_surface)

    def clicked(self, mouse_position):
        """Return True if the label was clicked, else return False."""
        text_surface = self._get_surface(self.center)
        return text_surface.collidepoint(mouse_position)

    def change_color(self, color):
        """Change label color."""
        self.font_color = color
        self.text = self.font.render(self.actual_text, True, self.font_color)

    def _get_surface(self, center):
        """Return the rectangular surface around the label."""
        return self.text.get_rect(center=center)

    @property
    def name(self):
        """Return the label's text."""
        pass

