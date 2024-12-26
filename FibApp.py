import tkinter as tk
from tkinter import messagebox
import time
from FibRecursive import FibonacciRecursive
from FibLoop import FibonacciLoop
from FibArray import FibonacciArray
from FibBinet import FibonacciBinet
from FibEvenOdd import FibonacciEvenOdd

class FibonacciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Вычисление чисел Фибоначчи")
        self.root.geometry("400x400+800+200")

        # Поле для ввода числа
        tk.Label(root, text="Введите n (1 ≤ n ≤ 64):").pack()
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Переменная для выбора алгоритма
        self.selected_algorithm = tk.StringVar(value="Recursive")

        # Радиокнопки для выбора алгоритма
        tk.Radiobutton(root, text="Рекурсивный", variable=self.selected_algorithm, value="Recursive").pack()
        tk.Radiobutton(root, text="Итеративный", variable=self.selected_algorithm, value="Loop").pack()
        tk.Radiobutton(root, text="Массив", variable=self.selected_algorithm, value="Array").pack()
        tk.Radiobutton(root, text="Формула Бине", variable=self.selected_algorithm, value="Binet").pack()
        tk.Radiobutton(root, text="Четность", variable=self.selected_algorithm, value="Even/Odd").pack()

        # Кнопка для запуска вычислений
        tk.Button(root, text="Вычислить", command=self.calculate).pack()

        # Создание экземпляров классов алгоритмов
        self.recursive = FibonacciRecursive()
        self.loop = FibonacciLoop()
        self.array = FibonacciArray()
        self.binet = FibonacciBinet()
        self.even_odd = FibonacciEvenOdd()

    def calculate(self):
        try:
            n = int(self.entry.get())
            if n < 1:
                raise ValueError("Число должно быть больше 0.")

            start_time = time.time()

            # Выбор алгоритма
            algorithm = self.selected_algorithm.get()
            if algorithm == "Recursive":
                result = self.recursive.calculate(n)
            elif algorithm == "Loop":
                result = self.loop.calculate(n)
            elif algorithm == "Array":
                result = self.array.calculate(n)
            elif algorithm == "Binet":
                result = self.binet.calculate(n)
            elif algorithm == "Even/Odd":
                result = self.even_odd.calculate(n)
            else:
                raise ValueError("Выберите алгоритм.")

            elapsed_time = (time.time() - start_time) * 1000  # Время в миллисекундах
            messagebox.showinfo("Результат", f"Результат: {result}\nВремя выполнения: {elapsed_time:.2f} мс")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()