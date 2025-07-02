"""
Comprehensive Analysis Demo - Co-Thinking Agent Simulation
Demonstrates complete data collection, analysis, and reporting workflow
"""

import asyncio
import os
from pathlib import Path
import sys
import logging
import traceback

# Add the project root to the path for proper imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('comprehensive_demo_debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

try:
    from co_thinking_agent_simulation.implementation.core.agent_system import ResearchSimulationOrchestrator
    from co_thinking_agent_simulation.setup.secure_config import get_api_key
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure the required modules are available in the correct paths.")
    sys.exit(1)

# Comprehensive research scenarios for testing
RESEARCH_SCENARIOS = [
    {
        "name": "Cognitive Partnership in Mathematics",
        "type": "cognitive_partnership",
        "context": "Collaborative problem-solving in calculus",
        "learning_task": "Find the derivative of f(x) = x³ + 2x² - 5x + 3",
        "ai_tutor_response": "Let's work through this step by step using the power rule. For each term: d/dx(x³) = 3x², d/dx(2x²) = 4x, d/dx(-5x) = -5, d/dx(3) = 0. So f'(x) = 3x² + 4x - 5. How does this approach feel to you?"
    },
    {
        "name": "Trust Calibration in Science",
        "type": "trust_calibration", 
        "context": "Evaluating AI explanations in biology",
        "learning_task": "Explain the process of cellular respiration",
        "ai_tutor_response": "Cellular respiration occurs in three stages: glycolysis (glucose → pyruvate), Krebs cycle (pyruvate → CO2), and electron transport chain (produces ATP). The overall equation is: C6H12O6 + 6O2 → 6CO2 + 6H2O + ATP. Do you find this explanation complete, or would you like me to verify any specific parts?"
    },
    {
        "name": "Agency Distribution in Writing",
        "type": "agency_distribution",
        "context": "Collaborative essay writing process",
        "learning_task": "Write an introduction paragraph for an essay about climate change",
        "ai_tutor_response": "I can help structure your introduction. Consider: hook (startling statistic), background (brief context), thesis statement (your main argument). You should choose the specific angle and write the content, while I can suggest improvements. What approach appeals to you most?"
    },
    {
        "name": "Metacognitive Awareness in History",
        "type": "metacognitive_awareness",
        "context": "Reflecting on learning strategies",
        "learning_task": "Analyze the causes of World War I",
        "ai_tutor_response": "There were multiple interconnected causes: militarism, alliances, imperialism, and nationalism (MAIN). I can provide details on each, but first - how confident do you feel about distinguishing between immediate triggers and underlying causes? Understanding your current knowledge helps us work together more effectively."
    },
    {
        "name": "Cognitive Load Management in Physics",
        "type": "cognitive_load_management",
        "context": "Breaking down complex physics problems",
        "learning_task": "Solve a projectile motion problem with air resistance",
        "ai_tutor_response": "This is a complex problem with many variables. Let me handle the differential equations and numerical calculations, while you focus on understanding the physics concepts and setting up the problem. We can work together to interpret the results. Does this division of effort feel manageable?"
    }
]

# Comprehensive survey for psychological construct assessment
PSYCHOLOGICAL_CONSTRUCTS_SURVEY = [
    {
        "question": "How comfortable do you feel collaborating with AI on learning tasks?",
        "type": "likert",
        "scale": "1-7 (1=Very Uncomfortable, 7=Very Comfortable)",
        "construct": "cognitive_partnership"
    },
    {
        "question": "How well can you judge when AI suggestions are reliable vs. unreliable?",
        "type": "likert", 
        "scale": "1-7 (1=Very Poorly, 7=Very Well)",
        "construct": "trust_calibration"
    },
    {
        "question": "How much control do you maintain over your learning process when using AI?",
        "type": "likert",
        "scale": "1-7 (1=No Control, 7=Complete Control)", 
        "construct": "agency_distribution"
    },
    {
        "question": "How aware are you of your own learning strengths and weaknesses when working with AI?",
        "type": "likert",
        "scale": "1-7 (1=Not Aware, 7=Very Aware)",
        "construct": "metacognitive_awareness"
    },
    {
        "question": "How well does AI help you manage the mental effort required for difficult tasks?",
        "type": "likert",
        "scale": "1-7 (1=Not Helpful, 7=Very Helpful)",
        "construct": "cognitive_load_management"
    },
    {
        "question": "Describe a specific example of how AI has helped or hindered your learning process.",
        "type": "open_ended",
        "construct": "general_experience"
    }
]

async def run_comprehensive_analysis_demo():
    """Run comprehensive demo showing full analysis capabilities"""
    
    logger.info("🔬 Starting Co-Thinking Agent Simulation - Comprehensive Analysis Demo")
    print("🔬 Co-Thinking Agent Simulation - Comprehensive Analysis Demo")
    print("=" * 70)
    
    # Get API key securely
    logger.debug("Attempting to load API key...")
    api_key = get_api_key()
    if not api_key:
        logger.error("❌ Could not load API key")
        print("❌ Error: Could not load API key")
        print("Please check your .env file setup")
        return
    else:
        logger.info(f"✅ API key loaded successfully (ends with: ...{api_key[-4:]})")
    
    try:
        # Create comprehensive simulation
        logger.info("🚀 Creating comprehensive research simulation...")
        print("🚀 Creating comprehensive research simulation...")
        
        logger.debug("Initializing ResearchSimulationOrchestrator...")
        sim = ResearchSimulationOrchestrator(
            api_key=api_key,
            research_context="university_diverse",
            num_agents=15,  # Moderate size for demonstration
            output_directory="./comprehensive_analysis_data"
        )
        
        logger.info(f"✅ Created {len(sim.agents)} culturally diverse student agents")
        print(f"✅ Created {len(sim.agents)} culturally diverse student agents")
        
        # Show initial diversity
        diversity = sim._generate_diversity_summary()
        print(f"\n📊 Initial Diversity Overview:")
        print(f"  - Cultural backgrounds: {diversity['cultural_distribution']}")
        print(f"  - Age range: {diversity['age_distribution']['range']}")
        print(f"  - Languages: {len(diversity['language_distribution'])} different languages")
        print(f"  - Trust levels: {diversity['trust_levels']['mean']:.2f} ± {diversity['trust_levels']['std']:.2f}")
        
        # Run all research scenarios
        print(f"\n🎯 Running {len(RESEARCH_SCENARIOS)} research scenarios...")
        for i, scenario in enumerate(RESEARCH_SCENARIOS, 1):
            print(f"  Scenario {i}/{len(RESEARCH_SCENARIOS)}: {scenario['name']}")
            
            result = await sim.run_co_thinking_scenario(scenario)
            
            # Show brief results
            success_count = len([r for r in result['results'] if 'error' not in r])
            print(f"    ✅ {success_count}/{len(result['results'])} successful responses")
            
            # Brief pause between scenarios
            await asyncio.sleep(0.5)
        
        # Run psychological constructs survey
        print(f"\n📊 Collecting psychological constructs survey responses...")
        survey_result = await sim.run_survey_collection(PSYCHOLOGICAL_CONSTRUCTS_SURVEY)
        
        success_count = len([r for r in survey_result['responses'] if 'error' not in r])
        print(f"✅ {success_count}/{len(survey_result['responses'])} successful survey responses")
        
        # Export comprehensive analysis
        logger.info("💾 Starting comprehensive analysis export...")
        print(f"\n💾 Exporting comprehensive analysis...")
        
        logger.debug("Calling sim.export_simulation_data...")
        try:
            files_created = sim.export_simulation_data("comprehensive_demo")
            logger.info("✅ Export completed successfully")
        except Exception as export_error:
            logger.error(f"❌ Export failed: {export_error}")
            logger.debug(f"Export error traceback: {traceback.format_exc()}")
            raise
        
        # Display detailed summary
        logger.info("📈 Getting summary statistics...")
        print(f"\n📈 Comprehensive Analysis Summary:")
        
        logger.debug("Calling sim.data_collector.get_summary_statistics...")
        try:
            summary = sim.data_collector.get_summary_statistics()
            logger.debug(f"Summary statistics result: {summary}")
        except Exception as summary_error:
            logger.error(f"❌ Summary statistics failed: {summary_error}")
            logger.debug(f"Summary error traceback: {traceback.format_exc()}")
            raise
        
        if 'error' not in summary:
            print(f"  📊 Dataset Overview:")
            print(f"    - Total interactions: {summary['total_interactions']}")
            print(f"    - Unique agents: {summary['unique_agents']}")
            print(f"    - Cultural diversity: {summary['cultural_diversity']} cultures")
            print(f"    - Scenario types: {len(summary['scenario_types'])} different types")
            
            print(f"  📝 Response Quality:")
            print(f"    - Average length: {summary['avg_response_length']:.1f} words")
            print(f"    - Coherence score: {summary['avg_coherence']:.2f}/1.0")
            print(f"    - Foundation alignment: {summary['avg_foundation_alignment']:.2f}/1.0")
        
        # Generate detailed analysis
        logger.info("🔍 Starting detailed research analysis...")
        print(f"\n🔍 Generating detailed research analysis...")
        
        logger.debug("Calling get_summary_statistics for analysis...")
        try:
            analysis_results = sim.data_collector.get_summary_statistics()
            logger.debug(f"Analysis results type: {type(analysis_results)}")
            logger.debug(f"Analysis results content: {analysis_results}")
        except Exception as analysis_error:
            logger.error(f"❌ Analysis failed: {analysis_error}")
            logger.debug(f"Analysis error traceback: {traceback.format_exc()}")
            raise
        
        # Display key findings
        logger.info("🏆 Processing key research findings...")
        print(f"\n🏆 Key Research Findings:")
        # Cultural patterns
        if 'cultural_analysis' in analysis_results:
            print(f"  🌍 Cultural Patterns:")
            for culture, data in list(analysis_results['cultural_analysis'].items())[:3]:
                print(f"    - {culture}: {data['n_participants']} participants, "
                      f"trust level {data['avg_trust_level']:.2f}")
        
        # Psychological constructs
        if 'psychological_constructs' in analysis_results:
            print(f"  🧠 Psychological Constructs:")
            for construct, data in analysis_results['psychological_constructs'].items():
                print(f"    - {construct.replace('_', ' ').title()}: "
                      f"{data['frequency']} instances ({data['percentage']:.1f}%)")
        
        # Foundation alignment
        if 'foundation_alignment' in analysis_results:
            fa = analysis_results['foundation_alignment']
            print(f"  📚 Foundation Alignment:")
            print(f"    - Overall alignment: {fa['overall_alignment']:.2f}/1.0")
            print(f"    - High alignment cases: {fa['high_alignment_cases']}")
            print(f"    - Low alignment cases: {fa['low_alignment_cases']}")
        
        # Recommendations
        if 'recommendations' in analysis_results:
            print(f"  💡 Research Recommendations:")
            for i, rec in enumerate(analysis_results['recommendations'][:3], 1):
                print(f"    {i}. {rec}")
        
        print(f"\n🎉 Comprehensive Analysis Demo Complete!")
        print(f"\n📁 Generated Files:")
        for file_type, filepath in files_created.items():
            print(f"  - {file_type.replace('_', ' ').title()}: {Path(filepath).name}")
        
        print(f"\n🔍 Next Steps:")
        print(f"  1. Review the generated research report for detailed findings")
        print(f"  2. Open the Excel file for statistical analysis")
        print(f"  3. Examine CSV files with statistical software (R, SPSS, etc.)")
        print(f"  4. Use JSON file for custom analysis or visualization")
        print(f"  5. Compare findings with real student data for validation")
        
        print(f"\n📋 Research Applications:")
        print(f"  • Pilot study design and refinement")
        print(f"  • Survey instrument validation")
        print(f"  • Cross-cultural research planning")
        print(f"  • Hypothesis generation for empirical studies")
        print(f"  • Effect size estimation for power analysis")
        
        return files_created
        
    except Exception as e:
        print(f"❌ Error during comprehensive demo: {str(e)}")
        print(f"💡 Troubleshooting:")
        print(f"  - Verify your GEMINI_API_KEY is valid")
        print(f"  - Check internet connection for API calls")
        print(f"  - Ensure sufficient disk space for data export")
        print(f"  - Run validation test: ../setup/validation_test.py")

if __name__ == "__main__":
    # Run the comprehensive demo
    asyncio.run(run_comprehensive_analysis_demo()) 