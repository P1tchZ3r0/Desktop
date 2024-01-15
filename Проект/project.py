from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import base64
root = Tk()
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb
def callbackFunc():
    if combobox.get() == "Шифр Цезаря":
        return cesar_cipher()
    if combobox.get() == "Шифр Base64":
        return base64_encode()
    if combobox.get() == "Шифр Виженера":
        return encrypt_vigenere()
    if combobox.get() == "Двоичный шифр":
        return binar_cipher()
    
def callbackTheme():
    if comboboxtheme.get() == "Blue/cyan":
        keywordInput.configure(background=rgb_hack((176,196,222)))
        loginInput.configure(background=rgb_hack((176,196,222)))
        canvas.configure(background=rgb_hack((112,128,144)))
        frame.configure(background=rgb_hack((112,128,144)))
        frame2.configure(background=rgb_hack((176,196,222)))
        frame3.configure(background=rgb_hack((112,128,144)))
        frame4.configure(background=rgb_hack((112,128,144)))
        frame5.configure(background=rgb_hack((112,128,144)))
        frame6.configure(background=rgb_hack((176,196,222)))
    if comboboxtheme.get() == "Gray":
        keywordInput.configure(background=rgb_hack((131,131,131)))
        loginInput.configure(background=rgb_hack((131,131,131)))
        canvas.configure(background=rgb_hack((178,178,178)))
        frame.configure(background=rgb_hack((178,178,178)))
        frame2.configure(background=rgb_hack((131,131,131)))
        frame3.configure(background=rgb_hack((178,178,178)))
        frame4.configure(background=rgb_hack((178,178,178)))
        frame5.configure(background=rgb_hack((178,178,178)))
        frame6.configure(background=rgb_hack((131,131,131)))
def encrypt_vigenere():
    plaintext = loginInput.get()
    keyword = keywordInput.get()
    if keywordInput.get() == '':
        messagebox.showinfo(title = "Ошибка",message = "Для шифра Виженера неообходимо ключевое слово")
    ciphertext = ''
    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
         #Расчитать сдвиг для данного символа
            shift = ord(keyword[keyword_index % len(keyword)].lower()) - ord('a')
            #Зашифровать данный символ используя сдвиг
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            keyword_index += 1
        else:
            ciphertext += char
    info = f"Зашифрованное сообщение:\n {ciphertext}"
    messagebox.showinfo(title= 'Зашифрованно',message=info) 
def cesar_cipher():
    shift = 3 

    text = loginInput.get()
    cipher_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        else:
     
            cipher_text += char
    info_str1 =f"Зашифрованное сообщение:\n {cipher_text}"
    messagebox.showinfo(title= 'Зашифровано',message=info_str1)
    
def base64_encode():
    plain_text = loginInput.get()
    message_bytes = plain_text.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_text = base64_bytes.decode('ascii')
    info_str1 =f"Зашифрованное сообщение:\n {base64_text}"
    messagebox.showinfo(title= 'Зашифрованно',message=info_str1)
def binar_cipher():
    message = loginInput.get() 
    encoded = ""
    for char in message:
        # Получаем код символа в двоичном виде
        binary = bin(ord(char))[2:]
        # Дополняем нулями до 8 бит
        padded_binary = binary.zfill(8)
        # Добавляем закодированный символ в сообщение
        encoded += padded_binary + " "
    # Удаляем последний пробел
    encoded = encoded[:-1]
    info_str1 =f"Зашифрованное сообщение:\n {encoded}"
    messagebox.showinfo(title= 'Зашифрованно',message=info_str1)

shifr = ["Шифр Цезаря","Шифр Base64","Шифр Виженера","Двоичный шифр"]
themes = ["Blue/cyan","Gray"]

root.geometry('500x500')
root.title('Шифрование')
root.attributes("-fullscreen", False)
root.maxsize(500,500)

canvas = Canvas(root, height= 500,width=500,borderwidth=2, relief="ridge",bg=rgb_hack((112,128,144)))
canvas.create_text(250,20,anchor=CENTER,text='Введите сообщение:',font=('Comic Sans MS','10'))
canvas.create_text(250,230,anchor=CENTER,text='Выберите тип шифрования:',font=('Comic Sans MS','10'))
canvas.create_text(250,120,anchor=CENTER,text='Для шифра Виженера введите ключевое слово:',font=('Comic Sans MS','10'))
canvas.pack()

frame = Frame(root,bg=rgb_hack((112,128,144)))
frame2 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame4 = Frame(root,bg=rgb_hack((112,128,144)),)
frame.place(relx=0.5, rely=0.555, anchor=CENTER, relwidth=0.5, relheight=0.05)
frame4.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=0.05)
frame2.place(relx=0.5, rely=0.1,anchor=CENTER, relwidth=0.5, relheight=0.05)
frame3 = Frame(root,bg=rgb_hack((112,128,144)))
frame3.place(relx=0.5, rely=0.7, anchor=CENTER, relwidth=0.5, relheight=0.05)
frame5 = Frame(root,bg=rgb_hack((112,128,144)))
frame5.place(relx=0.8, rely=0.9, anchor=CENTER)
frame6 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame6.place(relx=0.5, rely=0.3,anchor=CENTER, relwidth=0.5, relheight=0.05)

comboboxtheme = ttk.Combobox(frame5,values = themes, state = "readonly")
combobox =ttk.Combobox(frame, values=shifr, state="readonly")
combobox.pack()
comboboxtheme.pack()

loginInput = Entry(frame2,bg=rgb_hack((176,196,222)))
loginInput.config(font=('Comic Sans MS','10'))
keywordInput = Entry(frame6,bg=rgb_hack((176,196,222)))
keywordInput.pack()
loginInput.pack()

btn = Button(frame3, text = "Выполнить Шифрование", command = callbackFunc)
btnt = Button(frame5, text = "Изменить", command = callbackTheme)
btn.pack()
btnt.pack()

root.mainloop()
