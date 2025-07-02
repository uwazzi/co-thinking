# Quick Setup Guide - Co-Thinking Agent Simulation

## ⚠️ CRITICAL: .env FILE LOCATION

**The .env file MUST be at the PROJECT ROOT, NOT in the setup or co_thinking_agent_simulation directories!**

```
co-thinking/                    ← PROJECT ROOT (CREATE .env HERE!)
├── .env                        ← CREATE THIS FILE HERE!
├── co_thinking_agent_simulation/
│   ├── setup/
│   │   ├── validation_test.py  ← Run this to test
│   │   └── requirements.txt    ← Install this
│   └── implementation/
```

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
# Navigate to setup directory
cd co_thinking_agent_simulation/setup

# Install dependencies
pip3 install -r requirements.txt
```

### Step 2: Create .env File at PROJECT ROOT
```bash
# Navigate to PROJECT ROOT (3 levels up from setup/)
cd ../../../

# Verify you're in the correct location (should see co_thinking_agent_simulation folder)
ls -la

# Create .env file with your API key
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

### Step 3: Get Your API Key and Test
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API key"
3. Copy your API key
4. Replace `your_actual_api_key_here` in the .env file with your real API key:
   ```bash
   # Edit the .env file (still in project root)
   echo "GEMINI_API_KEY=AIzaSyD1234567890abcdefghijklmnopqrstuvwxyz" > .env
   ```

5. Test the setup:
   ```bash
   # Go back to setup directory
   cd co_thinking_agent_simulation/setup
   
   # Run validation test
   python3 validation_test.py
   ```

## ✅ Success Criteria
When setup is correct, you should see:
- ✅ API key loaded (ends with: ...abcd)
- ✅ Configuration loaded successfully
- ✅ Test scores showing "PASS" status

## 🔧 Troubleshooting

### Error: "GEMINI_API_KEY not found"
**Solution**: Check .env file location and content
```bash
# Go to project root
cd ../../../

# Check if .env exists
ls -la .env

# Check .env content
cat .env
# Should show: GEMINI_API_KEY=AIzaSy...your_key

# If empty or wrong location, recreate it:
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

### Error: "cannot access local variable 'Path'"
✅ **FIXED** - This error has been resolved in the latest version

### Error: "No module named 'pandas'"
**Solution**: Install requirements
```bash
cd co_thinking_agent_simulation/setup
pip3 install -r requirements.txt
```

### Error: "Module not found"
**Solution**: Make sure you're running from the correct directory (setup/)

## 📁 Project Structure After Setup
```
co-thinking/                           ← PROJECT ROOT
├── .env                               ← MUST BE HERE! (GEMINI_API_KEY=...)
├── co_thinking_agent_simulation/
│   ├── setup/
│   │   ├── validation_test.py         ← Run this to test
│   │   └── requirements.txt           ← Install these packages
│   ├── implementation/
│   └── examples/
```

## 🚨 Common Mistakes

❌ **WRONG LOCATIONS**:
- `.env` in setup directory
- `.env` in co_thinking_agent_simulation directory  

✅ **CORRECT LOCATION**:
- `.env` in project root (co-thinking directory)

❌ **WRONG CONTENT**:
- Empty .env file
- Placeholder text not replaced

✅ **CORRECT CONTENT**:
```
GEMINI_API_KEY=AIzaSyD1234567890abcdefghijklmnopqrstuvwxyz
```

## 💡 Need Help?
1. ✅ Check that `.env` file is in the correct location (project root)
2. ✅ Verify your API key is valid and active  
3. ✅ Ensure all dependencies are installed
4. ✅ Run validation test to check setup status

## 🎉 You're Ready!
Once validation passes, try the examples:
```bash
cd co_thinking_agent_simulation/examples
python3 comprehensive_analysis_demo.py
``` 