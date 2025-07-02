# 🚀 Co-Thinking Research System - Setup Guide

## ⚠️ CRITICAL: .env FILE LOCATION

**The .env file MUST be at the PROJECT ROOT, NOT in the setup directory!**

```
co-thinking/                    ← PROJECT ROOT
├── .env                        ← CREATE .env FILE HERE!
├── co_thinking_agent_simulation/
│   ├── setup/                  ← You are here now
│   │   ├── validation_test.py
│   │   └── requirements.txt
│   └── implementation/
```

## 🎯 5-Minute Setup (Follow Exactly)

### Step 1: Install Dependencies
```bash
# You should be in: co_thinking_agent_simulation/setup/
pip3 install -r requirements.txt
```

### Step 2: Create .env File at PROJECT ROOT
```bash
# Navigate to PROJECT ROOT (3 levels up from setup/)
cd ../../../

# Create .env file at PROJECT ROOT
touch .env

# Add your API key to the .env file
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

### Step 3: Get Your Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API key"
3. Copy your API key
4. Replace `your_actual_api_key_here` in the .env file with your real key

### Step 4: Verify .env File Location and Content
```bash
# Check you're in project root (should see co_thinking_agent_simulation folder)
ls -la

# Verify .env file exists and has content
cat .env
# Should show: GEMINI_API_KEY=AIzaSy...your_key_here

# OPTIONAL: Use our helper script to double-check everything
cd co_thinking_agent_simulation/setup
python3 check_env_location.py
```

### Step 5: Run Validation Test
```bash
# Go back to setup directory
cd co_thinking_agent_simulation/setup/

# Run validation
python3 validation_test.py
```

## 📁 Correct File Structure After Setup

```
co-thinking/                           ← PROJECT ROOT
├── .env                               ← MUST BE HERE! Contains GEMINI_API_KEY=...
├── co_thinking_agent_simulation/
│   ├── setup/
│   │   ├── validation_test.py         ← Run this to test
│   │   ├── requirements.txt           ← Install this
│   │   └── setup_guide.md             ← This file
│   ├── implementation/
│   └── examples/
```

## ✅ Success Indicators

When setup is correct, `python3 validation_test.py` should show:
- ✅ API key loaded (ends with: ...abcd)
- ✅ Configuration loaded successfully
- ✅ Test scores showing "PASS" status

## 🚨 Common Mistakes

❌ **WRONG**: `.env` in setup directory  
❌ **WRONG**: `.env` in co_thinking_agent_simulation directory  
✅ **CORRECT**: `.env` in project root (co-thinking directory)

❌ **WRONG**: Empty .env file  
✅ **CORRECT**: .env file with `GEMINI_API_KEY=your_actual_key`

## 🔧 Troubleshooting

### Error: "GEMINI_API_KEY not found"
```bash
# Check .env file location
cd ../../../  # Go to project root
ls -la .env   # Should exist
cat .env      # Should show your API key
```

### Error: "No module named 'pandas'"
```bash
# Install dependencies
cd co_thinking_agent_simulation/setup/
pip3 install -r requirements.txt
```

### Error: "cannot access local variable 'Path'"
✅ **FIXED** - This error has been resolved in the latest version

## 🎉 You're Ready!

Once validation passes, your system is ready for:
- Cross-cultural research simulation
- Psychological construct analysis  
- Foundation document alignment testing
- Comprehensive data export and analysis

Start with `examples/comprehensive_analysis_demo.py` to see full capabilities! 