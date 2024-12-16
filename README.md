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
