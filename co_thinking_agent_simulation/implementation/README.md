# Co-Thinking Agent Simulation - Implementation Guide

## Overview

This directory contains the core implementation of the Co-Thinking Research Simulation System. The system uses Large Language Models to simulate diverse student populations for educational AI research.

## Architecture

### Core Components

#### `core/`
- **`agent_system.py`** - Main orchestration system managing multiple agents
- **`student_profiles.py`** - Enhanced student profile generation with cultural/demographic diversity
- **`foundation_context.py`** - Integration of foundation document principles
- **`data_collection.py`** - Data collection, processing, and export functionality

#### `scenarios/`
- **`educational_scenarios.py`** - Pre-built educational research scenarios
- **`construct_tests.py`** - Psychological construct testing scenarios
- **`validation_scenarios.py`** - System validation and quality control tests

#### `analysis/`
- **`response_analyzer.py`** - Agent response analysis and pattern detection
- **`foundation_validator.py`** - Foundation document alignment verification
- **`diversity_metrics.py`** - Cultural and demographic diversity analysis

## System Flow

```
1. INITIALIZATION
   ├── Load foundation document context
   ├── Create diverse student agent profiles
   ├── Initialize LLM connections
   └── Set up data collection systems

2. AGENT CREATION
   ├── Generate cultural profiles
   ├── Create demographic backgrounds
   ├── Build personality prompts
   └── Initialize individual agent instances

3. SCENARIO EXECUTION
   ├── Present learning tasks to agents
   ├── Collect agent responses
   ├── Validate response quality
   └── Store interaction data

4. DATA COLLECTION
   ├── Run surveys with agents
   ├── Collect behavioral data
   ├── Generate analysis metrics
   └── Export research data

5. ANALYSIS & VALIDATION
   ├── Analyze response patterns
   ├── Validate foundation alignment
   ├── Measure diversity metrics
   └── Generate research insights
```

## Key Features

### 🎯 Research Simulation
- **Multi-Agent System**: Manage 10-100+ simultaneous student agents
- **Diverse Profiles**: Cultural, linguistic, demographic, and emotional diversity
- **Realistic Behaviors**: Authentic responses based on psychological research
- **Scalable Architecture**: Concurrent processing with rate limiting

### 🧠 Psychological Constructs
- **Cognitive Partnership**: Human-AI collaboration patterns
- **Trust Calibration**: Appropriate reliance on AI assistance
- **Agency Distribution**: Control and decision-making dynamics
- **Metacognitive Awareness**: Understanding of AI capabilities/limitations
- **Cognitive Load Management**: Mental effort allocation

### 📚 Foundation Integration
- **Mollick's Co-Intelligence**: Cognitive partnership principles
- **Swiss AI Guidelines**: Human-centered design principles
- **People Factor Framework**: Human-centered scaling approaches
- **Validation System**: Ensures agent responses align with theoretical frameworks

### 🌍 Cultural Diversity
- **6 Cultural Templates**: US, East Asian, European, Latin American, Middle Eastern, African
- **Linguistic Profiles**: Native language, English proficiency, communication style
- **Communication Patterns**: High/low context, direct/indirect, hierarchical/egalitarian
- **Value Systems**: Individual vs. collective, authority relationships, technology adoption

## Usage Examples

### Basic Agent Creation
```python
from core.agent_system import ResearchSimulationOrchestrator

# Create simulation with diverse agents
sim = ResearchSimulationOrchestrator(
    api_key="your-gemini-api-key",
    research_context="university_diverse",
    num_agents=20
)

# Check diversity
diversity = sim._generate_diversity_summary()
print(f"Cultural distribution: {diversity['cultural_distribution']}")
```

### Running Research Scenarios
```python
# Define learning scenario
scenario = {
    "name": "Math Problem Solving",
    "type": "cognitive_partnership",
    "context": "Collaborative calculus problem solving",
    "learning_task": "Find the derivative of f(x) = x² + 3x + 2",
    "ai_tutor_response": "Let's use the power rule..."
}

# Execute scenario with all agents
result = await sim.run_co_thinking_scenario(scenario)
print(f"Collected {len(result['results'])} agent responses")
```

### Survey Data Collection
```python
# Define survey questions
survey = [
    {
        "question": "How comfortable are you with AI tutoring?",
        "type": "likert",
        "scale": "1-7"
    }
]

# Collect responses from all agents
responses = await sim.run_survey_collection(survey)
```

### Custom Profile Creation
```python
from core.student_profiles import create_diverse_research_cohort

# Create custom cohort
profiles = create_diverse_research_cohort(
    num_agents=50,
    research_context="university_diverse",
    custom_distributions={
        "cultural_templates": ["US_Individualistic", "East_Asian_Collectivistic"],
        "age_range": (18, 22),
        "ses_focus": ["Middle_Class", "Upper_Middle_Class"]
    }
)
```

## Configuration

### Environment Variables
```bash
export GEMINI_API_KEY="your-api-key-here"
export CO_THINKING_CONFIG_PATH="./config.yaml"
```

### Configuration File
```yaml
# config.yaml
simulation:
  default_agents: 20
  research_context: "university_diverse"
  rate_limit: 60

profiles:
  cultural_templates:
    - "US_Individualistic"
    - "East_Asian_Collectivistic"
    - "European_Balanced"
```

## Data Flow

### Input Data
- **Foundation Documents**: PDF files with theoretical frameworks
- **Research Scenarios**: JSON/YAML files with learning tasks
- **Survey Instruments**: Structured questionnaires
- **Agent Profiles**: Cultural, demographic, and psychological parameters

### Processing Pipeline
1. **Profile Generation**: Create diverse student backgrounds
2. **Context Integration**: Incorporate foundation document principles
3. **Prompt Engineering**: Build personality-aware prompts
4. **LLM Interaction**: Generate authentic responses
5. **Validation**: Check quality and theoretical alignment
6. **Data Collection**: Store structured research data

### Output Data
- **Agent Responses**: Detailed interaction logs
- **Survey Data**: Structured questionnaire responses
- **Behavioral Metrics**: Quantitative interaction patterns
- **Diversity Metrics**: Population representation analysis
- **Foundation Alignment**: Theoretical consistency scores

## Quality Assurance

### Response Validation
- **Length Checks**: Appropriate response length for age/context
- **Coherence Validation**: Logical and contextually appropriate responses
- **Cultural Consistency**: Responses align with agent's cultural background
- **Foundation Alignment**: Adherence to theoretical principles

### Diversity Validation
- **Population Representation**: Balanced cultural/demographic distribution
- **Behavioral Variance**: Realistic individual differences
- **Linguistic Authenticity**: Appropriate language use patterns
- **Emotional Consistency**: Stable emotional context within agents

### System Validation
- **API Reliability**: Consistent LLM service connectivity
- **Concurrent Processing**: Stable multi-agent management
- **Data Integrity**: Complete and accurate data collection
- **Export Functionality**: Reliable data export in multiple formats

## Performance Optimization

### API Efficiency
- **Rate Limiting**: Respects LLM service limits
- **Batch Processing**: Groups requests when possible
- **Async Operations**: Concurrent agent processing
- **Error Handling**: Robust retry mechanisms

### Memory Management
- **Profile Caching**: Efficient profile storage and retrieval
- **Response Streaming**: Process large response sets efficiently
- **Data Compression**: Optimized storage formats
- **Garbage Collection**: Cleanup of temporary objects

### Scalability
- **Configurable Concurrency**: Adjust based on system resources
- **Modular Architecture**: Add new components without system changes
- **Database Integration**: Support for persistent data storage
- **Distributed Processing**: Framework for multi-machine deployment

## Development Guidelines

### Code Structure
- **Type Hints**: Full type annotation for better IDE support
- **Documentation**: Comprehensive docstrings and comments
- **Error Handling**: Robust exception handling and logging
- **Testing**: Unit tests for all core components

### Adding New Features
1. **Profile Extensions**: Add new cultural/demographic dimensions
2. **Scenario Types**: Create new research scenario templates
3. **Analysis Tools**: Develop new data analysis capabilities
4. **Export Formats**: Add support for additional data formats

### Integration Points
- **LLM Providers**: Support for multiple AI services
- **Data Storage**: Integration with databases and cloud storage
- **Analysis Tools**: Connection to statistical analysis packages
- **Visualization**: Integration with plotting and dashboard tools

## Troubleshooting

### Common Issues
- **API Key Problems**: Verification and configuration
- **Rate Limiting**: Handling service limitations
- **Memory Issues**: Managing large simulations
- **Data Export**: Handling large datasets

### Debug Mode
```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Use test mode for development
sim = ResearchSimulationOrchestrator(
    api_key="your-key",
    num_agents=3,  # Small number for testing
    debug_mode=True
)
```

### Performance Monitoring
```python
# Track API usage and costs
sim.enable_cost_tracking()
sim.set_cost_limit(10.0)  # USD

# Monitor agent performance
sim.enable_performance_monitoring()
```

## Next Steps

1. **Run Examples**: Start with `../examples/quick_start.py`
2. **Custom Scenarios**: Create research scenarios for your study
3. **Profile Customization**: Adapt agent profiles to your population
4. **Data Analysis**: Use analysis tools to examine results
5. **Validation Studies**: Compare with real participant data

For detailed API documentation, see `../documentation/api_reference.md`
For research methodology guidance, see `../research_objectives/research_framework.md` 