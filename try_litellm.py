import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def main():
    gemini_api_key = os.getenv("Gemini_Api_Key")
    # anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    if not gemini_api_key:
        print("Error: Gemini_Api_Key not found!")
        return
    
    # if not anthropic_api_key:
    #     print("Error: ANTHROPIC_API_KEY not found!")
    #     return


    user_input = input("Enter your message: ")
    response = completion(
       model = "gemini/gemini-2.0-flash",
        api_key=gemini_api_key,
        messages=[
            {
                "role": "user",
                "content":   user_input 
            }
        ],
        max_tokens=100,
        temperature=0.7,
    )

    print("LiteLLM Response:")
    print("=" * 40)
    print(response.choices[0].message.content)
    print("=" * 40)
    print(f"Model used: {response.model}")
    if hasattr(response, "usage") and response.usage:
        print(f"Tokens used: {response.usage.total_tokens}")

if __name__ == "__main__":
    main()
