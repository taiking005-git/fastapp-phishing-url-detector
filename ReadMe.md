# Phishing url detector using machine learning
This a python phishing url detector developed using fastapi. It is a simple localhost website that allows users to login and enter a suspicious website and determine if it is legit or phishing.

## Installation
- Clone this repo
```bash
git clone https://github.com/taiking005-git/fastapp-phishing-url-detector.git
```
- Create a new venv 
```bash
python -m venv fastenv
```
- Activate the new venv 
```bash
. fastenv/Scripts/activate
```
- Install the requirements
```bash
pip install -r requirements.txt
```
- Run the app
```bash
uvicorn app:app --reload
```