#!/usr/bin/env python3
"""
Minimal test to isolate Path error
"""

print("Testing Path error isolation...")

# Test 1: Basic import
try:
    from pathlib import Path
    print("✅ pathlib.Path import works")
except Exception as e:
    print(f"❌ pathlib.Path import failed: {e}")
    exit(1)

# Test 2: Path operations
try:
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent
    print(f"✅ Basic Path operations work")
except Exception as e:
    print(f"❌ Basic Path operations failed: {e}")
    exit(1)

# Test 3: sys.path manipulation  
try:
    import sys
    sys.path.insert(0, str(project_root))
    print(f"✅ sys.path manipulation works")
except Exception as e:
    print(f"❌ sys.path manipulation failed: {e}")
    exit(1)

# Test 4: Try the actual import sequence from validation_test.py
try:
    from co_thinking_agent_simulation.implementation.core.agent_system import ResearchSimulationOrchestrator
    print("✅ ResearchSimulationOrchestrator import successful")
except Exception as e:
    print(f"❌ ResearchSimulationOrchestrator import failed: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Test 5: Try creating a simple agent
try:
    # Just test with a dummy API key to see if the Path error occurs
    sim = ResearchSimulationOrchestrator("dummy_key", num_agents=1)
    print("✅ ResearchSimulationOrchestrator creation successful")
except Exception as e:
    print(f"❌ ResearchSimulationOrchestrator creation failed: {e}")
    import traceback
    traceback.print_exc()

print("Test complete.") 