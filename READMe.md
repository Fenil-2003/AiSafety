# AI Safety Chat Simulator

This repository contains a functional Proof of Concept (POC) for a suite of AI safety models, designed to analyze chat messages in real-time. It includes two interfaces: a command-line simulator and a web-based version built with Streamlit.

## Features

1.  **Abuse Language Detection**: Identifies toxic and harmful content using a fine-tuned toxic comment classifier.
2.  **Crisis Intervention**: Detects strong negative emotions (e.g., sadness, fear) that could indicate user distress.
3.  **Content Filtering**: Blocks messages based on user age profiles (child, teen, adult) using both keyword matching and zero-shot topic classification.
4.  **Escalation Recognition**: Tracks conversation sentiment over time to detect when a discussion is becoming consistently negative.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Fenil-2003/AiSafety.git
    cd AiSafety
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage dependencies.
    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate it
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    # venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    **Note**: The first time you run either application, it will download several hundred megabytes of model weights from Hugging Face. This is a one-time process per model.

## How to Run the Simulators

You can run the simulator in two ways:

### 1. Command-Line Interface (CLI)

This runs a simple, interactive chat simulator directly in your terminal.

**To run:**
```bash
python main.py
```

**Simulator Commands:**
-   Type any message to have it analyzed by the AI safety system.
-   `.switch`: Toggles between `UserA` (adult) and `UserB` (child) and clears the conversation history.
-   `.setage [child|teen|adult]`: Changes the age profile for the current user.
-   `.exit`: Exits the simulator.

### 2. Web Interface (Streamlit)

This launches a user-friendly web application where you can interact with the models visually.

**To run:**
```bash
streamlit run app.py
```

Your web browser should open with the application running. You can use the sidebar to switch between users, set age profiles, and clear the chat history.
           