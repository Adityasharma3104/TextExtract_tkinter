# TextExtract_tkinter
an Tkinter GUI that extracts text from images and pdf .


Here's a README file for your simplified Text Extractor project:


Text Extractor is a simple GUI application built with Python's Tkinter library to extract text from PDF documents and image files. It uses PyPDF2 for PDF text extraction and EasyOCR for image text extraction.

## Features

- Extract text from PDF files.
- Extract text from image files (.png, .jpg, .jpeg).
- Display extracted text within the application.
- Display selected images within the application.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)
- PyPDF2
- easyocr
- PIL (Pillow)

## Installation

1. Clone the repository or download the source code.

2. Install the required Python packages using pip:
   ```bash
   pip install PyPDF2 easyocr pillow
   ```

3. Ensure that the `craft_mlt_25k` model for EasyOCR is downloaded. EasyOCR will handle this automatically when you first run the application, but you can also download it manually if needed.

## Usage

1. Navigate to the directory containing the source code.
2. Run the application using Python:
   ```bash
   python text_extractor.py
   ```
3. The application window will appear with the following components:
   - A label indicating whether a file is selected.
   - A button to open and select a file.
   - A text area to display the extracted text.
   - An image display area for selected image files.

4. Click the "Open file" button to select a PDF or image file.
5. The selected file's text will be extracted and displayed in the text area. If an image file is selected, it will also be displayed in the image area.

## Code Overview


### extract_text_from_pdf

```python
def extract_text_from_pdf(filename):
    output_text = ""
    reader = PyPDF2.PdfReader(filename)
    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        output_text += current_text
    return output_text
```
This function extracts text from each page of a PDF file and concatenates it into a single string.

### extract_text_from_image

```python
def extract_text_from_image(image_path):
    reader = easyocr.Reader(['en'], model_storage_directory='.', gpu=False)
    result = reader.readtext(image_path)
    extracted_text = [text[1] for text in result]
    return '\n'.join(extracted_text)
```
This function uses EasyOCR to read text from an image file and returns the extracted text as a string.

### openfile

```python
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
```
This function handles the file selection dialog, determines the file type, and extracts text accordingly. It updates the UI with the extracted text and the selected image (if applicable).

## License

This project is open source and available under the [MIT License](LICENSE).

---

Feel free to customize this README to better suit your specific project details and preferences.
