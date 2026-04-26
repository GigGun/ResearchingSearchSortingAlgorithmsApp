import sys
import random

# импортируем главное окно
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QVBoxLayout

# импортируем диаграмму для отрисовки случайных чисел
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from interface import load_theory_content # загрузка краткой справки по алгоритмам в формате html

class SortSearchVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Алгоритмы поиска и сортировки')
        self.setGeometry(100, 100, 1400, 800)

        # первоначальный алгоритм
        self.array = self.generate_random_array(30, 1, 100)

        # Виджеты
        self.init_ui()

    def init_ui(self):
        # Главный виджет и layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # график
        self.canvas_widget = QWidget()
        self.canvas_layout = QVBoxLayout(self.canvas_widget)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.update_plot()
        self.canvas_layout.addWidget(self.canvas)

        # добавляем график на окно 
        main_layout.addWidget(self.canvas_widget, 70)


    def update_plot(self):
                        
        bar_width = 0.8
        bars = []
        colors = ['skyblue'] * len(self.array)
        
        # Отрисовка столбцов
        for idx, val in enumerate(self.array):
            x = idx

            bar = self.ax.bar(x, val, 
                              width=bar_width, 
                              color=colors[idx], 
                              edgecolor='black', 
                              linewidth=0.5)
            bars.append(bar[0])

            # Подписи значений
            if val > 5:  # Не показывать подписи для очень маленьких столбцов
                self.ax.text(x, 
                             val + 0.5, 
                             str(val),
                             ha='center',
                             va='bottom',
                             fontsize=8)



        # Настройка графика
        self.ax.set_title("Визуализация массива")
        self.ax.set_xlabel("Индекс")
        self.ax.set_ylabel("Значение")
        self.ax.set_xticks(range(len(self.array)))
        self.ax.set_xticklabels(range(len(self.array)))
        self.ax.grid(axis='y', alpha=0.3)

        self.canvas.draw()




    def generate_random_array(self, size, min_val, max_val):
    # метод для генерации массива случайных чисел
        return [random.randint(min_val, max_val) for _ in range(size)]


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SortSearchVisualizer()
    window.show()
    sys.exit(app.exec())