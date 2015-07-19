__author__ = 'Mystic Dav'
__version__ = "0.1"
#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os.path
import hashlib

class hexgen:
        def __init__(self,master):
                master.title('MYSTIC DAV HASH GENERATOR')
                master.resizable(False, False)
                master.geometry('500x303+370+150')
                master.configure(background = 'green')
                label=ttk.Label(master,text="\t     HASH GENERATOR by C.A.N.",foreground='white',background='orange')
                label.config(font = ('Courier', 12, 'bold'))
                label.place(x=0,y=0,width=500,height=21)
                label1=ttk.Label(master,text="      SELECT ALGORITHM",foreground='white',background='orange')
                label1.config(font = ('Courier', 11, 'bold'))
                label1.place(x=251,y=23,width=247,height=21)
                label2=ttk.Label(master,text="    SELECT I/O DIRECTORY",foreground='white',background='orange')
                label2.config(font = ('Courier', 11, 'bold'))
                label2.place(x=251,y=137,width=247,height=21)
                #buttons
                b3=ttk.Button(master,text='close', command=master.destroy) #done
                b3.place(x=417,y=275,width=80)
                b5=ttk.Button(master,text='Choose Input file', command=self.file_input_ask) #done
                b5.place(x=251,y=163,width=247,height=35)
                b6=ttk.Button(master,text='Output Dir', command=self.dir_output_ask) #done
                b6.place(x=251,y=205,width=100,height=35)
                b7=ttk.Button(master,text='Submit', command=self.submit) #done
                b7.place(x=251,y=243,width=247,height=29)
                b2=ttk.Button(master,text = 'About Us',command=self.about_us_button) #done
                b2.place(x=251,y=275,width=80)
                b2=ttk.Button(master,text = 'REST',command=self.rest) #done
                b2.place(x=334,y=275,width=80)
                #radio buttons
                self.hash_radio=StringVar()
                ttk.Radiobutton(master,text='MD5',variable=self.hash_radio,value='md5').place(x=271,y=51,width=66)
                ttk.Radiobutton(master,text='SHA 1',variable=self.hash_radio,value='sha1').place(x=271,y=81,width=66)
                ttk.Radiobutton(master,text='SHA 224',variable=self.hash_radio,value='sha224').place(x=271,y=111)
                ttk.Radiobutton(master,text='SHA 256',variable=self.hash_radio,value='sha256').place(x=411,y=51)
                ttk.Radiobutton(master,text='SHA 384',variable=self.hash_radio,value='sha384').place(x=411,y=81)
                ttk.Radiobutton(master,text='SHA 512',variable=self.hash_radio,value='sha512').place(x=411,y=111)
                #logo
                self.logo = PhotoImage(file='logo.gif')
                ttk.Label(image= self.logo).place(x=2,y=23)
                #text box
                self.te2= StringVar()
                ttk.Entry(master,textvariable=self.te2, width = 23).place(x=355,y=218)
                #label for text box
                label4=ttk.Label(master,text="OUTPUT FILE NAME",foreground='white',background='green')
                label4.config(font = ('Courier', 10))
                label4.place(x=355,y=201,width=142,height=15)
                #progress bar
                self.bar=ttk.Progressbar(master,orient = HORIZONTAL, length=246)
                self.bar.config(mode = 'determinate',maximum=100.0)
                self.bar.place(x=2,y=275,height=25)
                self.bar.config(value=1.0)
        def rest(self):
                self.te2.set('')
                #self.hash_Radio.set('')
                self.input_file.set('')
                self.output_dir.set('')
        def file_input_ask(self):
                self.input_file=filedialog.askopenfile()
        def dir_output_ask(self):
                self.output_dir=filedialog.askdirectory()
        def submit(self):
                self.bar.config(value=10.0)
                input_file1=self.input_file.name
                out_file=self.te2.get()
                new_out_dir=self.output_dir + '/'
                new= os.path.join(new_out_dir, out_file+".txt")
                FILE=open(input_file1,'r')
                OUT_FILE=open(new,'w')
                lines=FILE.readlines()
                comparison=self.hash_radio.get()
                if comparison=='md5':
                        self.bar.config(value=51.0)
                        for line in lines:
                                OUT_FILE.writelines(line+'\t\t'+hashlib.md5(line.encode('utf-8')).hexdigest()+'\n'+'-'*80+'\n')
                elif comparison=='sha1':
                        self.bar.config(value=51.0)
                        for line in lines:
                                OUT_FILE.writelines(line+'\t\t'+hashlib.sha1(line.encode('utf-8')).hexdigest()+'\n'+'-'*80+'\n')
                elif comparison=='sha224':
                        self.bar.config(value=51.0)
                        for line in lines:
                                OUT_FILE.writelines(line+'\t\t'+hashlib.sha224(line.encode('utf-8')).hexdigest()+'\n'+'-'*80+'\n')
                elif comparison=='sha256':
                        self.bar.config(value=51.0)
                        for line in lines:
                                OUT_FILE.writelines(line+'\t\t'+hashlib.sha256(line.encode('utf-8')).hexdigest()+'\n'+'-'*80+'\n')
                elif comparison=='sha384':
                        self.bar.config(value=51.0)
                        for line in lines:
                                OUT_FILE.writelines(line+'\t\t'+hashlib.sha384(line.encode('utf-8')).hexdigest()+'\n'+'-'*80+'\n')
                elif comparison=='sha512':
                        self.bar.config(value=51.0)
                        for line in lines:
                                OUT_FILE.writelines(line+'\t\t'+hashlib.sha512(line.encode('utf-8')).hexdigest()+'\n'+'-'*80+'\n')
                FILE.close()
                OUT_FILE.close()
                self.bar.config(value=100.0)
        def about_us_button(self):
                window=Toplevel()
                window.resizable(False,False)
                window.geometry('300x50+550+300')
                window.title('About Us')
                Label(window,text='Coding By      :DAVINDER PAL',font = ('Courier', 12, 'bold')).grid(row = 0, column = 0)
                Label(window,text='Logo Desgin By :ASHISH YADAV',font = ('Courier', 12, 'bold')).grid(row = 1, column = 0)


def main():
    root = Tk()
    hex1 = hexgen(root)
    root.mainloop()

if __name__ == "__main__": main()
