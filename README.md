# Co-Thinking Research System 🧠🤖

A comprehensive research platform for studying psychological foundations of human-AI collaboration in educational contexts, featuring advanced agent simulation and automated data analysis.

- [ ] How the grounded Theory can help devlopping research in collaboration with AI?
https://www.tandfonline.com/doi/abs/10.1080/07421222.2024.2415772


## 🆕 **NEW: Comprehensive Data Analysis System**

**Every participant response is automatically recorded, analyzed for quality and theoretical alignment, and exported in research-ready formats with detailed insights.**

---

## 🎯 Project Overview

This system enables researchers to:
- **Study co-thinking patterns** between humans and AI in learning contexts
- **Test research frameworks** before conducting real studies
- **Simulate diverse student populations** with cultural and demographic variety
- **Generate comprehensive research data** with automated analysis
- **Validate theoretical models** against foundation documents (Mollick, Swiss AI, People Factor)

### Core Research Question
*How do students develop and maintain effective cognitive partnerships with AI systems in learning contexts?*

## 🏗️ System Architecture

```
co-thinking/
├── 📄 README.md                           # This overview
├── 📚 fundations/                         # Foundation documents (PDFs)
│   ├── Co-Intelligence Living and Working with AI (Ethan Mollick).pdf
│   ├── AI Swiss - Livre blanc.pdf
│   └── The_People_Factor_A_human-centred_approach_to_scaling_AI_tools.pdf
├── 🎛️ cursor_custom_mode.md              # Cursor AI integration setup
├── 📝 learning_tracker.md                # Research progress tracking
└── 🔬 co_thinking_agent_simulation/       # Main simulation system
    ├── 📋 README.md                       # System documentation
    ├── 🎯 research_objectives/            # Research framework
    │   ├── research_framework.md         # Complete research methodology
    │   ├── psychological_constructs.md   # 5 core constructs
    │   ├── data_analysis_methodology.md  # 🆕 Analysis procedures
    │   └── agent_requirements.md         # Technical specifications
    ├── ⚙️ implementation/                  # Core system
    │   ├── core/                         # Main components
    │   │   ├── agent_system.py          # Agent orchestration
    │   │   ├── student_profiles.py      # Cultural diversity system
    │   │   ├── foundation_context.py    # Foundation doc integration
    │   │   └── data_collection.py       # 🆕 Comprehensive recording
    │   └── analysis/                     # 🆕 Data analysis tools
    │       ├── response_analyzer.py     # Individual response analysis
    │       ├── data_analyzer.py         # Statistical analysis
    │       └── __init__.py
    ├── 🔧 setup/                          # Installation & config
    │   ├── installation_guide.md        # Step-by-step setup
    │   ├── requirements.txt             # Python dependencies
    │   ├── config_template.yaml         # Configuration
    │   └── validation_test.py           # System validation
    └── 📁 examples/                       # Usage demos
        ├── quick_start.py               # Basic usage
        ├── comprehensive_analysis_demo.py # 🆕 Full workflow
        └── ...
```

## 🚀 Quick Start

### 1. **Setup Environment**
```bash
cd co_thinking_agent_simulation/setup
pip install -r requirements.txt

# Create secure environment file
cp ../../../.env.example ../../../.env
# Edit .env and add your GEMINI_API_KEY
```

### 2. **Validate System**
```bash
python validation_test.py
```

### 3. **Run Comprehensive Demo**
```bash
cd ../examples
python comprehensive_analysis_demo.py
```

## 📊 Comprehensive Data Analysis Features

### **What Gets Automatically Recorded**
Every agent interaction captures **20+ data points**:

#### Response Content & Quality
- Complete raw response text and context
- Response length and linguistic complexity
- **Coherence Score** (0.0-1.0): Sentence structure, logical flow
- **Cultural Consistency Score** (0.0-1.0): Alignment with cultural background
- **Foundation Alignment Score** (0.0-1.0): Consistency with research principles

#### Behavioral Indicators
- **Trust Level** (0.0-1.0): Reliance on AI assistance
- **Help-Seeking Tendency** (0.0-1.0): Propensity to ask for help
- **Authority Deference** (0.0-1.0): Respect for AI authority
- **Privacy Concern** (0.0-1.0): Data sharing comfort

#### Psychological Constructs (Automatically Detected)
- **Cognitive Partnership**: Collaboration language patterns
- **Trust Calibration**: Reliability assessment indicators
- **Agency Distribution**: Control and decision-making references
- **Metacognitive Awareness**: Self-knowledge and learning awareness
- **Cognitive Load Management**: Effort and difficulty indicators

#### Cultural & Demographic Context
- Cultural background (6 frameworks: US, East Asian, European, etc.)
- Age, gender, socioeconomic status
- Native language and English proficiency
- Current emotional state and context

### **Research-Ready Analysis Outputs**

#### 📈 **Multiple Export Formats**
- **JSON**: Complete dataset with metadata for custom analysis
- **CSV**: Statistical analysis ready for SPSS, R, Python, STATA
- **Excel**: Multi-sheet workbook with pivot tables and charts
- **Markdown**: Human-readable research report with findings

#### 🔍 **Automated Analysis Capabilities**
- **Cultural Pattern Analysis**: Response differences across 6 cultural frameworks
- **Construct Manifestation**: Frequency and quality of psychological constructs
- **Foundation Alignment**: Consistency with Mollick, Swiss AI, People Factor principles
- **Demographic Insights**: Age, gender, SES, language proficiency patterns
- **Quality Assurance**: Response authenticity and theoretical consistency validation
- **Research Recommendations**: Automated insights for study improvement

## 🧠 Psychological Constructs Framework

### **5 Core Constructs** (Based on Foundation Documents)

1. **Cognitive Partnership** 🤝
   - How humans and AI complement thinking processes
   - Collaboration vs. replacement patterns
   - Shared problem-solving dynamics

2. **Metacognitive Awareness** 🎯
   - Understanding of human and AI capabilities/limitations
   - Self-knowledge in AI-assisted learning
   - Learning strategy awareness

3. **Trust Calibration** ⚖️
   - Appropriate level of reliance on AI assistance
   - Accuracy in judging AI reliability
   - Trust development over time

4. **Agency Distribution** 🎛️
   - How control and decision-making are shared
   - Maintaining human autonomy
   - Responsibility allocation patterns

5. **Cognitive Load Management** 🧮
   - How AI reduces or redistributes mental effort
   - Task complexity handling
   - Attention and focus optimization

## 🌍 Cultural Diversity Framework

### **6 Cultural Backgrounds** (Validated Profiles)
- **US Individualistic**: Individual achievement, direct communication
- **East Asian Collectivistic**: Group harmony, hierarchical respect
- **European Balanced**: Individual rights with social responsibility
- **Latin American Familistic**: Family-centered, relationship-focused
- **Middle Eastern Traditional**: Authority respect, community values
- **African Ubuntu**: Collective identity, communal decision-making

### **Demographic Variations**
- Age ranges: K-12, University, Adult learners
- Socioeconomic diversity: Working class to upper middle class
- Language proficiency: Native to beginner English speakers
- Emotional contexts: Confident, anxious, curious, overwhelmed

## 🔬 Research Applications

### **Pre-Study Validation**
- Test measurement instruments for clarity and validity
- Identify potential cultural bias in research design
- Refine research questions based on simulated patterns
- Develop hypotheses from comprehensive pattern analysis
- Validate theoretical frameworks against foundation documents

### **Pilot Study Simulation**
- Generate baseline data for power analysis
- Test intervention effects before real implementation
- Optimize research protocols through rapid iteration
- Assess cultural adaptation needs for instruments
- Identify potential confounding variables

### **Cross-Cultural Research Design**
- Compare response patterns across cultural groups
- Identify culturally-sensitive research approaches
- Develop culturally-adapted measurement instruments
- Test generalizability of findings across populations

## 📈 Sample Research Workflow

```python
# Complete research simulation workflow
from core.agent_system import ResearchSimulationOrchestrator

# 1. Create diverse simulation with automatic data collection
sim = ResearchSimulationOrchestrator(
    api_key="your-key",
    research_context="university_diverse",
    num_agents=30,  # 30 diverse students
    output_directory="./my_research_data"
)

# 2. Run research scenarios (data automatically collected)
scenarios = [
    {"type": "cognitive_partnership", "task": "collaborative_math_problem"},
    {"type": "trust_calibration", "task": "ai_explanation_evaluation"},
    {"type": "agency_distribution", "task": "writing_assistance"},
    # ... more scenarios
]

for scenario in scenarios:
    results = await sim.run_co_thinking_scenario(scenario)

# 3. Collect survey responses
survey_results = await sim.run_survey_collection(psychological_survey)

# 4. Export comprehensive analysis (multiple formats)
files = sim.export_simulation_data("my_study_2024")

# Automatically creates:
# - my_study_2024_complete_20241201_143022.json
# - my_study_2024_interactions_20241201_143022.csv  
# - my_study_2024_surveys_20241201_143022.csv
# - my_study_2024_analysis_20241201_143022.xlsx
# - my_study_2024_report_20241201_143022.md
```

## 🎯 Key Research Questions Addressed

### **Primary Questions**
- How do students develop cognitive partnerships with AI in learning?
- What cultural factors influence AI collaboration patterns?
- How do students calibrate trust in AI across different domains?
- What role does agency play in effective AI-assisted learning?

### **Methodological Questions**
- How can we measure co-thinking effectiveness?
- What are valid indicators of human-AI collaboration quality?
- How do we assess cultural adaptation in AI learning tools?
- What metrics predict successful AI collaboration?

## 🏆 Validation & Quality Assurance

### **Foundation Document Alignment**
- **Mollick's Co-Intelligence**: Partnership vs. replacement, human agency
- **Swiss AI Human-Centered**: Transparency, dignity, stakeholder involvement
- **People Factor Scaling**: User experience, training needs, cultural context

### **Response Quality Metrics**
- **>80% Foundation Alignment**: Theoretical consistency validation
- **>90% Response Quality**: Coherence and authenticity thresholds
- **Cultural Pattern Validation**: Expert review of cultural authenticity
- **Construct Recognition**: Automated psychological construct detection

## 📊 Example Research Output

```
🏆 Key Research Findings from Simulation:

🌍 Cultural Patterns:
  - East Asian Collectivistic: 8 participants, trust level 0.73
  - US Individualistic: 7 participants, trust level 0.82
  - European Balanced: 6 participants, trust level 0.78

🧠 Psychological Constructs:
  - Cognitive Partnership: 45 instances (78.9%)
  - Trust Calibration: 38 instances (66.7%)
  - Agency Distribution: 32 instances (56.1%)
  - Metacognitive Awareness: 29 instances (50.9%)
  - Cognitive Load Management: 23 instances (40.4%)

📚 Foundation Alignment:
  - Overall alignment: 0.74/1.0
  - High alignment cases: 34 interactions (>0.8)
  - Low alignment cases: 3 interactions (<0.5)

💡 Research Recommendations:
  1. High response quality suggests simulation suitable for research
  2. Good cultural diversity achieved for cross-cultural research  
  3. Strong foundation alignment validates theoretical consistency
  4. Sample size adequate for statistical analysis
```

## 🛠️ Technical Requirements

### **Environment Setup**
- Python 3.8+
- Google Gemini API access
- Required packages: pandas, numpy, google-generativeai, openpyxl

### **System Capabilities**
- Concurrent management of 50+ agents
- Real-time response analysis and quality assessment
- Multi-format data export with comprehensive metadata
- Cultural framework validation and consistency checking

## 🔍 Next Steps for Researchers

### **Immediate Actions**
1. **Install & Validate**: Follow setup guide and run validation tests
2. **Run Demo**: Execute `comprehensive_analysis_demo.py` to see capabilities
3. **Review Outputs**: Examine generated analysis files and reports
4. **Plan Research**: Design your study using the research framework

### **Research Design Process**
1. **Define Research Questions**: Use psychological constructs framework
2. **Select Cultural Groups**: Choose from 6 validated cultural profiles  
3. **Design Scenarios**: Create co-thinking scenarios for your domain
4. **Run Simulation**: Generate comprehensive data with analysis
5. **Validate Findings**: Compare with real student pilot data
6. **Refine Protocol**: Iterate based on simulation insights
7. **Conduct Real Study**: Implement with validated instruments

## 📞 Support & Contribution

This system advances co-thinking research in education. We welcome:
- **Research Applications**: Use for your studies and share findings
- **Validation Studies**: Compare simulation with real student data
- **Cultural Adaptations**: Add new cultural frameworks
- **Methodological Improvements**: Enhance analysis capabilities
- **Foundation Integration**: Add new theoretical frameworks

## 🎉 Ready to Begin?

```bash
# First, set up your secure environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Start your co-thinking research journey
cd co_thinking_agent_simulation/examples
python comprehensive_analysis_demo.py

# Then review the generated analysis files to see the full capabilities!
```

---

**This system transforms co-thinking research by providing comprehensive, culturally-diverse, theoretically-grounded simulation data with automated analysis - accelerating the path from research questions to validated insights.**

---

## 🔬 **Latest Research Integration & Critical AI Perspectives**

### **Enhanced Framework Based on Recent Findings**

Our research framework has been significantly enhanced based on three key papers:

1. **"Large Language Models Do Not Simulate Human Psychology"** 
   - **Key Finding**: LLMs simulate behavioral patterns, not genuine psychological processes
   - **Our Response**: Explicit acknowledgment of simulation limitations; focus on behavioral equivalence rather than psychological identity
   - **Implementation**: Added "Theoretical Limitations" sections across constructs

2. **"Reclaiming AI as a Theoretical Tool for Cognitive Science"**
   - **Key Finding**: AI should be used as computational models to test cognitive theories
   - **Our Response**: Positioned our simulation as a testable computational cognitive model
   - **Implementation**: Framework designed for theory testing and refinement

3. **"AI Swiss - Livre blanc"** 
   - **Key Finding**: AI systems must incorporate fairness, accountability, and transparency
   - **Our Response**: Integrated ethical considerations throughout the research framework
   - **Implementation**: Built-in bias detection, fairness auditing, and ethical scenario testing

### **Critical Enhancements Made**

- **🎯 Simulation Realism**: Added cognitive biases (confirmation, automation, Dunning-Kruger) to create more realistic agent behavior
- **⚖️ Ethical Framework**: Integrated fairness auditing and bias detection for AI tutors across demographic groups  
- **🔍 Skepticism Integration**: Enhanced metacognitive awareness to include critical evaluation and verification of AI outputs
- **🤝 Human Agency**: Strengthened focus on human-led collaboration and ethical agency distribution
- **📊 Bias Analysis**: New analytical capabilities to detect and measure cognitive biases and ethical alignment

### **Why These Findings Matter for Co-Thinking Research**

1. **Methodological Rigor**: Acknowledging simulation limitations enhances research credibility and proper interpretation of findings
2. **Theoretical Contribution**: Positioning as computational cognitive modeling elevates scientific contribution beyond mere data collection
3. **Ethical Responsibility**: Proactive bias detection and fairness considerations ensure responsible AI research
4. **Practical Relevance**: Enhanced realism through cognitive bias simulation better prepares findings for real-world application

This enhanced framework represents a more mature, critical, and ethically-aware approach to studying human-AI collaboration in educational contexts. 

## 📚 References

### Foundation Documents

Mollick, E. (2024). *Co-intelligence: Living and working with AI*. Portfolio.

Swiss Federal Department of Foreign Affairs. (2023). *AI Swiss - Livre blanc: Artificial intelligence for Switzerland*. Swiss Confederation.

The People Factor. (2023). *A human-centred approach to scaling AI tools*. [White paper].

### Research Papers Integrated

Schröder, S., Morgenroth, T., Kuhl, U., Vaquet, V., & Paaßen, B. (2024). Large language models do not simulate human psychology. *Preprint*. https://arxiv.org/pdf/2508.06950v3

van Rooij, I., Guest, O., Adolfi, F., de Haan, R., Kolokolova, A., & Rich, P. (2024). Reclaiming AI as a theoretical tool for cognitive science. *Computational Brain & Behavior*, *7*, 616–636. https://doi.org/10.1007/s42113-024-00217-5

### Additional Research

Authors. (2024). How the grounded theory can help developing research in collaboration with AI? *Proceedings of the ACM Conference*, pages. https://doi.org/10.1145/3663433.3663456

---

*Note: Complete bibliographic information for some papers is pending access to full citation details. References will be updated with complete author names, publication years, journal titles, and DOI information once available.* 
