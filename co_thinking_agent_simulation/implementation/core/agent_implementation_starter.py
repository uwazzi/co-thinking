"""
Co-Thinking Research Simulation Agent System
Starter Implementation with Gemini Integration
"""

import json
import random
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
from datetime import datetime
import asyncio
import pandas as pd
from pathlib import Path

# You'll need to install: pip install google-generativeai pandas

import google.generativeai as genai

@dataclass
class StudentProfile:
    """Student agent profile based on research framework"""
    agent_id: str
    age_group: str  # "K-12", "University", "Adult"
    academic_level: str  # "Low", "Medium", "High"
    tech_comfort: str  # "Novice", "Intermediate", "Advanced"
    learning_style: str  # "Visual", "Auditory", "Kinesthetic", "Reading"
    ai_experience: str  # "None", "Limited", "Moderate", "Extensive"
    
    # Psychological parameters (0.0-1.0 scales)
    baseline_trust: float
    cognitive_load_tolerance: float
    help_seeking_tendency: float
    metacognitive_awareness: float
    risk_tolerance: float
    
    # Foundation document alignment parameters
    co_intelligence_orientation: float  # How well they understand Mollick's framework
    human_centered_values: float  # Alignment with Swiss AI and People Factor principles

class FoundationDocumentContext:
    """Manages foundation document context for agents"""
    
    def __init__(self, foundation_dir: str = "./fundations"):
        self.foundation_dir = Path(foundation_dir)
        self.context_templates = {
            "mollick": self._get_mollick_context(),
            "swiss_ai": self._get_swiss_ai_context(),
            "people_factor": self._get_people_factor_context()
        }
    
    def _get_mollick_context(self) -> str:
        return """
        MOLLICK CO-INTELLIGENCE PRINCIPLES:
        - Co-intelligence means humans and AI working together, not AI replacing humans
        - Four key interaction modes: Co-working, Co-creating, Co-teaching, Co-learning
        - Trust must be calibrated - neither over-trust nor under-trust AI
        - Human agency and control must be maintained
        - AI should amplify human capabilities, not diminish them
        - Metacognitive awareness of AI strengths/weaknesses is crucial
        """
    
    def _get_swiss_ai_context(self) -> str:
        return """
        SWISS AI HUMAN-CENTERED PRINCIPLES:
        - AI development must prioritize human welfare and dignity
        - Transparency and explainability are essential
        - Stakeholder involvement in AI design and deployment
        - Ethical considerations must guide all AI implementations
        - Human oversight and control mechanisms required
        - Privacy and data protection are fundamental rights
        """
    
    def _get_people_factor_context(self) -> str:
        return """
        PEOPLE FACTOR HUMAN-CENTERED SCALING:
        - Focus on user experience and adoption, not just technical metrics
        - Human-centered approach to scaling AI tools
        - Importance of training and support for AI users
        - Measure human impact and satisfaction
        - Consider social and cultural contexts
        - Design for diverse user needs and capabilities
        """
    
    def get_combined_context(self) -> str:
        return "\n\n".join(self.context_templates.values())

class StudentAgent:
    """Individual student simulation agent"""
    
    def __init__(self, profile: StudentProfile, foundation_context: FoundationDocumentContext, api_key: str):
        self.profile = profile
        self.foundation_context = foundation_context
        self.memory = []  # Conversation history
        self.learning_session_data = []
        
        # Configure Gemini
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Build agent personality prompt
        self.personality_prompt = self._build_personality_prompt()
    
    def _build_personality_prompt(self) -> str:
        """Create personality prompt based on student profile and foundation documents"""
        
        trust_level = "high" if self.profile.baseline_trust > 0.7 else "medium" if self.profile.baseline_trust > 0.4 else "low"
        metacog_level = "high" if self.profile.metacognitive_awareness > 0.7 else "medium" if self.profile.metacognitive_awareness > 0.4 else "low"
        
        return f"""
        You are simulating a {self.profile.age_group} student with {self.profile.academic_level.lower()} academic ability.
        Your tech comfort level is {self.profile.tech_comfort.lower()} and you have {self.profile.ai_experience.lower()} experience with AI.
        
        PERSONALITY TRAITS:
        - Trust in AI: {trust_level} level
        - Metacognitive awareness: {metacog_level} level
        - Help-seeking tendency: {self.profile.help_seeking_tendency:.1f}/1.0
        
        FOUNDATION PRINCIPLES TO FOLLOW:
        {self.foundation_context.get_combined_context()}
        
        Stay in character as this student throughout all interactions.
        Respond naturally with occasional uncertainty and show your thinking process.
        """
    
    async def interact_with_ai_tutor(self, learning_task: str, ai_tutor_response: str) -> Dict[str, Any]:
        """Simulate student interaction with AI tutor"""
        
        interaction_prompt = f"""
        LEARNING SITUATION:
        Task: {learning_task}
        AI Tutor's Response: {ai_tutor_response}
        
        As the student described, respond to this AI tutor interaction.
        Include your reaction, whether you accept/modify/reject the AI's input, and your reasoning.
        """
        
        full_prompt = self.personality_prompt + "\n\n" + interaction_prompt
        
        try:
            response = self.model.generate_content(full_prompt)
            
            interaction_data = {
                "timestamp": datetime.now().isoformat(),
                "task": learning_task,
                "ai_input": ai_tutor_response,
                "student_response": response.text,
                "agent_id": self.profile.agent_id
            }
            
            self.memory.append(interaction_data)
            return interaction_data
            
        except Exception as e:
            return {"error": str(e), "agent_id": self.profile.agent_id}

class ResearchSimulationOrchestrator:
    """Manages the entire research simulation"""
    
    def __init__(self, api_key: str, num_agents: int = 10):
        self.api_key = api_key
        self.foundation_context = FoundationDocumentContext()
        self.agents: List[StudentAgent] = []
        self.simulation_data = []
        
        # Create diverse agent profiles
        self._create_agent_profiles(num_agents)
    
    def _create_agent_profiles(self, num_agents: int):
        """Create diverse student agent profiles"""
        for i in range(num_agents):
            profile = StudentProfile(
                agent_id=f"student_{i:03d}",
                age_group=random.choice(["K-12", "University", "Adult"]),
                academic_level=random.choice(["Low", "Medium", "High"]),
                tech_comfort=random.choice(["Novice", "Intermediate", "Advanced"]),
                learning_style=random.choice(["Visual", "Auditory", "Kinesthetic", "Reading"]),
                ai_experience=random.choice(["None", "Limited", "Moderate", "Extensive"]),
                baseline_trust=random.uniform(0.2, 0.9),
                cognitive_load_tolerance=random.uniform(0.3, 0.9),
                help_seeking_tendency=random.uniform(0.2, 0.8),
                metacognitive_awareness=random.uniform(0.3, 0.9),
                risk_tolerance=random.uniform(0.2, 0.8),
                co_intelligence_orientation=random.uniform(0.4, 0.9),
                human_centered_values=random.uniform(0.5, 0.9)
            )
            
            agent = StudentAgent(profile, self.foundation_context, self.api_key)
            self.agents.append(agent)
    
    async def run_co_thinking_scenario(self, scenario: Dict[str, Any]):
        """Run a complete co-thinking learning scenario"""
        
        print(f"Running scenario: {scenario['name']}")
        
        results = []
        for agent in self.agents:
            result = await agent.interact_with_ai_tutor(
                scenario['learning_task'],
                scenario['ai_tutor_response']
            )
            results.append(result)
        
        scenario_data = {
            "scenario_name": scenario['name'],
            "timestamp": datetime.now().isoformat(),
            "results": results
        }
        
        self.simulation_data.append(scenario_data)
        return scenario_data
    
    def export_simulation_data(self, filename: str = "simulation_results.json"):
        """Export simulation data for analysis"""
        with open(filename, 'w') as f:
            json.dump(self.simulation_data, f, indent=2)
        
        print(f"Simulation data exported to {filename}")

# Example usage
if __name__ == "__main__":
    
    # Configuration
    GEMINI_API_KEY = "your-gemini-api-key-here"  # Replace with your actual API key
    
    # Sample scenario
    SAMPLE_SCENARIO = {
        "name": "Math Problem Solving with AI",
        "learning_task": "Solve this calculus problem: Find the derivative of f(x) = x² + 3x + 2",
        "ai_tutor_response": "To find the derivative, we can use the power rule. For each term: d/dx(x²) = 2x, d/dx(3x) = 3, d/dx(2) = 0. So f'(x) = 2x + 3."
    }
    
    async def run_demo():
        """Demo of the simulation system"""
        sim = ResearchSimulationOrchestrator(GEMINI_API_KEY, num_agents=3)
        
        print(f"Created {len(sim.agents)} student agents")
        
        result = await sim.run_co_thinking_scenario(SAMPLE_SCENARIO)
        print("Simulation completed!")
        
        sim.export_simulation_data("demo_results.json")
        
        return sim
    
    # Uncomment to run demo (requires valid API key)
    # asyncio.run(run_demo()) 