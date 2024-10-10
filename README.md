# Langchain

## Description

The **Langchain** project is an integration of various tools, agents, and machine learning models with the Langchain framework. It leverages powerful libraries such as OpenAI, Huggingface, Codellama, NVIDIA-NIM, and more to build and deploy state-of-the-art language models and agents capable of handling various natural language processing tasks.

The project also utilizes Langchain to create seamless pipelines for model training, data processing, and agent development, making it easier to interact with multiple models and frameworks in an efficient and scalable manner.

## Tools and Technologies Used
This repository includes integrations with the following:
- **Langchain**: A framework for developing applications powered by language models.
- **OpenAI**: Integration for leveraging GPT models via OpenAI API.
- **Huggingface**: Integrates Huggingface models with Langchain.
- **Codellama**: Codellama language models with Langchain for code-related tasks.
- **NVIDIA-NIM**: Utilizes NVIDIA’s Neural Interface models for accelerated NLP tasks.
- **Ollama**: Includes Ollama’s integration for multi-model execution in Langchain.
- **GraphDB**: A graph database integration for managing knowledge bases.
- **FastAPI**: API creation and deployment using FastAPI for handling model queries.

## Installation

To install the project dependencies, clone the repository and install the required packages:

```bash
git clone https://github.com/Koushik7893/langchain-project.git
cd langchain-project
pip install -r requirements.txt
```

## Usage

Once the dependencies are installed, you can begin using the various tools and agents integrated into Langchain.

### Running the Application
To launch the project with FastAPI:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, which you can access at `http://127.0.0.1:8000`.

### Example Usages
- **OpenAI and Langchain**: Use OpenAI’s GPT models for text generation:
   ```python
   from langchain.openai import OpenAI
   llm = OpenAI(model="gpt-4o")
   ```
   
- ## LangChain - Chat with Search

This Streamlit application integrates with **LangChain** to provide a chatbot that can perform live web searches, fetch academic papers from Arxiv, and retrieve information from Wikipedia. The app allows users to interact with the chatbot and receive relevant information based on real-time queries.

### Features:
- **Arxiv API**: Retrieves the top academic paper related to the user's query.
- **Wikipedia API**: Provides a concise summary from Wikipedia based on the query.
- **DuckDuckGo Search**: Performs web searches for information using DuckDuckGo.
- **ChatGroq Integration**: Utilizes the Llama3-8b-8192 model for natural language processing.
- **Streamlit Interface**: Uses `StreamlitCallbackHandler` to display the chatbot's thoughts and actions live in the app.

### How it Works:
1. Users input a query or topic through the chat interface.
2. The chatbot searches various sources (Arxiv, Wikipedia, and DuckDuckGo) to fetch relevant information.
3. The chatbot responds interactively, displaying results directly in the Streamlit app.

### Setup:
1. Clone the repository and install the required dependencies.
2. Add your Groq API key in the app sidebar to enable the chatbot's functionality.
3. Run the app locally with `streamlit run <your_file.py>`.

For more LangChain and Streamlit integrations, visit the official [LangChain GitHub page](https://github.com/langchain-ai/streamlit-agent).

## Features

- Multi-model integration with **Langchain** framework.
- Support for **NLP tasks**, **Code Generation**, and **Data Processing**.
- API creation and deployment using **FastAPI**.
- Leverages state-of-the-art models from **Huggingface**, **OpenAI**, **Codellama**, and more.
- Incorporates **GraphDB** for managing knowledge graphs.
- Seamless agent integration for managing workflows and tasks.


## License

This project is licensed under the MIT License. See the [Apache License 2.0](LICENSE) file for more information.
