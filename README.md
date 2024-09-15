# IntelliDoc - Document Processing and Q&A Application

## Overview
**IntelliDoc** is a document processing and Q&A application built using Streamlit. It allows users to upload files in various formats like PDF, DOCX, and Markdown, and it can extract and summarize text from these files. The application also integrates a Q&A chatbot feature that can answer questions based on the content of the uploaded documents.

## Features
- **Text Extraction**: Automatically extract text from PDF, DOCX, and Markdown files.
- **Q&A Bot**: Ask questions and get answers based on document content.
- **Multi-format Support**: Supports file formats like PDF, DOCX, and Markdown.
- **Interactive User Interface**: Built using Streamlit for a smooth and responsive user experience.

## Installation and Setup

### Prerequisites
Before setting up the project, make sure you have the following installed on your system:
- [Python 3.x](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Streamlit](https://streamlit.io/)

### Step-by-Step Setup

1. **Clone the Repository**
   Clone the project repository to your local machine.
   git clone https://github.com/your-username/my-starter-kit.git
2. **Navigate to Project Directory""
   cd my-starter-kit
3. **Install Dependencies Install all required dependencies using pip:**
   pip install -r requirements.txt
4. **Run the Application Launch the application with Streamlit:**
   streamlit run main.py
5. **Upload Documents** 
   Once the application is running, you can upload PDF, DOCX, or Markdown files.
   Use the Q&A bot to ask questions about the document content.

### Key Libraries:
Streamlit: For building the user interface.
PyPDF2: For extracting text from PDF files.
python-docx: For working with DOCX files.
Markdown: For handling Markdown file content.
