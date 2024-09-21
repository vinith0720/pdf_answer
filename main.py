import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import filedialog

# Create a root window and hide it
root = tk.Tk()
root.withdraw()
# Open a file dialog to select a file
# pdf_path = filedialog.askopenfilename()

# pdf_path ="C:/Users/vinit/Downloads/detail.pdf"

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Example usage
# pdf_text = extract_text_from_pdf('C:/Users/vinit/Downloads/detail.pdf')

def get_answer_from_pdf(question):
    
    document = pdf_text.split('\n')    # Load the extracted text from the PDF
    vectorizer = TfidfVectorizer()       # Initialize the TF-IDF Vectorizer
    tfidf_matrix = vectorizer.fit_transform(document)   # Fit and transform the document and question
    question_tfidf = vectorizer.transform([question])
    similarity = cosine_similarity(question_tfidf, tfidf_matrix)        # Calculate the cosine similarity
    most_similar_idx = similarity.argmax()      # Find the most similar text in the document
    return document[most_similar_idx]

# print(get_answer_from_pdf('wecrm contact detail'))
def main():
    name = input("enter the query:")
    name ="'" +name+"'"
    print(get_answer_from_pdf(name))
    main()

if __name__=="__main__":
    print("welcome to chatbot....")
    dummy =input("press (y/n) to insert pdf :")
    if dummy.lower() == 'y':
        pdf_path = filedialog.askopenfilename()
    pdf_text = extract_text_from_pdf(pdf_path=pdf_path)
    main()