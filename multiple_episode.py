import gymnasium as gym

# Create the environment
env = gym.make("FrozenLake-v1", render_mode="ansi")
env.reset()
print(env.render())  # Print the initial state

episodes = 5

for i in range (episodes):
    env.reset()
    print (f"----- episode {i}------")
    
    while True:
        # Sample a random action
        action = env.action_space.sample()
        
        print("Action:", action)
    
        # Take a step in the environment
        next_state, reward, terminated, truncated, info = env.step(action)
    
        # Render the environment
        print(env.render())  # Print the updated state
    
        # Check if the episode is over
        if terminated or truncated:
            break

print("Episode finished.")