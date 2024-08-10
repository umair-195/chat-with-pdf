# Question Answering System

## Overview

This project demonstrates a **Question Answering System** that utilizes a pre-trained model for natural language processing. Users can submit questions and receive answers based on provided text or PDF documents. The system leverages the Hugging Face `transformers` library and incorporates a simple web interface for user interaction.

## Features

- **Question Answering**: Users can input questions and receive answers based on a given context.
- **PDF Upload**: Users can upload PDF files, which are processed to extract text and use it as context for answering questions.
- **Web Interface**: A user-friendly HTML form for submitting questions and uploading PDF files.

## Technologies Used

- **Python**: For backend processing and serving the application.
- **Flask**: A lightweight WSGI web application framework for creating the web server.
- **Transformers Library**: From Hugging Face, used for leveraging pre-trained NLP models.
- **HTML/CSS/JavaScript**: For the front-end interface.

## File Descriptions
- **`app.py`**: Main application script containing Flask routes and logic.
- **`requirements.txt`**: List of dependencies.
- **`index.html`**: HTML templates.
- **`README.md`**: This documentation file.

## Screenshots

**Snapshot of the Web Interface:**

![Web Interface](1.png)

## How to Run

1. **Set Up Environment**:
   - Install Python and Flask.
   - Create a virtual environment and install the required packages using `requirements.txt`.

2. **Run Flask Application**:
   - Execute the command `python app.py` to start the Flask server.

3. **Open Web Browser**:
   - Navigate to `http://127.0.0.1:5000` to access the Question Answering System.

## Dependencies

- `Flask`: For the web application framework.
- `transformers`: For accessing pre-trained models.
- `PyPDF2`: For PDF file text extraction.

**To install the dependencies:**

```bash
pip install -r requirements.txt
```
## Future Work

### Optical Character Recognition (OCR)
- **Objective**: Integrate OCR capabilities to extract text from images and scanned documents.
- **Implementation**: Use libraries like `Tesseract` or `EasyOCR` to process images and convert them to text, which can then be used as context for the question answering system.

### Model Enhancements
- **Objective**: Implement and compare different pre-trained models to enhance the accuracy and performance of the question answering system.
- **Models to Consider**:
  - **BERT**: Fine-tune BERT models for question answering tasks.
  - **RoBERTa**: Experiment with RoBERTa for improved contextual understanding.
  - **DistilBERT**: Use DistilBERT for faster performance with a smaller model size.
  - **ALBERT**: Explore ALBERT for its efficiency in handling large-scale text.

### User Interface Improvements
- **Objective**: Enhance the user interface for a more intuitive experience.
- **Implementation**: Add features like real-time feedback, improved styling, and additional options for uploading various document formats.

### Deployment and Scalability
- **Objective**: Prepare the application for deployment and ensure it can handle increased user traffic.
- **Implementation**: Use cloud services like AWS or Azure for scalable deployment and implement load balancing and performance monitoring.

These enhancements will contribute to making the Question Answering System more versatile and user-friendly.
# Contact Information

If you have any questions or need further information, please reach out to me using the contact details below.

- **LinkedIn**: [Muhammad Umair Arshad](https://www.linkedin.com/in/muhammad-umair-arshad-a698651a5/)
- **Email**: [chumair327@gmail.com](mailto:chumair327@gmail.com)

