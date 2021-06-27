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

        ##########################################
        # 1. canvas Widgetを作成する。              #
        ##########################################
        # 参考 : https://kuroro.blog/python/V63iINoXI8iwMeRMEJPK/
        # frame Widget(Frame)を親要素として、canvas Widgetを作成する。
        # width : 幅の設定
        # height : 高さの設定
        # background : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        canvas = tk.Canvas(frame, width=500, height=500, background="white")

        ##########################################
        # 2. canvas Widget内へ図形や画像を描画する。   #
        ##########################################
        # 参考 : https://kuroro.blog/python/ANyM9WLpd0LSXRQAELOj/
        # canvas Widget内へ文字列を描画する。(x座標, y座標)を'文字列の中心'として描画する。
        # create_text(x座標, y座標, option1, option2, ...)
        # 第一引数 : x座標
        # 第二引数 : y座標
        # 第三引数以降(任意) : option
        # text : 文字列情報
        # fill : 文字列色
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # activefill : 文字列が選択される or 文字列の上にマウスが移動する場合に、色を変更する設定
        # canvas Widgetのstate optionが'disabled' or create_textのstate optionが'disabled'の場合に、色を変更する設定
        # tag : 文字列をtesttestと'名前付け'を行う。
        canvas.create_text(250, 250, text="テストテスト", fill='black', activefill='red', disabledfill='blue', tag="testtest")

        ##########################################
        # 3. 図形や画像を操作する。                   #
        ##########################################
        # 参考 : https://kuroro.blog/python/Qj1Czf3BgZiw4Jwxftad/
        # testtestとtag付け(名前付け)された図形や画像に対して操作を行う。
        # 開始index(文字位置)2から終わりindex(文字位置)4の間に当てはまる文字列を、選択状態にする。
        # select_from(tag名, 開始index(文字位置))
        canvas.select_from("testtest", 2)
        # select_to(tag名, 終わりindex(文字位置))
        canvas.select_to("testtest", 4)

        # frame Widget(Frame)を親要素とした場合に、canvas Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        canvas.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
