import random
import numpy as np
from scipy import ndimage
from scipy.ndimage import zoom

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt


class DrawingCanvas(QWidget):
    def __init__(self, parent, grid_size, cell_size=20):
        super().__init__(parent)
        self.grid_size = grid_size
        self.cell_size = cell_size

        self.grid = np.zeros((grid_size, grid_size), dtype=np.float32)

        self.setFixedSize(grid_size * cell_size, grid_size * cell_size)

    def get_grid_size(self):
        return self.grid_size * self.grid_size

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, False)

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                color = 0 if self.grid[y, x] == 1 else 255
                painter.setBrush(QColor(color, color, color))
                painter.setPen(QPen(QColor(220, 220, 220), 1))
                painter.drawRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )

    def mouseMoveEvent(self, event):
        x = int(event.position().x() // self.cell_size)
        y = int(event.position().y() // self.cell_size)

        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            if event.buttons() & Qt.LeftButton:
                self.grid[y, x] = 1.0
            elif event.buttons() & Qt.RightButton:
                self.grid[y, x] = 0.0
            self.update()

    def mousePressEvent(self, event):
        self.mouseMoveEvent(event)

    def clear(self):
        self.grid.fill(0.0)
        self.update()

    def normalize_grid(self, matrix):
        rows = np.any(matrix > 0, axis=1)
        cols = np.any(matrix > 0, axis=0)

        if not np.any(rows) or not np.any(cols):
            return np.zeros_like(matrix)

        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]

        cropped = matrix[rmin : rmax + 1, cmin : cmax + 1]

        target_size = 20
        h, w = cropped.shape
        scale = target_size / max(h, w)

        zoomed = zoom(cropped, scale, order=1)

        final_grid = np.zeros_like(matrix)
        off_y = (self.grid_size - zoomed.shape[0]) // 2
        off_x = (self.grid_size - zoomed.shape[1]) // 2

        final_grid[off_y : off_y + zoomed.shape[0], off_x : off_x + zoomed.shape[1]] = (
            zoomed
        )

        final_grid[final_grid > 0.1] = 1.0
        final_grid[final_grid <= 0.1] = 0.0

        return final_grid

    def get_sample_vector(self):

        norm_grid = self.normalize_grid(self.grid)
        return norm_grid.flatten()

    def get_augmented_dataset(self, count=10):
        original = self.normalize_grid(self.grid)
        variants = [original.flatten()]

        for _ in range(count):

            angle = random.uniform(-10, 10)
            variant = ndimage.rotate(original, angle, reshape=False, order=0)

            shift_x = random.uniform(-2, 2)
            shift_y = random.uniform(-2, 2)
            variant = ndimage.shift(variant, shift=[shift_y, shift_x], order=0)

            variant = (variant > 0.5).astype(np.float32)

            variants.append(variant.flatten())

        return variants
