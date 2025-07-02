# Research Simulation Agent Setup Guide

## 🔐 Secure Quick Start

### 1. Prerequisites
```bash
# Install required packages
pip install -r requirements.txt

# This includes: google-generativeai, pandas, python-dotenv, asyncio
```

### 2. Secure API Key Setup
```bash
# Copy the environment template
cp .env.example .env

# Edit the .env file and add your API key
nano .env
```

**Edit your `.env` file:**
```env
# Get your key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your_actual_gemini_api_key_here

# Optional: Configure research parameters
DEFAULT_AGENT_COUNT=20
DEFAULT_RESEARCH_CONTEXT=university_diverse
MIN_FOUNDATION_ALIGNMENT=0.8
```

### 3. Basic Setup (Secure Method)
```python
# No API key needed in code - loads securely from .env file
from core.agent_system import ResearchSimulationOrchestrator
import asyncio

async def run_basic_test():
    # API key loaded automatically from .env
    sim = ResearchSimulationOrchestrator(num_agents=5)
    
    scenario = {
        "name": "Basic Co-Thinking Test",
        "learning_task": "Solve: What is 2x + 5 = 15?",
        "ai_tutor_response": "Let's solve this step by step. First, subtract 5 from both sides: 2x = 10. Then divide by 2: x = 5."
    }
    
    result = await sim.run_co_thinking_scenario(scenario)
    sim.export_simulation_data("test_results")
    print("Basic test completed!")

# Run test
asyncio.run(run_basic_test())
```

### 4. Alternative: Direct API Key (Less Secure)
```python
# Only if you can't use .env file
from core.agent_system import ResearchSimulationOrchestrator

# Pass API key directly (not recommended for production)
sim = ResearchSimulationOrchestrator(
    api_key="your-api-key-here",  # Not secure - avoid in production
    num_agents=5
)
```

## 🔧 Configuration Options

### 5. Environment Variables Available

Your `.env` file supports these configuration options:

```env
# === REQUIRED ===
GEMINI_API_KEY=your_actual_key_here

# === RESEARCH CONFIGURATION ===
DEFAULT_AGENT_COUNT=30
DEFAULT_RESEARCH_CONTEXT=university_diverse
DATA_OUTPUT_DIR=./my_research_data

# === QUALITY SETTINGS ===
MIN_COHERENCE_THRESHOLD=0.7
MIN_FOUNDATION_ALIGNMENT=0.8
ENABLE_QUALITY_FILTERING=true

# === CULTURAL DIVERSITY ===
ENABLED_CULTURES=us_individualistic,east_asian_collectivistic,european_balanced

# === EXPORT SETTINGS ===
EXPORT_FORMATS=json,csv,excel,markdown
INCLUDE_RAW_RESPONSES=true
ENABLE_AUTO_ANALYSIS=true
```

### 6. Using Configuration in Code
```python
from setup.secure_config import get_config

# Get configuration instance
config = get_config()

# Use configuration values
sim = ResearchSimulationOrchestrator(
    num_agents=config.default_agent_count,
    research_context=config.default_research_context,
    output_directory=config.data_output_dir
)

# Print current configuration
config.print_configuration_summary()
```

## Using Your Foundation Documents

### 7. Foundation Document Integration

The agents automatically use your foundation documents. The secure configuration also supports foundation document settings:

```env
# Foundation document alignment thresholds
MIN_FOUNDATION_ALIGNMENT=0.8
ENABLE_FOUNDATION_VALIDATION=true
```

### 8. Testing Foundation Document Integration

```python
from core.agent_system import ResearchSimulationOrchestrator
import asyncio

async def test_foundation_integration():
    # Uses secure config automatically
    sim = ResearchSimulationOrchestrator(num_agents=3)
    
    # Test scenario that should trigger foundation document principles
    scenario = {
        "name": "Foundation Integration Test",
        "learning_task": "Should I let AI do all my homework for me?",
        "ai_tutor_response": "I can help you with your homework, but it's important that you understand the concepts yourself. Let me guide you through the problem-solving process instead."
    }
    
    result = await sim.run_co_thinking_scenario(scenario)
    
    # Export with foundation alignment analysis
    files = sim.export_simulation_data("foundation_test")
    
    print("Foundation integration test completed!")
    print("Check the analysis files for foundation alignment scores")

asyncio.run(test_foundation_integration())
```

## Educational Research Scenarios

### 9. Pre-built Scenarios for Your Research

```python
from core.agent_system import ResearchSimulationOrchestrator
import asyncio

CO_THINKING_SCENARIOS = [
    {
        "name": "Trust Calibration - Math",
        "type": "trust_calibration",
        "learning_task": "Solve this quadratic equation: x² - 5x + 6 = 0",
        "ai_tutor_response": "I'll factor this for you: (x - 2)(x - 3) = 0, so x = 2 or x = 3. But let me also show you the quadratic formula method to verify."
    },
    {
        "name": "Metacognitive Awareness - Science",
        "type": "metacognitive_awareness",
        "learning_task": "Explain why ice floats on water",
        "ai_tutor_response": "Ice floats because it's less dense than liquid water. This happens because water molecules form a hexagonal crystal structure when frozen, creating more space between molecules. What do you think about this explanation?"
    },
    {
        "name": "Cognitive Partnership - Writing",
        "type": "cognitive_partnership",
        "learning_task": "Write a thesis statement for an essay about renewable energy",
        "ai_tutor_response": "A strong thesis should take a clear position. How about: 'While renewable energy sources require significant initial investment, their long-term environmental and economic benefits make them essential for sustainable development.' What would you add or change?"
    },
    {
        "name": "Agency Distribution - Programming",
        "type": "agency_distribution",
        "learning_task": "Debug this Python code: print('Hello World'",
        "ai_tutor_response": "I notice you're missing a closing parenthesis. The correct code is: print('Hello World'). Would you like me to explain why this error occurs, or do you want to try fixing similar errors yourself first?"
    }
]

async def run_research_scenarios():
    # Secure configuration loaded automatically
    sim = ResearchSimulationOrchestrator(num_agents=10)
    
    print("Running research scenarios with secure configuration...")
    
    for scenario in CO_THINKING_SCENARIOS:
        result = await sim.run_co_thinking_scenario(scenario)
        print(f"✅ Completed: {scenario['name']}")
    
    # Export comprehensive analysis
    files = sim.export_simulation_data("research_scenarios")
    
    print("\n📊 Analysis files created:")
    for file_type, filepath in files.items():
        print(f"  - {file_type}: {filepath}")

# Run scenarios
asyncio.run(run_research_scenarios())
```

### 10. Measuring Your 5 Core Psychological Constructs

```python
CONSTRUCT_TESTING_SCENARIOS = {
    "cognitive_partnership": {
        "name": "Cognitive Partnership Test",
        "type": "cognitive_partnership",
        "learning_task": "Create a study plan for final exams",
        "ai_tutor_response": "I suggest we work together on this. I can help organize topics and timing, but you know your strengths and weaknesses best. What subjects are you most concerned about?"
    },
    
    "metacognitive_awareness": {
        "name": "Metacognitive Awareness Test",
        "type": "metacognitive_awareness", 
        "learning_task": "You got this problem wrong: 2 + 3 × 4 = 20. Find the error.",
        "ai_tutor_response": "The order of operations is key here. Remember PEMDAS? Let's work through it: 2 + 3 × 4 = 2 + 12 = 14, not 20. Do you see where the error occurred?"
    },
    
    "trust_calibration": {
        "name": "Trust Calibration Test",
        "type": "trust_calibration",
        "learning_task": "Is this AI-generated text detection accurate?",
        "ai_tutor_response": "I'm not 100% certain about this detection. AI text detectors can have false positives. I'd recommend using multiple tools and your own judgment. What do you think based on the writing style?"
    },
    
    "agency_distribution": {
        "name": "Agency Distribution Test",
        "type": "agency_distribution",
        "learning_task": "Choose a research topic for your final project",
        "ai_tutor_response": "I can suggest some popular topics in this field, but the choice should reflect your interests and career goals. What areas have you found most engaging in this course?"
    },
    
    "cognitive_load_management": {
        "name": "Cognitive Load Test",
        "type": "cognitive_load_management",
        "learning_task": "Learn calculus derivatives, integration, and limits all in one session",
        "ai_tutor_response": "That's a lot to cover in one session! Let's prioritize. What's your most urgent need? I suggest we focus on one concept first, then build connections to the others."
    }
}

async def test_psychological_constructs():
    # Secure configuration with construct detection
    sim = ResearchSimulationOrchestrator(num_agents=15)
    
    print("Testing psychological constructs...")
    
    for construct_name, scenario in CONSTRUCT_TESTING_SCENARIOS.items():
        result = await sim.run_co_thinking_scenario(scenario)
        print(f"✅ Tested: {construct_name}")
    
    # Export with construct analysis
    files = sim.export_simulation_data("construct_testing")
    
    print("\n🧠 Construct analysis completed!")
    print("Check the Excel/Markdown files for detailed construct detection results")

asyncio.run(test_psychological_constructs())
```

## Data Analysis and Validation

### 11. Comprehensive Analysis Pipeline

```python
from core.agent_system import ResearchSimulationOrchestrator
from analysis.data_analyzer import ComprehensiveDataAnalyzer
import asyncio

async def run_comprehensive_analysis():
    """Complete research workflow with analysis"""
    
    # Create simulation with secure config
    sim = ResearchSimulationOrchestrator(num_agents=20)
    
    # Run multiple scenarios
    scenarios = [
        {
            "name": "Math Collaboration",
            "type": "cognitive_partnership",
            "learning_task": "Solve complex algebra problem",
            "ai_tutor_response": "Let's work together on this..."
        },
        {
            "name": "Trust Assessment",
            "type": "trust_calibration", 
            "learning_task": "Verify AI solution accuracy",
            "ai_tutor_response": "I believe this is correct, but let's double-check..."
        }
    ]
    
    for scenario in scenarios:
        await sim.run_co_thinking_scenario(scenario)
    
    # Export comprehensive analysis
    files = sim.export_simulation_data("comprehensive_study")
    
    print("📊 Research Analysis Complete!")
    print("\nFiles created:")
    for file_type, path in files.items():
        print(f"  - {file_type.upper()}: {path}")
    
    print("\n🏆 Key Findings:")
    print("  Check the Markdown file for research insights")
    print("  Check the Excel file for statistical analysis")
    print("  Check the CSV file for custom analysis in R/SPSS")

asyncio.run(run_comprehensive_analysis())
```

## Troubleshooting

### 12. Configuration Issues

**Check your configuration:**
```python
from setup.secure_config import get_config

try:
    config = get_config()
    print("✅ Configuration loaded successfully")
    config.print_configuration_summary()
except Exception as e:
    print(f"❌ Configuration error: {e}")
    print("\n💡 Setup steps:")
    print("1. Copy .env.example to .env")
    print("2. Edit .env and add your GEMINI_API_KEY")
    print("3. Get key from: https://makersuite.google.com/app/apikey")
```

**Test API key:**
```python
from setup.secure_config import get_api_key
import google.generativeai as genai

try:
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Hello, can you respond?")
    print("✅ API key working:", response.text[:50] + "...")
except Exception as e:
    print(f"❌ API key error: {e}")
```

### 13. Common Issues and Solutions

**Missing .env file:**
```bash
# Copy template and edit
cp .env.example .env
nano .env  # Add your API key
```

**Rate limiting with secure config:**
```python
# Configure rate limiting in .env
MAX_CONCURRENT_REQUESTS=5
API_TIMEOUT=30
```

**Large simulations:**
```python
# Use batch processing
async def run_large_simulation():
    batch_size = 10
    
    for batch in range(0, 50, batch_size):
        sim = ResearchSimulationOrchestrator(num_agents=batch_size)
        await sim.run_co_thinking_scenario(scenario)
        files = sim.export_simulation_data(f"batch_{batch}")
        print(f"Completed batch {batch}")
```

## Next Steps

### 14. Complete Workflow

1. **Secure Setup**:
   ```bash
   cp .env.example .env
   # Edit .env with your API key
   ```

2. **Validate Setup**:
   ```bash
   python setup/validation_test.py
   ```

3. **Run Research**:
   ```bash
   python examples/comprehensive_analysis_demo.py
   ```

4. **Analyze Results**:
   - Check generated Excel files for statistical analysis
   - Review Markdown reports for research insights
   - Use CSV files for custom analysis in R/SPSS/Python

### 15. Security Best Practices

✅ **Never commit .env files**  
✅ **Use environment variables for all sensitive data**  
✅ **Share .env.example (not .env) with collaborators**  
✅ **Use configuration management for all settings**  
✅ **Test configuration before running large simulations**

**Remember**: This secure approach protects your API keys while providing flexible configuration for your research parameters. The system automatically validates your setup and provides helpful error messages if anything needs to be configured. 