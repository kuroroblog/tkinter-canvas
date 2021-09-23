import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、canvas Widgetを作成する。
        # width : 幅の設定
        # height : 高さの設定
        # background : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Canvasについて : https://kuroro.blog/python/V63iINoXI8iwMeRMEJPK/
        canvas = tk.Canvas(frame, width=500, height=500, background="white")

        # create_oval : 楕円を描く関数
        # create_ovalについて : https://kuroro.blog/python/ANyM9WLpd0LSXRQAELOj/
        canvas.create_oval(200, 100, 10, 20, fill='black')

        # frame Widget(Frame)を親要素とした場合に、canvas Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        canvas.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
