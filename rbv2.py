from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd

qtdd_refri, qtdd_chopd, qtdd_agua, qtdd_chop, qtdd_espeto, qtdd_doces, qtdd_semalcool, qtdd_porcoes, qtdd_ingressovidro, qtdd_ingressoacrilico = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
colaborador = 'lucas'
valor_a_pagar = 0

def limpa():
    txb_agua.delete(0,'end')
    txb_agua.insert(0, '0')
    txb_espeto.delete(0,'end')
    txb_espeto.insert(0, '0')
    txb_chop.delete(0,'end')
    txb_chop.insert(0, '0')
    txb_chopd.delete(0,'end')
    txb_chopd.insert(0, '0')
    txb_refri.delete(0,'end')
    txb_refri.insert(0, '0')
    txb_semalcool.delete(0,'end')
    txb_semalcool.insert(0, '0')
    txb_porcoes.delete(0,'end')
    txb_porcoes.insert(0, '0')
    txb_doces.delete(0,'end')
    txb_doces.insert(0, '0')
    txb_ingressovidro.delete(0,'end')
    txb_ingressovidro.insert(0, '0')
    txb_ingressoacrilico.delete(0,'end')
    txb_ingressoacrilico.insert(0, '0')
    txb_pago.delete(0,'end')
    txb_pago.insert(0, '')
    global valor_a_pagar
    valor_a_pagar = 0

def aumenta1(valor):
    inteiro = int (valor.get())
    quantidade = inteiro +1
    valor.delete(0,'end')
    valor.insert(0, str(quantidade))


def aumenta5(valor):
    inteiro = int(valor.get())
    quantidade = inteiro+5
    valor.delete(0,'end')
    valor.insert(0, str(quantidade))

def calcula():
    global qtdd_agua, qtdd_espeto, qtdd_refri, qtdd_chop, qtdd_chopd, qtdd_doces, qtdd_semalcool, qtdd_porcoes, qtdd_ingressoacrilico, qtdd_ingressovidro
    qtdd_agua = int(txb_agua.get())
    qtdd_espeto = int(txb_espeto.get())
    qtdd_refri = int(txb_refri.get())
    qtdd_chop = int(txb_chop.get())
    qtdd_chopd = int(txb_chopd.get())
    qtdd_doces = int(txb_doces.get())
    qtdd_semalcool = int(txb_semalcool.get())
    qtdd_porcoes = int(txb_porcoes.get())
    qtdd_ingressovidro = int(txb_ingressovidro.get())
    qtdd_ingressoacrilico = int(txb_ingressoacrilico.get())
    global valor_a_pagar
    valor_a_pagar = qtdd_agua*4 + qtdd_chop*10 + qtdd_chopd*13 + qtdd_espeto*9 + qtdd_refri*7 + qtdd_doces *10 +qtdd_semalcool *5 +qtdd_porcoes *30 +qtdd_ingressovidro * 65+qtdd_ingressoacrilico *25
    valor_configurado = 'R$'+str(valor_a_pagar)+',00'
    valor_pendente.configure(state= 'normal')
    valor_pendente.delete(0,'end')
    valor_pendente.insert(0,valor_configurado)
    valor_pendente.configure(state= 'readonly')

def finaliza():
    df = pd.read_csv("RelatoriodeVendas.csv")
    nova_linha = {'Colaborador': colaborador, 'Chop': qtdd_chop,'Chopd': qtdd_chopd, 'Agua': qtdd_agua, 'Refri': qtdd_refri, 'Espeto': qtdd_espeto, 'Porção': qtdd_porcoes, 'IngressoVidro': qtdd_ingressovidro ,'IngressoAcrilico':qtdd_ingressoacrilico}
    df = pd.concat([df, pd.DataFrame(nova_linha, index=[-1])], ignore_index=True)
    valor_pendente.configure(state= 'normal')
    valor_pendente.delete(0,'end')
    valor_pendente.configure(state= 'readonly')
    txb_troco.configure(state= 'normal')
    txb_troco.delete(0,'end')
    txb_troco.configure(state= 'readonly')
    df.to_csv('RelatoriodeVendas.csv', index=False)
    limpa()

def seta_colaborador(ajudante, janela):
    global colaborador
    colaborador = ajudante.get()
    janela.detroy()


def verifica_senha(janela, senha):
    if senha.get() == '31p4ul40':
        ajudante = Entry(janela, justify= 'center')
        ajudante.place(relx = 0.05, rely = 0.50, relwidth=0.90, relheight=0.20)
        
        confere_colaborador = Button(janela, text="entrar", command=lambda:seta_colaborador(ajudante, janela)).place(relx = 0.1, rely = 0.70, relwidth=0.80, relheight=0.20)
        colaborador = ajudante.get()

def abrir_nova_janela():
    nova_janela = tk.Toplevel(home)
    nova_janela.title("Verificação")
    nova_janela.geometry("200x100")
    senha = Entry(nova_janela,show = '*', justify= 'center')
    senha.place(relx=0.1,rely=0.1,relheight=0.2,relwidth=0.80)
    btn_entrar = Button(nova_janela, text="entrar", command=lambda:verifica_senha(nova_janela, senha)).place(relx = 0.1, rely = 0.70, relwidth=0.80, relheight=0.20)

def calcula_troco():
    valor_pago = int(txb_pago.get())
    global valor_a_pagar
    valor_troco = valor_pago - valor_a_pagar 
    valor_troco_configurado = 'R$'+str(valor_troco)+',00'
    txb_troco.configure(state= 'normal')
    txb_troco.delete(0,'end')
    txb_troco.insert(0,valor_troco_configurado)
    txb_troco.configure(state= 'readonly')

    pass

home= Tk()
font_produtos= tkFont.Font(family= 'Germania One', size=25, weight= 'bold')
font_numero= tkFont.Font(family= 'Germania One', size=20, weight= 'bold')
font_preco = tkFont.Font(family= 'Germania One', size=90, weight='bold')
font_entri= tkFont.Font(family= 'Helvetica', size=20, weight= 'bold')
try:
    df = pd.read_csv("RelatoriodeVendas.csv")
except FileNotFoundError:
    dados = {'Colaborador': [], 'Chop': [],'Chopd': [], 'Agua': [], 'Refri': [], 'Espeto': [], 'Porção': [], 'IngressoVidro':[],'IngressoAcrilico': [] }
    df = pd.DataFrame(dados)
    df.to_csv('RelatoriodeVendas.csv', index=False)
bg = PhotoImage(file = "bg.png") 

home.title('Caixa RochasBier')
home.geometry("%dx%d" % (home.winfo_screenwidth(), home.winfo_screenheight()))
home.resizable(False, False)
canvas1 = Canvas(home, width = home.winfo_screenwidth(), height = home.winfo_screenheight()) 
canvas1.pack(fill = "both", expand = True) 
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
frame1 = Frame(home, background="white", highlightbackground= 'black', highlightthickness= 2)
frame1.place(relx=0.02, rely=0.03, relheight=0.40, relwidth=0.40)
frame3 = Frame(home,background="white", highlightbackground= 'black', highlightthickness= 2)
frame3.place(relx=0.02, rely=0.46, relheight=0.25, relwidth=0.40)
frame2 = Frame(home,background="white", highlightbackground= 'black', highlightthickness= 2)
frame2.place(relx=0.02, rely=0.74, relheight=0.15, relwidth=0.40)
frame4 = Frame(home,background="white", highlightbackground= 'black', highlightthickness= 2)
frame4.place(relx=0.48, rely=0.03, relheight=0.28, relwidth=0.45)

chop = Label(home,background="white",text= 'CHOPP LAGER:', font= font_produtos ).place(relx= 0.04, rely=0.06)
chopd = Label(home,background="white",text= 'CHOPP DIVER:', font= font_produtos ).place(relx= 0.04, rely=0.13)
agua = Label(home,background="white",text= 'ÁGUA:', font= font_produtos ).place(relx= 0.04, rely=0.20)
refri = Label(home,background="white",text= 'REFRIGERANTE:', font= font_produtos ).place(relx= 0.04, rely=0.27)
estela = Label(home,background="white",text= 'SEM ALCOOL:', font= font_produtos ).place(relx= 0.04, rely=0.34)
######################################
espeto = Label(home,background="white",text= 'ESPETO:', font= font_produtos ).place(relx= 0.04, rely=0.49)
porcoes = Label(home,background="white",text= 'PORÇÕES:', font= font_produtos ).place(relx= 0.04, rely=0.56)
doce = Label(home,background="white",text= 'DOCES:', font= font_produtos ).place(relx= 0.04, rely=0.63)
######################################
preco= Label(home,background="white",text= 'PREÇO:', font= font_produtos ).place(relx= 0.49, rely=0.04)
######################################
IngresoVidro = Label(home,background="white",text= 'INGRESSO VIDRO:', font= font_produtos ).place(relx= 0.04, rely=0.76)       
IngresoAcrilico = Label(home,background="white",   text= 'INGRESSO ACRILICO:', font= font_produtos ).place(relx= 0.04, rely=0.82)  


frame_troco= Frame(home,background="white", highlightbackground= 'black', highlightthickness= 2)
frame_troco.place(relx=0.58, rely=0.515, relwidth=0.25,relheight=0.30)
troco = Label(home,background="white",text= 'TROCO:', font= font_produtos ).place(relx= 0.595, rely=0.73)
pago = Label(home,background="white",text= 'PAGO:', font= font_produtos ).place(relx= 0.595, rely=0.54)
txb_pago = Entry(home,font = font_entri, highlightthickness= 0, justify='center')
txb_pago.place(relx=0.675,rely=0.54,relheight=0.06,relwidth=0.14)
txb_troco = Entry(home,state= 'readonly',font = font_entri, highlightthickness= 0, justify='center')
txb_troco.place(relx=0.675,rely=0.73,relheight=0.06,relwidth=0.14)

calcular_troco = Button(home, text= 'CALCULA TROCO', command=lambda:calcula_troco(), bd=5, font= font_numero).place(relx= 0.59, rely=0.627, relwidth=0.23, relheight=0.075)


txb_chop = Entry(home, justify= 'center', font= font_entri)
txb_chop.place(relx=0.368,rely=0.05,relheight=0.06,relwidth=0.04)
txb_chopd = Entry(home, justify= 'center', font= font_entri)
txb_chopd.place(relx=0.368,rely=0.12,relheight=0.06,relwidth=0.04)
txb_agua = Entry(home, justify= 'center', font= font_entri)
txb_agua.place(relx=0.368,rely=0.19,relheight=0.06,relwidth=0.04)
txb_refri = Entry(home, justify= 'center', font= font_entri)
txb_refri.place(relx=0.368,rely=0.26,relheight=0.06,relwidth=0.04)
txb_semalcool = Entry(home, justify= 'center', font= font_entri)
txb_semalcool.place(relx=0.368,rely=0.33,relheight=0.06,relwidth=0.04)
txb_espeto = Entry(home, justify= 'center', font= font_entri)
txb_espeto.place(relx=0.368,rely=0.48,relheight=0.06,relwidth=0.04)
txb_porcoes = Entry(home, justify= 'center', font= font_entri)
txb_porcoes.place(relx=0.368,rely=0.55,relheight=0.06,relwidth=0.04)
txb_doces = Entry(home, justify= 'center', font= font_entri)
txb_doces.place(relx=0.368,rely=0.62,relheight=0.06,relwidth=0.04)
txb_ingressovidro = Entry(home, justify= 'center', font= font_entri)
txb_ingressovidro.place(relx=0.368,rely=0.75,relheight=0.06,relwidth=0.04)
txb_ingressoacrilico = Entry(home, justify= 'center', font= font_entri)
txb_ingressoacrilico.place(relx=0.368,rely=0.82,relheight=0.06,relwidth=0.04)
valor_pendente = Entry(home, state= 'readonly',font = font_preco, highlightthickness= 0, justify='center')
valor_pendente.place(relx=0.55,rely=0.10,relwidth=0.365,relheight=0.18)

limpa()

umchop = Button(home, text= '+1', command=lambda:aumenta1(txb_chop), bd=5, font= font_numero).place(relx= 0.28, rely=0.05 , relwidth=0.04, relheight=0.06)
cincochop = Button(home, text= '+5', command=lambda:aumenta5(txb_chop), bd=5, font= font_numero).place(relx= 0.325, rely=0.05 , relwidth=0.04, relheight=0.06)
umchopd = Button(home, text= '+1', command=lambda:aumenta1(txb_chopd), bd=5, font= font_numero).place(relx= 0.28, rely=0.12, relwidth=0.04, relheight=0.06)
cincochopd = Button(home, text= '+5', command=lambda:aumenta5(txb_chopd), bd=5, font= font_numero).place(relx= 0.325, rely=0.12 , relwidth=0.04, relheight=0.06)
umagua = Button(home, text= '+1', command=lambda:aumenta1(txb_agua), bd=5, font= font_numero).place(relx= 0.28, rely=0.19, relwidth=0.04, relheight=0.06)
cincoagua = Button(home, text= '+5', command=lambda:aumenta5(txb_agua), bd=5, font= font_numero).place(relx= 0.325, rely=0.19 , relwidth=0.04, relheight=0.06)

umrefri = Button(home, text= '+1', command=lambda:aumenta1(txb_refri), bd=5, font= font_numero).place(relx= 0.28, rely=0.26, relwidth=0.04, relheight=0.06)
cincorefri = Button(home, text= '+5', command=lambda:aumenta5(txb_refri), bd=5, font= font_numero).place(relx= 0.325, rely=0.26 , relwidth=0.04, relheight=0.06)

umsemalcool = Button(home, text= '+1', command=lambda:aumenta1(txb_semalcool), bd=5, font= font_numero).place(relx= 0.28, rely=0.33, relwidth=0.04, relheight=0.06)
cincosemalcool = Button(home, text= '+5', command=lambda:aumenta5(txb_semalcool), bd=5, font= font_numero).place(relx= 0.325, rely=0.33 , relwidth=0.04, relheight=0.06)

umespeto = Button(home, text= '+1', command=lambda:aumenta1(txb_espeto), bd=5, font= font_numero).place(relx= 0.28, rely=0.48, relwidth=0.04, relheight=0.06)
cincoespeto = Button(home, text= '+5', command=lambda:aumenta5(txb_espeto), bd=5, font= font_numero).place(relx= 0.325, rely=0.48 , relwidth=0.04, relheight=0.06)

umporcoes = Button(home, text= '+1', command=lambda:aumenta1(txb_porcoes), bd=5, font= font_numero).place(relx= 0.28, rely=0.55, relwidth=0.04, relheight=0.06)
cincoporcoes = Button(home, text= '+5', command=lambda:aumenta5(txb_porcoes), bd=5, font= font_numero).place(relx= 0.325, rely=0.55 , relwidth=0.04, relheight=0.06)

umdoces = Button(home, text= '+1', command=lambda:aumenta1(txb_doces), bd=5, font= font_numero).place(relx= 0.28, rely=0.62, relwidth=0.04, relheight=0.06)
cincodoces = Button(home, text= '+5', command=lambda:aumenta5(txb_doces), bd=5, font= font_numero).place(relx= 0.325, rely=0.62 , relwidth=0.04, relheight=0.06)

umingressov = Button(home, text= '+1', command=lambda:aumenta1(txb_ingressovidro), bd=5, font= font_numero).place(relx= 0.28, rely=0.75, relwidth=0.04, relheight=0.06)
cincoingressosv = Button(home, text= '+5', command=lambda:aumenta5(txb_ingressovidro), bd=5, font= font_numero).place(relx= 0.325, rely=0.75 , relwidth=0.04, relheight=0.06)

umingressoa = Button(home, text= '+1', command=lambda:aumenta1(txb_ingressoacrilico), bd=5, font= font_numero).place(relx= 0.28, rely=0.82, relwidth=0.04, relheight=0.06)
cincoingressosa = Button(home, text= '+5', command=lambda:aumenta5(txb_ingressoacrilico), bd=5, font= font_numero).place(relx= 0.325, rely=0.82 , relwidth=0.04, relheight=0.06)

finalizar = Button(home,bg = 'red', text= 'FINALIZA', command=lambda:finaliza(), bd=5, font= font_numero).place(relx= 0.59, rely=0.33, relwidth=0.34, relheight=0.10)
calcular = Button(home, text= 'CALCULA', command=lambda:calcula(), bd=5, font= font_numero).place(relx= 0.48, rely=0.33, relwidth=0.10, relheight=0.10)

btn_nova_janela = Button(home, text="?", command=abrir_nova_janela).place(relx = 0.90, rely = 0.90, relwidth=0.02, relheight=0.02)

home.mainloop()