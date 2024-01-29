from tkinter import Tk, Canvas, BOTH


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color: str = "black"):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=1)


class Window:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.__root = Tk()
        self.__root.title("Boot.dev")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()
        self.running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()
        print("window closed ...")

    def close(self) -> None:
        self.running = False

    def draw_line(self, line: Line, fill_color: str = "black"):
        line.draw(self.canvas, fill_color=fill_color)
