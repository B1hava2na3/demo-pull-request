name: Run Python on Windows
on:
  pull:
    branches:
      - '**'  # Trigger on push to any branch
jobs:
  run-python-script:
    runs-on: windows-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'  # You can change the version if needed

      - name: Run Python Script
        run: python hello.py
