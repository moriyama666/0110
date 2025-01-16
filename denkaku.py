# 電卓アプリを作る
import tkinter as tk

root = tk.Tk()
root.minsize(270, 330) #電卓サイズ
root.title("電卓")
root.configure( bg = "#d2b48c") #背景色

# 関数
def clear(event):
    txt.delete(0, tk.END)

def call(event, num):
    """数字のボタン

    クリックした数字を続けて表示
    """
    txt.insert(tk.END, num)

def call2(event, num):
    """/, *, +, - ボタン
    
    クリックしたときに前に入力した値を調査
    演算子が入っていた場合、続けて演算子を入力できない
    """
    i = txt.get()
    if len(i) >= 1:
        if i[-1] not in ["/", "*", "-", "+"]:
            txt.insert(tk.END, num)
        # print(i[-1])

def call3(event, num):
    """ . ボタン
    
    クリックしたときに前に入力した値を調査
    「.」が入っていた場合、続けて入力させない
    """
    dot = txt.get()
    if len(dot) >= 1:
        if dot[-1] != ".":
            txt.insert(tk.END, num)

def calc(event):
    """式を取得して画面に計算結果を表示
    """
    total = txt.get()
    txt.delete(0, tk.END)
    txt.insert(tk.END, eval(total))
    # print(eval(total))
    # print(type(total))




# 値を表示するエリア
txt = tk.Entry( font=("", 16, ""))
txt.place( x=30, y=30, width=150, height=30)


# ボタン
btn_c = tk.Button( text="c", bg="#778899", foreground="#ffffff", font=("bold","15",""))
btn_c.bind("<1>", clear)
btn_c.place( x=210, y=30, width=35, height=35)

btn0 = tk.Button( text="0")
btn0.bind("<1>", lambda event:call(event, "0"))
btn0.place( x=30, y=270, width=35, height=35)

btn1 = tk.Button( text="1")
btn1.bind("<1>", lambda event:call(event, "1"))
btn1.place( x=30, y=210, width=35, height=35)

btn2 = tk.Button( text="2")
btn2.bind("<1>", lambda event:call(event, "2"))
btn2.place( x=90, y=210, width=35, height=35)

btn3 = tk.Button( text="3")
btn3.bind("<1>", lambda event:call(event, "3"))
btn3.place( x=150, y=210, width=35, height=35)

btn4 = tk.Button( text="4")
btn4.bind("<1>", lambda event:call(event, "4"))
btn4.place( x=30, y=150, width=35, height=35)

btn5 = tk.Button( text="5")
btn5.bind("<1>", lambda event:call(event, "5"))
btn5.place( x=90, y=150, width=35, height=35)

btn6 = tk.Button( text="6")
btn6.bind("<1>", lambda event:call(event, "6"))
btn6.place( x=150, y=150, width=35, height=35)

btn7 = tk.Button( text="7")
btn7.bind("<1>", lambda event:call(event, "7"))
btn7.place( x=30, y=90, width=35, height=35)

btn8 = tk.Button( text="8")
btn8.bind("<1>", lambda event:call(event, "8"))
btn8.place( x=90, y=90, width=35, height=35)

btn9 = tk.Button( text="9")
btn9.bind("<1>", lambda event:call(event, "9"))
btn9.place( x=150, y=90, width=35, height=35)

btn_11 = tk.Button( text="/", bg="#b0c4de")
btn_11.bind("<1>", lambda event:call2(event, "/"))
btn_11.place( x=210, y=90, width=35, height=35)

btn_12 = tk.Button( text="×", bg="#b0c4de")
btn_12.bind("<1>", lambda event:call2(event, "*"))
btn_12.place( x=210, y=150, width=35, height=35)

btn_13 = tk.Button( text="-", bg="#b0c4de")
btn_13.bind("<1>", lambda event:call2(event, "-"))
btn_13.place( x=210, y=210, width=35, height=35)

btn_14 = tk.Button( text="+", bg="#b0c4de")
btn_14.bind("<1>", lambda event:call2(event, "+"))
btn_14.place( x=210, y=270, width=35, height=35)

btn_15 = tk.Button( text="=", bg="#b0c4de")
btn_15.bind("<1>", calc)
btn_15.place( x=150, y=270, width=35, height=35)

btn_16 = tk.Button( text=".")
btn_16.bind("<1>", lambda event:call3(event, "."))
btn_16.place( x=90, y=270, width=35, height=35)

root.mainloop()
