# Sales Agent

![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54&style=for-the-badge) ![Code Style](https://img.shields.io/badge/code%20style-pep8-orange) [![Linting and Unit Tests](https://github.com/Nomia-Limited/sales-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/Nomia-Limited/sales-agent/actions/workflows/ci.yml)

| Folder | Description |
|--------|-------------|
|.github/workflows|CI pipeline|
|config|Configuration settings such as connection strings and file paths|
|docs|Project documentation in markdown format|
|notebooks|Jupyter notebooks|
|utils|Provides helper functions and utilities that support the main scripts|

# Installation Guide

## Quick Start

1. **Install core dependencies:**
   ```bash
   uv sync --no-dev --no-default-groups
   ```

2. **Install development dependencies (optional):**
   ```bash
   uv sync --extra dev
   ```

3. **Install notebook dependencies (optional):**
   ```bash
   uv sync --extra notebook
   ```

## OpenAI Agents SDK Installation

The `agents` package (OpenAI Agents SDK) has TensorFlow as a dependency, which can cause installation issues on macOS 15.0+ due to platform compatibility.

### Option 1: Manual Installation (Recommended)
```bash
uv pip install agents --python-platform macos
```

### Option 2: Install with Extra
```bash
uv sync --extra agents
```
*Note: This may fail on macOS 15.0+ due to TensorFlow platform compatibility.*

### Option 3: Alternative Installation Methods
If the above methods don't work, you can try:

1. **Using conda/mamba:**
   ```bash
   conda install -c conda-forge agents
   ```

2. **Using pip directly:**
   ```bash
   pip install agents
   ```

3. **Building from source:**
   ```bash
   git clone https://github.com/openai/agents-python.git
   cd agents-python
   pip install -e .
   ```

## Troubleshooting

### TensorFlow Platform Compatibility Error
If you encounter the error:
```
Distribution `tensorflow==2.19.0` can't be installed because it doesn't have a source distribution or wheel for the current platform
```

This is a known issue with TensorFlow on macOS 15.0+. The workaround is to use the `--python-platform macos` flag when installing the agents package.

### SSL Certificate Issues
If you encounter SSL certificate errors with SendGrid:
```bash
uv pip install --upgrade certifi
```

Then add this to your Python code:
```python
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()
```

## Environment Setup

1. **Create a `.env` file** with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SENDGRID_API_KEY=your_sendgrid_api_key_here
   ```

2. **Verify SendGrid setup:**
   - Create a SendGrid account at https://sendgrid.com/
   - Generate an API key
   - Verify your sender email address

## Running the Labs

1. **Lab 1:** Basic OpenAI Agents SDK usage
   ```bash
   python 1_lab1.py
   ```

2. **Lab 2:** Sales agent with email functionality
   ```bash
   python 2_lab2.py
   ```

3. **Lab 3:** Advanced features and guardrails
   ```bash
   python 3_lab3.py
   ```

## Dependencies

### Core Dependencies
- `python-dotenv`: Environment variable management
- `openai`: OpenAI API client
- `sendgrid`: Email functionality
- `pydantic`: Data validation
- `certifi`: SSL certificate handling

### Optional Dependencies
- `dev`: Development tools (pytest, black, isort, flake8, mypy)
- `notebook`: Jupyter and data science tools
- `agents`: OpenAI Agents SDK (may require manual installation) 
