import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
import time
fen=Tk()
def quitter_fen():
	## Quitter le jeu
        reponse = tk.messagebox.askyesno("Terminer le jeu","Voulez-vous réellement quitter ? \n Cliquer « Oui » pour finir",)
        if reponse :
            ## On quitte le programme
            fen.quit()
def home(fen):
    global sta,about,typ
    
    higf=open("c:/sab1-0-2/scores/sab francais hight score.txt","a")
    higf.write("")
    higf.close()
    higs=open("c:/sab1-0-2/scores/sab standar hight score.txt","a")
    higs.write("")
    higs.close()
    higa=open("c:/sab1-0-2/scores/sab allemagne hight score.txt","a")
    higa.write("")
    higa.close()
    higt=open("c:/sab1-0-2/scores/test hight score.txt","a")
    higt.write("")
    higt.close()
    record=open("c:/sab1-0-2/scores/record.txt","a")
    record.write("")
    record.close()
    record=open("c:/sab1-0-2/scores/record.txt","r")
    rl=record.readlines()
    if len(rl)>21:
        ln=""
        g=(len(rl)-20)
        for y in range(g,22):
            ln=ln+rl[y]
        record=open("c:/sab1-0-2/scores/record.txt","w")
        record.write(ln)
        record.close()
    def affichage():
        global jeu, posx, posy, nbre,ct,td,H,B,p
        ws = fen.winfo_screenwidth()
        hs = fen.winfo_screenheight()
        def aide():
            ws = fen.winfo_screenwidth()
            hs = fen.winfo_screenheight()
            waide=540
            haide=547
            aaide=(ws-waide)//2
            baide=(hs-haide)//2
            fenaide=Toplevel(fen)
            fenaide.geometry("%dx%d+%d+%d" % (waide, haide, aaide, baide))
            fenaide.resizable(height=False,width=False)
            fenaide.focus()
            fenaide.title("Aide")
            fenaide.configure(bg='white')
            lbaide=Label(fenaide,background='white',foreground='black',font=fonte,justify='left')
            txtlbaide='SOLITAIRES\n\n'
            txtlbaide=txtlbaide+"BUT DU JEU :\n\n"
            txtlbaide=txtlbaide+"Débarasser le plateau de toutes les billes (sauf une).\n\n"
            txtlbaide=txtlbaide+'CONTRAINTES :\n\n'
            txtlbaide=txtlbaide+"1. Choisir une bille et en prendre une autre.\n"
            txtlbaide=txtlbaide+"2. La prise de bille se fait horizontalement ou verticalement.\n"
            txtlbaide=txtlbaide+"3. La prise de bille ne peut se faire que si une case vide se\n"
            txtlbaide=txtlbaide+"situe immédiatement après.\n"
            txtlbaide=txtlbaide+'4. La bille à prendre doit être adjacente à la bille preneuse.\n'
            txtlbaide=txtlbaide+'5. Le joueur peut changer de bille preneuse en cours de partie.\n\n'
            txtlbaide=txtlbaide+"COMMENT JOUER :\n\n"
            txtlbaide=txtlbaide+"Le joueur clique avec la souris sur une bille qui devient preneuse.\n"
            txtlbaide=txtlbaide+"Le joueur clique avec la souris sur une case vide pour prendre une boule.\n"
            txtlbaide=txtlbaide+"Le clic se fait avec le bouton gauche de la souris.\n\n"
            lbaide.configure(text=txtlbaide)
            lbaide.grid(row=0,column=0,padx=5,pady=10)
            btaidequit=tk.Button(fenaide,text='Quitter',command=fenaide.destroy)
            btaidequit.grid(row=1,column=0,pady=10)
            fenaide.grab_set() 
        canv.delete(ALL)
        canv.create_image(0,0,image=TBG,anchor='nw')
        nbre=0
        y=0
        x=0
        def principale():
            reponse = tk.messagebox.askyesno("abandonner","Voulez-vous réellement quitter cette partie ? \n Cliquer « non » pour continue")
            if reponse :
                ## On vas suprimer tout et on vas au menu principale
                p.destroy()
                B.destroy()
                H.destroy()
                home(fen)
        H = tk.Button(fen, image=hel,command=aide)
        H.place(x=0,y=150)
        H.place_forget
        B = tk.Button(fen, image=rec,command=retry)
        B.place(x=0,y=200)
        B.place_forget
        p = tk.Button(fen, image=hom,command=principale)
        p.place(x=0,y=250)
        p.place_forget
        while y<14:
            while x <14:
                if jeu[y][x]=='M':
                    
                    canv.create_image(x*50,y*50,image=mur,anchor='nw')
                if jeu[y][x]=='V':
                    #canv.create_text(x*50,y*50,text='○',anchor='nw', font= ('Helvetica 17 bold',50))
                    canv.create_image(x*50,y*50,image=vide,anchor='nw')
                elif jeu[y][x]=='B':
                    #canv.create_text(x*50,y*50,text='●',anchor='nw', font= ('Helvetica 17 bold',50))
                    canv.create_image(x*50,y*50,image=boule,anchor='nw')
                    nbre=nbre+1
                elif jeu[y][x]=='J':
                    #canv.create_text(x*50,y*50,text='●',anchor='nw', font= ('Helvetica 17 bold',50))
                    canv.create_image(x*50,y*50,image=boule_select,anchor='nw')
                    nbre=nbre+1
                    posx=x
                    posy=y
                x=x+1
            x=0
            y=y+1
        ## On vérifie le nombre de boules restantes
        verif_nbre(nbre,typ)
    def retry():
        reponse = tk.messagebox.askyesno("recommancer","Voulez-vous vraiment recommancer ? \n Cliquer « non » pour continue")
        if reponse :
            ## On restart
            star()
    def rece():
        higf=open("c:/sab1-0-2/scores/sab francais hight score.txt","r") 
        f=higf.read()
        higf.close()
        higs=open("c:/sab1-0-2/scores/sab standar hight score.txt","r")
        s=higs.read()
        higs.close()
        higa=open("c:/sab1-0-2/scores/sab allemagne hight score.txt","r")
        a=higa.read()
        higa.close()
        higt=open("c:/sab1-0-2/scores/test hight score.txt","r")
        t=higt.read()
        higt.close()
        reco=open("c:/sab1-0-2/scores/record.txt","r")
        rcd=reco.read()
        reco.close
        if rcd=="" and t=="" and a=="" and s=="" and f=="":
            tk.messagebox.showinfo( "record", "pas de record")
        if rcd!="" :
            dd='hight score:\nsab standar est: '+s+'\n'
            dd+='sab francais est: '+f+'\n'
            dd+='sab allemagne est: '+a+'\n'
            dd+='test est: '+t+'\n\n\n'+rcd
            ws = fen.winfo_screenwidth()
            hs = fen.winfo_screenheight()
            wx=(len(rcd)+len(t)+120)*1.3+80
            waide=240
            haide=(wx)
            aaide=(ws-waide)//2
            baide=(hs-haide)//2
            rcdfen=Toplevel(fen)
            rcdfen.geometry("%dx%d+%d+%d" % (waide, haide, aaide, baide))
            rcdfen.resizable(height=False,width=False)
            rcdfen.focus()
            rcdfen.title("record")
            rcdfen.configure(bg='blue')
            lbrcd=Label(rcdfen,background='blue',foreground='yellow',justify='left')
            lbrcd.configure(text=dd)
            if len(rcd)<150:
                lbrcd.configure(font=('calibre',8,'bold'))
            if len(rcd)>150:
                lbrcd.configure(font=fonte)
            lbrcd.grid(row=0,column=0,padx=5,pady=10)
            btquit=tk.Button(rcdfen,bg="yellow",text='Quitter',font=("Times_New_Roman",14),fg="blue",border="10",command=rcdfen.destroy)
            def reset():
                        higf=open("c:/sab1-0-2/scores/sab francais hight score.txt","w")
                        higf.write("")
                        higf.close()
                        higs=open("c:/sab1-0-2/scores/sab standar hight score.txt","w")
                        higs.write("")
                        higs.close()
                        higa=open("c:/sab1-0-2/scores/sab allemagne hight score.txt","w")
                        higa.write("")
                        higa.close()
                        higt=open("c:/sab1-0-2/scores/test hight score.txt","w")
                        higt.write("")
                        higt.close()
                        reco=open("c:/sab1-0-2/scores/record.txt","w")
                        reco.write("")
                        reco.close
                        rcdfen.destroy()
                        rece()

            btreset=tk.Button(rcdfen,bg="red",text='reset',font=("Times_New_Roman",14),fg="blue",border="10",command=reset)
            btquit.grid(row=1,column=0,pady=10)
            btreset.grid(row=1,column=2,pady=20)
            rcdfen.grab_set()
        reco.close()
    def about_game():
        ws = fen.winfo_screenwidth()
        hs = fen.winfo_screenheight()
        waide=840
        haide=447
        aaide=(ws-waide)//2
        baide=(hs-haide)//2
        fenaide=Toplevel(fen)
        fenaide.geometry("%dx%d+%d+%d" % (waide, haide, aaide, baide))
        fenaide.resizable(height=False,width=False)
        fenaide.focus()
        fenaide.title("A propos")
        fenaide.configure(bg='white')
        lbaide=Label(fenaide,background='white',foreground='black',font=fonte,justify='left')
        bgim=Label(fenaide,image=sav)
        bgim.place(x=00,y=250)
        bgim2=Label(fenaide,image=sav2)
        bgim2.place(x=550,y=250)
        txtlbaide='SOLITAIRES A BILLE\n\n'
        txtlbaide=txtlbaide+"Le Solitaire est, comme son nom l’indique, un jeu où l’on n’a aucun adversaire.\n\n"
        txtlbaide=txtlbaide+'Il se joue seul. Le but est de déplacer des billes sur un plateau\n\n'
        txtlbaide=txtlbaide+"de les ôter petit à petit selon une règle précise jusqu’à ce qu’il ne reste plus qu’une seule bille sur le plateau.\n"
        txtlbaide=txtlbaide+"Il existe deux types principaux de Solitaire :\n le Solitaire anglais(sab standar) et le Solitaire français(sab francais) et le solitaire allemand(sab allemagne)\n"
        txtlbaide=txtlbaide+"Le jeu du Solitaire remonterait à des temps très anciens et serait un jeu romain.\n"
        txtlbaide=txtlbaide+"La première trace écrite date de 1710 et est due au philosophe Leibniz qui s’est intéressé de très près à ce jeu.\n"
        txtlbaide=txtlbaide+"Leibniz, qui en fut grand amateur, a longuement épilogué sur l'intérêt du Solitaire.\n"
        lbaide.configure(text=txtlbaide)
        lbaide.grid(row=0,column=0,padx=5,pady=10)
        btaidequit=tk.Button(fenaide,text='Quitter',command=fenaide.destroy)
        btaidequit.grid(row=1,column=0,pady=10)
        fenaide.grab_set()
    def star():
        canv.bind('<Button-1>',fonction_jeu)
        fen.geometry("700x600")
        global level,bverif,nbre,posx,posy,ancien_x,ancien_y,partie,partie_finie,typ
        bverif=False
        nbre=0
        posx=-1
        posy=-1
        ancien_x=-1
        ancien_y=-1
        partie=True
        partie_finie=False
        typ=stvar.get()
        level='C:/sab1-0-2/modele/'+typ+'.txt'
        canv.delete(ALL)
        s.destroy()
        a.destroy()
        r.destroy()
        option.destroy()
        MODELE()
        affichage()
    canv=Canvas(fen,height=700,width=700,bg='#1d4b20',bd=0,highlightthickness=0,)
    canv.grid(row=0,column=0,padx=0,pady=0)  
    canv.delete(ALL) 
    canv.create_image(0,0,image=TBG,anchor='nw')
    s = tk.Button(fen,bg='red',image=sta,command=star)
    s.place(x=195,y=225)
    s.place_forget
    a = tk.Button(fen,bg='red',image=about,command=about_game)
    a.place(x=195,y=300)
    a.place_forget
    r = tk.Button(fen,bg='red',image=recod,command=rece)
    r.place(x=195,y=375)
    r.place_forget
    stvar=tk.StringVar()
    stvar.set("sab standar")
    option=tk.OptionMenu(fen, stvar,"sab standar", "sab francais", "sab allemagne","test")
    option.place(x=155,y=145)
    option.configure(activebackground="yellow")
    option.configure(activeforeground="blue")
    option.configure(bg="red")
    option.configure(border="10")
    option.configure(fg="yellow")
    option.configure(font=("New_Times_Roman",15))
    typ=stvar.get()
    level='C:/sab1-0-2/scores/'+typ+'.txt'
    def MODELE():
        ## INITIALISER LE MODELE
        global jeu,level
        ## On lit le fichier niveau
        fich= open(level,'r')
        jeu[:]=[]
        for ligne in fich :
            a=ligne.rstrip('\n\r')
            jeu.append(list(a))
        fich.close()
    def verif_nbre(n,typ):
        global lstresolu, partie, partie_finie,ct,td,sd
        ## On vérifie que le niveau est terminé
        if n==3 and typ=="test":
            td=time.time()
        if n==31 and typ=="sab standar":
            td=time.time()
        if n==43 and typ=="sab allemagne":
            td=time.time()
        if n==35 and typ=="sab francais" :
            td=time.time()
        if n==1:
            ## On déclare la partie finie
            partie=False
            partie_finie=True
            sd=time.time()
            ct="%.2f" %(sd-td)
            ct=float(ct)
            ch="c:/sab1-0-2/scores/"+typ+" hight score.txt"
            hig=open(ch,"r")
            c=hig.read()
            hig.close()
            record=open("c:/sab1-0-2/scores/record.txt","r")
            rcod=record.read()
            record.close()
            if c!="" and rcod!="" :
                c=float(c)
                if c>ct:
                    et=str(ct)
                    hig=open(ch,"w")
                    hig.write(et)
                    hig.close()
            if c=="":
                et=str(ct)
                hig=open(ch,"w")
                hig.write(et)
                hig.close()
            tyt="\nrecord "+typ+" :"
            record=open("c:/sab1-0-2/scores/record.txt","a")
            rcd=tyt+ str(ct)+"s"
            record.write(rcd)
            record.close()
                
            ## On informe le joueur qu'il a gagné
            txt="tu est reussi dans "+str(ct)+"s"
            rep=tk.messagebox.showinfo("VICTOIRE !!",txt)
            
        else:
            ## Si non, vérifier si partie est bloquée
            verif_blocage()
            
    def verif_blocage():
        global nbre, jeu, bverif, partie, partie_finie
        ## On parcourt la grille à la recherche d'un boule
        ## Vérification si boule à une case et vide à 2 cases
        bx=0
        by=0
        bverif=False
        while by<14:
            while bx<14:
                if (jeu[by][bx]=='B' or jeu[by][bx]=='J'):
                    ## On vérifie à gauche
                    if bx>1 :
                        if jeu[by][bx-2]=='V': 
                            if (jeu[by][bx-1]=='B' or jeu[by][bx-1]=='J'):
                                bverif=True
                    ## On vérifie à droite
                    if bx<12:
                        if jeu[by][bx+2]=='V':
                            if (jeu[by][bx+1]=='B' or jeu[by][bx+1]=='J'):
                                bverif=True
                    ## On vérifie en haut
                    if by>1 :
                        if jeu[by-2][bx]=='V': 
                            if (jeu[by-1][bx]=='B' or jeu[by-1][bx]=='J'):
                                bverif=True
                    ## On vérifie en bas
                    if by<12 :
                        if jeu[by+2][bx]=='V':
                            if (jeu[by+1][bx]=='B' or jeu[by+1][bx]=='J'):
                                bverif=True				
                bx=bx+1
            bx=0
            by=by+1
        ## Si la variable bverif est toujours à False
        ## il n'y a plus de possibilités
        if bverif==False :
            ## On bloque la partie
            partie=False
            partie_finie=True
            
            
        
            ## On envoie un messagebox
            j="il reste "+str(nbre)+"bille"+"\n"+"Il n'existe plus de possibilité ! "
            repv=tk.messagebox.showinfo('Plus de possibilité',j)
    def fonction_jeu(event):
        ## Fonction principale du jeu
        global jeu, posx, posy, ancien_x, ancien_y, partie, partie_finie,ct,i,bac
        i=1
        ## On ne vérifie que si partie en cours
        if partie==True and partie_finie==False :
            ## On récupère les coordonnées de la case cliquée
            def bac():
                global jeu, posx, posy, ancien_x, ancien_y, partie, partie_finie,ct,i
                
                if partie==True and partie_finie==False:
                    if i==2:
                        jeu[y+2][x]="J"
                        jeu[y+1][x]="B"
                        jeu[y][x]="V"
                        posy+=2
                        affichage()
                    if i==3:
                        jeu[y-2][x]="J"
                        jeu[y-1][x]="B"
                        jeu[y][x]="V"
                        posy-=2
                        affichage()
                    if i==4:
                        jeu[y][x-2]="J"
                        jeu[y][x-1]="B"
                        jeu[y][x]="V"
                        posx-=2
                        affichage()
                    if i==5:
                        jeu[y][x+2]="J"
                        jeu[y][x+1]="B"
                        jeu[y][x]="V"
                        posx+=2
                        affichage()
                if partie==False and partie_finie==True:
                    tk.messagebox.showinfo("partie finie","tu peut pas retour en arrier")
            x=event.x//50
            y=event.y//50
            ## On ne vérifie que les actions possibles
            ## Le joueur appuie sur une boule noire
            if jeu[y][x]=='B':
                ## On la change en boule SELECT (sélectionnée)
                jeu[y][x]='J'
                z=x
                u=y
                
                ## On change l'ancienne boule SELECT en bleu (si existe)
                if posx!=-1 and posy!=-1:
                    jeu[posy][posx]='B'
                    
                ## On affiche le tout
                affichage()
                ## On change les coordonées de la boule sélectionnée
                posx=x
                posy=y
            ## Le joueur appuie sur une case vide
            elif jeu[y][x]=='V':
                ## On vérifie si nous sommes 2 cases à droite de la boule sélectionnée
                if jeu[y][x-2]=='J':
                    ## On vérifie que la case au milieu est une boule noire
                    if jeu[y][x-1]=='B':
                        ## On garde la position précédente
                        ancien_x=posx
                        ancien_y=posy
                        i=4
                        ## On procède au déplacement
                        jeu[posy][posx]='V' # Case vide sur ancienne position
                        jeu[posy][posx+1]='V' # Et sur boule sautée
                        jeu[posy][posx+2]='J' # Boule sélectionnée
                        ## On modifie les coordonnées de la boule preneuse
                        posx=posx+2
                        ## On affiche le tout
                        affichage()
                ## On vérifie si nous sommes 2 cases à gauche
                if jeu[y][x+2]=='J':
                    ## On vérifie que la case au milieu est une boule noire
                    if jeu[y][x+1]=='B':
                        ## On garde la position précédente
                        ancien_x=posx
                        ancien_y=posy
                        i=5
                        ## On procède au déplacement
                        jeu[posy][posx]='V' # Case vide sur ancienne position
                        jeu[posy][posx-1]='V' # Et sur boule sautée
                        jeu[posy][posx-2]='J' # Boule sélectionnée
                        ## On modifie les coordonnées de la boule preneuse
                        posx=posx-2
                        ## On affiche le tout
                        affichage()
                ## On vérifie si nous sommes 2 cases en haut
                if jeu[y+2][x]=='J':
                    ## On vérifie que la case au milieu est une boule 
                    if jeu[y+1][x]=='B':
                        ## On garde la position précédente
                        ancien_x=posx
                        ancien_y=posy
                        ## On procède au déplacement
                        jeu[posy][posx]='V' # Case vide sur ancienne position
                        jeu[posy-1][posx]='V' # Et sur boule sautée
                        jeu[posy-2][posx]='J'
                        i=2 # Boule sélectionnée
                        ## On modifie les coordonnées de la boule preneuse
                        posy=posy-2
                        ## On affiche le tout
                        affichage()
                ## On vérifie si nous sommes 2 cases en bas
                if jeu[y-2][x]=='J':
                    ## On vérifie que la case au milieu est une boule 
                    if jeu[y-1][x]=='B':
                        ## On garde la position précédente
                        ancien_x=posx
                        ancien_y=posy
                        ## On procède au déplacement
                        jeu[posy][posx]='V' # Case vide sur ancienne position
                        jeu[posy+1][posx]='V' # Et sur boule sautée
                        jeu[posy+2][posx]='J' # Boule sélectionnée
                        ## On modifie les coordonnées de la boule preneuse
                        posy=posy+2
                        i=3## On affiche le tout
                        affichage()
        
        back = tk.Button(fen,bg='red',text="back",font=('Times_New_Roman',15),command=bac)
        back.place(x=150,y=150)
        back.configure(fg="yellow")
        back.place_forget
        
            
    
    ws = fen.winfo_screenwidth()
    hs = fen.winfo_screenheight()

## Variables et Images
mur=PhotoImage(file='C:/sab1-0-2/interface/Mur.png')
sav=PhotoImage(file='C:/sab1-0-2/interface/sav.png')
sav2=PhotoImage(file='C:/sab1-0-2/interface/sav2.png')
TBG=PhotoImage(file='C:/sab1-0-2/interface/sab.png')
boule=PhotoImage(file='C:/sab1-0-2/interface/Boule.png')
boule_select=PhotoImage(file='C:/sab1-0-2/interface/Boule Sélection.png')
vide=PhotoImage(file='C:/sab1-0-2/interface/Vide.png')
bverif=False
nbre=0
fonte=('Arial',11,'bold')
posx=-1
posy=-1
ancien_x=-1
ancien_y=-1
jeu=[]
partie=True
partie_finie=False
sd=0
td=0

## Fin variables et images

## Intérieur Fenêtre
fen.title('SAB')
fen.resizable(height=False,width=False)

fen.iconphoto(True, PhotoImage(file='C:/sab1-0-2/interface/logo.png'))
canv=Canvas(fen,height=700,width=700,bg='#1d4b20',bd=0,highlightthickness=0,cursor='target')
canv.grid(row=0,column=0,columnspan=2)
#canv.create_image(70,70,image=mur,anchor='nw')
## Fin Intérieur Fenêtre
## On lit le fichier du modele et on l'affiche


## Fin de lecture et affichage du niveau

## Placement de la fenêtre
fen.geometry("700x600+300+50")
## Fin placement de la fenêtre
## Fonction de fermeture de la fenêtre
fen.protocol("WM_DELETE_WINDOW",quitter_fen)
## Fin fonction fermeture de fenêtre
## Liens d'action

## Fin liens d'action
sta=PhotoImage(file='C:/sab1-0-2/interface/start.png')
rec=PhotoImage(file='C:/sab1-0-2/interface/retry.png')
recod=PhotoImage(file='C:/sab1-0-2/interface/record.png')
hel=PhotoImage(file='C:/sab1-0-2/interface/help.png')
hom=PhotoImage(file='C:/sab1-0-2/interface/principale.png')
about=PhotoImage(file='C:/sab1-0-2/interface/about.png')
canv=Canvas(fen,height=700,width=700,bg='#1d4b20',bd=0,highlightthickness=0,)
canv.grid(row=0,column=0,padx=0,pady=0)   
home(fen)
fen.mainloop()