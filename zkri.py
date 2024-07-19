import tkinter as tk



sayfa=tk.Tk()
""" zikir sayısı başlangıcı sayacı  """
zikir_sys=0
""" zikir sayısını arttırmak """
def artı():
    global zikir_sys
    zikir_sys +=1
    adet.config(text=str(zikir_sys))

""" zikir sayısını sıfırlama """
def zro():
     zikir_sys=0
     adet.config(text=zikir_sys)

""" yazılan zikiri ekranda gösterme """

def gstr():
     """ yazı al """
    
     gt=yazz.get()

     wiv.config(text=gt)
  

     


sayfa.geometry("600x600")
""" ne kadar zikir çekdiğin """
adet=tk.Label(sayfa, text=str(zikir_sys) )
adet.place(x=265, y=150, height=25,width=50)
""" bas buttonu sayıyı arttırr button """
btn=tk.Button(sayfa,text="bas",command=artı)
btn.place(y=210,x=250,height=25,width=80)


""" zikir_sys yi sıfırlamak  """
sfr=tk.Button(sayfa,text="sıfırla", command=zro)
sfr.place(height=25, width=80,x=250,y=270)


""" ekranda gözükücek zikiri yazma yeri  """
yazz=tk.Entry(sayfa,)
yazz.place(x=170 , y=30, height=20, width=220)

""" çekilcek zikiri ekranda gözükecek yer """

wiv=tk.Label(sayfa, text="",wraplength=250,justify="left")
wiv.place(x=170 , y=85, height=50, width=250)
""" kaydet buttonu zikiri kadeder """
kyd=tk.Button(sayfa,text="kaydet", command=gstr)
kyd.place(x=400, y=30, height=20 , width=80)
sayfa.mainloop()