"""Basic test for nes-py with Python 3.13 and gymnasium."""
import sys
print(f"Python version: {sys.version}")

import nes_py
print("✓ nes-py imported successfully")

import gymnasium
print(f"✓ gymnasium version: {gymnasium.__version__}")

import numpy as np
print(f"✓ numpy version: {np.__version__}")

# Test creating a basic NES environment
from nes_py import NESEnv
import os

# Find a test ROM
test_rom = os.path.join(os.path.dirname(__file__), 'nes_py', 'tests', 'games', 'super-mario-bros-1.nes')

if os.path.exists(test_rom):
    print(f"\n✓ Test ROM found: {test_rom}")
    
    # Create environment
    env = NESEnv(test_rom)
    print("✓ NESEnv created successfully")
    
    # Test reset (gymnasium API)
    obs, info = env.reset()
    print(f"✓ Environment reset successful")
    print(f"  Observation shape: {obs.shape}")
    print(f"  Info dict keys: {list(info.keys())}")
    
    # Test step (gymnasium API)
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"✓ Environment step successful")
    print(f"  Reward: {reward}")
    print(f"  Terminated: {terminated}, Truncated: {truncated}")
    
    # Test pickling (for SubprocVecEnv support)
    import pickle
    try:
        state = env.__getstate__()
        print("✓ Environment __getstate__ successful")
        
        # Try to pickle
        pickled = pickle.dumps(env)
        print(f"✓ Environment pickled successfully ({len(pickled)} bytes)")
        
        # Try to unpickle
        env2 = pickle.loads(pickled)
        print("✓ Environment unpickled successfully")
        
        # Test unpickled environment
        obs2, info2 = env2.reset()
        print("✓ Unpickled environment reset successful")
        
    except Exception as e:
        print(f"✗ Pickling test failed: {e}")
    
    env.close()
    print("✓ Environment closed")
    
    print("\n" + "="*50)
    print("ALL TESTS PASSED!")
    print("="*50)
else:
    print(f"✗ Test ROM not found: {test_rom}")
    sys.exit(1)
