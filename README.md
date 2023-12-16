# UltraGPT - Gemini AI Chat

UltraGPT is a Streamlit web application powered by the Gemini AI Chat model. This application allows users to interact with a generative language model for chat-based conversations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Introduction

Gemini Pro Chat is a conversational AI application built using the [Gemini Pro Model](https://deepmind.google/technologies/gemini/) model. It leverages the Vertex AI library and Streamlit for a user-friendly interface. The application enables users to engage in chat conversations with a powerful generative model.

## Features

- **Interactive Chat**: Users can engage in conversations with the AI model through a user-friendly chat interface.
- **Real-time Responses**: The application makes API requests to the Gemini AI model for generating responses in real-time.
- **Error Handling**: The application handles errors gracefully and notifies users if there's an issue with fetching responses.

## Getting Started

To run Gemini Pro Web App locally, follow these steps:

1. Install and initialize the gcloud CLI.

When you initialize the gcloud CLI, be sure to specify a Google Cloud project in which you have permission to access the resources your application needs.

2. Create your credential file:

```bash
gcloud auth application-default login
```

3. Install the required dependencies:

```bash
pip install vertexai streamlit
```
Replace ```your_app_file.py``` with the name of the file containing the provided code.
## Usage

    Open the Streamlit application in your browser.

    Enter your messages in the chat input box labeled "You:".

    The AI model will generate responses in real-time and display them in the chat interface.

    Conversations are stored in the chat history for reference.

## Contributing

If you would like to contribute to UltraGPT, feel free to submit issues or pull requests. Your contributions are welcome!
## Author

UltraGPT was created by Saurabh.
## License

This project is licensed under the MIT License.

