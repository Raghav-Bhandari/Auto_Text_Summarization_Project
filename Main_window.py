from tkinter import *
import os
# from DocTextSummarizer import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.scrolledtext import *
from tkinter import ttk  # ttk contains 18 widgets
from cgitb import text
from textwrap import fill
from bs4 import BeautifulSoup
from urllib.request import urlopen
import main_script as ms
counter = [0,0]
my_dir=''
plain_text=''
filepath  = "D:\python(full)\Project\Documents\Summary.txt"
files = [ #('All Files','.*'),
        ('Text File', '*.txt'),
        ('Document File', '*.docx'),
        ('PDF File', '*.pdf')]
main_counter=[0,0,0]
def About_us_clicked():
    os.startfile(r'About Us.txt')
def Help_clicked():
    os.startfile(r'Help.txt')
def btn_clicked():
    print("Menu Button Clicked")

def doc_sum_open(window):

#---------------------------------------------------------------------------


    def sel_btn_clicked(entry0):
        global counter
        if counter[0]<1:
            global my_dir
            # doc_window.withdraw()
            counter[0]+=1
            my_dir = filedialog.askopenfilename(filetypes=files,defaultextension=files,
            initialdir=r"Documents")
            # doc_window.deiconify()
            #initialdir=r"C:\Users\HP\Downloads\Documents")

            if(my_dir):
                entry0.delete(0,END)
                entry0.insert(0,my_dir)
            print("Select Button Clicked")
        counter=[0,0]
        # doc_window.grab_release()


    def reset_btn_clicked(textBox0,entry0):
        global my_dir,counter
        counter=[0,0]
        my_dir=""
        if os.path.isfile(filepath):
            os.remove(filepath)
            entry0.delete(0,END)
            textBox0.delete("1.0","end")
            messagebox.showinfo("Message","Successfully Reset!")
        elif len(entry0.get()) != 0:
            entry0.delete(0,END)
            textBox0.delete("1.0","end")
            messagebox.showinfo("Message","Successfully Reset!")
        else:    ## Show an error ##
            messagebox.showerror("Error","Already Reset!")
        print("Reset Button Clicked")


    def summary_btn_clicked(textBox0):
        if not os.path.isfile(my_dir):
            messagebox.showinfo("Message","No such file found!")
        else:
            print("Directory is " + my_dir)

            file_obj=open(my_dir,mode='r',encoding="utf-8")
                # Locatio of the file
            plain_text=file_obj.read()
            file_obj.close()
            summary_text = ms.text_summarizer(plain_text,4)
            textBox0.insert(END,"                                     Summary\n\n",)
            textBox0.insert(END,summary_text)
            print(summary_text)
            
            
            f=open(filepath,'w')
            f.write(summary_text)
            f.close()
            # os.startfile(filepath)
            print("Summary Button Clicked")

    def save_btn_clicked():
        if not os.path.isfile(filepath) and not os.path.isfile(my_dir):
            messagebox.showinfo("Message","No such file found!")
        else:
            if os.path.isfile(filepath):
                save_file_dir = filepath
                file_obj=open(save_file_dir,'r')
                # Locatio of the file
                summary_text=file_obj.read()
                file_obj.close()
            elif os.path.isfile(my_dir):
                save_file_dir = my_dir
                file_obj=open(save_file_dir,'r')
                # Locatio of the file
                plain_text=file_obj.read()
                file_obj.close()
                summary_text = ms.text_summarizer(plain_text,7)

            print("Directory is " + save_file_dir)
            global counter
            print(summary_text)
            if counter[1]<1:
                counter[1]+1
                save_dir=filedialog.asksaveasfilename(filetypes = files, defaultextension = '.txt')
                with open(save_dir,'w') as sv:
                    sv.write(summary_text)
                print("Save Button Clicked")
            counter=[0,0]


    def home_btn_clicked():
        bol_ans=messagebox.askokcancel("Message","Go to Home Page ?")
        if bol_ans == True:
            doc_window.destroy()
            window.deiconify()
        print("Button Clicked")


    # def main(root):
    # global doc_window
    # window.grab_set()
    doc_window = Toplevel(window)
    # doc_window=Tk()
    window.withdraw()
    doc_window.geometry("1200x690+350+200")
    doc_window.title("Text Summarizer")
    doc_window.iconbitmap(r"Doc Text Summarizer GUI\textsummary.ico")
    doc_window.configure(bg = "#141012")
    canvas = Canvas(
    doc_window,
    bg = "#141012",
    height = 690,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = r"Doc Text Summarizer GUI\Docbackground.png")
    background = canvas.create_image(
    650.5, 129.0,
    image=background_img)

# Text Box 1
    textBox0_img = PhotoImage(file = r"Doc Text Summarizer GUI\img_textBox0.png")
    textBox0_bg = canvas.create_image(
    816.5, 361.0,
    image = textBox0_img)

    textBox0 = scrolledtext.ScrolledText(
    master=canvas,
    bd = 0,
    bg = "#d9d9d9",
    wrap = WORD,
    highlightthickness = 0)

    textBox0.place(
    x = 488.1428575515747, y = 211,
    width = 656.7142848968506,
    height = 298)

# Text Box 2
    entry0_img = PhotoImage(file = r"Doc Text Summarizer GUI\img_textBox1.png")
    entry0_bg = canvas.create_image(
    732.5, 126.5,
    image = entry0_img)

    entry0 = Entry(
    master=canvas,
    font=("Helvetica 12"),
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

    entry0.insert(0,r"D:\python(full)\Project\Documents")

    entry0.place(
    x = 534.1428575515747, y = 101,
    width = 396.7142848968506,
    height = 49)

    imgHome = PhotoImage(file = r"Doc Text Summarizer GUI\DocHome_Button.png")
    ButtonHome = Button(
    master=canvas,
    image = imgHome,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : home_btn_clicked(),
    bd=0,
    activebackground="#59192b",
    background="#59192b",
    relief = "flat")

    ButtonHome.place(
     x = 227, y = 568,
    width = 61,
    height = 61)

    imgReset = PhotoImage(file = r"Doc Text Summarizer GUI\DocReset_Button.png")
    resetButton = Button(
    master=canvas,
    image = imgReset,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : reset_btn_clicked(textBox0=textBox0,entry0=entry0),
    bd=0,
    activebackground="#1e1e1e",
    background="#1e1e1e",
    relief = "flat")

    resetButton.place(
    x = 982, y = 568,
    width = 170,
    height = 68)

    imgSummary = PhotoImage(file = r"Doc Text Summarizer GUI\DocSummary_Button.png")
    summaryButton = Button(
    master=canvas,    
    image = imgSummary,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : summary_btn_clicked(textBox0=textBox0),
    bd=0,
    activebackground="#1e1e1e",
    background="#1e1e1e",
    relief = "flat")

    summaryButton.place(
    x = 487, y = 568,
    width = 170,
    height = 68)

    imgSave = PhotoImage(file = r"Doc Text Summarizer GUI\DocSave_Button.png")
    saveButton = Button(
    master=canvas,
    image = imgSave,
    borderwidth = 0,
    highlightthickness = 0,
    command = save_btn_clicked,
    bd=0,
    activebackground="#1e1e1e",
    relief = "flat")

    saveButton.place(
    x = 737, y = 568,
    width = 170,
    height = 68)

    imgSelect = PhotoImage(file = r"Doc Text Summarizer GUI\DocSelect_Button.png")
    selectButton = Button(
    master=canvas,
    image = imgSelect,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : sel_btn_clicked(entry0=entry0),
    bd=0,
    activebackground="#1e1e1e",
    relief = "flat")

    selectButton.place(
    x = 981, y = 94,
    width = 170,
    height = 68)

    doc_window.resizable(False, False)
    def doSomething():
    # check if saving
    # if not:
        window.deiconify()
        doc_window.destroy()
    doc_window.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
    doc_window.mainloop()

    # main_window()
    

def url_sum_open(window):
    url_window = Toplevel(window)
    window.withdraw()
    url_window.title("Input TextBox GUI")
    url_window.geometry("730x480+550+300")

    # Frame Layout
    textBox = Frame(url_window)
    textBox.pack(side=TOP, fill=X)


    # FUNCTIONS
    # Read text entered and then call summary function to generate summary
    def gett_url_summary():
        if (len(str(urll_entry.get()))!=1):
            raw_text = str(urll_entry.get())
            page = urlopen(raw_text)
            # print(len(final_text))
            # if len(final_text)==0:
            #     messagebox.showerror("Error", "Unable to generate summary due to forbidden site!")
            soup = BeautifulSoup(page,features="html.parser")
            fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
            final_text = ms.text_summarizer(fetched_text,5)
            # else:
            result = '\nSummary:{}'.format(final_text)
            displayy_textBox.insert(END,result)	
            
        else:
            messagebox.showerror("Error", "Input textbox is empty!")

    # Clear input textbox and display textbox widget
    def clearr_text():
        if len(urll_entry.get()) != 1:
            urll_entry.delete(0,END)
            displayy_textBox.delete('1.0', END)
            messagebox.showinfo("Message", "Successfully Reset!")
        else:  # Show an error
            messagebox.showerror("Error", "Already Reset!")

    # Save the generated summary in a specified .txt file
    def savee_summary():
        # get whatever text entered in input box
        raw_text = str(urll_entry.get())
        if (len(raw_text)) != 1:
            # get summarised text using text_summarize function of spacy_summarization.py file
            final_text = ms.text_summarizer(raw_text,5)
            # = 'yourSummary' + timestr + '.txt' # create file name based on current time
            files = [  # ('All Files','.*'),
                ('Text File', '*.txt'),
                ('Document File', '*.docx'),
                ('PDF File', '*.pdf')]
            file_name = filedialog.asksaveasfilename(
                filetypes=files, defaultextension='.txt')
            with open(file_name, 'w', encoding='utf-8') as sv:
                sv.write(final_text)
            messagebox.showinfo("Message", "Summary is saved successfully!")
            result = '\nName of File: {} \nSummary:{}'.format(
                file_name, final_text) 
            displayy_textBox.delete('1.0', END)
        
            displayy_textBox.insert(END, result)
        else:
            messagebox.showerror("Error", "Input textbox is empty!")

    ll1=Label(textBox,text="Enter URL To Summarize",background='grey', foreground='white')
    ll1.grid(row=1,column=0,pady=(15, 0), padx=(18, 0))

    raww_entry=StringVar()
    urll_entry=Entry(textBox,textvariable=raww_entry,width=50)
    urll_entry.grid(row=1,column=1)

    # BUTTONS
    buttonn1 = Button(textBox, text="Reset", command=clearr_text,
                    width=12, bg='#cd201f', fg='#fff')
    buttonn1.grid(row=4, column=0, padx=5, pady=5)

    buttonn2 = Button(textBox, text="Summarize", command=gett_url_summary,
                    width=12, bg='#03A9F4', fg='#fff')
    buttonn2.grid(row=4, column=1, padx=10)

    buttonn3 = Button(textBox, text="Save", command=savee_summary,
                    width=12, bg='#25D366', fg='#fff')
    buttonn3.grid(row=4, column=2, padx=13)

    # Resultant Summary display text Area
    ll2 = Label(textBox, text="                                                                                    Resultant Summary                                                                                     ", background='grey', foreground='white')
    ll2.grid(row=6, column=0, columnspan=3, pady=(20, 0), padx=(17, 0))
    displayy_textBox = ScrolledText(textBox)
    displayy_textBox.grid(row=7, column=0, columnspan=3, padx=(35, 0), pady=(0, 10))

    url_window.resizable(False, False)
    def doSomething():
    # check if saving
    # if not:
        window.deiconify()
        url_window.destroy()
    url_window.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
    url_window.mainloop()



def text_sum_open(window):
    

    text_window = Toplevel(window)
    window.withdraw()
    #window.iconbitmap(r"D:/Programming/Auto text summarizer/Images/textsummary.ico")
    text_window.title("Text Summarizer")
    text_window.geometry("800x483+500+300")

    canvas1 = Canvas(
        text_window,
        height = 550,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas1.place(x = 0, y = 0)

    background2_img = PhotoImage(file = r'Simple Text Summarizer GUI\final_bg.png')
    background2 = canvas1.create_image(
        0, 0,
        image=background2_img,
        anchor = "nw")

    # FUNCTIONS
    # Read text entered and then call summary function to generate summary 
    def get_summary():
        raw_text = str(input_textBox.get('1.0',END)) # get whatever text entered in input box
        if (len(raw_text)) != 1:
            final_text = ms.text_summarizer(raw_text,4) # get summarised text using text_summarize function of spacy_summarization.py file
            result = '\nSummary:{}'.format(final_text) # final resultant text to display on GUI
            display_textBox.insert(END,result) # display_textBox is result display screen 
        else:
            messagebox.showerror("Error","Input textbox is empty!")

    # Clear input textbox and display textbox widget
    def clear_text():
        if len(input_textBox.get('1.0',END)) != 1:
            input_textBox.delete('1.0',END)
            display_textBox.delete('1.0',END)
            messagebox.showinfo("Message","Successfully Reset!")
        else:    ## Show an error
            messagebox.showerror("Error","Already Reset!")

    # Save the generated summary in a specified .txt file
    def save_summary():
        raw_text = str(input_textBox.get('1.0',END)) # get whatever text entered in input box
        if (len(raw_text)) != 1:
            final_text = ms.text_summarizer(raw_text,4) # get summarised text using text_summarize function of spacy_summarization.py file
            files = [ #('All Files','.*'),
                ('Text File', '*.txt'),
                ('Document File', '*.docx'),
                ('PDF File', '*.pdf')]
            file_name=filedialog.asksaveasfilename(filetypes = files, defaultextension = '.txt')
            with open(file_name,'w',encoding='utf-8') as sv:
                sv.write(final_text)
            messagebox.showinfo("Message","Summary is saved successfully!")
            result = '\nName of File: {} \nSummary:{}'.format(file_name,final_text) # final resultant text to display on GUI
            display_textBox.delete('1.0',END)
            display_textBox.insert(END,result) # display_textBox is display screen of home tab
        else:
            messagebox.showerror("Error","Input textbox is empty!")

    # Home button
    def home_btn_clicked():
        bol_ans=messagebox.askokcancel("Message","Go to Home Page ?")
        if bol_ans == True:
            text_window.destroy()
            window.deiconify()
        print("Button Clicked")

    # Title label
    # title_lbl = Label(canvas,text="Sumr!zer",font=("Algerian",25,"bold"),bg="#59192b",fg="white")
    # title_lbl = Label(canvas,text="Sumr!zer",font=("Algerian",25,"bold"),bg="#87213b",fg="white")
    title_lbl = Label(canvas1,text="Sumr!zer",font=("Algerian",25,"bold"),bg="#1e1e1e",fg="white")
    title_lbl.place(x=0,y=0,width=800,height=40)

    # Input Text Box
    input_textBox = ScrolledText(
        canvas1,
        bd = 0,
        # bg = "#DBDBDB",
        bg = "old lace",
        wrap = WORD,
        highlightthickness = 0)

    input_textBox.place(
        x = 40, y = 100,
        width = 320,
        height = 320)

    # l1=Label(canvas,text="Original text",background='#ff3465',foreground='white')
    l1=Label(canvas1,text="Original text",background='#87213b',foreground='white')
    l1.place(x=40, y=80,width=100,height=25)

    # Output Text Box
    display_textBox = ScrolledText(
        canvas1,
        bd = 0,
        # bg = "old lace",
        bg = "linen",
        wrap = WORD,
        highlightthickness = 0)

    display_textBox.place(
        x = 445, y = 100,
        width = 320,
        height = 320)

    # l2=Label(canvas,text="Summarized text",background='#7F7FFF',foreground='white')
    # l2=Label(canvas,text="Summarized text",background='purple2',foreground='white')
    # l2=Label(canvas,text="Summarized text",background='#59192b',foreground='white')
    l2=Label(canvas1,text="Summarized text",background='#87213b',foreground='white')
    l2.place(x=445, y=80,width=100,height=25)

    #BUTTONS
    # HOME BUTTON
    imggHome = PhotoImage(file = r'Simple Text Summarizer GUI\Home_Button.png')
    ButtonHome = Button(
        canvas1,
        image = imggHome,
        borderwidth = 0,
        highlightthickness = 0,
        command = home_btn_clicked,
        bd=0,
        activebackground="#59192b",
        relief = "flat")

    ButtonHome.place(
        x = 0, y = 0,
        width = 43,
        height = 40)

    # RESET BUTTON
    imggReset = PhotoImage(file = r'Simple Text Summarizer GUI\Reset_Button.png')
    ButtonReset = Button(
        canvas1,
        image = imggReset,
        borderwidth = 0,
        highlightthickness = 0,
        command = clear_text,
        bd=0,
        activebackground="#1e1e1e",
        relief = "flat")

    ButtonReset.place(
        x = 150, y = 435,
        width = 119,
        height = 40)

    # SUMMARY BUTTON
    imggSummary = PhotoImage(file = r'Simple Text Summarizer GUI\Summary_Button.png')
    ButtonSummary = Button(
        canvas1,
        image = imggSummary,
        borderwidth = 0,
        highlightthickness = 0,
        command = get_summary,
        bd=0,
        activebackground="#1e1e1e",
        relief = "flat")

    ButtonSummary.place(
        x = 350, y = 435,
        width = 119,
        height = 40)

    # SAVE BUTTON
    imggSave = PhotoImage(file = r'Simple Text Summarizer GUI\Save_Button.png')
    ButtonSave = Button(
        canvas1,
        image = imggSave,
        borderwidth = 0,
        highlightthickness = 0,
        command = save_summary,
        bd=0,
        activebackground="#1e1e1e",
        relief = "flat")

    ButtonSave.place(
        x = 550, y = 435,
        width = 119,
        height = 40)

    text_window.resizable(False, False)
    def doSomething():
    # check if saving
    # if not:
        window.deiconify()
        text_window.destroy()
    text_window.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
    text_window.mainloop()

#----------------------------------------------------------------------------------    
    
# Define a function to close the window
def close(window):
   window.destroy()
#    window.quit()

def main_window():
    window = Tk()
    window.overrideredirect(True)
    window.geometry("1503x865+210+110")
    window.configure(bg = "#0f0f11")
    canvas = Canvas(
    window,
    bg = "#0f0f11",
    height = 865,
    width = 1503,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = r"Final Main GUI\background.png")
    background = canvas.create_image(
    767.5, 156.0,
    image=background_img)

    docImg = PhotoImage(file = r"Final Main GUI\docImg.png")
    b0 = Button(
    image = docImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : doc_sum_open(window=window),
    # bd=0,
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b0.place(
    x = 973, y = 132,
    width = 212,
    height = 203)

    SumImg = PhotoImage(file = r"Final Main GUI\SumImg.png")
    b1 = Button(
    image = SumImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    bd=0,
    activebackground="#87213b",
    relief = "flat")

    b1.place(
    x = 937, y = 433,
    width = 286,
    height = 266)

    textImg = PhotoImage(file = r"Final Main GUI\textImg.png")
    b2 = Button(
    image = textImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : text_sum_open(window=window),
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b2.place(
    x = 649, y = 343,
    width = 203,
    height = 195)

    UrlImg = PhotoImage(file = r"Final Main GUI\UrlImg.png")
    b3 = Button(
    image = UrlImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : url_sum_open(window=window),
    bd=0,
    activebackground="#87213b",
    relief = "flat")

    b3.place(
    x = 1290, y = 366,
    width = 200,
    height = 193)

    menuImg = PhotoImage(file = r"Final Main GUI\menuImg.png")
    b4 = Button(
    image = menuImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    bd=0,
    activebackground="#0B0E10",
    background="#0B0E10",
    relief = "flat")

    b4.place(
    x = 101, y = 51,
    width = 75,
    height = 35)

    aboutImg = PhotoImage(file = r"Final Main GUI\aboutImg.png")
    b5 = Button(
    image = aboutImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = About_us_clicked,
    bd=0,
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b5.place(
    x = 500, y = 53,
    width = 112,
    height = 33)

    helpImg = PhotoImage(file = r"Final Main GUI\helpImg.png")
    b6 = Button(
    image = helpImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = Help_clicked,
    bd=0,
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b6.place(
    x = 692, y = 53,
    width = 69,
    height = 33)

    closeImg = PhotoImage(file = r"Final Main GUI\closeImg.png")
    b7 = Button(
    image = closeImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : close(window=window),
    bd=0,
    activebackground="#87213b",
    background="#87213b",
    relief = "flat")

    b7.place(
    x = 1406, y = 50,
    width = 35,
    height = 33)

    window.resizable(False, False)
    window.mainloop()

if __name__== '__main__':
    main_window()
