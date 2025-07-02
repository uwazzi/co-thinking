"""
Enhanced Student Profile System for Co-Thinking Research
Includes cultural, linguistic, demographic, and emotional factors
Based on recent educational research on student diversity and AI interaction patterns
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import random
from enum import Enum

@dataclass
class CulturalProfile:
    """Cultural background affecting AI interaction patterns"""
    primary_culture: str  # e.g., "Western_Individualistic", "East_Asian_Collectivistic", "Latin_American", etc.
    cultural_values: Dict[str, float]  # Values from 0.0 to 1.0
    communication_style: str  # "Direct", "Indirect", "High_Context", "Low_Context"
    authority_relationship: str  # "Hierarchical", "Egalitarian", "Mixed"
    collaboration_preference: str  # "Individual_Focus", "Group_Focus", "Balanced"
    technology_adoption: str  # "Early_Adopter", "Pragmatic", "Conservative", "Skeptical"

@dataclass
class LinguisticProfile:
    """Language background affecting AI communication"""
    native_language: str
    english_proficiency: str  # "Native", "Fluent", "Intermediate", "Basic"
    other_languages: List[str]
    language_learning_context: str  # "Immersion", "Academic", "Self_taught", "Heritage"
    communication_confidence: float  # 0.0 to 1.0
    prefers_visual_aids: bool

@dataclass
class DemographicProfile:
    """Detailed demographic information"""
    age_exact: int
    grade_level: Optional[str]  # "Grade_9", "Sophomore", "Graduate_1st_Year", etc.
    gender_identity: str
    socioeconomic_status: str  # "Low", "Lower_Middle", "Middle", "Upper_Middle", "High"
    geographic_location: str  # "Urban", "Suburban", "Rural"
    family_education_level: str  # "No_College", "Some_College", "College_Graduate", "Graduate_Degree"
    first_generation_student: bool
    disability_status: Optional[str]  # None, "Learning", "Physical", "Sensory", "Multiple"

@dataclass
class EmotionalContextProfile:
    """Current emotional and psychological state"""
    stress_level: float  # 0.0 (very low) to 1.0 (very high)
    academic_confidence: float  # 0.0 to 1.0
    technology_anxiety: float  # 0.0 to 1.0
    social_anxiety: float  # 0.0 to 1.0
    current_mood: str  # "Positive", "Neutral", "Stressed", "Excited", "Overwhelmed", "Curious"
    motivation_level: float  # 0.0 to 1.0
    recent_academic_performance: str  # "Excellent", "Good", "Average", "Below_Average", "Poor"
    support_system_strength: float  # 0.0 to 1.0
    mental_health_status: str  # "Excellent", "Good", "Fair", "Poor", "Seeking_Help"

@dataclass
class EnhancedStudentProfile:
    """Comprehensive student profile for realistic simulation"""
    # Basic identification
    agent_id: str
    profile_name: str
    
    # Original core attributes
    age_group: str  # Keep for compatibility
    academic_level: str
    tech_comfort: str
    learning_style: str
    ai_experience: str
    
    # Enhanced profiles
    cultural: CulturalProfile
    linguistic: LinguisticProfile
    demographic: DemographicProfile
    emotional: EmotionalContextProfile
    
    # Original psychological parameters
    baseline_trust: float
    cognitive_load_tolerance: float
    help_seeking_tendency: float
    metacognitive_awareness: float
    risk_tolerance: float
    co_intelligence_orientation: float
    human_centered_values: float
    
    # New behavioral parameters
    cultural_adaptation_speed: float  # How quickly they adapt to AI interactions
    peer_influence_susceptibility: float  # How much peer opinions affect AI usage
    authority_deference_level: float  # Tendency to accept AI as authority
    creative_risk_taking: float  # Willingness to use AI for creative tasks
    privacy_concern_level: float  # Concern about data sharing with AI

class ProfileTemplateGenerator:
    """Generates realistic profile templates based on educational research"""
    
    # Based on recent educational demographics and AI interaction studies
    CULTURAL_TEMPLATES = {
        "US_Individualistic": {
            "primary_culture": "US_Individualistic",
            "cultural_values": {
                "individualism": 0.8,
                "uncertainty_avoidance": 0.4,
                "power_distance": 0.3,
                "achievement_orientation": 0.7
            },
            "communication_style": "Direct",
            "authority_relationship": "Egalitarian",
            "collaboration_preference": "Individual_Focus",
            "technology_adoption": "Early_Adopter"
        },
        
        "East_Asian_Collectivistic": {
            "primary_culture": "East_Asian_Collectivistic",
            "cultural_values": {
                "individualism": 0.3,
                "uncertainty_avoidance": 0.7,
                "power_distance": 0.8,
                "achievement_orientation": 0.9
            },
            "communication_style": "Indirect",
            "authority_relationship": "Hierarchical",
            "collaboration_preference": "Group_Focus",
            "technology_adoption": "Pragmatic"
        },
        
        "European_Balanced": {
            "primary_culture": "European_Balanced",
            "cultural_values": {
                "individualism": 0.6,
                "uncertainty_avoidance": 0.6,
                "power_distance": 0.4,
                "achievement_orientation": 0.6
            },
            "communication_style": "Mixed",
            "authority_relationship": "Mixed",
            "collaboration_preference": "Balanced",
            "technology_adoption": "Pragmatic"
        },
        
        "Latin_American": {
            "primary_culture": "Latin_American",
            "cultural_values": {
                "individualism": 0.4,
                "uncertainty_avoidance": 0.8,
                "power_distance": 0.7,
                "achievement_orientation": 0.5
            },
            "communication_style": "High_Context",
            "authority_relationship": "Hierarchical",
            "collaboration_preference": "Group_Focus",
            "technology_adoption": "Conservative"
        },
        
        "Middle_Eastern": {
            "primary_culture": "Middle_Eastern",
            "cultural_values": {
                "individualism": 0.3,
                "uncertainty_avoidance": 0.7,
                "power_distance": 0.8,
                "achievement_orientation": 0.6
            },
            "communication_style": "High_Context",
            "authority_relationship": "Hierarchical",
            "collaboration_preference": "Group_Focus",
            "technology_adoption": "Conservative"
        },
        
        "African_Ubuntu": {
            "primary_culture": "African_Ubuntu",
            "cultural_values": {
                "individualism": 0.2,
                "uncertainty_avoidance": 0.5,
                "power_distance": 0.6,
                "achievement_orientation": 0.7
            },
            "communication_style": "High_Context",
            "authority_relationship": "Mixed",
            "collaboration_preference": "Group_Focus",
            "technology_adoption": "Pragmatic"
        }
    }
    
    DEMOGRAPHIC_SCENARIOS = {
        "urban_high_ses": {
            "socioeconomic_status": "High",
            "geographic_location": "Urban",
            "family_education_level": "Graduate_Degree",
            "first_generation_student": False,
            "tech_access": "High"
        },
        
        "rural_low_ses": {
            "socioeconomic_status": "Low",
            "geographic_location": "Rural",
            "family_education_level": "No_College",
            "first_generation_student": True,
            "tech_access": "Limited"
        },
        
        "suburban_middle": {
            "socioeconomic_status": "Middle",
            "geographic_location": "Suburban",
            "family_education_level": "College_Graduate",
            "first_generation_student": False,
            "tech_access": "Good"
        },
        
        "urban_immigrant": {
            "socioeconomic_status": "Lower_Middle",
            "geographic_location": "Urban",
            "family_education_level": "Some_College",
            "first_generation_student": True,
            "tech_access": "Moderate"
        }
    }
    
    EMOTIONAL_CONTEXTS = {
        "exam_stress": {
            "stress_level": 0.8,
            "academic_confidence": 0.4,
            "current_mood": "Stressed",
            "motivation_level": 0.7,
            "recent_academic_performance": "Average"
        },
        
        "high_achiever": {
            "stress_level": 0.6,
            "academic_confidence": 0.9,
            "current_mood": "Positive",
            "motivation_level": 0.9,
            "recent_academic_performance": "Excellent"
        },
        
        "struggling_student": {
            "stress_level": 0.7,
            "academic_confidence": 0.3,
            "current_mood": "Overwhelmed",
            "motivation_level": 0.4,
            "recent_academic_performance": "Below_Average"
        },
        
        "curious_explorer": {
            "stress_level": 0.3,
            "academic_confidence": 0.7,
            "current_mood": "Curious",
            "motivation_level": 0.8,
            "recent_academic_performance": "Good"
        },
        
        "tech_anxious": {
            "stress_level": 0.6,
            "academic_confidence": 0.6,
            "technology_anxiety": 0.8,
            "current_mood": "Neutral",
            "motivation_level": 0.5,
            "recent_academic_performance": "Average"
        }
    }
    
    @classmethod
    def create_realistic_profile(cls, 
                               profile_id: str,
                               cultural_template: str = None,
                               demographic_scenario: str = None,
                               emotional_context: str = None,
                               age_range: tuple = (16, 22),
                               custom_params: Dict[str, Any] = None) -> EnhancedStudentProfile:
        """Create a realistic student profile based on research templates"""
        
        # Random selection if not specified
        if cultural_template is None:
            cultural_template = random.choice(list(cls.CULTURAL_TEMPLATES.keys()))
        if demographic_scenario is None:
            demographic_scenario = random.choice(list(cls.DEMOGRAPHIC_SCENARIOS.keys()))
        if emotional_context is None:
            emotional_context = random.choice(list(cls.EMOTIONAL_CONTEXTS.keys()))
        
        # Generate age
        age = random.randint(age_range[0], age_range[1])
        
        # Cultural profile
        cultural_data = cls.CULTURAL_TEMPLATES[cultural_template].copy()
        cultural_profile = CulturalProfile(**cultural_data)
        
        # Linguistic profile
        linguistic_profile = cls._generate_linguistic_profile(cultural_template, demographic_scenario)
        
        # Demographic profile
        demo_data = cls.DEMOGRAPHIC_SCENARIOS[demographic_scenario].copy()
        demographic_profile = cls._generate_demographic_profile(age, demo_data)
        
        # Emotional context
        emotional_data = cls.EMOTIONAL_CONTEXTS[emotional_context].copy()
        emotional_profile = cls._generate_emotional_profile(emotional_data, demographic_profile)
        
        # Generate compatible core attributes
        core_attributes = cls._generate_core_attributes(cultural_profile, demographic_profile, emotional_profile)
        
        # Apply custom parameters if provided
        if custom_params:
            core_attributes.update(custom_params)
        
        return EnhancedStudentProfile(
            agent_id=profile_id,
            profile_name=f"{cultural_template}_{demographic_scenario}_{emotional_context}_{age}",
            cultural=cultural_profile,
            linguistic=linguistic_profile,
            demographic=demographic_profile,
            emotional=emotional_profile,
            **core_attributes
        )
    
    @classmethod
    def _generate_linguistic_profile(cls, cultural_template: str, demographic_scenario: str) -> LinguisticProfile:
        """Generate linguistic profile based on cultural and demographic context"""
        
        # Language mappings based on culture
        language_map = {
            "US_Individualistic": {"native": "English", "proficiency": "Native"},
            "East_Asian_Collectivistic": {"native": random.choice(["Chinese", "Japanese", "Korean"]), "proficiency": random.choice(["Fluent", "Intermediate"])},
            "European_Balanced": {"native": random.choice(["German", "French", "Spanish", "Italian"]), "proficiency": "Fluent"},
            "Latin_American": {"native": "Spanish", "proficiency": random.choice(["Intermediate", "Fluent"])},
            "Middle_Eastern": {"native": "Arabic", "proficiency": random.choice(["Intermediate", "Fluent"])},
            "African_Ubuntu": {"native": random.choice(["Swahili", "Yoruba", "Zulu"]), "proficiency": "Fluent"}
        }
        
        lang_info = language_map.get(cultural_template, {"native": "English", "proficiency": "Native"})
        
        return LinguisticProfile(
            native_language=lang_info["native"],
            english_proficiency=lang_info["proficiency"],
            other_languages=[],
            language_learning_context="Academic" if lang_info["proficiency"] != "Native" else "Native",
            communication_confidence=0.8 if lang_info["proficiency"] in ["Native", "Fluent"] else 0.6,
            prefers_visual_aids=lang_info["proficiency"] not in ["Native"]
        )
    
    @classmethod
    def _generate_demographic_profile(cls, age: int, demo_data: Dict[str, Any]) -> DemographicProfile:
        """Generate demographic profile"""
        
        # Determine grade level based on age
        if age <= 14:
            grade_level = f"Grade_{age-5}"
        elif age <= 18:
            grade_level = f"Grade_{age-5}"
        elif age <= 22:
            grade_level = random.choice(["Freshman", "Sophomore", "Junior", "Senior"])
        else:
            grade_level = "Graduate"
        
        return DemographicProfile(
            age_exact=age,
            grade_level=grade_level,
            gender_identity=random.choice(["Female", "Male", "Non_binary"]),
            socioeconomic_status=demo_data["socioeconomic_status"],
            geographic_location=demo_data["geographic_location"],
            family_education_level=demo_data["family_education_level"],
            first_generation_student=demo_data["first_generation_student"],
            disability_status=None if random.random() > 0.15 else random.choice(["Learning", "Physical", "Sensory"])
        )
    
    @classmethod
    def _generate_emotional_profile(cls, emotional_data: Dict[str, Any], demographic: DemographicProfile) -> EmotionalContextProfile:
        """Generate emotional profile with demographic influences"""
        
        # Adjust emotional factors based on demographics
        stress_modifier = 0.1 if demographic.socioeconomic_status in ["Low", "Lower_Middle"] else 0
        confidence_modifier = -0.1 if demographic.first_generation_student else 0
        
        return EmotionalContextProfile(
            stress_level=min(1.0, emotional_data.get("stress_level", 0.5) + stress_modifier),
            academic_confidence=max(0.0, emotional_data.get("academic_confidence", 0.6) + confidence_modifier),
            technology_anxiety=emotional_data.get("technology_anxiety", 0.4),
            social_anxiety=emotional_data.get("social_anxiety", 0.4),
            current_mood=emotional_data.get("current_mood", "Neutral"),
            motivation_level=emotional_data.get("motivation_level", 0.6),
            recent_academic_performance=emotional_data.get("recent_academic_performance", "Average"),
            support_system_strength=0.8 if demographic.socioeconomic_status == "High" else 0.6,
            mental_health_status=emotional_data.get("mental_health_status", "Good")
        )
    
    @classmethod
    def _generate_core_attributes(cls, cultural: CulturalProfile, demographic: DemographicProfile, emotional: EmotionalContextProfile) -> Dict[str, Any]:
        """Generate core attributes based on cultural, demographic, and emotional factors"""
        
        # Age group mapping
        if demographic.age_exact <= 18:
            age_group = "K-12"
        elif demographic.age_exact <= 25:
            age_group = "University"
        else:
            age_group = "Adult"
        
        # Academic level influenced by performance and SES
        academic_level_map = {
            "Excellent": "High",
            "Good": random.choice(["Medium", "High"]),
            "Average": "Medium",
            "Below_Average": random.choice(["Low", "Medium"]),
            "Poor": "Low"
        }
        academic_level = academic_level_map.get(emotional.recent_academic_performance, "Medium")
        
        # Tech comfort influenced by culture, age, and SES
        base_tech_comfort = 0.7 if demographic.age_exact < 25 else 0.5
        cultural_tech_modifier = {
            "Early_Adopter": 0.2,
            "Pragmatic": 0.0,
            "Conservative": -0.2,
            "Skeptical": -0.3
        }.get(cultural.technology_adoption, 0.0)
        
        tech_comfort_score = base_tech_comfort + cultural_tech_modifier
        tech_comfort = "Advanced" if tech_comfort_score > 0.7 else "Intermediate" if tech_comfort_score > 0.4 else "Novice"
        
        # AI experience influenced by tech comfort and cultural adoption
        ai_exp_map = {
            "Advanced": random.choice(["Moderate", "Extensive"]),
            "Intermediate": random.choice(["Limited", "Moderate"]),
            "Novice": random.choice(["None", "Limited"])
        }
        ai_experience = ai_exp_map[tech_comfort]
        
        # Trust influenced by cultural values and emotional state
        baseline_trust = (
            cultural.cultural_values.get("uncertainty_avoidance", 0.5) * 0.3 +
            emotional.academic_confidence * 0.4 +
            (1 - emotional.technology_anxiety) * 0.3
        )
        
        # Other psychological parameters
        help_seeking = cultural.cultural_values.get("power_distance", 0.5) * 0.4 + emotional.support_system_strength * 0.6
        
        return {
            "age_group": age_group,
            "academic_level": academic_level,
            "tech_comfort": tech_comfort,
            "learning_style": random.choice(["Visual", "Auditory", "Kinesthetic", "Reading"]),
            "ai_experience": ai_experience,
            "baseline_trust": baseline_trust,
            "cognitive_load_tolerance": emotional.academic_confidence * 0.6 + (1 - emotional.stress_level) * 0.4,
            "help_seeking_tendency": help_seeking,
            "metacognitive_awareness": emotional.academic_confidence * 0.5 + (1 - cultural.cultural_values.get("uncertainty_avoidance", 0.5)) * 0.5,
            "risk_tolerance": (1 - cultural.cultural_values.get("uncertainty_avoidance", 0.5)) * 0.7 + emotional.motivation_level * 0.3,
            "co_intelligence_orientation": random.uniform(0.4, 0.9),
            "human_centered_values": random.uniform(0.5, 0.9),
            "cultural_adaptation_speed": (1 - cultural.cultural_values.get("uncertainty_avoidance", 0.5)) * 0.8 + emotional.motivation_level * 0.2,
            "peer_influence_susceptibility": cultural.cultural_values.get("individualism", 0.5) * -0.5 + 0.7,
            "authority_deference_level": cultural.cultural_values.get("power_distance", 0.5),
            "creative_risk_taking": (1 - cultural.cultural_values.get("uncertainty_avoidance", 0.5)) * 0.6 + emotional.motivation_level * 0.4,
            "privacy_concern_level": cultural.cultural_values.get("uncertainty_avoidance", 0.5) * 0.6 + emotional.technology_anxiety * 0.4
        }

def create_diverse_research_cohort(num_agents: int = 20, 
                                 research_context: str = "university_diverse",
                                 custom_distributions: Dict[str, List[str]] = None) -> List[EnhancedStudentProfile]:
    """Create a diverse cohort of student profiles for research simulation"""
    
    profiles = []
    
    # Predefined research contexts
    context_configs = {
        "university_diverse": {
            "cultural_templates": ["US_Individualistic", "East_Asian_Collectivistic", "European_Balanced", "Latin_American"],
            "demographic_scenarios": ["urban_high_ses", "suburban_middle", "urban_immigrant", "rural_low_ses"],
            "emotional_contexts": ["high_achiever", "exam_stress", "curious_explorer", "struggling_student"],
            "age_range": (18, 24)
        },
        
        "high_school_multicultural": {
            "cultural_templates": ["US_Individualistic", "East_Asian_Collectivistic", "Latin_American", "Middle_Eastern"],
            "demographic_scenarios": ["suburban_middle", "urban_immigrant", "rural_low_ses", "urban_high_ses"],
            "emotional_contexts": ["exam_stress", "curious_explorer", "tech_anxious", "high_achiever"],
            "age_range": (14, 18)
        },
        
        "adult_learners": {
            "cultural_templates": ["US_Individualistic", "European_Balanced", "African_Ubuntu"],
            "demographic_scenarios": ["suburban_middle", "urban_high_ses", "rural_low_ses"],
            "emotional_contexts": ["curious_explorer", "tech_anxious", "struggling_student"],
            "age_range": (25, 45)
        }
    }
    
    config = context_configs.get(research_context, context_configs["university_diverse"])
    if custom_distributions:
        config.update(custom_distributions)
    
    for i in range(num_agents):
        profile_id = f"enhanced_agent_{i:03d}"
        
        # Ensure diversity by cycling through options
        cultural_template = config["cultural_templates"][i % len(config["cultural_templates"])]
        demographic_scenario = config["demographic_scenarios"][i % len(config["demographic_scenarios"])]
        emotional_context = config["emotional_contexts"][i % len(config["emotional_contexts"])]
        
        profile = ProfileTemplateGenerator.create_realistic_profile(
            profile_id=profile_id,
            cultural_template=cultural_template,
            demographic_scenario=demographic_scenario,
            emotional_context=emotional_context,
            age_range=config["age_range"]
        )
        
        profiles.append(profile)
    
    return profiles

# Example usage and testing
if __name__ == "__main__":
    # Create a diverse university cohort
    university_cohort = create_diverse_research_cohort(
        num_agents=12,
        research_context="university_diverse"
    )
    
    print("Created diverse university cohort:")
    for profile in university_cohort[:3]:  # Show first 3 examples
        print(f"\nAgent ID: {profile.agent_id}")
        print(f"Profile: {profile.profile_name}")
        print(f"Culture: {profile.cultural.primary_culture}")
        print(f"Age: {profile.demographic.age_exact}")
        print(f"Native Language: {profile.linguistic.native_language}")
        print(f"English Proficiency: {profile.linguistic.english_proficiency}")
        print(f"SES: {profile.demographic.socioeconomic_status}")
        print(f"Current Mood: {profile.emotional.current_mood}")
        print(f"Academic Confidence: {profile.emotional.academic_confidence:.2f}")
        print(f"Trust Level: {profile.baseline_trust:.2f}")
    
    # Create specific profile for testing
    test_profile = ProfileTemplateGenerator.create_realistic_profile(
        profile_id="test_001",
        cultural_template="East_Asian_Collectivistic",
        demographic_scenario="urban_immigrant",
        emotional_context="exam_stress",
        age_range=(19, 21)
    )
    
    print(f"\n\nTest Profile Details:")
    print(f"Cultural values: {test_profile.cultural.cultural_values}")
    print(f"Authority deference: {test_profile.authority_deference_level:.2f}")
    print(f"Privacy concerns: {test_profile.privacy_concern_level:.2f}") 