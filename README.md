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
