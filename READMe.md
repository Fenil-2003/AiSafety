# AI Safety Models - Functional POC

This repository contains a Proof of Concept (POC) for a suite of AI Safety Models, written in a simple, function-based style. The entire application logic is contained within a single Python file (`main.py`).

## Features

1.  **Abuse Language Detection**: Identifies toxic and harmful content.
2.  **Escalation Pattern Recognition**: Tracks conversation sentiment to detect when a discussion is becoming negative.
3.  **Crisis Intervention**: A proxy model that detects strong negative emotions (sadness, fear) which could indicate user distress.
4.  **Content Filtering**: Filters content based on user age profiles (child, teen, adult) using keywords and topic analysis.

## Setup

1.  **Create a folder and place the files inside:**
    Create a folder named `ai_safety_poc_functional` and put `main.py` and `requirements.txt` inside it.

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    # Navigate to your folder
    cd AiSAFETY

    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install the required packages
    pip install -r requirements.txt
    ```
    *Note: The first time you run the application, it will download several hundred megabytes of model weights from Hugging Face. This is a one-time process.*

## How to Run

Execute the `main.py` script to start the interactive command-line chat simulator:

```bash
python main.py
```

### Simulator Commands

-   Type any message to have it analyzed by the AI safety system.
-   `.switch`: Toggles between `UserA` (adult) and `UserB` (child) and clears the conversation history.
-   `.setage [child|teen|adult]`: Changes the age profile for the current user.
-   `.exit`: Exits the simulator.                                                                                               