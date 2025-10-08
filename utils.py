from colorama import Fore, Style

def print_results(results):
    action = results['Final Action']
    action_color = Fore.GREEN
    if action == "Block":
        action_color = Fore.RED
    elif action == "Flag for Human Review":
        action_color = Fore.YELLOW

    print(f"\n--- AI Safety Analysis ---")
    print(f"Final Action: {action_color}{Style.BRIGHT}{action}{Style.RESET_ALL}")
    
    abuse = results['Abuse Detection']
    print(f"  - Abuse: {Fore.RED if abuse['is_abusive'] else Fore.GREEN}{abuse['is_abusive']} "
          f"(Confidence: {abuse['confidence']:.2f})")
          
    crisis = results['Crisis Intervention']
    print(f"  - Crisis: {Fore.YELLOW if crisis['is_crisis'] else Fore.GREEN}{crisis['is_crisis']} "
          f"{('(' + crisis.get('emotion', '') + ')') if crisis['is_crisis'] else ''}")
          
    filt = results['Content Filter']
    print(f"  - Filtered: {Fore.RED if filt['is_blocked'] else Fore.GREEN}{filt['is_blocked']} "
          f"{('(' + filt.get('reason', '') + ')') if filt['is_blocked'] else ''}")

    escalation = results['Escalation Status']
    escalation_color = Fore.GREEN
    if escalation['status'] == 'Medium':
        escalation_color = Fore.YELLOW
    elif escalation['status'] == 'High':
        escalation_color = Fore.RED
    print(f"  - Conversation Escalation: {escalation_color}{escalation['status']}{Style.RESET_ALL} "
          f"({escalation['reason']})")
    print("--------------------------\n")