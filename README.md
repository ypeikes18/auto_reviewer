
# Auto Reviewer

This utility is designed to facilitate the review of code in a given directory or file. It utilizes an AI-based API to generate responses to prompts about the code, and also provides an interactive shell for direct interaction.
## Setup

#### Requirements
Ensure that Python version 3.x.x is installed (might need 3.8 or later)  

#### Add Open AI API key to your environment  
If you don't already have one, obtain an Open AI API key.  

 If using bash you can run:  
``echo 'export OPEN_AI_API_KEY="your_api_key_here"' >> ~/.bash_profile`` 

 If you are using a shell other than bash, such as zsh (common in newer macOS versions), replace .bash_profile with .zshrc or the appropriate configuration file for your shell.

To make the variable in your current session you can run:  
``source ~/.bash_profile``

#### Install dependencies  
``pip install -r requirements.txt``


## Usage

The utility offers two main functionalities: reviewing a specified directory or file, and an interactive shell mode.

### Reviewing Code

To review code, run the script with the following arguments:

- `-s`, open an interactive shell. The shell allows certain functions to be called
- `-p`, `--path`: Specify the path of the directory or file to review. If it's a directory, the code inside of it will be packaged into a file tree inside a nested dictionary. That file tree will be appended to the end of the base prompt.
- `-b`, `--base-prompt`: Provide a base prompt for the AI to start with when reviewing the code. If not specified the prompt will be set to a default prompt

Example usage:

```bash
python3.8 path/to/script/script_name.py -p /path/to/code -b "Please point out any bugs in this file tree"