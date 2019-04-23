from gym.envs.registration import register

register(
    id='LunarOrbiter-v0',
    entry_point='gym_lunar_orbiter.envs:LunarOrbiter',
    max_episode_steps=1000,
    reward_threshold=200,
)

