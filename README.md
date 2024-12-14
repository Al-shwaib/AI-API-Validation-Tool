# AI API Validation Tool

## Project Description
A versatile program that validates and interacts with multiple AI APIs including OpenAI's ChatGPT and Google's Gemini. It allows users to send prompts and receive responses from their chosen AI model, with detailed insights into the interaction.

---

## Features
1. **Multiple AI API Support**:
   - ChatGPT (OpenAI) API integration
   - Gemini (Google) API integration
   - Extensible structure for adding more AI services

2. **API Key Validation**:
   - Validates API keys before making actual requests
   - Provides immediate feedback on API key validity
   - Secure handling of API keys (runtime input only)

3. **Model Selection**:
   - For ChatGPT: Supports both GPT-4 and GPT-3.5 models
   - For Gemini: Uses the latest Gemini Pro model

4. **Robust Error Handling**:
   - Comprehensive error checking for API responses
   - Clear error messages for troubleshooting
   - Timeout protection for API requests

5. **Response Analysis**:
   - Formatted JSON response display
   - Model-specific response parsing
   - Usage statistics (for supported APIs)

6. **User-Friendly Interface**:
   - Simple menu for AI service selection
   - Clear prompts for user input
   - Organized output display

7. **Code Structure**:
   - Modular design with separate functions for each API
   - Type hints for better code clarity
   - Comprehensive error handling
   - Clean and maintainable codebase

---

## Requirements
- Python 3.6 or higher
- `requests` library
- API keys for the services you want to use:
  - OpenAI API key for ChatGPT
  - Google API key for Gemini

---

## Setup and Running Instructions
1. Install the required library:
```bash
pip install requests
```

2. Run the program:
```bash
python API_validation.py
```

3. Follow the prompts:
   - Choose your AI service (ChatGPT or Gemini)
   - Enter your API key when prompted
   - Type your prompt/question
   - View the response and any additional information

---

## Response Format
### ChatGPT
- Full JSON response
- Main response text
- Usage details (tokens used)
- Model information

### Gemini
- Full JSON response
- Main response text
- Additional response details when available

---

## Error Handling
The program handles various error cases:
- Invalid API keys
- Network connection issues
- API timeout errors
- Invalid response formats
- Service-specific errors

---

## Security Notes
- API keys are never stored in the code
- Keys are requested at runtime
- All API requests use secure HTTPS
- Timeout limits prevent hanging requests