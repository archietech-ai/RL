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
------------------------------

