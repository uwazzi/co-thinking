#!/usr/bin/env python3
"""
Debug Path Error - Mac venv specific
This script will help us isolate exactly where the Path error is occurring
"""

import sys
from pathlib import Path

def test_step_by_step():
    """Test each import step to find where Path error occurs"""
    
    print("🔍 Debug Path Error - Mac venv")
    print("=" * 50)
    
    # Step 1: Test basic Path operations
    print("Step 1: Testing basic Path operations...")
    try:
        current_file = Path(__file__)
        project_root = current_file.parent.parent.parent
        print(f"✅ Basic Path operations work")
        print(f"   Current file: {current_file}")
        print(f"   Project root: {project_root}")
    except Exception as e:
        print(f"❌ Basic Path operations failed: {e}")
        return
    
    # Step 2: Test path manipulation
    print("\nStep 2: Testing path manipulation...")
    try:
        sys.path.insert(0, str(project_root))
        print(f"✅ Path manipulation works")
        print(f"   Added to sys.path: {str(project_root)}")
    except Exception as e:
        print(f"❌ Path manipulation failed: {e}")
        return
    
    # Step 3: Test individual module imports
    print("\nStep 3: Testing individual module imports...")
    
    modules_to_test = [
        'co_thinking_agent_simulation.implementation.core.foundation_context',
        'co_thinking_agent_simulation.setup.secure_config',
        'co_thinking_agent_simulation.implementation.core.student_profiles',
        'co_thinking_agent_simulation.implementation.core.data_collection',
        'co_thinking_agent_simulation.implementation.core.agent_system'
    ]
    
    for module_name in modules_to_test:
        try:
            __import__(module_name)
            print(f"✅ {module_name}")
        except Exception as e:
            print(f"❌ {module_name}: {e}")
            # Print full traceback for the failing module
            import traceback
            print("   Full traceback:")
            traceback.print_exc()
            print("-" * 30)
    
    # Step 4: Test validation_test specific imports
    print("\nStep 4: Testing validation_test specific imports...")
    try:
        from co_thinking_agent_simulation.implementation.core.agent_system import ResearchSimulationOrchestrator
        from co_thinking_agent_simulation.implementation.core.foundation_context import FoundationDocumentContext
        from co_thinking_agent_simulation.setup.secure_config import get_config, get_api_key
        print("✅ All validation_test imports successful")
    except Exception as e:
        print(f"❌ Validation test imports failed: {e}")
        import traceback
        traceback.print_exc()

def check_python_environment():
    """Check Python environment details"""
    print("\n" + "=" * 50)
    print("🐍 Python Environment Info")
    print("=" * 50)
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Virtual env: {'✅ Active' if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) else '❌ Not detected'}")
    print(f"Platform: {sys.platform}")
    
    # Check installed packages related to our project
    print(f"\nPython path entries:")
    for i, path in enumerate(sys.path[:5]):  # Show first 5 entries
        print(f"  {i}: {path}")
    
    if len(sys.path) > 5:
        print(f"  ... and {len(sys.path) - 5} more entries")

if __name__ == "__main__":
    check_python_environment()
    test_step_by_step()
    print("\n" + "=" * 50)
    print("Debug complete. If you see the exact error above,")
    print("we can fix the specific module causing the issue.")
    print("=" * 50) 