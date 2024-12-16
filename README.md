# PDF Question Answering Chatbot

This project implements a simple chatbot that answers questions based on the content extracted from a PDF file. It uses natural language processing (NLP) techniques, such as TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity, to find the most relevant text in the PDF document that matches the user's query.

## Features

- Extracts text from a PDF file.
- Allows users to ask questions about the content of the PDF.
- Returns the most relevant section of text that answers the user's question.
- Uses `TF-IDF` for text representation and `cosine similarity` for measuring text relevance.

## Requirements

- Python 3.x
- Libraries:
  - PyPDF2
  - scikit-learn
  - tkinter

You can install the required libraries by running the following command:

  ```bash
    pip install PyPDF2 scikit-learn
  ```
How It Works

## Upload the PDF file
When prompted, select the PDF file you want to upload using a file dialog.

## Ask a question
Enter your query related to the content of the PDF. The chatbot will return the most relevant section of the document.

## Repeat the process
The chatbot will keep running until you choose to exit.


### Functions

1. **`extract_text_from_pdf(pdf_path)`**  
   This function extracts text from the given PDF file.

2. **`get_answer_from_pdf(question)`**  
   This function processes the user’s question and the text extracted from the PDF to find the most relevant answer.

3. **`main()`**  
   This function handles the interaction with the user.


# The tkinter library is used for creating a file dialog for PDF selection.
Example Usage
```bash
$ python pdf_qa_chatbot.py
Welcome to the PDF Question Answering Chatbot...
Press (y/n) to insert a PDF: y
Enter the query: "wecrm contact detail"
The most relevant text from the PDF will be shown here.
```
## Script Explanation

1. **User Input for PDF**  
   When prompted with `Press (y/n) to insert a PDF:`, the user can select a PDF file using a file dialog.

2. **Text Extraction**  
   The selected PDF file is processed, and the text is extracted page by page.

3. **Querying**  
   After extracting the PDF text, the script allows the user to enter a query.

4. **Continuous Interaction**  
   The chatbot remains interactive, accepting multiple queries.

## License
```
This project is licensed under the MIT License. See the LICENSE file for details.
