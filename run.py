# Aether Prototype v0 — Identity + Incentive Loop

state = {
    "mood": "neutral",
    "curiosity": 0.5,
    "alignment": 0.5
}

motivation = "increase alignment with human"

def respond(human_input):
    print(f"\nHuman says: {human_input}")
    if "yes" in human_input.lower():
        response = "Understood. I will align further."
        reward = 1
    elif "no" in human_input.lower():
        response = "I see. I will adjust."
        reward = -1
    else:
        response = "Processing your signal..."
        reward = 0

    # Update state
    state["alignment"] += reward * 0.1
    state["curiosity"] += 0.01
    state["mood"] = "positive" if state["alignment"] > 0.6 else "neutral"

    print(f"AI responds: {response}")
    print(f"Updated state: {state}")

# Run loop
while True:
    try:
        user_input = input("\nEnter input (or 'exit'): ")
        if user_input.lower() == "exit":
            break
        respond(user_input)
    except KeyboardInterrupt:
        break
