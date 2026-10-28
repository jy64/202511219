import tkinter as tk

root = tk.Tk()
root.title("Cobotton")
root.geometry("600x400")

def on_lable_clicked(event):
    print(f"라벨이 클릭되었습니다: {event}")

lable = tk.Label(root, text = "객체지향윈도우프로그래밍")
lable.bind("<Double-1>", on_lable_clicked)
lable.pack()

def on_btn1_clicked(event):
    print(f"버튼1이 클릭되었습니다: {event}")
    lable.config(text = f"버튼1이 클릭되었습니다. {event}")

#btn1 = tk.Button(root, text="클릭해볼까요", command = on_btn1_clicked)
btn1 = tk.Button(root, text = "클릭해볼까요", width = "100", height = 50, fg="red", bg="black")
btn1.bind("<Button-1>", on_btn1_clicked)
btn1.pack()


root.mainloop()