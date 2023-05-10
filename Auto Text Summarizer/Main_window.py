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
from urllib.request import Request,urlopen
import main_script as ms
from fpdf import FPDF
counter = [0,0]
my_dir=''
plain_text=''
filepath  = "Documents\Summary.txt"
files = [ #('All Files','.*'),
        ('Text File', '*.txt'),
        ('Document File', '*.docx'),
        ('PDF File', '*.pdf')]
main_counter=[0,0,0]

def text_to_pdf(final_text,file_name):

                    pdf = FPDF(format='letter', unit='in')      
                    # Add a page 
                    pdf.add_page()  
                    # set style and size of font  
                    # that you want in the pdf 
                    pdf.set_font('Times','',20.0) 

                    effective_page_width = pdf.w - 2*pdf.l_margin
    

                    pdf.set_font('Times','B',20.0)
                    # pdf.cell(1.0,0.0, 'Using multi_cell and effective page width:')
                    pdf.ln(0.5)
                    
                    pdf.set_font('Times','',20.0)
                    # Cell is as wide as the effective page width
                    # and multi_cell requires declaring the height of the cell.
                    pdf.multi_cell(effective_page_width, 0.3, final_text)
                    pdf.ln(0.5)

                    pdf.output(file_name)

def About_us_clicked():
    os.startfile(r'About Us.txt')

def Help_clicked():
    os.startfile(r'Help.txt')

def btn_clicked():
    print("Menu Button Clicked")

def doc_sum_open(window):

    def sel_btn_clicked(entry0):
        global counter
        if counter[0]<1:
            global my_dir
            counter[0]+=1
            my_dir = filedialog.askopenfilename(filetypes=files,defaultextension=files,
            initialdir=r"Documents")
            if(my_dir):
                entry0.delete(0,END)
                entry0.insert(0,my_dir)
            print("Select Button Clicked")
        counter=[0,0]


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
            if '.pdf' in my_dir:
                    import fitz # install using: pip install PyMuPDF
                    with fitz.open(my_dir) as pdfdoc:
                        plain_text = ""
                        for sipage in pdfdoc:
                            plain_text += sipage.get_text()

                    print(plain_text)
            else:
                file_obj=open(my_dir,mode='r',encoding="utf-8")
                plain_text=file_obj.read()
                file_obj.close()
            # summary_text = ms.text_summarizer(plain_text,4)
            summary_text = ms.text_summarizer(plain_text,4) 
            result = f'\nSummary:{summary_text[0]}\nKeywords:{summary_text[1]}' # final resultant text to display on GUI
            textBox0.insert(END,result)
            # textBox0.insert(END,"                                     Summary\n\n")
            # textBox0.insert(END,"\nKeywords : ")
            # textBox0.insert(END,summary_text[0])
            # textBox0.insert(END,summary_text[1])
            f=open(filepath,'w')
            f.write(summary_text[0])
            f.close()
    
    def save_btn_clicked():
        if not os.path.isfile(filepath) and not os.path.isfile(my_dir):
            messagebox.showinfo("Message","No such file found!")
        else:
            if os.path.isfile(filepath):
                save_file_dir = filepath
                file_obj=open(save_file_dir,'r')
                summary_text=file_obj.read()
                file_obj.close()
            elif os.path.isfile(my_dir):
                save_file_dir = my_dir
                file_obj=open(save_file_dir,'r')
                plain_text=file_obj.read()
                file_obj.close()
                summary_text = ms.text_summarizer(plain_text,4)[0]

            print("Directory is " + save_file_dir)
            global counter
            if counter[1]<1:
                counter[1]+1
                save_dir=filedialog.asksaveasfilename(filetypes = files, defaultextension = '.txt')
                print(summary_text)
                # with open(save_dir,'w') as sv:
                #     sv.write(summary_text)
                with open(save_dir,'w',encoding='utf-8') as sv:
                    sv.write(summary_text)
                if ('.pdf' in save_dir): 
                    text_to_pdf(summary_text,save_dir)
                messagebox.showinfo("Message","Summary is saved successfully!")
                
            counter=[0,0]


    def home_btn_clicked():
        bol_ans=messagebox.askokcancel("Message","Go to Home Page ?")
        if bol_ans == True:
            doc_window.destroy()
            window.deiconify()


    doc_window = Toplevel(window)
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

    # entry0.insert(0,r"Paste")

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
    
 # *********************************************************************************************************************************************************************************************************************************   

def url_sum_open(window):

    # FUNCTIONS
    # Read text entered and then call summary function to generate summary 
    def get_summary():
        if (len(str(entry0.get()))!=1) and (str(entry0.get())!='Enter URL here...'):
            raw_text = str(entry0.get())
            req = Request(
            url= entry0.get(), headers={'User-Agent': 'Mozilla/5.0'}
            )
            page = urlopen(req).read()
            # page = urlopen(raw_text)
            
            soup = BeautifulSoup(page,features="html.parser")
            fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
            finall_text = ms.text_summarizer(fetched_text,5)
            
            result = f'\nSummary:{finall_text[0]}\nKeywords:{finall_text[1]}' # final resultant text to display on GUI

            textBox0.insert(END,result)	
            
        else:
            messagebox.showerror("Error", "Input textbox is empty!")

    # Clear input textbox and display textbox widget
    def clear_text():
        if len(entry0.get()) != 1:
            entry0.delete(0,END)
            textBox0.delete('1.0', END)
            messagebox.showinfo("Message", "Successfully Reset!")
        else:  # Show an error
            messagebox.showerror("Error", "Already Reset!")

    # Save the generated summary in a specified .txt file
    def save_summary():
        # get whatever text entered in input box
        raw_text = str(entry0.get())
        if (len(raw_text)) != 1 and (str(entry0.get())!='Enter URL here...'):
            # get summarised text using text_summarize function of spacy_summarization.py file
            raw_text = str(entry0.get())
            page = urlopen(raw_text)
            soup = BeautifulSoup(page,features="html.parser")
            fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
            finall_text = ms.text_summarizer(fetched_text,5)[0]

            


            # = 'yourSummary' + timestr + '.txt' # create file name based on current time
            files = [  # ('All Files','.*'),
                ('Text File', '*.txt'),
                ('Document File', '*.docx'),
                ('PDF File', '*.pdf')]
            file_name = filedialog.asksaveasfilename(
                filetypes=files, defaultextension='.txt')
            with open(file_name, 'w', encoding='utf-8') as sv:
                sv.write(finall_text)
            messagebox.showinfo("Message", "Summary is saved successfully!")
            # result = '\nName of File: {} \nSummary:{}'.format(
            #     file_name, final_text) 
            textBox0.delete('1.0', END)
        
            # textBox0.insert(END, result)
        else:
            messagebox.showerror("Error", "Input textbox is empty!")

    # Home button
    def home_btn_clicked():
        bol_ans=messagebox.askokcancel("Message","Go to Home Page ?")
        if bol_ans == True:
            doc_window.destroy()
            window.deiconify()
        print("Button Clicked")


    doc_window = Toplevel(window)
    # doc_window=Tk()
    window.withdraw()
    doc_window.geometry("1200x690+350+200")
    doc_window.title("URL Summarizer")
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

    def temp_text(e):
        entry0.delete(0,"end")

    raww_entry=StringVar()
    entry0 = Entry(
    master=canvas,
    font=("Helvetica 12"),
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0,textvariable=raww_entry)

    entry0.insert(0,"Enter URL here...")
    # url = raww_entry.get()

    entry0.place(
    x = 534.1428575515747, y = 101,
    width = 396.7142848968506,
    height = 49)
    entry0.bind("<FocusIn>",temp_text)

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
    command = lambda : clear_text(),
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
    command = lambda : get_summary(),
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
    command = save_summary,
    bd=0,
    activebackground="#1e1e1e",
    relief = "flat")

    saveButton.place(
    x = 737, y = 568,
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

# *********************************************************************************************************************************************************************************************************************************

def text_sum_open(window):
    text_window = Toplevel(window)
    window.withdraw()
    # text_window.geometry("1024x600+100+20")
    text_window.geometry("1200x690+350+200")
    text_window.title("Text Summarizer")
    text_window.iconbitmap(r"Simple Text Summarizer GUI\textsummary.ico")

    # Canvas Layout
    texbox_canvas = Canvas(
        text_window,
        height = 690,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    texbox_canvas.place(x = 0, y = 0)

    textbox_background_img = PhotoImage(file = r'Simple Text Summarizer GUI\bbg.png')
    textbox_background = texbox_canvas.create_image(
        0, 0,
        image=textbox_background_img,
        anchor = "nw")

    ## ---- FUNCTIONS ----
    # Function that Read text entered and then call summary function to generate summary 
    def get_summary():
        raw_text = str(input_textBox.get('1.0',END)) # get whatever text entered in input box
        if (len(raw_text)) != 1:
            final_text = ms.text_summarizer(raw_text,5) 
            result = f'\nSummary:{final_text[0]}\nKeywords:{final_text[1]}' # final resultant text to display on GUI
            display_textBox.insert(END,result) # display_textBox is result display screen 
        else:
            messagebox.showerror("Error","Input textbox is empty!")

    # Function that Clear input textbox and display textbox widget
    def clear_text():
        if len(input_textBox.get('1.0',END)) != 1:
            input_textBox.delete('1.0',END)
            display_textBox.delete('1.0',END)
            messagebox.showinfo("Message","Successfully Reset!")
        else:   
            messagebox.showerror("Error","Already Reset!")

    # Function that Save the generated summary in a specified .txt file
    def save_summary():
       

        raw_text = str(input_textBox.get('1.0',END)) # get whatever text entered in input box
        if (len(raw_text)) != 1:
            final_text = ms.text_summarizer(raw_text,5)
            file_name=filedialog.asksaveasfilename(filetypes = files, defaultextension = '.txt')
            print(file_name)
            with open(file_name,'w',encoding='utf-8') as sv:
                sv.write(final_text)
            if ('.pdf' in file_name):
                
                text_to_pdf(final_text,file_name)
            messagebox.showinfo("Message","Summary is saved successfully!")
            # result = '\nName of File: {} \nSummary:{}'.format(file_name,final_text) # final resultant text to display on GUI
            display_textBox.delete('1.0',END)
            # display_textBox.insert(END,result) # display_textBox is display screen of home tab
        else:
            messagebox.showerror("Error","Input textbox is empty!")

    # Funcion that takes you back to home page
    def textbox_home_button_clicked():
        bol_ans=messagebox.askokcancel("Message","Go to Home Page ?")
        if bol_ans == True:
            text_window.destroy()
            window.deiconify()

    # Title label
    title_lbl = Label(texbox_canvas,text="Sumr!zer",font=("Helvetica",24,"bold"),bg="#1e1e1e",fg="white")
    title_lbl.place(x=0,y=0,width=1024,height=50)

    # Input Text Box
    input_textBox = ScrolledText(
        texbox_canvas,
        bd = 0,
        bg = "old lace",
        wrap = WORD,
        highlightthickness = 0)

    input_textBox.place(
        x = 110, y = 115,
        width = 430,
        height = 400)

    l1=Label(texbox_canvas,text="Original text",background='#87213b',foreground='white')
    l1.place(x=110, y=80,width=100,height=35)

    # Output Text Box
    display_textBox = ScrolledText(
        texbox_canvas,
        bd = 0,
        bg = "linen",
        wrap = WORD,
        highlightthickness = 0)

    display_textBox.place(
        x = 690, y = 115,
        width = 430,
        height = 400)

    l2=Label(texbox_canvas,text="Summarized text",background='#87213b',foreground='white')
    l2.place(x=690, y=80,width=100,height=35)

    ## ---- BUTTONS ----
    # HOME BUTTON
    textbox_home_img = PhotoImage(file = r'Simple Text Summarizer GUI\Home_Button.png')
    textbox_home_button = Button(
        texbox_canvas,
        image = textbox_home_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = textbox_home_button_clicked,
        bd=0,
        activebackground="#59192b",
        relief = "flat")

    textbox_home_button.place(
        x = 0, y = 0,
        width = 61,
        height = 61)

    # RESET BUTTON
    textbox_reset_img = PhotoImage(file = r'Simple Text Summarizer GUI\Reset_Button.png')
    textbox_reset_buuton = Button(
        texbox_canvas,
        image = textbox_reset_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = clear_text,
        bd=0,
        activebackground="#1e1e1e",
        relief = "flat")

    textbox_reset_buuton.place(
        x = 230, y = 600,
        width = 170,
        height = 68)

    # SUMMARY BUTTON
    textbox_summary_img = PhotoImage(file = r'Simple Text Summarizer GUI\Summary_Button.png')
    textbox_summary_button = Button(
        texbox_canvas,
        image = textbox_summary_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = get_summary,
        bd=0,
        activebackground="#1e1e1e",
        relief = "flat")

    textbox_summary_button.place(
        x = 480, y = 600,
        width = 170,
        height = 68)

    # SAVE BUTTON
    textbox_save_img = PhotoImage(file = r'Simple Text Summarizer GUI\Save_Button.png')
    textbox_save_button = Button(
        texbox_canvas,
        image = textbox_save_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = save_summary,
        bd=0,
        activebackground="#1e1e1e",
        relief = "flat")

    textbox_save_button.place(
        x = 730, y = 600,
        width = 170,
        height = 68)

    text_window.resizable(False, False)

    # FUNCTION TO CLOSE WINDOW ABRUPTLY 
    def doSomething():
        window.deiconify()
        text_window.destroy()

    text_window.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
    text_window.mainloop()


# *********************************************************************************************************************************************************************************************************************************
# Define a function to close the window
def close(window):
   window.destroy()

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
