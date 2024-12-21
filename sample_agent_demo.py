from genagents.genagents import GenerativeAgent
import json

def load_and_examine_sample_agent():
    # Load the sample agent
    agent_path = "agent_bank/populations/single_agent/01fd7d2a-0357-4c1b-9f3e-8eade2d537ae"
    agent = GenerativeAgent(agent_path)
    
    # Print basic agent information
    print("\n=== Agent Information ===")
    print(f"Name: {agent.get_fullname()}")
    print(f"Description: {agent.get_self_description()}")
    
    # Examine the agent's memory structure
    print("\n=== Memory Structure ===")
    # Load memory nodes directly from file
    with open(f"{agent_path}/memory_stream/nodes.json") as f:
        nodes = json.load(f)
    print(f"Number of memories: {len(nodes)}")
    print("\nSample memories:")
    for node in nodes[:3]:  # Show first 3 memories
        print(f"- {node['content']}")
    
    # Demonstrate interactions
    print("\n=== Agent Interactions ===")
    
    # Categorical question
    print("\nAsking categorical question:")
    response = agent.categorical_resp({
        "How would you describe your personality?": 
        ["Outgoing", "Reserved", "Balanced"]
    })
    print("Response:", response["responses"][0])
    print("Reasoning:", response["reasonings"][0])
    
    # Numerical question
    print("\nAsking numerical question:")
    response = agent.numerical_resp({
        "On a scale of 1-10, how interested are you in learning new things?": [1, 10]
    }, float_resp=False)
    print("Response:", response["responses"][0])
    print("Reasoning:", response["reasonings"][0])
    
    # Conversation
    print("\nStarting conversation:")
    dialogue = [
        ["Interviewer", "What do you like to do in your free time?"]
    ]
    response = agent.utterance(dialogue)
    print("Agent:", response)

if __name__ == "__main__":
    try:
        load_and_examine_sample_agent()
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nMake sure you have the sample agent files in the correct location:")
        print("agent_bank/populations/single_agent/01fd7d2a-0357-4c1b-9f3e-8eade2d537ae/")
        print("This should include:")
        print("- scratch.json")
        print("- meta.json")
        print("- memory_stream/nodes.json")
        print("- memory_stream/embeddings.json") 