import sys
from grok_client import GrokClient

def main():
    print("Welcome to the Grok Multimodal Roleplay Agent!")
    print("----------------------------------------------")
    
    # Initialize client
    # Set mock_mode=True explicitly if you don't have a key yet
    client = GrokClient(mock_mode=False) 
    
    if client.mock_mode:
        print("[INFO] Running in MOCK MODE. No real API calls will be made.")
    
    scenario = input("\nEnter a roleplay scenario (e.g., 'A cyberpunk detective in Neo-Tokyo'): ")
    
    messages = [
        {"role": "system", "content": f"You are a roleplay partner. The scenario is: {scenario}. Be descriptive and engaging."},
        {"role": "user", "content": "Let's start the roleplay. Set the scene."}
    ]

    print("\n[Grok is thinking...]")
    response = client.chat_completion(messages)
    print(f"\nGrok: {response}")
    messages.append({"role": "assistant", "content": response})

    # Initial Scene Generation
    print("\n[System] Would you like to generate a visual for this scene? (y/n)")
    if input("> ").lower().startswith('y'):
        image_url = client.generate_image(f"Scene description: {scenario}")
        print(f"Generated Image: {image_url}")

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['quit', 'exit']:
                break
            
            messages.append({"role": "user", "content": user_input})
            
            print("\n[Grok is thinking...]")
            response = client.chat_completion(messages)
            print(f"\nGrok: {response}")
            messages.append({"role": "assistant", "content": response})
            
            # Check for special actions
            if "look" in user_input.lower() or "show me" in user_input.lower():
                print("\n[System] It seems you want to see something. Generate an image? (y/n)")
                if input("> ").lower().startswith('y'):
                    # In a real app, we'd ask Grok to summarize the scene for the prompt
                    prompt = f"Visual representation of: {user_input} in the context of {scenario}"
                    image_url = client.generate_image(prompt)
                    print(f"Generated Image: {image_url}")
            
            if "move" in user_input.lower() or "run" in user_input.lower() or "dance" in user_input.lower():
                 print("\n[System] Action detected. Generate a short video clip? (y/n)")
                 if input("> ").lower().startswith('y'):
                     prompt = f"Video of action: {user_input} in the context of {scenario}"
                     video_url = client.generate_video(prompt)
                     print(f"Generated Video: {video_url}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
