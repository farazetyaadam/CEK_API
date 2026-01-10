name: Check Gemini API Models

on:
  push:
    branches: [ main ]
  workflow_dispatch: # Memungkinkan dijalankan manual dari HP/Browser

jobs:
  check-models:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          
      - name: Run API Check
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: python check_api.py
