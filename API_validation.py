import requests
import json
from typing import Dict, Optional

def validate_api_key(api_key: str, api_type: str) -> bool:
    """
    Validate API key for different AI services
    Returns True if the API key is valid, False otherwise
    """
    endpoints = {
        "chatgpt": {
            "url": "https://api.openai.com/v1/chat/completions",
            "headers": {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            "data": {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": "Hello"}],
                "max_tokens": 5
            }
        },
        "gemini": {
            "url": f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}",
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "contents": [{"parts":[{"text": "Hello"}]}]
            }
        }
    }

    if api_type not in endpoints:
        print(f"Error: {api_type} is not supported")
        return False

    try:
        endpoint = endpoints[api_type]
        response = requests.post(
            endpoint["url"],
            headers=endpoint["headers"],
            json=endpoint["data"],
            timeout=10
        )
        return response.status_code == 200
    except Exception as e:
        print(f"Error validating {api_type} API key: {str(e)}")
        return False

def get_ai_response(api_key: str, api_type: str, prompt: str) -> Optional[Dict]:
    """
    Get response from the selected AI service
    Returns the response data if successful, None otherwise
    """
    if not validate_api_key(api_key, api_type):
        print(f"Invalid {api_type} API key")
        return None

    try:
        if api_type == "chatgpt":
            return get_chatgpt_response(api_key, prompt)
        elif api_type == "gemini":
            return get_gemini_response(api_key, prompt)
        else:
            print(f"Unsupported API type: {api_type}")
            return None
    except Exception as e:
        print(f"Error getting response from {api_type}: {str(e)}")
        return None

def get_chatgpt_response(api_key: str, prompt: str) -> Dict:
    """Get response from ChatGPT API"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4",  # or gpt-3.5-turbo based on subscription
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()

def get_gemini_response(api_key: str, prompt: str) -> Dict:
    """Get response from Google's Gemini API"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts":[{"text": prompt}]}]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()

def main():
    # Get API type and key from user
    print("Select AI Service:")
    print("1. ChatGPT")
    print("2. Gemini")
    choice = input("Enter your choice (1 or 2): ")
    
    api_type = "chatgpt" if choice == "1" else "gemini"
    api_key = input(f"Enter your {api_type.upper()} API key: ")
    prompt = input("Enter your prompt: ")

    # Get and display the response
    response = get_ai_response(api_key, api_type, prompt)
    
    if response:
        print("\n--- Full Response ---")
        print(json.dumps(response, indent=4))
        
        print("\n--- Main Response ---")
        if api_type == "chatgpt":
            print(response["choices"][0]["message"]["content"])
            print("\n--- Usage Details ---")
            print(f"Model used: {response.get('model', 'Not available')}")
            print(f"Tokens used:")
            print(f"  Input: {response['usage'].get('prompt_tokens', 0)}")
            print(f"  Output: {response['usage'].get('completion_tokens', 0)}")
            print(f"  Total: {response['usage'].get('total_tokens', 0)}")
        elif api_type == "gemini":
            try:
                print(response["candidates"][0]["content"]["parts"][0]["text"])
            except KeyError:
                print("Could not parse Gemini response")

if __name__ == "__main__":
    main()