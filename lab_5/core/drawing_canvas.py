from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt


class DrawingCanvas(QWidget):
    def __init__(self, parent=None, grid_size=20, cell_size=20):
        super().__init__(parent)
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

        self.setFixedSize(grid_size * cell_size, grid_size * cell_size)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, False)

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x] == 1:
                    painter.setBrush(QColor(0, 0, 0))
                else:
                    painter.setBrush(QColor(255, 255, 255))

                painter.setPen(QPen(QColor(220, 220, 220), 1))
                painter.drawRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )

    def mouseMoveEvent(self, event):
        x = event.position().x() // self.cell_size
        y = event.position().y() // self.cell_size

        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            if event.buttons() & Qt.LeftButton:
                self.grid[int(y)][int(x)] = 1
            elif event.buttons() & Qt.RightButton:
                self.grid[int(y)][int(x)] = 0
            self.update()

    def mousePressEvent(self, event):
        self.mouseMoveEvent(event)

    def clear(self):
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.update()

    def get_vector(self):
        return [float(item) for sublist in self.grid for item in sublist]
