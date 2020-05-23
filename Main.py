import string
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import themed_tk as tk
import tkinter.scrolledtext




class Application(object):

    def __init__(self, master):

        self.master = master

        #FRAMES
        self.left = Frame(master, height = 525, width =500 , bg="#DFDEDE")
        self.left.place(x=0, y=0)

        self.right = Frame(master, height = 525, width =500, bg="#E9E8E8" )
        self.right.place(x=500, y=0)


        self.bottom = Frame(master, height =80, width =1000, bg="#e6e6e6")
        self.bottom.place(x=0, y=525)



        #ENCRYPTION
        self.heading1 = Label(self.left, text="ENCRYPTION", font = "Broadway 45 ", fg = "black", bg="#DFDEDE")
        self.heading1.place(x = 40, y=20)

        self.choice1 = Label(self.left, text="Choose Cipher: ",bg="#DFDEDE" , font = "Courier 15")
        self.choice1.place(x = 40, y = 120)

        self.combobox1 = ttk.Combobox(self.left, textvariable="Algorithm", values=("Caesar", 'Vernam', "Vigenère"), state='readonly', width=20)
        self.combobox1.place(x = 215, y = 120)

        self.label1 = Label(self.left, text="Enter Code: ",bg="#DFDEDE" , font = "Courier 15")
        self.label1.place(x=40, y=170)

        self.input1 = ttk.Entry(self.left, width = 40)
        self.input1.place(x = 215, y=173)

        self.label11 = Label(self.left, text="Key(optional): ", bg="#DFDEDE", font="Courier 15")
        self.label11.place(x=40, y=220)

        self.key1 = ttk.Entry(self.left, width=40)
        self.key1.place(x=215, y=223)

        self.button1 = ttk.Button(self.left, text = "Encrypt", width = 20, command = self.encrypt)
        self.button1.place( x = 200, y = 273)

        self.output1 = tkinter.scrolledtext.ScrolledText(self.left, height = 10, width = 50, wrap = WORD)
        self.output1.config(state="disabled")
        self.output1.place(x = 50, y = 330)

        # self.scroll1 = Scrollbar(self.left, orient = VERTICAL, command = self.output1.yview)
        # self.scroll1.place(x= 440, y=330, fill = Y)
        #
        # self.output1.config(yscrollcommand = self.scroll1.set)
        #
        #DECRYPTION
        self.heading2 = Label(self.right, text="DECRYPTION", font = "Broadway 45 ", fg = "black", bg="#E9E8E8" )
        self.heading2.place(x = 40, y=20)

        self.choice2 = Label(self.right, text="Choose Cipher: " , bg="#E9E8E8" , font = "Courier 15")
        self.choice2.place(x = 40, y = 120)

        self.combobox2 = ttk.Combobox(self.right , textvariable="Algorithm", values=("Caesar",'Vernam', "Vigenère"), state='readonly', width=20)
        self.combobox2.place(x = 215, y = 120)

        self.label2 = Label(self.right, text="Enter Code: ", bg="#E9E8E8", font="Courier 15")
        self.label2.place(x=40, y=170)

        self.input2 = ttk.Entry(self.right, width = 40)
        self.input2.place(x = 215, y=173)

        self.label22 = Label(self.right, text="Key(optional): ", bg="#E9E8E8", font="Courier 15")
        self.label22.place(x=40, y=220)

        self.key2 = ttk.Entry(self.right, width=40)
        self.key2.place(x=215, y=223)

        self.button2 = ttk.Button(self.right, text = "Decrypt", width =20, command = self.decrypt)
        self.button2.place( x = 200, y = 273)

        self.output2 = tkinter.scrolledtext.ScrolledText(self.right, height = 10, width = 50, wrap = WORD)
        self.output2.config(state = "disabled")
        self.output2.place(x = 50, y = 330)

        self.info = Label(self.bottom,
                           text="IMPORTANT INFORMATION: \n\n=> Mandatory to have keys for Vernam and Vigenère algorithms. \n=> In Vernam algorthim, length of code & key should be equal.",
                           font="Courier 10 bold", fg="#660000", bg="#e6e6e6")
        self.info.place(x=250, y=3)

    def encrypt(self):


        global s_string
        s_string = ""

        # def pig_latin(str):
        #     global sfinal
        #     global s_string
        #     vowels_lower = ["a", "e", "i", "o", "u"]
        #     vowels_upper = ["A", "E", "I", "O", "U"]
        #     l1 = str.split()
        #     for x in l1:
        #         for y in x:
        #             if y.islower():
        #                 if y in vowels_lower and y == x[0]:
        #                     sfinal = x + "way"
        #                     s_string = s_string + sfinal + " "
        #                     break
        #                 elif y in vowels_lower and y!=x[0]:
        #                     pos = x.find(y)
        #                     s1 = x[:pos]
        #                     s2 = x[pos:]
        #                     sfinal = s2 + s1 + "ay"
        #                     s_string = s_string + sfinal + " "
        #                     break
        #
        #             else:
        #                 if y in vowels_upper and y == x[0]:
        #                     sfinal = x + "way"
        #                     s_string = s_string + sfinal + " "
        #                     break
        #                 elif y in vowels_upper and y!=x[0]:
        #                     pos = x.find(y)
        #                     s1 = x[:pos]
        #                     s2 = x[pos:]
        #                     sfinal = s2 + s1 + "ay"
        #                     s_string = s_string + sfinal + " "
        #                     break
        #
        #     print(s_string)
        #     self.output1.config(state="normal")
        #     self.output1.insert(1.0, s_string)
        #     self.output1.config(state="disabled")


        def caesar_cipher(istr):
            global s_string
            lower_str = string.ascii_lowercase
            lower_list = list(lower_str)

            upper_str = string.ascii_uppercase
            upper_list = list(upper_str)

            l1 = istr.split()
            for x in l1:
                s_final = ""
                for y in x:
                    if y.isupper():
                        pos = upper_list.index(y)
                        if pos == 23:
                            alphabet = "a"
                        elif pos == 24:
                            alphabet = "b"
                        elif pos == 25:
                            alphabet = "c"
                        else:
                            alphabet = upper_list[pos+3]

                        s_final += alphabet

                    else:
                        pos = lower_list.index(y)
                        if pos == 23:
                            alphabet = "a"
                        elif pos == 24:
                            alphabet = "b"
                        elif pos == 25:
                            alphabet = "c"
                        else:
                            alphabet = lower_list[pos + 3]

                        s_final += alphabet
                s_string = s_string + s_final + " "


            print(s_string)
            self.output1.config(state="normal")
            self.output1.insert(1.0, s_string+"\n")
            self.output1.config(state="disabled")

        def vernam(istr, imp):
            global s_string
            count1 = []
            count2 = []
            count3 = []

            lower_str = string.ascii_lowercase
            lower_list = list(lower_str)

            upper_str = string.ascii_uppercase
            upper_list = list(upper_str)

            for x in istr:
                pos = lower_list.index(x.lower())
                count1.append(pos)
            print(count1)

            for y in imp:
                num = lower_list.index(y.lower())
                count2.append(num)
            print(count2)

            # numlist= []
            # for i in count1:
            #     a = [i,]
            #     numlist.append(a)
            #
            # for j in count2:
            #     for x in range(len(count1)):
            #         numlist[x].append(j)
            #
            # print(numlist)

            for x in range(len(count1)):
                sum = count1[x]+count2[x]
                count3.append(sum)
            print(count3)

            for b in count3:
                if b>25:
                    d = b-26
                    print(d)
                    var = lower_list[d]
                    s_string += var
                else:
                    var = lower_list[b]
                    s_string += var

            print(s_string.upper())

            self.output1.config(state="normal")
            self.output1.insert(1.0, s_string+"\n")
            self.output1.config(state="disabled")

        def vigenere(istr, imp):
            global s_string
            count1 = []
            count2 = []
            count3 = []

            lower_str = string.ascii_lowercase
            lower_list = list(lower_str)

            upper_str = string.ascii_uppercase
            upper_list = list(upper_str)

            for x in istr:
                pos = lower_list.index(x.lower())
                count1.append(pos)
            print(count1)

            len1 = len(istr)
            len2 = len(imp)

            if len2 > len1:
                difference = len2 - len1
                imp = imp[:-difference]
                print(imp, "1")
            elif len2 == len1:
                print(imp, "1-2")
            else:
                diff = len1-len2
                print(diff)
                if diff == len2:
                    imp = imp*2
                    print(imp, "2-1")
                elif diff > len2:
                    fit = diff//len2
                    print(fit)
                    imp = imp*(fit+1)
                    print(imp)
                    new_len = len(imp)
                    new_diff = len1 - new_len
                    print(new_diff)
                    imp = imp + imp[:new_diff]
                    print(imp, "2-2")
                elif diff < len2:
                    imp = imp + imp[:diff]
                    print(imp, "2-3")

            print(imp)

            for y in imp:
                num = lower_list.index(y.lower())
                count2.append(num)
            print(count2)

            for i in range(len(count1)):
                sum = count1[i] + count2[i]
                if sum<=25:
                    var = lower_list[sum]
                    s_string += var
                else:
                    var = lower_list[sum-26]
                    s_string += var

            print(s_string)
            self.output1.config(state="normal")
            self.output1.insert(1.0, s_string+"\n")
            self.output1.config(state="disabled")





        algo = self.combobox1.get()
        input = self.input1.get()
        key = self.key1.get()

        if algo == "Vernam":
            if key == "":
                messagebox.showwarning("Warning", "Please enter a key", icon="warning")
            elif len(key) != len(input):
                messagebox.showwarning("Warning", "Please enter a key of equal length", icon="warning")
            else:
                vernam(input, key)

        elif algo == "Vigenère":
            if key == "":
                messagebox.showwarning("Warning", "Please enter a key", icon="warning")
            else:
                vigenere(input, key)

        elif algo == "Caesar":
            caesar_cipher(input)

        else:
            messagebox.showwarning("Warning", "Please choose an algorithm", icon = "warning")



    def decrypt(self):

        global s_string
        s_string = ""

        def caesar_cipher(istr):

            global s_string
            lower_str = string.ascii_lowercase
            lower_list = list(lower_str)

            upper_str = string.ascii_uppercase
            upper_list = list(upper_str)

            l1 = istr.split()
            for x in l1:
                s_final = ""
                for y in x:
                    if y.isupper():
                        pos = upper_list.index(y)
                        if pos == 0:
                            alphabet = "X"
                        elif pos == 1:
                            alphabet = "Y"
                        elif pos == 2:
                            alphabet = "Z"
                        else:
                            alphabet = upper_list[pos - 3]

                        s_final += alphabet

                    else:
                        pos = lower_list.index(y)
                        if pos == 0:
                            alphabet = "x"
                        elif pos == 1:
                            alphabet = "y"
                        elif pos == 2:
                            alphabet = "z"
                        else:
                            alphabet = lower_list[pos - 3]

                        s_final += alphabet
                s_string = s_string + s_final + " "

            print(s_string)
            self.output2.config(state="normal")
            self.output2.insert(1.0, s_string + "\n")
            self.output2.config(state="disabled")

        # def pig_latin(istr):
        #
        #     l1 = istr.split()
        #     s_final = ""
        #
        #     for x in l1:
        #
        #         #LOWER
        #
        #         if x[-3:] == "way":
        #             s_final += x[-3:]

        def vernam(istr, imp):
            global s_string
            count1 = []
            count2 = []
            count3 = []

            lower_str = string.ascii_lowercase
            lower_list = list(lower_str)

            upper_str = string.ascii_uppercase
            upper_list = list(upper_str)

            for x in istr:
                pos = lower_list.index(x.lower())
                count1.append(pos)
            print(count1)

            for y in imp:
                num = lower_list.index(y.lower())
                count2.append(num)
            print(count2)

            # numlist= []
            # for i in count1:
            #     a = [i,]
            #     numlist.append(a)
            #
            # for j in count2:
            #     for x in range(len(count1)):
            #         numlist[x].append(j)
            #
            # print(numlist)

            for x in range(len(count1)):
                diff = count1[x] - count2[x]
                count3.append(diff)
            print(count3)

            for b in count3:
                if b < 0:
                    d = b + 26
                    var = lower_list[d]
                    s_string += var
                else:
                    var = lower_list[b]
                    s_string += var

            print(s_string.upper())

            self.output2.config(state="normal")
            self.output2.insert(1.0, s_string + "\n")
            self.output2.config(state="disabled")

        def vigenere(istr, imp):
            global s_string
            count1 = []
            count2 = []
            count3 = []

            lower_str = string.ascii_lowercase
            lower_list = list(lower_str)

            upper_str = string.ascii_uppercase
            upper_list = list(upper_str)

            for x in istr:
                pos = lower_list.index(x.lower())
                count1.append(pos)
            print(count1)

            len1 = len(istr)
            len2 = len(imp)

            if len2 > len1:
                difference = len2 - len1
                imp = imp[:-difference]
                print(imp, "1")
            elif len2 == len1:
                print(imp, "1-2")
            else:
                diff = len1 - len2
                print(diff)
                if diff == len2:
                    imp = imp * 2
                    print(imp, "2-1")
                elif diff > len2:
                    fit = diff // len2
                    print(fit)
                    imp = imp * (fit + 1)
                    print(imp)
                    new_len = len(imp)
                    new_diff = len1 - new_len
                    print(new_diff)
                    imp = imp + imp[:new_diff]
                    print(imp, "2-2")
                elif diff < len2:
                    imp = imp + imp[:diff]
                    print(imp, "2-3")

            print(imp)

            for y in imp:
                num = lower_list.index(y.lower())
                count2.append(num)
            print(count2)

            for i in range(len(count1)):
                diff = count1[i] - count2[i]
                if diff >= 0:
                    var = lower_list[diff]
                    s_string += var
                else:
                    var = lower_list[diff + 26]
                    s_string += var

            print(s_string)
            self.output2.config(state="normal")
            self.output2.insert(1.0, s_string + "\n")
            self.output2.config(state="disabled")



        algo = self.combobox2.get()
        input = self.input2.get()
        key = self.key2.get()

        if algo == "Vernam":
            if key == "":
                messagebox.showwarning("Warning", "Please enter a key", icon="warning")
            elif len(key) != len(input):
                messagebox.showwarning("Warning", "Please enter a key of equal length", icon="warning")
            else:
                vernam(input, key)

        elif algo == "Vigenère":
            if key == "":
                messagebox.showwarning("Warning", "Please enter a key", icon="warning")
            else:
                vigenere(input, key)

        elif algo == "Caesar":
            caesar_cipher(input)

        else:
            messagebox.showwarning("Warning", "Please choose an algorithm", icon="warning")






def main():

    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("elegance")
    root.title("CRYPTOGRAPHY")
    root.geometry("1000x600+180+50")
    app = Application(root)
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
