name: Pull Request Checks

on:
  pull_request:
    branches:
      - main  # or the branch you want to target

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Node.js (example for JS projects)
      uses: actions/setup-node@v4
      with:
        node-version: '18'

    - name: Install dependencies
      run: npm install

    - name: Run Lint
      run: npm run lint

    - name: Run Tests
      run: npm test
