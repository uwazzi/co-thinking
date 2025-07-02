"""
Co-Thinking Research Simulation Agent System
Main agent orchestration and management system
"""

import json
import random
import sys
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
from datetime import datetime
import asyncio
import pandas as pd
from pathlib import Path

# You'll need to install: pip install google-generativeai pandas python-dotenv

import google.generativeai as genai

# Import from absolute paths to avoid relative import issues
try:
    from co_thinking_agent_simulation.implementation.core.student_profiles import EnhancedStudentProfile, create_diverse_research_cohort
    from co_thinking_agent_simulation.implementation.core.foundation_context import FoundationDocumentContext
    from co_thinking_agent_simulation.implementation.core.data_collection import ComprehensiveDataCollector
except ImportError:
    # Fallback for direct execution - add current directory to path first
    import sys
    from pathlib import Path
    current_dir = Path(__file__).parent
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))
    from student_profiles import EnhancedStudentProfile, create_diverse_research_cohort
    from foundation_context import FoundationDocumentContext
    from data_collection import ComprehensiveDataCollector

# Try to import secure configuration
try:
    from co_thinking_agent_simulation.setup.secure_config import get_api_key, SecureConfig
    SECURE_CONFIG_AVAILABLE = True
except ImportError:
    # Fallback for direct execution - avoid Path scoping conflicts
    try:
        # Use intermediate variables to avoid Path scoping issues
        current_file_path = Path(__file__)
        setup_dir = current_file_path.parent.parent.parent / "setup"
        sys.path.append(str(setup_dir))
        from secure_config import get_api_key, SecureConfig
        SECURE_CONFIG_AVAILABLE = True
    except ImportError:
        SECURE_CONFIG_AVAILABLE = False
        print("💡 Secure config not available. Pass api_key parameter or install python-dotenv and set up .env file")
    except Exception as e:
        SECURE_CONFIG_AVAILABLE = False
        print(f"⚠️  Error setting up secure config: {e}")
        print("💡 Falling back to manual API key parameter")

class StudentAgent:
    """Individual student simulation agent with enhanced cultural and demographic profiles"""
    
    def __init__(self, profile: EnhancedStudentProfile, foundation_context: FoundationDocumentContext, api_key: Optional[str] = None):
        self.profile = profile
        self.foundation_context = foundation_context
        self.memory = []  # Conversation history
        self.learning_session_data = []
        
        # Get API key securely
        if api_key is None:
            if SECURE_CONFIG_AVAILABLE:
                api_key = get_api_key()
                if not api_key:
                    raise ValueError("No API key provided and secure config not set up. Please set up .env file or pass api_key parameter.")
            else:
                raise ValueError("No API key provided and secure config not available. Please pass api_key parameter.")
        
        # Configure Gemini
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Build agent personality prompt
        self.personality_prompt = self._build_personality_prompt()
    
    def _build_personality_prompt(self) -> str:
        """Create comprehensive personality prompt based on enhanced profile"""
        
        # Cultural context
        cultural_desc = f"""
        CULTURAL BACKGROUND: {self.profile.cultural.primary_culture}
        - Communication style: {self.profile.cultural.communication_style}
        - Authority relationship preference: {self.profile.cultural.authority_relationship}
        - Collaboration approach: {self.profile.cultural.collaboration_preference}
        - Technology adoption style: {self.profile.cultural.technology_adoption}
        """
        
        # Linguistic context
        linguistic_desc = f"""
        LINGUISTIC PROFILE:
        - Native language: {self.profile.linguistic.native_language}
        - English proficiency: {self.profile.linguistic.english_proficiency}
        - Communication confidence: {self.profile.linguistic.communication_confidence:.1f}/1.0
        - Prefers visual aids: {self.profile.linguistic.prefers_visual_aids}
        """
        
        # Demographic context
        demographic_desc = f"""
        DEMOGRAPHIC BACKGROUND:
        - Age: {self.profile.demographic.age_exact} ({self.profile.demographic.grade_level})
        - Gender: {self.profile.demographic.gender_identity}
        - Socioeconomic status: {self.profile.demographic.socioeconomic_status}
        - Location: {self.profile.demographic.geographic_location}
        - First-generation student: {self.profile.demographic.first_generation_student}
        """
        
        # Emotional context
        emotional_desc = f"""
        CURRENT EMOTIONAL STATE:
        - Stress level: {self.profile.emotional.stress_level:.1f}/1.0
        - Academic confidence: {self.profile.emotional.academic_confidence:.1f}/1.0
        - Current mood: {self.profile.emotional.current_mood}
        - Technology anxiety: {self.profile.emotional.technology_anxiety:.1f}/1.0
        - Recent performance: {self.profile.emotional.recent_academic_performance}
        """
        
        # Behavioral parameters
        behavioral_desc = f"""
        BEHAVIORAL TENDENCIES:
        - Trust in AI: {self.profile.baseline_trust:.1f}/1.0
        - Help-seeking: {self.profile.help_seeking_tendency:.1f}/1.0
        - Authority deference: {self.profile.authority_deference_level:.1f}/1.0
        - Privacy concerns: {self.profile.privacy_concern_level:.1f}/1.0
        """
        
        return f"""
        You are simulating a student with the following comprehensive profile:
        
        {cultural_desc}
        {linguistic_desc}
        {demographic_desc}
        {emotional_desc}
        {behavioral_desc}
        
        FOUNDATION PRINCIPLES TO FOLLOW:
        {self.foundation_context.get_combined_context()}
        
        BEHAVIORAL GUIDELINES:
        - Respond authentically based on your cultural, linguistic, and emotional profile
        - Show personality traits consistent with your background
        - Express uncertainty, questions, and learning processes naturally
        - Reflect your trust level, help-seeking tendencies, and communication style
        - Consider your stress level, academic confidence, and current mood
        - Maintain consistency with your demographic and cultural background
        
        Stay in character throughout all interactions. Your responses should feel genuine and reflect the complexity of your background and current state.
        """
    
    async def interact_with_ai_tutor(self, learning_task: str, ai_tutor_response: str, scenario_context: str = "") -> Dict[str, Any]:
        """Simulate student interaction with AI tutor"""
        
        interaction_prompt = f"""
        LEARNING SCENARIO: {scenario_context}
        
        TASK: {learning_task}
        AI TUTOR'S RESPONSE: {ai_tutor_response}
        
        As the student described in your profile, respond to this AI tutor interaction.
        Your response should reflect:
        1. Your cultural communication style and authority relationships
        2. Your current emotional state and academic confidence
        3. Your trust level and help-seeking tendencies
        4. Your language proficiency and communication preferences
        5. Your understanding of the foundation principles (co-intelligence, human-centered AI)
        
        Show your authentic reaction, reasoning process, and how you would engage with both the task and the AI's input.
        """
        
        full_prompt = self.personality_prompt + "\n\n" + interaction_prompt
        
        try:
            response = self.model.generate_content(full_prompt)
            
            interaction_data = {
                "timestamp": datetime.now().isoformat(),
                "scenario_context": scenario_context,
                "task": learning_task,
                "ai_input": ai_tutor_response,
                "student_response": response.text,
                "agent_id": self.profile.agent_id,
                "profile_summary": {
                    "culture": self.profile.cultural.primary_culture,
                    "age": self.profile.demographic.age_exact,
                    "language": self.profile.linguistic.native_language,
                    "english_proficiency": self.profile.linguistic.english_proficiency,
                    "ses": self.profile.demographic.socioeconomic_status,
                    "mood": self.profile.emotional.current_mood,
                    "stress": self.profile.emotional.stress_level,
                    "confidence": self.profile.emotional.academic_confidence,
                    "trust": self.profile.baseline_trust
                }
            }
            
            self.memory.append(interaction_data)
            return interaction_data
            
        except Exception as e:
            return {"error": str(e), "agent_id": self.profile.agent_id}
    
    async def respond_to_survey(self, survey_questions: List[Dict[str, str]]) -> Dict[str, Any]:
        """Generate culturally and demographically appropriate survey responses"""
        
        survey_prompt = f"""
        You are completing a research survey about your experience with AI in learning.
        Answer each question based on your profile, cultural background, and recent experiences.
        
        Consider your:
        - Cultural values and communication style
        - Current emotional state and academic confidence
        - Language proficiency and understanding
        - Socioeconomic background and educational context
        
        QUESTIONS:
        """
        
        for i, q in enumerate(survey_questions, 1):
            survey_prompt += f"\n{i}. {q['question']}"
            if q.get('type') == 'likert':
                survey_prompt += f" (Scale: {q.get('scale', '1-7')})"
        
        survey_prompt += """
        
        Provide thoughtful answers that reflect your authentic perspective and background.
        For Likert scales, give the number and brief reasoning that shows your cultural and personal context.
        """
        
        full_prompt = self.personality_prompt + "\n\n" + survey_prompt
        
        try:
            response = self.model.generate_content(full_prompt)
            return {
                "agent_id": self.profile.agent_id,
                "survey_responses": response.text,
                "timestamp": datetime.now().isoformat(),
                "profile_context": self.profile.profile_name
            }
        except Exception as e:
            return {"error": str(e), "agent_id": self.profile.agent_id}

class ResearchSimulationOrchestrator:
    """Manages the entire research simulation with enhanced diversity"""
    
    def __init__(self, api_key: Optional[str] = None, research_context: str = "university_diverse", num_agents: int = 20, custom_profiles: List[EnhancedStudentProfile] = None, output_directory: str = "./simulation_data"):
        # Get API key securely
        if api_key is None:
            if SECURE_CONFIG_AVAILABLE:
                api_key = get_api_key()
                if not api_key:
                    raise ValueError("No API key provided and secure config not set up. Please set up .env file or pass api_key parameter.")
            else:
                raise ValueError("No API key provided and secure config not available. Please pass api_key parameter.")
        
        self.api_key = api_key
        self.research_context = research_context
        self.foundation_context = FoundationDocumentContext()
        self.agents: List[StudentAgent] = []
        self.simulation_data = []
        self.output_directory = Path(output_directory)
        
        # Initialize comprehensive data collector
        self.data_collector = ComprehensiveDataCollector(output_directory)
        
        # Create output directory if it doesn't exist
        self.output_directory.mkdir(parents=True, exist_ok=True)
        
        # Create diverse agent profiles or use custom ones
        if custom_profiles:
            self.agent_profiles = custom_profiles
        else:
            self.agent_profiles = create_diverse_research_cohort(num_agents, research_context)
        
        # Create agents
        for profile in self.agent_profiles:
            agent = StudentAgent(profile, self.foundation_context, self.api_key)
            self.agents.append(agent)
    
    async def run_co_thinking_scenario(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """Run a complete co-thinking learning scenario with diverse agents"""
        
        print(f"Running scenario: {scenario['name']} with {len(self.agents)} diverse agents")
        
        results = []
        for agent in self.agents:
            result = await agent.interact_with_ai_tutor(
                scenario['learning_task'],
                scenario['ai_tutor_response'],
                scenario.get('context', '')
            )
            
            # Record interaction in data collector
            if 'error' not in result:
                result['scenario_type'] = scenario.get('type', 'general')
                try:
                    interaction_record = self.data_collector.record_agent_interaction(
                        agent.profile.agent_id, 
                        result
                    )
                    print(f"✅ Recorded interaction for agent {agent.profile.agent_id}")
                except Exception as e:
                    print(f"❌ Failed to record interaction for agent {agent.profile.agent_id}: {e}")
                    import traceback
                    traceback.print_exc()
            
            results.append(result)
        
        scenario_data = {
            "scenario_name": scenario['name'],
            "scenario_type": scenario.get('type', 'general'),
            "research_context": self.research_context,
            "timestamp": datetime.now().isoformat(),
            "results": results,
            "agent_diversity_summary": self._generate_diversity_summary()
        }
        
        self.simulation_data.append(scenario_data)
        return scenario_data
    
    async def run_survey_collection(self, survey_questions: List[Dict[str, str]]) -> Dict[str, Any]:
        """Collect survey responses from all diverse agents"""
        
        print(f"Collecting survey responses from {len(self.agents)} culturally diverse agents")
        
        results = []
        for agent in self.agents:
            result = await agent.respond_to_survey(survey_questions)
            
            # Record survey response in data collector
            if 'error' not in result:
                survey_record = self.data_collector.record_survey_response(
                    agent.profile.agent_id,
                    result
                )
            
            results.append(result)
        
        survey_data = {
            "survey_type": "co_thinking_effectiveness",
            "research_context": self.research_context,
            "timestamp": datetime.now().isoformat(),
            "responses": results,
            "diversity_summary": self._generate_diversity_summary()
        }
        
        self.simulation_data.append(survey_data)
        return survey_data
    
    def _generate_diversity_summary(self) -> Dict[str, Any]:
        """Generate summary of agent diversity for research validation"""
        
        profiles = [agent.profile for agent in self.agents]
        
        return {
            "total_agents": len(profiles),
            "cultural_distribution": self._count_distribution([p.cultural.primary_culture for p in profiles]),
            "age_distribution": {
                "mean": sum(p.demographic.age_exact for p in profiles) / len(profiles),
                "range": (min(p.demographic.age_exact for p in profiles), max(p.demographic.age_exact for p in profiles))
            },
            "language_distribution": self._count_distribution([p.linguistic.native_language for p in profiles]),
            "ses_distribution": self._count_distribution([p.demographic.socioeconomic_status for p in profiles]),
            "gender_distribution": self._count_distribution([p.demographic.gender_identity for p in profiles]),
            "emotional_context_distribution": self._count_distribution([p.emotional.current_mood for p in profiles]),
            "trust_levels": {
                "mean": sum(p.baseline_trust for p in profiles) / len(profiles),
                "std": self._calculate_std([p.baseline_trust for p in profiles])
            },
            "academic_confidence": {
                "mean": sum(p.emotional.academic_confidence for p in profiles) / len(profiles),
                "std": self._calculate_std([p.emotional.academic_confidence for p in profiles])
            }
        }
    
    def _count_distribution(self, items: List[str]) -> Dict[str, int]:
        """Count distribution of categorical items"""
        distribution = {}
        for item in items:
            distribution[item] = distribution.get(item, 0) + 1
        return distribution
    
    def _calculate_std(self, values: List[float]) -> float:
        """Calculate standard deviation"""
        if len(values) < 2:
            return 0.0
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
        return variance ** 0.5
    
    def export_simulation_data(self, filename_prefix: str = "co_thinking_simulation"):
        """Export comprehensive simulation data with analysis"""
        
        # Export comprehensive dataset using data collector
        files_created = self.data_collector.export_comprehensive_dataset(filename_prefix)
        
        print(f"✅ Comprehensive simulation data exported!")
        print(f"📊 Files created:")
        for file_type, filepath in files_created.items():
            print(f"  - {file_type}: {filepath}")
        
        print(f"\n📋 Summary:")
        summary = self.data_collector.get_summary_statistics()
        if 'error' not in summary:
            print(f"  - Total interactions: {summary['total_interactions']}")
            print(f"  - Unique agents: {summary['unique_agents']}")
            print(f"  - Cultural diversity: {summary['cultural_diversity']} cultures")
            print(f"  - Average response length: {summary['avg_response_length']:.1f} words")
            print(f"  - Average coherence: {summary['avg_coherence']:.2f}")
            print(f"  - Foundation alignment: {summary['avg_foundation_alignment']:.2f}")
        
        return files_created

# Example usage
if __name__ == "__main__":
    
    # Configuration
    GEMINI_API_KEY = "your-gemini-api-key-here"  # Replace with your actual API key
    
    # Sample scenario with enhanced context
    SAMPLE_SCENARIO = {
        "name": "Cross-Cultural Math Problem Solving",
        "type": "cognitive_partnership",
        "context": "You are working on a calculus problem in a collaborative learning environment",
        "learning_task": "Find the derivative of f(x) = x² + 3x + 2",
        "ai_tutor_response": "To find the derivative, we can use the power rule. For each term: d/dx(x²) = 2x, d/dx(3x) = 3, d/dx(2) = 0. So f'(x) = 2x + 3. Does this approach make sense to you?"
    }
    
    async def run_enhanced_demo():
        """Demo of the enhanced simulation system with cultural diversity"""
        
        # Create simulation with diverse university cohort
        sim = ResearchSimulationOrchestrator(
            GEMINI_API_KEY, 
            research_context="university_diverse",
            num_agents=8
        )
        
        print(f"Created {len(sim.agents)} culturally diverse student agents")
        print("Cultural diversity:", sim._generate_diversity_summary()['cultural_distribution'])
        
        result = await sim.run_co_thinking_scenario(SAMPLE_SCENARIO)
        print("Enhanced simulation completed!")
        
        sim.export_simulation_data("enhanced_demo_results.json")
        
        return sim
    
    # Uncomment to run demo (requires valid API key)
    # asyncio.run(run_enhanced_demo()) 