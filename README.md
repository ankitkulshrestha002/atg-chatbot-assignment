# Local Command-Line Chatbot

This project is a modular, command-line chatbot built in Python using the Hugging Face `transformers` library, as required for the ATG Technical Assignment. It features a conversational AI with a unique personality that can maintain short-term memory.

## Key Features

-   **Modular Architecture:** Code is logically separated into an interface, a model loader, and a chat manager for maintainability.
-   **Local Model Inference:** Runs the `TinyLlama-1.1B-Chat-v1.0` model locally, ensuring it works without a constant internet connection after initial setup.
-   **Conversational Memory:** Implements a sliding window mechanism to remember the last 3 turns of conversation, ensuring contextual coherence.
-   **Customizable Personality:** Utilizes a strong system prompt to give the chatbot a unique "witty pirate" persona.
-   **Robust CLI:** A user-friendly command-line interface that accepts continuous input and handles exits gracefully.

## Design Decisions

I made several key design decisions to ensure the project was robust and modern:

1.  **Model Selection:** I chose `TinyLlama-1.1B-Chat-v1.0`, a powerful yet compact model specifically fine-tuned for chat. This provides high-quality conversational ability on local hardware.

2.  **`text-generation` Pipeline with Chat Template:** Instead of using the older `conversational` pipeline, I opted for the more stable and flexible `text-generation` pipeline combined with the model's built-in chat template (`apply_chat_template`). This approach is the current best practice, offers greater control over the prompt, and avoids the versioning issues common with the `Conversation` object.

3.  **System Prompt for Behavior Control:** I implemented a strong system prompt to strictly define the bot's persona and rules. This is a core "prompt engineering" technique that prevents the model from generating undesirable or out-of-character responses.

4.  **Local Model Loading:** The setup process requires downloading the model files first and then pointing the script to the local path. I chose this design to make the application's runtime independent of network connectivity and to prevent download timeouts on startup.

## Setup & Installation

Please follow these steps to run the chatbot on your local machine.

### 1. Prerequisite: Download the Model

This project requires the model files to be downloaded beforehand. Please run the following command in your terminal. This will download the model (approx. 2.2 GB) into a folder in your current directory.

```bash
pip install -U huggingface-hub
huggingface-cli download TinyLlama/TinyLlama-1.1B-Chat-v1.0 --local-dir TinyLlama-1.1B-Chat-v1.0 --local-dir-use-symlinks False