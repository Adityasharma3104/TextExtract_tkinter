import tkinter
from tkinter import filedialog, Label, Text, Button
import PyPDF2
import easyocr
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title('Text Extractor')


def extract_text_from_pdf(filename):
    output_text = ""
    reader = PyPDF2.PdfReader(filename)
    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        output_text += current_text
    return output_text


def extract_text_from_image(image_path):
    reader = easyocr.Reader(['en'], model_storage_directory='.',gpu=False)
    result = reader.readtext(image_path)
    extracted_text = [text[1] for text in result]
    return '\n'.join(extracted_text) 


def openfile():
    filename = filedialog.askopenfilename(
        title="Open file",
        initialdir='D:\\vscode\\pythonn'
    )
    if filename:
        print(filename)

        file_label.configure(text="Selected file: " + filename)

        if filename.lower().endswith('.pdf'):
            output_text = extract_text_from_pdf(filename)
        elif filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            output_text = extract_text_from_image(filename)
        else:
            output_text = "Unsupported file format."

        output_file_text.delete("1.0", tkinter.END)
        output_file_text.insert(tkinter.END, output_text)

       
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(filename)
            img = img.resize((200, 200)) 
            img = ImageTk.PhotoImage(img) 
           

            panel.configure(image=img)
            panel.image = img  
            panel.pack(side="top", padx=10, pady=10, anchor='nw')


file_label = Label(root, text="No file selected")
output_file_text = Text(root)
openfile_button = Button(root, text="Open file", command=openfile)
panel = Label(root) 

file_label.pack()
output_file_text.pack()
openfile_button.pack()

root.mainloop()
