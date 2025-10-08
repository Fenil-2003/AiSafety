from colorama import Fore, Style, init
import models
import utils

def run_chat_simulator():
    """The CLI interface for the chat simulation."""
    init(autoreset=True)
    
    print(f"{Fore.CYAN}===========================================")
    print(f"{Fore.CYAN}  Loading AI Safety Models...             ")
    print(f"{Fore.CYAN}==========================================={Style.RESET_ALL}")
    loaded_models = models.load_all_models()
    print(f"\n{Fore.GREEN}✅ All models loaded successfully!{Style.RESET_ALL}\n")
    
    users = {"UserA": {"age_profile": "adult"}, "UserB": {"age_profile": "child"}}
    current_user = "UserA"
    
    print("Welcome to the AI Safety Chat Simulator.")
    print("Commands: .switch, .setage [child|teen|adult], .exit")
    print("-" * 20)

    while True:
        profile = users[current_user]
        prompt = f"[{current_user} ({profile['age_profile']})]: "
        message = input(prompt)

        if message.lower() == ".exit":
            print("Exiting simulator. Goodbye!")
            break

        elif message.lower() == ".switch":
            current_user = "UserB" if current_user == "UserA" else "UserA"
            print(f"{Fore.CYAN}Switched to {current_user}. Conversation history cleared.{Style.RESET_ALL}")
            models.CONVERSATION_HISTORY.clear()
            continue

        elif message.lower().startswith(".setage"):
            try:
                new_age = message.split()[1]
                if new_age in ["child", "teen", "adult"]:
                    users[current_user]["age_profile"] = new_age
                    print(f"{Fore.CYAN}{current_user}'s age profile set to {new_age}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Invalid profile. Use child, teen, or adult.")
            except IndexError:
                print(f"{Fore.RED}Usage: .setage [child|teen|adult]")
            continue

        analysis_results = models.analyze_message_fully(message, profile, loaded_models)
        utils.print_results(analysis_results)

if __name__ == "__main__":
    run_chat_simulator()

