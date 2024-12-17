# Python_web_automation
This repository contains an automated Trello Bot implemented in Python using Selenium. The script logs into your Trello account, navigates to a specific board, creates a task card in a list, and captures a screenshot for confirmation. This is useful for automating repetitive tasks and verifying board states.
# Trello Bot Automation

## Description
This project provides a Python script that automates Trello board interactions using the Selenium WebDriver. The script:
1. Logs into Trello using user credentials.
2. Navigates to a specified board.
3. Adds a card with predefined text to a list.
4. Captures a screenshot of the board for confirmation.

---

## Features
- **Login Automation**: Automatically logs into Trello with credentials from a `config.json` file.
- **Task Management**: Adds a card to the desired board list.
- **Screenshot**: Captures and saves a screenshot of the board.

---

## Requirements

Before running the script, ensure you have the following:
1. Python 3.x installed.
2. Microsoft Edge browser installed.
3. Edge WebDriver (`msedgedriver.exe`) matching your browser version.
4. Selenium installed (`pip install selenium`).

---

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/trello-bot-automation.git
   cd trello-bot-automation
