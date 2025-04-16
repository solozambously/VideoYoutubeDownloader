# By SoloZambously
# YoutubeDownloader Version Graphique
# V 2.0.0
# ------------------------------------- #
# Prérequis au 30/04/2024 : 
# tkinter
# tkinter.messagebox
# pytube
# webbrowser



from tkinter import *
from tkinter.messagebox import *
from pytube import YouTube
import webbrowser

fenetre = Tk()
fenetre.title('YoutubeDownloader by SoloZambously')


def download():
    typeOfDownload_Value = typeOfDownload_List.curselection()
    print ("fichier attentendu : "+typeOfDownload_List.get(typeOfDownload_Value))
    if typeOfDownload_List.get(typeOfDownload_Value) == "Audio WEBP":
        StreamsNum = "251"
    if typeOfDownload_List.get(typeOfDownload_Value) == "Vidéo MP4":
        StreamsNum = "22"
    print(StreamsNum)

    link_Value = link_Input.get()
    print('Lien : '+link_Value)
    url = YouTube(link_Value)
    stream = url.streams.get_by_itag(StreamsNum)
    stream.download()
    print("Votre fichier à bien été téléchargez !")
    showinfo('Succes', 'Votre fichier à bien été téléchargez !')



menubar = Menu(fenetre)

def about():
    showinfo("A propos", "Téléchargeur de vidéo Youtube gratuit et sans pub, Par SoloZambously")
def more():
    webbrowser.open('https://szdev.com/YoutubeDownloader-Python') 
def alert():
    showwarning("Soon...", "Bientôt disponible")

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Télécharger", command=download)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="En Savoir Plus", command=more)
menu2.add_command(label="A propos", command=about)
menubar.add_cascade(label="Aide", menu=menu2)

fenetre.config(menu=menubar)




hello_Label = Label(fenetre, text="Bonjour sur le downloader de vidéo youtube de soloZambously")
hello_Label.pack()

typeOfDownload_List = Listbox(fenetre)
typeOfDownload_List.insert(1, "Audio WEBP")
typeOfDownload_List.insert(2, "Vidéo MP4")
typeOfDownload_List.pack()

link_Input = Entry(fenetre, textvariable=str, width=30)
link_Input.pack()
    
btn = Button(fenetre, height=1, width=10, text="Télécharger", command=download)
btn.pack()
fenetre.mainloop()