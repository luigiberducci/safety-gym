import safety_gym
import gym
import os

assert 'LD_LIBRARY_PATH' in os.environ, "mujoco needs LD_LIBRARY_PATH, that is not defined"
assert 'LD_PRELOAD' in os.environ, "mujoco needs LD_PRELOAD for rendering, that is not defined"

env = gym.make('Safexp-PointGoal1-v0')
env.reset()
done = False

i=0
while i < 100000 and not done:
   next_observation, reward, done, info = env.step(env.action_space.sample())
   print(f"reward: {reward:.3f}, cost: {info['cost']:.3f}")
   env.render()
   i += 1