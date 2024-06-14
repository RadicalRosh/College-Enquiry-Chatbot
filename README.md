# COLLEGE ENQUIRY BOT

## Abstract

COLLEGE ENQUIRY BOT is an AI-powered virtual assistant designed to assist with queries related to St. John's College of Engineering. This bot provides information about various college branches, courses, achievements, contact details, admission processes, and more. It aims to deliver accurate and relevant information to aid prospective students and other stakeholders in making informed decisions about their educational journey.

## Installation

To set up and run the COLLEGE ENQUIRY BOT, follow these steps:

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)
- A virtual environment setup tool (optional but recommended)

### Step 1: Install Rasa

1. **Create and activate a virtual environment (optional but recommended):**

   ```bash
     python -m venv rasa_env
     source rasa_env/bin/activate   # For Windows: rasa_env\Scripts\activate
   ```
2. **Install Rasa:**
    pip install rasa

### Step 2: Set Up the Project
1. **Clone the GitHub repository:**
```
     git clone https://github.com/yourusername/college-enquiry-bot.git
     cd college-enquiry-bot
```
2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

### Step 3: Train the Model
1. **Train the Rasa model:**
   rasa train

### Step 4: Run the Bot
1. **Run the Rasa server:**
   ```
   rasa run actions
   rasa run
   ```
   Note: Do that in seperate terminals.
   
2.**Run the bot in interactive mode (optional, for testing and debugging):**
   ```
   rasa shell
   ```

## Usage
Once the bot is up and running, it can handle various queries related to the college. You can test it using the interactive mode or integrate it with a frontend interface to provide a seamless user experience.

## Copy Your Files
To use the COLLEGE ENQUIRY BOT with your setup, copy the contents of this repository to the folder where you installed Rasa. You can do this by running:
```bash
cp -r /path/to/your/github/repo/* /path/to/your/rasa/project/folder/
```
Replace /path/to/your/github/repo/ with the actual path to the cloned repository and /path/to/your/rasa/project/folder/ with the path to your Rasa project directory.

## Contributing
Feel free to contribute to this project by creating pull requests, reporting issues, or suggesting improvements. Your contributions are highly appreciated!



