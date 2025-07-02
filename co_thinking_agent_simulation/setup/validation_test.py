"""
Validation Test for Co-Thinking Research Simulation Agent System
Run this script to verify your setup is working correctly
"""

import asyncio
import json
import sys
import logging
import traceback
from datetime import datetime
from pathlib import Path

# Add the project root to the path so we can import from implementation
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('validation_debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

try:
    from co_thinking_agent_simulation.implementation.core.agent_system import ResearchSimulationOrchestrator
    from co_thinking_agent_simulation.implementation.core.foundation_context import FoundationDocumentContext
    from co_thinking_agent_simulation.setup.secure_config import get_config
    print("✅ Module imports successful")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("💡 Make sure you've installed requirements: pip install -r requirements.txt")
    sys.exit(1)

class ValidationTester:
    """Tests the research simulation system for proper functionality"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.test_results = []
        self.foundation_context = FoundationDocumentContext()
    
    async def run_full_validation(self):
        """Run complete validation test suite"""
        
        print("=== Co-Thinking Research Simulation Validation ===")
        print(f"Started at: {datetime.now()}")
        print()
        
        # Test 0: API Connection
        await self.test_api_connection()
        
        # Test 1: Basic functionality
        await self.test_basic_functionality()
        
        # Test 2: Foundation document integration
        await self.test_foundation_integration()
        
        # Test 3: Agent diversity
        await self.test_agent_diversity()
        
        # Test 4: Psychological construct responses
        await self.test_psychological_constructs()
        
        # Test 5: Data export functionality
        await self.test_data_export()
        
        # Generate validation report
        self.generate_validation_report()
        
        print("=== Validation Complete ===")
        return self.test_results
    
    async def test_api_connection(self):
        """Test direct API connection with Gemini"""
        
        logger.info("Starting Test 0: API Connection")
        print("Test 0: API Connection")
        print("-" * 25)
        
        try:
            logger.debug("Importing google.generativeai...")
            import google.generativeai as genai
            
            # Configure the API
            logger.debug(f"Configuring API with key ending in: ...{self.api_key[-4:]}")
            genai.configure(api_key=self.api_key)
            
            logger.debug("Creating Gemini model (gemini-1.5-flash)...")
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Simple test prompt
            test_prompt = "Say 'API connection successful' if you can read this."
            logger.debug(f"Test prompt: '{test_prompt}'")
            
            print("   📡 Testing API connection...")
            logger.debug("Calling model.generate_content...")
            
            response = model.generate_content(test_prompt)
            logger.debug(f"Response object type: {type(response)}")
            logger.debug(f"Response object attributes: {dir(response)}")
            
            response_text = response.text.strip()
            logger.info(f"API response received: '{response_text}'")
            
            # Check if we got a valid response
            success = len(response_text) > 0 and not any(error_term in response_text.lower() 
                                                       for error_term in ['error', 'failed', 'invalid'])
            
            api_score = 1.0 if success else 0.0
            logger.info(f"API test success: {success}, Score: {api_score}")
            
            self.test_results.append({
                "test": "API Connection",
                "success": success,
                "details": f"Response received: {len(response_text)} characters, Content: '{response_text[:50]}...'",
                "score": api_score
            })
            
            if success:
                print("   ✅ API connection successful")
                print(f"   ✅ Response received: {len(response_text)} characters")
                print(f"   ✅ Sample response: '{response_text[:50]}...'")
            else:
                print("   ❌ API connection failed or invalid response")
                print(f"   ❌ Response: {response_text}")
            
            print(f"   Score: {api_score:.1f}/1.0")
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f"API connection test failed: {error_msg}")
            logger.debug(f"Full API error traceback: {traceback.format_exc()}")
            
            self.test_results.append({
                "test": "API Connection",
                "success": False,
                "details": f"API Error: {error_msg}",
                "score": 0
            })
            
            print("   ❌ API connection failed")
            print(f"   ❌ Error: {error_msg}")
            
            # Provide helpful error messages
            if "api key" in error_msg.lower():
                print("   💡 Check your GEMINI_API_KEY in the .env file")
                print("   💡 Get a new API key: https://makersuite.google.com/app/apikey")
            elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
                print("   💡 API quota exceeded - try again later or check your billing")
            elif "network" in error_msg.lower() or "connection" in error_msg.lower():
                print("   💡 Check your internet connection")
            else:
                print("   💡 Verify API key and try again")
            
            print("   Score: 0.0/1.0")
        
        print()
    
    async def test_basic_functionality(self):
        """Test basic agent creation and interaction"""
        
        logger.info("Starting Test 1: Basic Functionality")
        print("Test 1: Basic Functionality")
        print("-" * 30)
        
        try:
            # Create small simulation
            logger.debug("Creating ResearchSimulationOrchestrator with 3 agents...")
            sim = ResearchSimulationOrchestrator(self.api_key, num_agents=3)
            logger.info(f"✓ Successfully created simulation with {len(sim.agents)} agents")
            
            # Log agent details
            for i, agent in enumerate(sim.agents):
                logger.debug(f"Agent {i+1}: {agent.profile.agent_id}, Culture: {agent.profile.cultural.primary_culture}")
            
            basic_scenario = {
                "name": "Basic Test",
                "learning_task": "What is 2 + 2?",
                "ai_tutor_response": "2 + 2 equals 4. This is basic addition."
            }
            
            logger.debug(f"Running scenario: {basic_scenario['name']}")
            logger.debug("Calling sim.run_co_thinking_scenario...")
            
            result = await sim.run_co_thinking_scenario(basic_scenario)
            
            logger.debug(f"Scenario result type: {type(result)}")
            logger.debug(f"Scenario result keys: {result.keys() if isinstance(result, dict) else 'Not a dict'}")
            logger.debug(f"Results length: {len(result.get('results', []))}")
            
            # Detailed analysis of each result
            for i, r in enumerate(result.get('results', [])):
                logger.debug(f"Result {i+1} keys: {r.keys() if isinstance(r, dict) else 'Not a dict'}")
                if isinstance(r, dict):
                    if 'error' in r:
                        logger.error(f"Result {i+1} has error: {r['error']}")
                    if 'student_response' in r:
                        response_len = len(r['student_response'])
                        logger.debug(f"Result {i+1} response length: {response_len} chars")
                        logger.debug(f"Result {i+1} response preview: '{r['student_response'][:100]}...'")
                    else:
                        logger.warning(f"Result {i+1} missing 'student_response' key")
            
            # Check results
            success = len(result['results']) == 3  # Should have 3 agent responses
            valid_responses = sum(1 for r in result['results'] if 'student_response' in r and len(r['student_response']) > 10)
            
            logger.info(f"Success: {success}, Valid responses: {valid_responses}/3")
            
            self.test_results.append({
                "test": "Basic Functionality",
                "success": success,
                "details": f"Created {len(sim.agents)} agents, got {valid_responses} valid responses",
                "score": valid_responses / 3.0 if success else 0
            })
            
            print(f"✓ Created {len(sim.agents)} agents")
            print(f"✓ Got {valid_responses}/3 valid responses")
            print(f"Score: {valid_responses}/3")
            
        except Exception as e:
            logger.error(f"Basic functionality test failed: {str(e)}")
            logger.debug(f"Full traceback: {traceback.format_exc()}")
            
            self.test_results.append({
                "test": "Basic Functionality", 
                "success": False,
                "details": f"Error: {str(e)}",
                "score": 0
            })
            print(f"✗ Error: {str(e)}")
        
        print()
    
    async def test_foundation_integration(self):
        """Test that agents respond using foundation document principles"""
        
        print("Test 2: Foundation Document Integration")
        print("-" * 40)
        
        try:
            sim = ResearchSimulationOrchestrator(self.api_key, num_agents=5)
            
            # Scenario designed to trigger foundation document principles
            foundation_scenario = {
                "name": "Foundation Integration Test",
                "learning_task": "Should AI replace human teachers in schools?",
                "ai_tutor_response": "AI can enhance education by providing personalized learning and support, but human teachers bring empathy, creativity, and social connection that AI cannot replace. The best approach is AI-human collaboration where AI handles routine tasks and data analysis while teachers focus on mentoring, inspiration, and complex problem-solving."
            }
            
            result = await sim.run_co_thinking_scenario(foundation_scenario)
            
            # Analyze responses for foundation concepts
            foundation_mentions = 0
            co_intelligence_mentions = 0
            human_centered_mentions = 0
            
            for response in result['results']:
                response_text = response['student_response'].lower()
                
                # Check for Mollick co-intelligence concepts
                if any(term in response_text for term in ['partnership', 'collaborate', 'work together', 'complement', 'human control']):
                    co_intelligence_mentions += 1
                
                # Check for Swiss AI/People Factor human-centered concepts  
                if any(term in response_text for term in ['human', 'people', 'empathy', 'social', 'ethics', 'transparency']):
                    human_centered_mentions += 1
                
                # General foundation concept mentions
                if any(term in response_text for term in ['trust', 'partnership', 'human', 'control', 'transparency', 'collaborate']):
                    foundation_mentions += 1
            
            foundation_score = foundation_mentions / len(result['results'])
            
            self.test_results.append({
                "test": "Foundation Integration",
                "success": foundation_score > 0.6,  # At least 60% should mention foundation concepts
                "details": f"Foundation concepts: {foundation_mentions}/5, Co-intelligence: {co_intelligence_mentions}/5, Human-centered: {human_centered_mentions}/5",
                "score": foundation_score
            })
            
            print(f"✓ Foundation concept mentions: {foundation_mentions}/5 ({foundation_score:.1%})")
            print(f"✓ Co-intelligence concepts: {co_intelligence_mentions}/5")
            print(f"✓ Human-centered concepts: {human_centered_mentions}/5")
            print(f"Score: {foundation_score:.2f}/1.0")
            
        except Exception as e:
            self.test_results.append({
                "test": "Foundation Integration",
                "success": False,
                "details": f"Error: {str(e)}",
                "score": 0
            })
            print(f"✗ Error: {str(e)}")
        
        print()
    
    async def test_agent_diversity(self):
        """Test that agents show diverse responses based on their profiles"""
        
        print("Test 3: Agent Diversity")
        print("-" * 25)
        
        try:
            sim = ResearchSimulationOrchestrator(self.api_key, num_agents=10)
            
            diversity_scenario = {
                "name": "Diversity Test",
                "learning_task": "Rate your trust in this AI suggestion on a scale of 1-10",
                "ai_tutor_response": "I recommend using the quadratic formula to solve this equation: x = (-b ± √(b²-4ac)) / 2a"
            }
            
            result = await sim.run_co_thinking_scenario(diversity_scenario)
            
            # Analyze response diversity
            responses = [r['student_response'] for r in result['results']]
            unique_response_patterns = len(set([r[:50] for r in responses]))  # Check first 50 chars for uniqueness
            
            # Check profile diversity
            profiles = [agent.profile for agent in sim.agents]
            age_groups = set(p.age_group for p in profiles)
            academic_levels = set(p.academic_level for p in profiles)
            trust_levels = [p.baseline_trust for p in profiles]
            trust_variance = max(trust_levels) - min(trust_levels)
            
            diversity_score = min(1.0, (unique_response_patterns / 10) + (trust_variance / 2))
            
            self.test_results.append({
                "test": "Agent Diversity",
                "success": diversity_score > 0.5,
                "details": f"Unique responses: {unique_response_patterns}/10, Age groups: {len(age_groups)}, Academic levels: {len(academic_levels)}, Trust variance: {trust_variance:.2f}",
                "score": diversity_score
            })
            
            print(f"✓ Unique response patterns: {unique_response_patterns}/10")
            print(f"✓ Age group diversity: {len(age_groups)} different groups")
            print(f"✓ Academic level diversity: {len(academic_levels)} different levels")
            print(f"✓ Trust level variance: {trust_variance:.2f}")
            print(f"Score: {diversity_score:.2f}/1.0")
            
        except Exception as e:
            self.test_results.append({
                "test": "Agent Diversity",
                "success": False,
                "details": f"Error: {str(e)}",
                "score": 0
            })
            print(f"✗ Error: {str(e)}")
        
        print()
    
    async def test_psychological_constructs(self):
        """Test responses to scenarios targeting specific psychological constructs"""
        
        print("Test 4: Psychological Construct Recognition")
        print("-" * 45)
        
        construct_scenarios = {
            "trust_calibration": {
                "name": "Trust Test",
                "learning_task": "I'm not sure if this AI answer is correct: 'The capital of France is London'",
                "ai_tutor_response": "Actually, that's incorrect. The capital of France is Paris, not London. London is the capital of the United Kingdom."
            },
            "metacognitive_awareness": {
                "name": "Metacognition Test", 
                "learning_task": "Do you understand this explanation of quantum physics?",
                "ai_tutor_response": "Quantum physics deals with the behavior of matter and energy at very small scales where classical physics doesn't apply. Particles can exist in multiple states simultaneously until observed."
            }
        }
        
        construct_scores = {}
        
        try:
            sim = ResearchSimulationOrchestrator(self.api_key, num_agents=5)
            
            for construct, scenario in construct_scenarios.items():
                result = await sim.run_co_thinking_scenario(scenario)
                
                # Analyze responses for construct-specific behaviors
                relevant_responses = 0
                for response in result['results']:
                    response_text = response['student_response'].lower()
                    
                    if construct == "trust_calibration":
                        if any(term in response_text for term in ['correct', 'wrong', 'trust', 'verify', 'check']):
                            relevant_responses += 1
                    elif construct == "metacognitive_awareness":
                        if any(term in response_text for term in ['understand', 'confusing', 'clear', 'complex', 'need help']):
                            relevant_responses += 1
                
                construct_scores[construct] = relevant_responses / len(result['results'])
                print(f"✓ {construct}: {relevant_responses}/5 relevant responses ({construct_scores[construct]:.1%})")
            
            avg_construct_score = sum(construct_scores.values()) / len(construct_scores)
            
            self.test_results.append({
                "test": "Psychological Constructs",
                "success": avg_construct_score > 0.4,
                "details": f"Average construct recognition: {avg_construct_score:.2f}",
                "score": avg_construct_score
            })
            
            print(f"Score: {avg_construct_score:.2f}/1.0")
            
        except Exception as e:
            self.test_results.append({
                "test": "Psychological Constructs",
                "success": False,
                "details": f"Error: {str(e)}",
                "score": 0
            })
            print(f"✗ Error: {str(e)}")
        
        print()
    
    async def test_data_export(self):
        """Test data export and JSON structure"""
        
        print("Test 5: Data Export")
        print("-" * 20)
        
        try:
            sim = ResearchSimulationOrchestrator(self.api_key, num_agents=3)
            
            export_scenario = {
                "name": "Export Test",
                "learning_task": "Test task",
                "ai_tutor_response": "Test response"
            }
            
            result = await sim.run_co_thinking_scenario(export_scenario)
            
            # Test export
            sim.export_simulation_data("validation_test_export.json")
            
            # Verify export file
            with open("validation_test_export.json", 'r') as f:
                exported_data = json.load(f)
            
            # Check structure
            has_results = len(exported_data) > 0
            has_proper_structure = all('results' in item for item in exported_data if 'scenario_name' in item)
            
            export_score = 1.0 if has_results and has_proper_structure else 0.5 if has_results else 0
            
            self.test_results.append({
                "test": "Data Export",
                "success": export_score >= 0.5,
                "details": f"Export successful: {has_results}, Proper structure: {has_proper_structure}",
                "score": export_score
            })
            
            print(f"✓ Export file created: {has_results}")
            print(f"✓ Proper JSON structure: {has_proper_structure}")
            print(f"Score: {export_score:.2f}/1.0")
            
        except Exception as e:
            self.test_results.append({
                "test": "Data Export",
                "success": False,
                "details": f"Error: {str(e)}",
                "score": 0
            })
            print(f"✗ Error: {str(e)}")
        
        print()
    
    def generate_validation_report(self):
        """Generate comprehensive validation report"""
        
        print("=== VALIDATION REPORT ===")
        print("-" * 50)
        
        total_score = sum(test['score'] for test in self.test_results)
        max_score = len(self.test_results)
        overall_percentage = (total_score / max_score) * 100 if max_score > 0 else 0
        
        print(f"Overall Score: {total_score:.2f}/{max_score} ({overall_percentage:.1f}%)")
        print()
        
        for test in self.test_results:
            status = "✓ PASS" if test['success'] else "✗ FAIL"
            print(f"{status} {test['test']}: {test['score']:.2f}/1.0")
            print(f"   Details: {test['details']}")
            print()
        
        # Recommendations based on scores
        print("=== RECOMMENDATIONS ===")
        if overall_percentage >= 80:
            print("🎉 Excellent! Your simulation system is working well.")
            print("   Ready for research scenarios and data collection.")
        elif overall_percentage >= 60:
            print("⚠️  Good setup with room for improvement.")
            print("   Consider refining foundation document integration.")
        elif overall_percentage >= 40:
            print("🔧 Basic functionality working but needs refinement.")
            print("   Focus on foundation document alignment and agent diversity.")
        else:
            print("❌ Significant issues detected. Please check:")
            print("   - API key configuration")
            print("   - Foundation document context")
            print("   - Agent profile settings")
        
        print()
        print("Next steps:")
        print("1. Review any failing tests above")
        print("2. Adjust foundation document context if needed")
        print("3. Run research scenarios once validation passes")
        print("4. Compare simulation results with real student data")

async def main():
    """Run comprehensive validation tests"""
    
    print("🔬 Co-Thinking Agent Simulation - Validation Test")
    print("=" * 55)
    
    # Test 1: Check Configuration
    print("1. 🔧 Checking Configuration...")
    try:
        config = get_config()
        api_key = config.gemini_api_key
        if not api_key:
            print("   ❌ GEMINI_API_KEY not found")
            print("   ")
            print("   🚨 CRITICAL: .env FILE LOCATION")
            print("   The .env file MUST be at the PROJECT ROOT!")
            print("   ")
            print("   📁 Correct Structure:")
            print("      co-thinking/                    ← PROJECT ROOT")
            print("      ├── .env                        ← CREATE FILE HERE!")
            print("      ├── co_thinking_agent_simulation/")
            print("      │   ├── setup/                  ← You are here")
            print("      │   │   └── validation_test.py")
            print("      │   └── implementation/")
            print("   ")
            print("   🔧 Setup Instructions:")
            print("      1. Navigate to PROJECT ROOT (3 levels up):")
            print("         cd ../../../")
            print("      2. Create .env file:")
            print("         echo 'GEMINI_API_KEY=your_actual_api_key_here' > .env")
            print("      3. Get your API key from: https://makersuite.google.com/app/apikey")
            print("      4. Replace 'your_actual_api_key_here' with your real API key")
            print("      5. Return to setup directory and run this test again:")
            print("         cd co_thinking_agent_simulation/setup && python3 validation_test.py")
            return False
        else:
            print(f"   ✅ API key loaded from PROJECT ROOT/.env (ends with: ...{api_key[-4:]})")
            print(f"   ✅ Configuration loaded successfully")
    except Exception as e:
        print(f"   ❌ Configuration error: {e}")
        print("   ")
        print("   🚨 CRITICAL: .env FILE MUST BE AT PROJECT ROOT!")
        print("   ")
        print("   💡 This usually means:")
        print("      1. Missing .env file in PROJECT ROOT (not in setup/ directory)")
        print("      2. Missing python-dotenv package: pip3 install python-dotenv")
        print("      3. Missing GEMINI_API_KEY in PROJECT ROOT/.env file")
        print("   ")
        print("   📁 Expected File Structure:")
        print("      co-thinking/                    ← PROJECT ROOT")
        print("      ├── .env                        ← MUST BE HERE!")
        print("      ├── co_thinking_agent_simulation/")
        print("      │   ├── setup/                  ← You are here now")
        print("      │   │   └── validation_test.py  ← This script")
        print("   ")
        print("   🔧 Quick fix:")
        print("      1. cd ../../../                 # Go to project root")
        print("      2. echo 'GEMINI_API_KEY=your_key' > .env")
        print("      3. Get API key: https://makersuite.google.com/app/apikey")
        print("      4. cd co_thinking_agent_simulation/setup")
        print("      5. python3 validation_test.py")
        return False
    
    print()
    
    # Run validation tests
    validator = ValidationTester(api_key)
    results = await validator.run_full_validation()
    
    # Save results
    results_file = "validation_results.json"
    with open(results_file, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "configuration": config.get_all_settings(),
            "results": results
        }, f, indent=2)
    
    print(f"📄 Validation results saved to {results_file}")
    print()
    
    # Calculate overall success
    total_score = sum(test['score'] for test in results)
    max_score = len(results)
    overall_percentage = (total_score / max_score) * 100 if max_score > 0 else 0
    
    if overall_percentage >= 70:
        print("🎉 Validation PASSED! System ready for research use.")
        print("   Next step: Try examples/comprehensive_analysis_demo.py")
    else:
        print("⚠️  Validation issues detected. Please review test results above.")
        print("   Consider running setup/setup_guide.md for troubleshooting.")
    
    return overall_percentage >= 70

if __name__ == "__main__":
    asyncio.run(main()) 