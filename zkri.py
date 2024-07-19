import tkinter as tk



sayfa=tk.Tk()
""" zikir sayısı artışı """

zikir_sys=0

def artı():
    global zikir_sys
    zikir_sys +=1
    adet.config(text=str(zikir_sys))







sayfa.geometry("600x600")
""" ne kadar zikir çekdiğin """
adet=tk.Label(sayfa, text=str(zikir_sys) )
adet.place(x=250, y=150, height=25,width=50)
""" bas buttonu sayıyı arttırr button """
btn=tk.Button(sayfa,text="bas",command=artı)
btn.place(y=300,x=250,height=25,width=80)

 
sayfa.mainloop()