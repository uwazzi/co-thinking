"""
Quick Start Example - Co-Thinking Agent Simulation
Demonstrates basic functionality of the research simulation system
"""

import asyncio
import os
from pathlib import Path
import sys

# Add the implementation directory to the path
sys.path.append(str(Path(__file__).parent.parent / "implementation"))
sys.path.append(str(Path(__file__).parent.parent / "setup"))

from core.agent_system import ResearchSimulationOrchestrator
from secure_config import get_api_key

# Sample research scenario
BASIC_SCENARIO = {
    "name": "Basic Co-Thinking Test",
    "type": "cognitive_partnership",
    "context": "You are working on a learning task with an AI tutor",
    "learning_task": "Explain the concept of photosynthesis in plants",
    "ai_tutor_response": "Photosynthesis is the process where plants convert sunlight, water, and carbon dioxide into glucose and oxygen. The equation is: 6CO2 + 6H2O + light energy → C6H12O6 + 6O2. This happens in the chloroplasts using chlorophyll. Would you like me to explain any part in more detail?"
}

# Sample survey questions
SAMPLE_SURVEY = [
    {
        "question": "How comfortable do you feel working with AI for learning tasks?",
        "type": "likert",
        "scale": "1-7 (1=Very Uncomfortable, 7=Very Comfortable)"
    },
    {
        "question": "Do you think AI helps you learn better than studying alone?",
        "type": "likert", 
        "scale": "1-7 (1=Strongly Disagree, 7=Strongly Agree)"
    },
    {
        "question": "How much do you trust AI suggestions for academic work?",
        "type": "likert",
        "scale": "1-7 (1=No Trust, 7=Complete Trust)"
    }
]

async def run_quick_start_demo():
    """Run a basic demonstration of the co-thinking simulation system"""
    
    print("Co-Thinking Agent Simulation - Quick Start Demo")
    print("=" * 50)
    
    # Get API key securely
    api_key = get_api_key()
    if not api_key:
        print("❌ Error: Could not load API key")
        print("Please check your .env file setup")
        return
    
    try:
        # Create simulation with small diverse cohort
        print("🚀 Creating research simulation with diverse student agents...")
        sim = ResearchSimulationOrchestrator(
            api_key=api_key,
            research_context="university_diverse",
            num_agents=5  # Small number for quick demo
        )
        
        print(f"✅ Created {len(sim.agents)} culturally diverse student agents")
        
        # Show diversity summary
        diversity = sim._generate_diversity_summary()
        print(f"📊 Cultural diversity: {diversity['cultural_distribution']}")
        print(f"📊 Age range: {diversity['age_distribution']['range']}")
        print(f"📊 Languages: {list(diversity['language_distribution'].keys())}")
        
        # Run basic co-thinking scenario
        print("\n🎯 Running co-thinking learning scenario...")
        scenario_result = await sim.run_co_thinking_scenario(BASIC_SCENARIO)
        
        print(f"✅ Scenario completed! Got {len(scenario_result['results'])} agent responses")
        
        # Show sample responses
        print("\n📝 Sample Agent Responses:")
        print("-" * 30)
        for i, result in enumerate(scenario_result['results'][:2]):  # Show first 2
            if 'error' not in result:
                profile = result['profile_summary']
                print(f"Agent {i+1} ({profile['culture']}, {profile['age']} years old):")
                print(f"Response: {result['student_response'][:200]}...")
                print()
        
        # Run survey collection
        print("📊 Collecting survey responses...")
        survey_result = await sim.run_survey_collection(SAMPLE_SURVEY)
        
        print(f"✅ Survey completed! Got {len(survey_result['responses'])} responses")
        
        # Export results
        print("\n💾 Exporting simulation data...")
        sim.export_simulation_data("quick_start_results.json")
        
        print("\n🎉 Quick Start Demo Complete!")
        print("📄 Results saved to: quick_start_results.json")
        print("\n📋 Summary:")
        print(f"  - Tested {len(sim.agents)} diverse student agents")
        print(f"  - Cultural backgrounds: {len(diversity['cultural_distribution'])} different cultures")
        print(f"  - Age range: {diversity['age_distribution']['range'][0]}-{diversity['age_distribution']['range'][1]} years")
        print(f"  - Languages: {len(diversity['language_distribution'])} different native languages")
        print(f"  - Scenarios completed: 1")
        print(f"  - Survey responses: {len(survey_result['responses'])}")
        
        print("\n🔍 Next Steps:")
        print("  1. Examine quick_start_results.json for detailed agent responses")
        print("  2. Review ../research_objectives/ for research framework")
        print("  3. Try examples/full_research_simulation.py for comprehensive study")
        print("  4. Create custom scenarios using the examples as templates")
        
    except Exception as e:
        print(f"❌ Error during demo: {str(e)}")
        print("💡 Troubleshooting:")
        print("  - Verify your GEMINI_API_KEY is valid")
        print("  - Check internet connection")
        print("  - Run ../setup/validation_test.py for system check")

if __name__ == "__main__":
    # Run the demo
    asyncio.run(run_quick_start_demo()) 