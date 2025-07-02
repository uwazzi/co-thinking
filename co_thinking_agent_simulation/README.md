# Co-Thinking Research Simulation Agent System

## 🔬 Research-Grade AI Agent System for Educational Co-Thinking Studies

This system enables researchers to simulate and analyze human-AI collaborative thinking in educational contexts, based on **Ethan Mollick's Co-Intelligence framework**, **Swiss AI human-centered principles**, and **The People Factor** research.

### 🎯 **Key Capabilities**

- **20+ Data Points** automatically recorded per interaction
- **5 Psychological Constructs** detection and analysis  
- **6 Cultural Frameworks** for diverse participant simulation
- **4 Export Formats**: JSON, CSV, Excel, Markdown
- **Automated Research Reports** with statistical insights
- **Foundation Document Alignment** validation (>80% target)

---

## 🚀 **Quick Start (5 Minutes)**

### 1. **Setup Environment**
```bash
# Install dependencies
cd co_thinking_agent_simulation/setup
pip3 install -r requirements.txt

# Create .env file at PROJECT ROOT (3 levels up from setup/)
cd ../../../
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
# Edit .env and add your real API key from https://makersuite.google.com/app/apikey
```

### 2. **Validate Setup**
```bash
# Return to setup directory
cd co_thinking_agent_simulation/setup
python3 validation_test.py
```

### 3. **Run Analysis Demo**
```bash
# Navigate to examples
cd ../examples
python3 comprehensive_analysis_demo.py
```

---

## 🔐 **Secure Configuration**

⚠️ **CRITICAL: .env FILE LOCATION**

**The .env file MUST be at the PROJECT ROOT!**

```
co-thinking/                    ← PROJECT ROOT
├── .env                        ← CREATE .env FILE HERE!
├── co_thinking_agent_simulation/
│   ├── setup/
│   │   └── validation_test.py
│   └── implementation/
```

✅ **API keys never committed to git**  
✅ **Automatic .env file exclusion**  
✅ **Secure configuration management**  
✅ **Helpful error messages for missing keys**

**Setup your `.env` file at PROJECT ROOT:**
```env
# Get your key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your_actual_gemini_api_key_here

# Optional: Configure research parameters
DEFAULT_AGENT_COUNT=30
DEFAULT_RESEARCH_CONTEXT=university_diverse
MIN_FOUNDATION_ALIGNMENT=0.8
```

---

## 📊 **What You Get**

### **Comprehensive Data Collection**
Every interaction automatically captures:
- Complete response content and context
- Cultural authenticity and consistency scores
- Psychological construct manifestation (5 types)
- Foundation document alignment validation
- Emotional states and behavioral indicators
- Quality metrics and authenticity validation

### **Research Analysis Pipeline**
- **Cultural Pattern Analysis** across 6 frameworks
- **Statistical Insights** with significance testing
- **Foundation Document Validation** against research texts
- **Quality Assurance** and authenticity checking
- **Automated Research Recommendations**

### **Multi-Format Export**
- **JSON**: Complete dataset with metadata
- **CSV**: Statistical analysis ready format  
- **Excel**: Multi-sheet workbook with summaries
- **Markdown**: Human-readable research reports

---

## 🎓 **Research Applications**

### **Pre-Study Validation**
- Instrument testing and validation
- Sample size and power analysis
- Cultural diversity verification
- Foundation alignment verification

### **Cross-Cultural Research**
- 6 cultural framework simulation
- Authentic response generation
- Cultural pattern identification
- Demographic representation analysis

### **Psychological Research**
- **Trust Calibration** studies
- **Metacognitive Awareness** assessment
- **Help-Seeking Behavior** analysis
- **Authority Deference** patterns
- **Privacy Concern** evaluation

---

## 📁 **Project Structure**

```
co_thinking_agent_simulation/
├── setup/
│   ├── requirements.txt       # Dependencies
│   ├── secure_config.py       # Secure API key management
│   ├── validation_test.py     # System validation
│   └── setup_guide.md        # Quick setup guide
├── implementation/
│   ├── core/
│   │   ├── agent_system.py    # Main orchestration system
│   │   ├── student_profiles.py # Enhanced cultural profiles
│   │   ├── foundation_context.py # Research foundation integration
│   │   └── data_collection.py # Comprehensive data recording
│   └── analysis/
│       ├── response_analyzer.py # Individual response analysis
│       └── data_analyzer.py   # Comprehensive data analysis
├── examples/
│   ├── quick_start.py         # Basic usage example
│   └── comprehensive_analysis_demo.py # Full capabilities demo
└── research_objectives/
    ├── research_framework.md  # Complete research framework
    ├── psychological_constructs.md # Construct definitions
    └── data_analysis_methodology.md # Analysis methodology
```

---

## 🏆 **Expected Results**

After running the comprehensive demo, you'll see:

```
🏆 Key Research Findings:
  🌍 Cultural Patterns: 6 cultures represented
  🧠 Psychological Constructs: 5 constructs detected (87% avg quality)
  📚 Foundation Alignment: 0.78/1.0 average
  💡 Research Recommendations: 4 actionable insights

📊 Quality Assurance Results:
  ✅ Response Coherence: 91% above threshold
  ✅ Cultural Authenticity: 89% validated
  ✅ Foundation Alignment: 84% above target
  ✅ Theoretical Consistency: 93% validated
```

---

## 🔧 **Advanced Configuration**

Use your `.env` file to customize research parameters:

```env
# Research Configuration
DEFAULT_AGENT_COUNT=50
DEFAULT_RESEARCH_CONTEXT=university_diverse
ENABLED_CULTURES=us_individualistic,east_asian_collectivistic,european_balanced

# Quality Thresholds
MIN_COHERENCE_THRESHOLD=0.7
MIN_FOUNDATION_ALIGNMENT=0.8
ENABLE_QUALITY_FILTERING=true

# Export Settings
EXPORT_FORMATS=json,csv,excel,markdown
INCLUDE_RAW_RESPONSES=true
ENABLE_AUTO_ANALYSIS=true
```

---

## 📚 **Research Foundation**

This system is built on rigorous research foundations:

### **Ethan Mollick's Co-Intelligence (2024)**
- Human-AI collaboration patterns
- Trust calibration mechanisms
- Co-working, co-creating, co-teaching, co-learning modes
- Metacognitive awareness importance

### **Swiss AI Human-Centered Principles**  
- Transparency and explainability requirements
- Stakeholder involvement in AI design
- Human oversight and control mechanisms
- Privacy and data protection priorities

### **The People Factor Research**
- Human-centered approach to AI scaling
- User experience and adoption focus
- Cultural context consideration
- Diverse user needs accommodation

---

## 🎉 **Ready to Start?**

```bash
# First, set up your virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r setup/requirements.txt

# Set up your secure environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Validate your setup
python3 setup/validation_test.py

# Start your co-thinking research journey
python3 examples/comprehensive_analysis_demo.py

# Then review the generated analysis files to see the full capabilities!
```

**Your secure Co-Thinking research system is ready for:**
- Pre-study validation and instrument testing
- Cross-cultural research design and analysis
- Comprehensive data collection with automated insights
- Foundation document alignment validation
- Publication-ready research with statistical rigor

---

*Built with research rigor, security-first design, and practical usability for educational technology researchers.* 