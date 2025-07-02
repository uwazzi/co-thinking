# Co-Thinking Agent Simulation - Installation Guide

## System Requirements

### Minimum Requirements
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space for dependencies and data
- **Internet**: Stable connection for LLM API calls

### Recommended Requirements
- **Python**: 3.10 or higher
- **RAM**: 16GB for large simulations (50+ agents)
- **Storage**: 5GB for extensive data collection
- **Internet**: High-speed connection for concurrent API calls

## Step 1: Python Environment Setup

### Option A: Using Conda (Recommended)
```bash
# Create new environment
conda create -n co-thinking python=3.10
conda activate co-thinking

# Navigate to project directory
cd co_thinking_agent_simulation
```

### Option B: Using venv
```bash
# Create virtual environment
python -m venv co_thinking_env

# Activate environment
# On Windows:
co_thinking_env\Scripts\activate
# On Mac/Linux:
source co_thinking_env/bin/activate

# Navigate to project directory
cd co_thinking_agent_simulation
```

## Step 2: Install Dependencies

### Core Dependencies
```bash
# Install from requirements file
pip install -r setup/requirements.txt

# Or install manually:
pip install google-generativeai>=0.3.0
pip install pandas>=1.5.0
pip install pyyaml>=6.0
pip install asyncio
pip install dataclasses-json
pip install numpy>=1.21.0
pip install matplotlib>=3.5.0
pip install seaborn>=0.11.0
```

### Optional Dependencies (for advanced features)
```bash
# For data visualization
pip install plotly>=5.0.0

# For statistical analysis
pip install scipy>=1.8.0
pip install scikit-learn>=1.1.0

# For export formats
pip install openpyxl>=3.0.0
```

## Step 3: API Key Configuration

### Get Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with Google account
3. Create new API key
4. Copy the API key

### 2. Set Up API Key (Secure Method)

⚠️ **CRITICAL: .env FILE LOCATION**

**The .env file MUST be at the PROJECT ROOT, NOT in the setup directory!**

```
co-thinking/                    ← PROJECT ROOT
├── .env                        ← CREATE .env FILE HERE!
├── co_thinking_agent_simulation/
│   ├── setup/                  ← You are here now
│   │   └── installation_guide.md
│   └── implementation/
```

#### Create Environment File at PROJECT ROOT
```bash
# Navigate to PROJECT ROOT (3 levels up from setup/)
cd ../../../

# Create .env file at PROJECT ROOT
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

#### Add Your API Key
Replace the placeholder with your actual API key:
```bash
# Edit the .env file with your real API key
echo "GEMINI_API_KEY=AIzaSyC123...your-actual-key-here" > .env
```

#### Security Note
- ✅ The `.env` file is automatically excluded from git
- ✅ Your API key will never be committed to version control
- ✅ Safe to share the project without exposing credentials

#### Optional: Configure Additional Settings
The `.env` file also supports optional research configuration:
```bash
# Add additional settings to .env file
echo "DEFAULT_AGENT_COUNT=30" >> .env
echo "DEFAULT_RESEARCH_CONTEXT=university_diverse" >> .env
echo "MIN_FOUNDATION_ALIGNMENT=0.8" >> .env
```

## Step 4: Verify Installation

### Check .env File Location (Optional Helper)
```bash
# Navigate to setup directory  
cd co_thinking_agent_simulation/setup

# Use our helper script to verify .env location and content
python3 check_env_location.py
```

### Run Validation Test
```bash
# Make sure you're in setup directory
cd co_thinking_agent_simulation/setup

# Run validation test
python3 validation_test.py
```

### Expected Output
```
Co-Thinking Research Simulation Validation
=================================================
This will test your simulation system setup.

=== Co-Thinking Research Simulation Validation ===
Started at: 2024-01-15 10:30:00.123456

Test 1: Basic Functionality
------------------------------
✓ Created 3 agents
✓ Got 3/3 valid responses
Score: 3/3

Test 2: Foundation Document Integration
----------------------------------------
✓ Foundation concept mentions: 4/5 (80%)
✓ Co-intelligence concepts: 3/5
✓ Human-centered concepts: 4/5
Score: 0.80/1.0

...

=== VALIDATION REPORT ===
--------------------------------------------------
Overall Score: 4.2/5 (84%)

✓ PASS Basic Functionality: 1.00/1.0
✓ PASS Foundation Integration: 0.80/1.0
✓ PASS Agent Diversity: 0.85/1.0
✓ PASS Psychological Constructs: 0.75/1.0
✓ PASS Data Export: 1.00/1.0

=== RECOMMENDATIONS ===
🎉 Excellent! Your simulation system is working well.
   Ready for research scenarios and data collection.
```

### Troubleshooting Validation Issues

#### API Key Issues
```bash
# Test API key manually
python -c "
import google.generativeai as genai
genai.configure(api_key='your-api-key')
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Hello')
print(response.text)
"
```

#### Import Errors
```bash
# Check installed packages
pip list | grep -E "(google|pandas|yaml)"

# Reinstall if needed
pip install --upgrade google-generativeai pandas pyyaml
```

#### Rate Limiting
```python
# Add delays in validation_test.py
import time
time.sleep(1)  # Between API calls
```

## Step 5: Run First Example

### Quick Start Example
```bash
# Navigate to examples directory
cd ../examples

# Run quick start
python quick_start.py
```

### Expected Output
```
Created 5 culturally diverse student agents
Cultural diversity: {'US_Individualistic': 2, 'East_Asian_Collectivistic': 1, 'European_Balanced': 1, 'Latin_American': 1}
Running scenario: Basic Co-Thinking Test with 5 diverse agents
Enhanced simulation completed!
Simulation data exported to quick_start_results.json
```

## Step 6: Foundation Document Integration

### Add Your Foundation Documents
```bash
# Create foundation documents directory (if not exists)
mkdir -p foundation_documents

# Copy your PDFs
cp "path/to/Co-Intelligence Living and Working with AI (Ethan Mollick).pdf" foundation_documents/
cp "path/to/AI Swiss - Livre blanc.pdf" foundation_documents/
cp "path/to/The_People_Factor_A_human-centred_approach_to_scaling_AI_tools.pdf" foundation_documents/
```

### Update Foundation Context
Edit `implementation/core/foundation_context.py`:

```python
def _get_mollick_context(self) -> str:
    # Add specific insights from your reading of Mollick's book
    return """
    MOLLICK CO-INTELLIGENCE PRINCIPLES (Your Specific Insights):
    - [Key insight 1 from your reading]
    - [Key insight 2 from your reading]
    - [Key insight 3 from your reading]
    """
```

## Step 7: Configuration Options

### Basic Configuration
```python
# In your research scripts
from implementation.core.agent_system import ResearchSimulationOrchestrator

# Basic setup
sim = ResearchSimulationOrchestrator(
    api_key="your-api-key",
    research_context="university_diverse",  # or "high_school_multicultural", "adult_learners"
    num_agents=20
)
```

### Advanced Configuration
```python
# Custom agent profiles
from implementation.core.student_profiles import create_diverse_research_cohort

custom_profiles = create_diverse_research_cohort(
    num_agents=30,
    research_context="university_diverse",
    custom_distributions={
        "cultural_templates": ["US_Individualistic", "East_Asian_Collectivistic"],
        "age_range": (18, 22)
    }
)

sim = ResearchSimulationOrchestrator(
    api_key="your-api-key",
    custom_profiles=custom_profiles
)
```

## Common Installation Issues

### Issue 1: SSL Certificate Errors
```bash
# Update certificates
pip install --upgrade certifi

# Or use system certificates
pip install --trusted-host pypi.org --trusted-host pypi.python.org google-generativeai
```

### Issue 2: API Rate Limiting
```python
# Add rate limiting to your code
import time
import asyncio

async def rate_limited_execution():
    for i in range(num_operations):
        if i > 0:
            await asyncio.sleep(1)  # 1 second delay
        # Your operation here
```

### Issue 3: Memory Issues with Large Simulations
```python
# Process in batches
batch_size = 10
for i in range(0, total_agents, batch_size):
    batch_agents = agents[i:i+batch_size]
    # Process batch
    # Clear memory if needed
    del batch_agents
```

### Issue 4: Windows Path Issues
```python
# Use pathlib for cross-platform compatibility
from pathlib import Path

data_path = Path("simulation_data") / "results.json"
```

## Next Steps

### For Researchers
1. **Read research framework**: Review `research_objectives/research_framework.md`
2. **Understand constructs**: Study `research_objectives/psychological_constructs.md`
3. **Design your study**: Use templates in `examples/`
4. **Run pilot simulation**: Start with small agent count
5. **Analyze results**: Use tools in `implementation/analysis/`

### For Developers
1. **Explore codebase**: Understand `implementation/core/` structure
2. **Read API docs**: Review `documentation/api_reference.md`
3. **Contribute features**: Add new profile types or analysis tools
4. **Submit validation**: Test with your research contexts

### For System Administrators
1. **Set up shared environment**: Configure for multiple users
2. **Monitor API usage**: Track costs and rate limits
3. **Backup data**: Implement data retention policies
4. **Scale infrastructure**: Plan for large simulations

## Support

### Getting Help
- **Documentation**: Check `documentation/` folder
- **Troubleshooting**: See `documentation/troubleshooting.md`
- **Examples**: Explore `examples/` directory
- **Validation**: Run `setup/validation_test.py` regularly

### Contributing
- Report issues with validation results
- Share new cultural profiles or scenarios
- Contribute analysis tools
- Submit research validation studies

**Your simulation system is now ready for co-thinking research!**

Next step: Read `../research_objectives/research_framework.md` to understand the research methodology and design your first study. 