#!/usr/bin/env python3
"""
Check .env File Location Helper
Verifies that .env file is in the correct location (PROJECT ROOT)
"""

import os
from pathlib import Path

def check_env_location():
    """Check if .env file is in the correct location"""
    
    print("🔍 Co-Thinking .env File Location Checker")
    print("=" * 50)
    
    # Get current directory info
    current_dir = Path.cwd()
    print(f"📍 Current directory: {current_dir}")
    
    # Determine project root (3 levels up from setup/)
    if current_dir.name == "setup":
        project_root = current_dir.parent.parent.parent
        print(f"📁 Detected project root: {project_root}")
    else:
        print("⚠️  You should run this from the setup/ directory")
        print("   cd co_thinking_agent_simulation/setup/")
        return False
    
    # Check for .env file in project root
    env_file_path = project_root / ".env"
    
    print(f"\n🎯 Expected .env location: {env_file_path}")
    
    if env_file_path.exists():
        print("✅ .env file found in correct location!")
        
        # Check if it has content
        env_content = env_file_path.read_text().strip()
        if env_content:
            lines = env_content.split('\n')
            print(f"✅ .env file has {len(lines)} line(s)")
            
            # Check for API key
            has_gemini_key = any('GEMINI_API_KEY' in line for line in lines)
            if has_gemini_key:
                print("✅ GEMINI_API_KEY found in .env file")
                print("\n🎉 Your .env setup looks correct!")
                return True
            else:
                print("❌ GEMINI_API_KEY not found in .env file")
                print("\n💡 Add your API key:")
                print(f"   echo 'GEMINI_API_KEY=your_api_key_here' >> {env_file_path}")
                return False
        else:
            print("❌ .env file is empty")
            print("\n💡 Add your API key:")
            print(f"   echo 'GEMINI_API_KEY=your_api_key_here' > {env_file_path}")
            return False
    else:
        print("❌ .env file NOT found in project root")
        print("\n🔧 Create .env file in correct location:")
        print(f"   echo 'GEMINI_API_KEY=your_api_key_here' > {env_file_path}")
        print("\n📋 Get your API key from:")
        print("   https://makersuite.google.com/app/apikey")
        return False

def show_wrong_locations():
    """Show common wrong locations where users might put .env file"""
    
    current_dir = Path.cwd()
    
    # Check for .env in wrong locations
    wrong_locations = [
        current_dir / ".env",  # In setup/ directory
        current_dir.parent / ".env",  # In co_thinking_agent_simulation/ directory
    ]
    
    wrong_files_found = []
    for wrong_path in wrong_locations:
        if wrong_path.exists():
            wrong_files_found.append(wrong_path)
    
    if wrong_files_found:
        print("\n⚠️  Found .env files in WRONG locations:")
        for wrong_path in wrong_files_found:
            print(f"   ❌ {wrong_path}")
        print("\n💡 Move these to the PROJECT ROOT or they won't be found!")

if __name__ == "__main__":
    success = check_env_location()
    show_wrong_locations()
    
    print("\n" + "=" * 50)
    if success:
        print("🚀 Ready to run: python3 validation_test.py")
    else:
        print("🔧 Fix .env location/content, then run: python3 validation_test.py")
    print("=" * 50) 