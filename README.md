# Grok Multimodal Roleplay Agent

This project demonstrates how to build a multimodal AI agent using xAI's Grok API. The agent can engage in roleplay conversations, generate scene images, and create short video clips based on the narrative.

## Features
- **Text Roleplay**: Powered by Grok's LLM capabilities.
- **Image Generation**: Visualizes scenes using Grok's image models.
- **Video Generation**: Creates short clips for actions using Grok's video capabilities.
- **Mock Mode**: Run the application without API keys to see the flow.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **API Keys**:
    - Create a `.env` file in the root directory.
    - Add your xAI API key:
      ```
      XAI_API_KEY=your_api_key_here
      ```

3.  **Run the Agent**:
    ```bash
    python main.py
    ```
    If no API key is found, it will automatically default to **Mock Mode**.

## Usage
- Start the application.
- Enter a roleplay scenario (e.g., "A sci-fi explorer on Mars").
- Chat with the agent.
- Type keywords like "look" or "show me" to trigger image generation prompts.
- Type keywords like "run", "move", or "dance" to trigger video generation prompts.

## Web Application
To run the modern web interface:
1.  **Start the Server**:
    ```bash
    uvicorn server:app --reload
    ```
2.  **Open Browser**:
    Navigate to `http://127.0.0.1:8000` to use the multimodal agent interface.
