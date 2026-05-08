#!/usr/bin/env python3
"""
Cyclone Assistant - ChatGPT-like AI Chatbot
Interactive command-line interface for conversing with OpenAI's GPT models.
"""

from chatbot import Chatbot
import sys


def print_banner():
    """Print welcome banner."""
    print("\n" + "="*60)
    print("🌪️  CYCLONE ASSISTANT - AI CHATBOT")
    print("="*60)
    print("Powered by OpenAI GPT")
    print("Type 'help' for commands or 'exit' to quit\n")


def print_help():
    """Print available commands."""
    print("\n" + "-"*60)
    print("AVAILABLE COMMANDS:")
    print("-"*60)
    print("  help        - Show this help message")
    print("  clear       - Clear conversation history")
    print("  stats       - Show token usage statistics")
    print("  reset       - Reset the chatbot")
    print("  exit/quit   - Exit the chatbot")
    print("-"*60 + "\n")


def format_stats(stats):
    """Format token usage statistics."""
    return f"""
Token Usage:
  • Prompt tokens: {stats['prompt_tokens']}
  • Completion tokens: {stats['completion_tokens']}
  • Total tokens: {stats['total_tokens']}
"""


def main():
    """Main chatbot loop."""
    print_banner()
    chatbot = Chatbot()
    
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['exit', 'quit']:
                print("\n🌪️  Thank you for using Cyclone Assistant! Goodbye! 👋\n")
                sys.exit(0)
            
            elif user_input.lower() == 'help':
                print_help()
            
            elif user_input.lower() == 'clear':
                chatbot.clear_history()
                print("✅ Conversation history cleared!")
            
            elif user_input.lower() == 'stats':
                stats = chatbot.get_stats()
                print(format_stats(stats))
            
            elif user_input.lower() == 'reset':
                chatbot = Chatbot()
                print("✅ Chatbot reset!")
            
            else:
                # Get AI response
                print("\n🤖 Assistant: ", end="")
                chatbot.get_response(user_input)
        
        except KeyboardInterrupt:
            print("\n\n🌪️  Chatbot interrupted. Goodbye! 👋\n")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()
