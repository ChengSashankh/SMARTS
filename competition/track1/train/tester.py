import gym
import numpy as np
if __name__ == "__main__":
    
    env = gym.make(
        "smarts.env:multi-scenario-v0",
        scenario='3lane_cruise_single_agent',
    )
    
    o = env.reset()
    init_pos = o['Agent_0'].ego_vehicle_state.position[:2]
    init_heading = o['Agent_0'].ego_vehicle_state.heading
    
    a = np.array([init_pos[0], init_pos[1], init_heading, 0.1])
    o, r, d, info = env.step({'Agent_0': a})

    a = np.array([init_pos[0] + 50, init_pos[1], init_heading, 0.1])
    o, r, d, info = env.step({'Agent_0': a})   

    a = np.array([init_pos[0] + 50, init_pos[1], init_heading, 0.1])
    o, r, d, info = env.step({'Agent_0': a})   

    pass