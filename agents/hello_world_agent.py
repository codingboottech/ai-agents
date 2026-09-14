"""
Hello World Agent
A simple AI agent that greets the user and responds to basic queries.
"""

class HelloWorldAgent:
    """A simple agent that says hello and responds to basic queries."""
    
    def __init__(self, name: str = "HelloWorldAgent"):
        """
        Initialize the Hello World Agent.
        
        Args:
            name: The name of the agent
        """
        self.name = name
        self.greeting_message = "Hello, World! 👋"
    
    def greet(self) -> str:
        """
        Return a greeting message.
        
        Returns:
            A greeting string
        """
        return self.greeting_message
    
    def respond(self, user_input: str) -> str:
        """
        Respond to user input.
        
        Args:
            user_input: The user's message
            
        Returns:
            A response string
        """
        user_input_lower = user_input.lower().strip()
        
        if "hello" in user_input_lower or "hi" in user_input_lower:
            return f"{self.greeting_message} Nice to meet you!"
        elif "name" in user_input_lower:
            return f"My name is {self.name}"
        elif "help" in user_input_lower:
            return "I'm a simple Hello World Agent. Try asking me 'hello', 'hi', 'what's your name', or 'help'!"
        else:
            return "I'm a simple agent. Try saying hello! 😊"
    
    def run(self):
        """Run the agent in interactive mode."""
        print(self.greet())
        print("\nType 'quit' to exit\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ["quit", "exit"]:
                print(f"{self.name}: Goodbye! 👋")
                break
            
            if not user_input:
                continue
            
            response = self.respond(user_input)
            print(f"{self.name}: {response}\n")


if __name__ == "__main__":
    agent = HelloWorldAgent()
    agent.run()
