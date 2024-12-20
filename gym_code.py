#import gym
import gymnasium as gym
#import matplotlib.pyplot as plt

# Create the FrozenLake environment with rgb_array rendering
#env = gym.make("FrozenLake-v1", render_mode="rgb_array")
env = gym.make("FrozenLake-v1", render_mode="ansi")
env.reset()
env.step(2)
# Render the frame as an array
frame = env.render()

# Display the frame using matplotlib
# plt.imshow(frame)
# plt.axis("off")
# plt.show()
print(frame)
#print(env.observation_space)
#print (env.action_space)
#print (env.P)
#print (env.P[3][1])