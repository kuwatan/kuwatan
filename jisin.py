import requests
import tkinter as tk 
#requestを使えないときpy -m pip install requestsを実行する
while True:
    p2pquake_url = 'https://api.p2pquake.net/v2/history?codes=551&limit=1'
#https://api-v2-sandbox.p2pquake.net/v2/history?codes=551&limit=1
#https://api.p2pquake.net/v2/history?codes=551&limit=1
    p2pquake_json = requests.get(p2pquake_url).json()
#震央地名を取り出して、変数に代入する
    Eq_name = p2pquake_json[0]["earthquake"]["hypocenter"]["name"]
    Eq_hukasa = p2pquake_json[0]["earthquake"]["hypocenter"]["depth"]
    Eq_maguni = p2pquake_json[0]["earthquake"]["hypocenter"]["magnitude"]
    Eq_sin = p2pquake_json[0]["earthquake"]["maxScale"]
    Eq_time = p2pquake_json[0]["earthquake"]["time"]
#if文で震度1から7までを変換
    if Eq_sin==10:
        Eq_sindo = "震度1"
    if Eq_sin==20:
        Eq_sindo = "震度2"
    if Eq_sin==30:
        Eq_sindo = "震度3"
    if Eq_sin==40:
        Eq_sindo = "震度4"
    if Eq_sin==50:
        Eq_sindo = "震度5弱"
    if Eq_sin==55:
        Eq_sindo = "震度5強"
    if Eq_sin==60:
        Eq_sindo = "震度6弱"
    if Eq_sin==65:
        Eq_sindo = "震度6強"
    if Eq_sin==70:
        Eq_sindo = "震度7"
    elif Eq_sin <10:
        Eq_sindo = "震度不明"
#ウィンドウ表示部分
    root = tk.Tk()
    root.title("情報くん")
    root.geometry("300x500")
    label = tk.Label(root, text="地震情報",font=("",50))
    label.pack()
    label = tk.Label(root, text="")
    label.pack()
    label = tk.Label(root, text="震源地",font=("",20))
    label.pack()
    label = tk.Label(root, text=Eq_name,font=("",15))
    label.pack()
    label = tk.Label(root, text="深さ(km)",font=("",20))
    label.pack()
    label = tk.Label(root, text=Eq_hukasa,font=("",15))
    label.pack()
    label = tk.Label(root, text="マグニチュード",font=("",20))
    label.pack()
    label = tk.Label(root, text=Eq_maguni,font=("",15))
    label.pack()
    label = tk.Label(root, text="震度",font=("",20))
    label.pack()
    label = tk.Label(root, text=Eq_sindo,font=("",15))
    label.pack()
    label = tk.Label(root, text="発生時刻",font=("",20))
    label.pack()
    label = tk.Label(root, text=Eq_time,font=("",15))
    label.pack()
    root.after(60010, lambda: root.destroy()) 
    root.mainloop()
