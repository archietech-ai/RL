# My RL Notes

### MDP and Terminologies
- We use MDP to model states in RL problems
- MP (Markov Process) --> when the nex step only depends on the last state only
- MRP (We add reward to MP)
  When we introduce reward to the MP, a new concept called Gain which is based on return values appears. We will use it later:
  
  ![image](https://github.com/user-attachments/assets/021e4ed6-6ef7-4b73-b249-bee310390b71)

- MDP --> Now we an action for decision (D) to MRP
- Transition Matrix is a matrix that its values show the probability of transition from one state to another
- In MDP the transition matrix is a bit more complex as it will be a 3D matrix. It shows the dynamic of the environment.
  p(s'|s,a)--> represents the probability of transitioning to state ( s' ) given that action ( a ) was taken in state ( s ).
- Why do we need action in the above probability? The reason is we do not always get the same result when we move to a specific direction when we are in a specific state. See the next item.
- Environment types: 1) Deterministic Environment--> means when we do specific action we go to a specific place. So in this case p(s'|s,a)=1  2)Stochastic Environment--> Where the same action in the same state brings a probability distribution. For example if we are in state s and do action a, then p(s'|s,a) = 0.7 and p(s''|s,a)= 0.3. The sum of all probabilities of all states and actions is equal to 1.
- In MDP, we do actions, while in MP we just observe (no action). That's the reason MP alone is not good enough and we need to add action and reward to it to make it more useful to simulate RL environment.
- State space: all the states in the environment
- Action space: all the actions that an agent can do in an environment
- Action space can be Discrete or Continuous
- Policy: is about the behaviour of an agent being in an state. A policy is a strategy used by an agent to decide which actions to take in a given state. It can be defined as a mapping from states of the environment to actions to be taken when in those states.
- A policy can be "deterministic", where a specific action is chosen for each state, or "stochastic", where actions are chosen according to a probability distribution. The probablity distribution is over action space.
- In RL, we want to find the optimal policy. Optimal policy is not about being deterministic or stochastic
- Having a stochastic policy is very important in RL as that is the way the agent learns the best action. Do not forget that at the beginning the agent does not know which action is the best to take in a state, so having a way to let an agent to see all possible actions (by introducing an element of randomness) is the best way to try before an agent selects the best action being in a state
- Episode (Trajectory) --> Means one round of going from start to the end. We usually run many many episode to see all cases to find the best policy
- Task types from episode viewpoint: we can have Episodic tasks (meaning we have a terminal state) or continuous (no terminal state, like robots at home)
- In an episode, we pass through many states and we get rewards (return) by going through those states. In each state we get a reward. So to find the optimial policy we want to maximize the sum of those rewards in an episode
- The discount factor (between 0 and 1) allows us to not get infinite return. If we use smaller discount factor, we care more about immidiate rewards. When we use larger discount factors, we include more future rewards in the total return. When discount factor is 0, then that means we just care about next first reward and nothing else.
- Why do we care about future rewards?  Becuase in many cases, you care about final results not the intermidiate and more immidiate rewards
  ![image](https://github.com/user-attachments/assets/4df6b941-2a02-4bae-bc8c-90eb1f7e2fc0)

------------------------------

### v(s)   value function or state value function
- value function or state value function
- It is a function that show the value of being in a state. It's like a credit of that state. Do not forget that we do not always use the same episode, so if you are in a state and take episod 1 to get to the destination, you may get +40 but next time that you use the same state as start point and go to end state you may get +10. Why? becuase you face a sochastic policy. We have an stochastic environment. Nothing is deterministic
- So we calculate the value by Expected value (mean). We calcualte the expected values we get if we start from state S and try it by many episodes 
  
  ![image](https://github.com/user-attachments/assets/08abdf8c-8333-4ab5-93a7-d526f16cef76)

  - If the state space is small we can show a state values in a table
  - So the "best" value of being in a state is defined as v*:

    ![image](https://github.com/user-attachments/assets/0232b0ae-d0ed-4098-bfa6-6cdea2bb77a7)

- The state value function does not care too much about the policies and actions in that policy, all it cares is the value of that state. In the next function, we change the focus on the action we perform being in that state and the value of that action.

- ---------------------------------------------
### State-action value function

- To me this sounds more important than state value function as this time we focus on the actions of being in a specific state
- Here it is important to know that when we are in state s, we may have two possible action a1 and a2. When you choose a1, we go to state s'. From here we may follow a stochastic policy to get to the destination. If we use a2, we get to s" state and use another policy from that point. So what I want to say here is, the first step (selecting a1 or a2) does not following specific policy, we just select a1 and then we get to the next state. After that we follow a policy
  
  ![image](https://github.com/user-attachments/assets/2d058819-9ea7-4ccc-b893-0f0eef24b1a6)
- We also have an optimal satte action value function:

- ![image](https://github.com/user-attachments/assets/7ed36bd5-3937-43ac-9bcc-d4352e917d49)

----------------------------------------------------

### Testing Frozen Lake code with OpenAI Gym

![image](https://github.com/user-attachments/assets/ae2cdfd0-d028-459f-9e22-216dec99184c)

Action Mapping
0: Left
1: Down
2: Right
3: Up


print (env.P[3][1])  ---> [(0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 7, 0.0, True), (0.3333333333333333, 3, 0.0, False)]

The above output is the "transition probability" information for state 3 when taking action 1 (Down):

(prob, next_state, reward, done):

prob: Probability of transitioning to next_state.

next_state: The state you transition to.

reward: Reward received after taking the action.

done: Whether the episode ends after this transition (meaning we end of one of those cells that is terminal state).

![image](https://github.com/user-attachments/assets/6f03d163-afad-47be-923c-11fdced569ba)


Now that we have transition probability matrix we should introduce actions to generate episodes. To generate episode we need to perform a "step":

env.step(2) --> Meaning at the current state, do action 2, meaning go to right. It may not go to right neccessary as we are running in a stochastic env.

The output of env.step(2) is a tuple with 4 components: (where you landed i.e. next state, 

                                                          what reward you get, 
                                                          
                                                          do you land in a terminal state, 
                                                          
                                                          some debugging info)


![image](https://github.com/user-attachments/assets/8ea08396-1f77-4d26-b147-fb2d1137315f)

![image](https://github.com/user-attachments/assets/bca585ce-de9a-4b81-b4ce-8747c640791e)


In gymnasium's step() method returns five values:

next_state: The next state.

reward: The reward obtained from the action.

terminated: A boolean indicating if the episode has ended normally.

truncated: A boolean indicating if the episode was truncated (e.g., time limit).

info: Additional metadata


Now rather than we click on thr run bottom to do an action, we can write a loop and say do action until reaching a terminal state:

![image](https://github.com/user-attachments/assets/7abbde6d-7039-429b-b704-eab2b40aece7)


And here are output samples:

![image](https://github.com/user-attachments/assets/292a0f2a-d42d-4e9a-ac6c-71977560f724)

![image](https://github.com/user-attachments/assets/ccfe3418-31ec-4f7c-855e-febf51e3ee07)

![image](https://github.com/user-attachments/assets/516f4a84-5fba-41b1-bb6e-45c7bfd70cf6)






