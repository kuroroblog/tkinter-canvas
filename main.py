import tkinter as tk

class Application(tk.Frame):
    # canvasに関する情報を格納する変数
    canvas = None

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # Frameを親要素として、canvas Widgetを作成する。
        # width : 幅の大きさ
        # height : 高さの大きさ
        # background : 背景色
        self.canvas = tk.Canvas(width=500, height=500, background="white")

        # Frameを親要素とした場合に、canvas Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.canvas.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
