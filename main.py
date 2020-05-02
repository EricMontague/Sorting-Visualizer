"""This script contains the main function for the sorting visualizer."""


from visualizer import SortingVisualizerGUI
from visualizer import SortingVisualizerController


def main():
    """Start the sorting visualizer."""
    interface = SortingVisualizerGUI()
    visualizer = SortingVisualizerController(interface)
    visualizer.run()


if __name__ == "__main__":
    main()

