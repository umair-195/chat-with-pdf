from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from flask import Flask, request, jsonify, send_from_directory
import fitz  # PyMuPDF
import os

# Load pre-trained model and tokenizer
model_name = "distilbert-base-uncased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Flask web server setup
app = Flask(__name__)

# Directory to save uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to handle question answering
def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text += page.get_text()
    return text

# Endpoint to handle user questions with context from PDF
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    context = data.get('context')
    pdf_path = data.get('pdf_path')

    if not question or (not context and not pdf_path):
        return jsonify({"error": "Question and context or PDF path are required"}), 400

    if pdf_path:
        context = extract_text_from_pdf(pdf_path)

    answer = answer_question(question, context)
    return jsonify({"answer": answer})

# Endpoint to handle PDF file uploads
@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return jsonify({"filepath": file_path})

# Serve the HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
