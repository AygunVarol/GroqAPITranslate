# GroqAPITranslate

GroqAPITranslate is a simple FastAPI application that demonstrates API integration using Groq. The API translates English text into Spanish using a Hugging Face translation pipeline.

## Features

- **API Token Authentication:** Secures the translation endpoint.
- **Translation Endpoint:** Translates English text to Spanish.
- **Hugging Face Integration:** Uses the `Helsinki-NLP/opus-mt-en-es` model for translation.
- **FastAPI:** Provides a lightweight framework for serving the API.

## Files

- `task3.py`: The main FastAPI application file.
- `README.md`: This file.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)
- (Optional) A virtual environment (recommended)

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/aygunvarol/GroqAPITranslate.git
   cd GroqAPITranslate
   ```

2. **Create and Activate a Virtual Environment:**


#### On Windows
```bash
python -m venv venv
venv\Scripts\activate
```
#### On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Clone the Repository:**

```bash
pip install fastapi uvicorn transformers
```

# Running the API Locally

```bash
uvicorn task3:app --reload
```

### The API will be available at: http://127.0.0.1:8000

# API Endpoint

## 1. Simple GET Request

```bash
curl "http://127.0.0.1:8000/translate?text=Hello%2C%20how%20are%20you%3F" -H "token: my_secret_token_12345"
```

## 2. GET Request with Verbose Output

```bash
curl -v -X GET "http://127.0.0.1:8000/translate?text=Hello%2C%20how%20are%20you%3F" -H "token: my_secret_token_12345"
```

## 3. Saving the Response to a File

```bash
curl "http://127.0.0.1:8000/translate?text=Hello" -H "token: my_secret_token_12345" -o response.json
```
