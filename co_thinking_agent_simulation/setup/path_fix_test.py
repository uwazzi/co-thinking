#!/usr/bin/env python3
"""
Simple test to verify Path variable scoping fixes
This script tests the import paths without requiring all dependencies
"""

import sys
from pathlib import Path

def test_path_imports():
    """Test that all modules can be imported without Path scoping errors"""
    
    print("🔧 Testing Path variable scoping fixes...")
    print("-" * 50)
    
    # Add project to path
    project_root = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(project_root))
    
    success_count = 0
    total_tests = 0
    
    # Test 1: agent_system imports
    total_tests += 1
    try:
        print("1. Testing agent_system.py imports...")
        sys.path.append(str(Path(__file__).parent.parent / "implementation"))
        
        # Test the imports that caused the issue
        from co_thinking_agent_simulation.implementation.core import agent_system
        print("   ✅ agent_system.py imports successfully")
        success_count += 1
    except Exception as e:
        print(f"   ❌ agent_system.py import failed: {e}")
    
    # Test 2: data_collection imports
    total_tests += 1
    try:
        print("2. Testing data_collection.py imports...")
        from co_thinking_agent_simulation.implementation.core import data_collection
        print("   ✅ data_collection.py imports successfully")
        success_count += 1
    except Exception as e:
        print(f"   ❌ data_collection.py import failed: {e}")
    
    # Test 3: foundation_context imports
    total_tests += 1
    try:
        print("3. Testing foundation_context.py imports...")  
        from co_thinking_agent_simulation.implementation.core import foundation_context
        print("   ✅ foundation_context.py imports successfully")
        success_count += 1
    except Exception as e:
        print(f"   ❌ foundation_context.py import failed: {e}")
    
    # Test 4: secure_config imports
    total_tests += 1
    try:
        print("4. Testing secure_config.py imports...")
        from co_thinking_agent_simulation.setup import secure_config
        print("   ✅ secure_config.py imports successfully")
        success_count += 1
    except Exception as e:
        print(f"   ❌ secure_config.py import failed: {e}")
    
    print("-" * 50)
    print(f"📊 Test Results: {success_count}/{total_tests} imports successful")
    
    if success_count == total_tests:
        print("🎉 ALL PATH FIXES SUCCESSFUL!")
        print("✅ The Path variable scoping errors have been resolved")
        print("💡 You can now proceed with the full validation test")
        return True
    else:
        print("⚠️  Some imports still have issues")
        print("💡 Check the specific error messages above")
        return False

def test_basic_path_operations():
    """Test basic Path operations to ensure pathlib is working correctly"""
    
    print("\n🔍 Testing basic Path operations...")
    
    try:
        # Test Path creation and operations
        current_file = Path(__file__)
        parent_dir = current_file.parent
        grandparent = parent_dir.parent
        
        print(f"   ✅ Current file: {current_file.name}")
        print(f"   ✅ Parent directory: {parent_dir.name}")
        print(f"   ✅ Grandparent directory: {grandparent.name}")
        
        # Test path joining
        test_path = parent_dir / "test_file.txt"
        print(f"   ✅ Path joining works: {test_path.name}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Basic Path operations failed: {e}")
        return False

if __name__ == "__main__":
    print("Path Fix Verification Test")
    print("=" * 40)
    
    # Test basic Path operations first
    basic_success = test_basic_path_operations()
    
    if basic_success:
        # Test module imports
        import_success = test_path_imports()
        
        if import_success:
            print("\n🚀 READY FOR VALIDATION TEST!")
            print("Next step: Run the full validation test")
            print("Command: python3 validation_test.py")
        else:
            print("\n🔧 ADDITIONAL FIXES NEEDED")
            print("Some modules still have import issues")
    else:
        print("\n❌ BASIC PATH OPERATIONS FAILED")
        print("There may be a fundamental issue with pathlib")
    
    print("\nDone.") 