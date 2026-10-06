# capstone_project

# 📚 AI Powered Study Guide Generator

> **Upload any lecture PDF, get a complete study pack.**

Study Guide Generator is an AI-powered **Streamlit application** that helps students convert lecture PDFs or syllabus text into a structured and easy-to-study learning pack.

The application uses the **Groq API** to generate study material based on the selected difficulty level: **Beginner, Intermediate, or Advanced**.

---

## 🚀 Features

### 📄 PDF Upload

* Upload a lecture PDF directly.
* Supports PDFs up to **15 pages**.
* Extracts text automatically using `pypdf`.

### 📝 Syllabus Text Input

Students can also paste their syllabus, lecture notes, or study content directly into the application.

### 🎯 Difficulty Selection

Choose from three difficulty levels:

* **Beginner** – Simple explanations and fundamental concepts.
* **Intermediate** – Moderate technical depth and conceptual relationships.
* **Advanced** – Detailed explanations, deeper concepts, and challenging questions.

The selected difficulty level changes the complexity of the generated study material.

### 📖 Complete Study Pack

The AI generates:

1. **Concise Summary Notes**
2. **20 Practice MCQs**
3. **MCQ Answers**
4. **MCQ Explanations**
5. **5 Short-Answer Questions**
6. **Model Answers**
7. **Key Terms Glossary**
8. **Suggested Study Order**

### 📥 Download Options

The generated content can be downloaded as:

* 📄 Formatted PDF – Complete study pack
* 📊 CSV – MCQs for flashcard/import tools

---

# 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │       Student        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Streamlit App      │
                    │       app.py         │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  │                         │
                  ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │   Lecture PDF   │       │  Syllabus Text  │
        └────────┬────────┘       └────────┬────────┘
                 │                         │
                 ▼                         │
        ┌─────────────────┐                │
        │     pypdf       │                │
        │  Text Extraction│                │
        └────────┬────────┘                │
                 │                         │
                 └────────────┬────────────┘
                              ▼
                    ┌──────────────────────┐
                    │   Prompt Generation  │
                    │ Difficulty Selection  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Groq API        │
                    │   LLM Generation      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Study Pack        │
                    ├──────────────────────┤
                    │ Summary Notes        │
                    │ 20 MCQs              │
                    │ 5 Short Answers      │
                    │ Glossary             │
                    │ Study Order          │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    ▼                      ▼
             ┌──────────────┐      ┌──────────────┐
             │ PDF Download │      │ CSV Download │
             └──────────────┘      └──────────────┘
```

---

# 🛠️ Technologies Used

| Technology                     | Purpose                               |
| ------------------------------ | ------------------------------------- |
| **Python**                     | Application development               |
| **Streamlit**                  | Web application UI                    |
| **Groq API**                   | AI-powered study material generation  |
| **LangChain / LangChain-Groq** | LLM integration and prompt management |
| **pypdf**                      | PDF text extraction                   |
| **python-dotenv**              | Environment variable management       |
| **ReportLab**                  | PDF generation                        |
| **Pandas**                     | CSV generation                        |
| **CSV**                        | MCQ export                            |

---

# 🤖 AI Model

This project uses the **Groq API** instead of the Claude API.

The model name is configured through the environment variable:

```text
GROQ_MODEL
```

For example:

```env
GROQ_MODEL=llama-3.3-70b-versatile
```

> **Note:** Groq model availability can change. If the configured model is unavailable in your Groq account, replace it with a currently supported Groq model.

---

# 📁 Project Structure

```text
study-guide-generator/
│
├── app.py
├── models.py
├── prompts.py
├── study_generator.py
├── pdf_processor.py
├── exporters.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# 📌 File Responsibilities

### `app.py`

Main Streamlit application.

Responsible for:

* PDF upload
* Syllabus text input
* Difficulty selection
* Generate button
* Displaying generated content
* PDF download
* CSV download

---

### `models.py`

Contains the Groq/LangChain model configuration.

Example responsibilities:

```text
Groq API initialization
Model configuration
Temperature configuration
API key loading
```

---

### `prompts.py`

Contains prompts used to generate the study material.

The prompts control the output based on:

```text
Beginner
Intermediate
Advanced
```

---

### `study_generator.py`

Main AI generation logic.

Responsible for generating:

```text
Summary
MCQs
Short-answer questions
Glossary
Study order
```

---

### `pdf_processor.py`

Handles lecture PDF processing.

Responsible for:

```text
PDF upload
Page validation
Text extraction
15-page limit
```

---

### `exporters.py`

Responsible for converting generated content into downloadable formats.

Supports:

```text
Study Pack → PDF
MCQs → CSV
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/study-guide-generator.git
```

Move into the project directory:

```bash
cd study-guide-generator
```

---

# 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 4. Configure Groq API

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_supported_groq_model
```

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
GROQ_MODEL=llama-3.3-70b-versatile
```

**Never upload your actual ****`.env`**** file or API key to GitHub.**

Use `.env.example` instead:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_supported_groq_model
```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🧑‍🎓 How to Use

### Step 1 — Upload Content

Upload a lecture PDF containing up to **15 pages**.

OR

Paste syllabus/lecture content into the text input area.

---

### Step 2 — Select Difficulty

Choose:

```text
Beginner
Intermediate
Advanced
```

---

### Step 3 — Generate Study Pack

Click:

```text
Generate Study Pack
```

The application sends the content and difficulty instructions to the Groq-powered LLM.

---

### Step 4 — Review the Study Pack

The application generates:

### Summary Notes

Short and structured notes containing the important concepts.

### 20 MCQs

Each question contains:

```text
Question
Options
Correct Answer
Explanation
```

### 5 Short-Answer Questions

Each question includes a model answer.

### Key Terms Glossary

Important concepts are presented with simple definitions.

### Suggested Study Order

Topics are organized into a recommended learning sequence.

---

# 📥 Export

## Complete Study Pack

The complete study material can be downloaded as a formatted PDF.

```text
study_pack.pdf
```

The PDF contains:

```text
Summary Notes
↓
20 MCQs
↓
MCQ Answers & Explanations
↓
5 Short-Answer Questions
↓
Model Answers
↓
Key Terms Glossary
↓
Suggested Study Order
```

---

## MCQ CSV Export

The MCQs can be exported separately as CSV.

Example structure:

```csv
Question,Option A,Option B,Option C,Option D,Answer,Explanation
"What is Python?","Language","Database","OS","Browser","A","Python is a programming language."
```

This makes the questions suitable for importing into spreadsheet-based or flashcard tools.

---

# 🎯 Difficulty System

The application uses different instructions for each difficulty level.

## Beginner

Focuses on:

* Simple language
* Basic definitions
* Fundamental concepts
* Easy examples
* Basic MCQs

Example:

```text
Explain the concept in simple language.
Assume the student is new to the topic.
Avoid unnecessary technical terminology.
```

---

## Intermediate

Focuses on:

* Technical terminology
* Conceptual relationships
* Practical examples
* Moderate-level MCQs
* Application-based questions

Example:

```text
Assume the student understands basic terminology.
Explain relationships between concepts.
Include practical examples.
```

---

## Advanced

Focuses on:

* Deep technical concepts
* Complex relationships
* Real-world applications
* Analytical questions
* Challenging MCQs

Example:

```text
Provide deeper technical explanations.
Include advanced concepts and edge cases.
Use analytical and application-oriented questions.
```

Therefore, the difficulty selector does not simply change a label — it changes the instructions used for content generation.

---

# 🔒 Security

API keys are stored using environment variables.

The project uses:

```text
python-dotenv
```

Example:

```python
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
```

Do not hard-code your API key:

```python
# ❌ Don't do this

GROQ_API_KEY = "gsk_your_actual_key"
```

Instead:

```python
# ✅ Use environment variables

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
```

---

# 🚫 PDF Limit

The application supports lecture PDFs up to:

```text
15 pages
```

If a PDF exceeds the supported page limit, the application should display an appropriate error message instead of processing the document.

---

# 📦 Example Requirements

Your `requirements.txt` can contain packages such as:

```text
streamlit
groq
langchain
langchain-groq
pypdf
python-dotenv
reportlab
pandas
```

Use the versions appropriate for your current Python environment.

---

# 💡 Use Cases

This project can be useful for:

* College students
* University students
* Exam preparation
* Lecture revision
* Certification preparation
* Self-learning
* Technical interview preparation
* Quick revision from lecture PDFs

---

# 🔮 Future Enhancements

Possible improvements include:

* [ ] Multiple PDF upload
* [ ] DOCX support
* [ ] PPTX support
* [ ] YouTube lecture transcript support
* [ ] Automatic topic detection
* [ ] Interactive quiz mode
* [ ] Score tracking
* [ ] Flashcard generation
* [ ] Spaced-repetition study plans
* [ ] Chat with uploaded lecture
* [ ] RAG-based question answering
* [ ] User authentication
* [ ] Study progress dashboard
* [ ] Cloud deployment

---

# 🌐 Deployment

The application can be deployed using platforms that support Streamlit applications.

Before deployment, configure the Groq API key using the platform's **Secrets/Environment Variables** feature rather than committing `.env` to GitHub.

---

# 🧪 Example Workflow

```text
Student
   │
   ▼
Upload Lecture PDF
   │
   ▼
Extract Text using pypdf
   │
   ▼
Select Difficulty
   │
   ▼
Generate Prompt
   │
   ▼
Groq API
   │
   ▼
AI Study Pack
   │
   ├── Summary Notes
   ├── 20 MCQs
   ├── 5 Short Answers
   ├── Glossary
   └── Study Order
          │
          ▼
     ┌────┴────┐
     ▼         ▼
    PDF       CSV
```

---

# 🎓 Project Objective

The main objective of the **Study Guide Generator** is to reduce the time students spend manually converting lecture material into revision resources.

Instead of reading a long lecture document and creating notes, questions, and revision material manually, students can upload their content and receive a structured study pack generated by AI.

---

# 👨‍💻 Author

**Pavan Kalyan**

AI / GenAI Developer | Python | LangChain | LLMs | Cloud

---

# ⭐ Project Highlights

```text
✅ Streamlit AI Application
✅ Groq API Integration
✅ PDF Text Extraction
✅ Difficulty-Based AI Generation
✅ 20 MCQs with Explanations
✅ Short-Answer Questions
✅ Key Terms Glossary
✅ Recommended Study Order
✅ PDF Export
✅ CSV Export
✅ Environment Variable Security
```

---

## 📜 License

This project is created for educational and portfolio purposes.

# Study_Guide_Generator
# study-guide-generator
