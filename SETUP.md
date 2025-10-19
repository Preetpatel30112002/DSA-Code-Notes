# Medical Assistant AI 🩺💊

An intelligent medical document analysis system powered by Retrieval-Augmented Generation (RAG) that allows users to upload medical PDFs and ask questions about their content.

## 🌟 Features

- **PDF Document Processing**: Upload and process medical documents in PDF format
- **Intelligent Question Answering**: Ask questions about document content and receive AI-powered responses
- **Vector Database Storage**: Efficient document embedding and retrieval using ChromaDB
- **Context-Aware Responses**: Answers are generated based on relevant document sections
- **Interactive Chat Interface**: User-friendly Streamlit-based chat interface
- **Source Citations**: Responses include references to specific document sections
- **GPU/CPU Support**: Automatic device detection for optimal performance

## 🏗️ Architecture

The system consists of several key components:

1. **Document Ingestion** (`data_ingest.py`): Extracts and chunks text from PDF documents
2. **Embedding Pipeline** (`embed_chunks_chromadb.py`): Converts text chunks into vector embeddings
3. **RAG Pipeline** (`rag_pipeline.py`): Retrieves relevant context and generates responses
4. **Streamlit UI** (`main.py`): Interactive web interface for document upload and chat
5. **Model Training** (`model_training.py`): Optional fine-tuning capabilities with LoRA

## 📋 Prerequisites

- Python 3.12.0
- CUDA-compatible GPU (optional, for faster processing)
- No HuggingFace API token due to usage of public model (for model access)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd medical-assistant-ai
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

## 💻 Usage

### Running the Application

```bash
streamlit run main.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Interface

1. **Upload Document**: Click "Choose a PDF file to analyze" in the sidebar
2. **Process Document**: Click the "🔄 Process" button to analyze the document
3. **Ask Questions**: Type your questions in the chat input at the bottom
4. **View Responses**: The AI will provide answers based on the document content
5. **Clear Chat**: Use the "🗑️ Clear Chat" button to start a new conversation
6. **Reset Document**: Click "🗑️ Clear" to upload a new document

## 📁 Project Structure

```
medical-assistant-ai/
│
├── config.py                    # Configuration settings
├── data_ingest.py              # PDF text extraction
├── embed_chunks_chromadb.py    # Vector embedding pipeline
├── rag_pipeline.py             # RAG chain implementation
├── main.py                     # Streamlit application
├── model_training.py           # Model fine-tuning (optional)
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
│
├── /tmp/chroma_db/            # Vector database storage (auto-created)
└── /tmp/uploads/              # Temporary file storage (auto-created)
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Model configurations
EMBEDDING_MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
LLM_MODEL_NAME = "google/flan-t5-base"

# Retrieval settings
TOP_K = 3  # Number of relevant chunks to retrieve

# Text chunking
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

# Database settings
CHROMA_PERSIST_DIRECTORY = "/tmp/chroma_db"
COLLECTION_NAME = "medical_documents"
```

## 🎯 Key Components

### Embedding Model
- **Model**: `sentence-transformers/all-mpnet-base-v2`
- **Purpose**: Converts text into vector embeddings for semantic search

### Language Model
- **Model**: `google/flan-t5-base`
- **Purpose**: Generates natural language responses based on retrieved context

### Vector Database
- **Technology**: ChromaDB
- **Purpose**: Stores and retrieves document embeddings efficiently

## 🛠️ Troubleshooting

### Common Issues

**Issue**: "No documents found in database"
- **Solution**: Upload and process a PDF document first

**Issue**: GPU not being used
- **Solution**: Ensure CUDA is properly installed and PyTorch can access GPU

**Issue**: Out of memory errors
- **Solution**: Reduce `CHUNK_SIZE` and `TOP_K` in config.py

**Issue**: Slow processing
- **Solution**: Consider using a GPU or reducing document size

## 📊 Performance Tips

1. **GPU Usage**: Enable GPU for 5-10x faster processing
2. **Chunk Size**: Smaller chunks (500-800) improve accuracy but increase processing time
3. **Top K**: Start with 3-5 relevant chunks for balanced performance
4. **Model Selection**: Use smaller models for faster inference on CPU

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📝 License

This project is provided as-is for educational and research purposes.

## 🙏 Acknowledgments

- **LangChain**: For the RAG framework
- **HuggingFace**: For transformer models
- **ChromaDB**: For vector database
- **Streamlit**: For the web interface

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the documentation
- Review closed issues for similar problems

## 🔮 Future Enhancements

- [ ] Multi-document support
- [ ] Advanced citation formatting
- [ ] Export conversation history
- [ ] Multi-language support
- [ ] Custom model fine-tuning UI
- [ ] Batch document processing
- [ ] API endpoint for integration
