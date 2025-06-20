# interface.py
from model_loader import load_text_generation_pipeline
from chat_manager import ChatManager

def main():
    model_path = "C:/Chatbot/TinyLlama-1.1B-Chat-v1.0"
    
    pipeline = load_text_generation_pipeline(model_path)
    chatbot = ChatManager(pipeline)

    print("\n--- Captain Code is on Deck! ---")
    print("Speak with the pirate bot. Type '/exit' to make him walk the plank.")
    print("-" * 60)

    while True:
        try:
            user_input = input("You(Ankit): ")
            if user_input.lower() == "/exit":
                print("Captain Code: Arr, farewell!")
                break
            bot_response = chatbot.generate_reply(user_input)
            print(f"Captain Code: {bot_response}")
        except KeyboardInterrupt:
            print("\nCaptain Code: Off to the plank ye go! Goodbye!")
            break

if __name__ == "__main__":
    main()