"""
Data Collection and Recording System
Comprehensive recording of all agent responses and interactions for research analysis
"""

import json
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import re
from dataclasses import dataclass, asdict

@dataclass
class InteractionRecord:
    """Single interaction record between agent and system"""
    timestamp: str
    agent_id: str
    interaction_type: str  # "scenario", "survey", "followup"
    scenario_name: str
    scenario_type: str  # "cognitive_partnership", "trust_calibration", etc.
    
    # Input data
    prompt_text: str
    context: str
    task_description: str
    
    # Agent response
    raw_response: str
    response_length_words: int
    response_length_chars: int
    
    # Agent profile context
    cultural_background: str
    age: int
    gender: str
    native_language: str
    english_proficiency: str
    socioeconomic_status: str
    emotional_state: str
    
    # Behavioral indicators
    trust_level: float
    help_seeking_tendency: float
    authority_deference: float
    privacy_concern: float
    
    # Response quality metrics
    coherence_score: float
    cultural_consistency_score: float
    foundation_alignment_score: float
    
    # Analysis tags
    question_types_asked: List[str]
    response_categories: List[str]
    psychological_constructs_evident: List[str]

class ComprehensiveDataCollector:
    """Comprehensive data collection system for research analysis"""
    
    def __init__(self, output_directory: str = "./simulation_data"):
        self.output_dir = Path(output_directory)
        self.output_dir.mkdir(exist_ok=True)
        
        # Data storage
        self.interaction_records: List[InteractionRecord] = []
        self.survey_responses: List[Dict[str, Any]] = []
        self.session_metadata: Dict[str, Any] = {}
        
        # Import response analyzer
        # Import from absolute paths to avoid relative import issues
        try:
            from co_thinking_agent_simulation.implementation.analysis.response_analyzer import ResponseAnalyzer
        except ImportError:
            # Fallback for direct execution - avoid Path variable scoping conflicts
            import sys
            # Use intermediate variables to avoid Path scoping issues
            current_file_path = Path(__file__)
            analysis_dir = current_file_path.parent.parent / "analysis"
            sys.path.append(str(analysis_dir))
            from response_analyzer import ResponseAnalyzer
        self.response_analyzer = ResponseAnalyzer()
        
    def record_agent_interaction(self, agent_id: str, interaction_data: Dict[str, Any]) -> InteractionRecord:
        """Record a single agent interaction with comprehensive data"""
        
        print(f"🔍 Recording interaction for agent: {agent_id}")
        print(f"🔍 Interaction data keys: {list(interaction_data.keys())}")
        print(f"🔍 Student response length: {len(interaction_data.get('student_response', ''))}")
        
        # Extract basic information
        timestamp = interaction_data.get('timestamp', datetime.now().isoformat())
        raw_response = interaction_data.get('student_response', '')
        profile_summary = interaction_data.get('profile_summary', {})
        
        print(f"🔍 Profile summary keys: {list(profile_summary.keys())}")
        
        # Analyze response
        try:
            response_analysis = self.response_analyzer.analyze_response(
                raw_response, 
                profile_summary,
                interaction_data
            )
        except Exception as e:
            print(f"❌ Response analysis failed: {e}")
            # Create dummy analysis to prevent failure
            response_analysis = {
                'coherence_score': 0.5,
                'cultural_consistency': 0.5,
                'foundation_alignment': 0.5,
                'question_types': [],
                'response_categories': [],
                'constructs_evident': []
            }
        
        # Create comprehensive record
        record = InteractionRecord(
            timestamp=timestamp,
            agent_id=agent_id,
            interaction_type=interaction_data.get('interaction_type', 'scenario'),
            scenario_name=interaction_data.get('scenario_context', ''),
            scenario_type=interaction_data.get('scenario_type', 'general'),
            
            # Input data
            prompt_text=interaction_data.get('task', ''),
            context=interaction_data.get('scenario_context', ''),
            task_description=interaction_data.get('task', ''),
            
            # Response data
            raw_response=raw_response,
            response_length_words=len(raw_response.split()),
            response_length_chars=len(raw_response),
            
            # Profile data
            cultural_background=profile_summary.get('culture', ''),
            age=profile_summary.get('age', 0),
            gender=profile_summary.get('gender', ''),
            native_language=profile_summary.get('language', ''),
            english_proficiency=profile_summary.get('english_proficiency', ''),
            socioeconomic_status=profile_summary.get('ses', ''),
            emotional_state=profile_summary.get('mood', ''),
            
            # Behavioral data
            trust_level=profile_summary.get('trust', 0.0),
            help_seeking_tendency=profile_summary.get('help_seeking', 0.0),
            authority_deference=profile_summary.get('authority_deference', 0.0),
            privacy_concern=profile_summary.get('privacy_concern', 0.0),
            
            # Quality metrics
            coherence_score=response_analysis['coherence_score'],
            cultural_consistency_score=response_analysis['cultural_consistency'],
            foundation_alignment_score=response_analysis['foundation_alignment'],
            
            # Analysis results
            question_types_asked=response_analysis['question_types'],
            response_categories=response_analysis['response_categories'],
            psychological_constructs_evident=response_analysis['constructs_evident']
        )
        
        self.interaction_records.append(record)
        return record
    
    def record_survey_response(self, agent_id: str, survey_data: Dict[str, Any]) -> Dict[str, Any]:
        """Record survey responses with structured analysis"""
        
        survey_record = {
            'timestamp': survey_data.get('timestamp', datetime.now().isoformat()),
            'agent_id': agent_id,
            'survey_type': survey_data.get('survey_type', 'general'),
            'raw_responses': survey_data.get('survey_responses', ''),
            'profile_context': survey_data.get('profile_context', ''),
            'parsed_responses': self._parse_survey_responses(survey_data.get('survey_responses', '')),
            'response_quality': self._assess_survey_quality(survey_data.get('survey_responses', ''))
        }
        
        self.survey_responses.append(survey_record)
        return survey_record
    
    def _parse_survey_responses(self, raw_response: str) -> Dict[str, Any]:
        """Parse structured survey responses from agent text"""
        
        parsed = {}
        
        # Extract Likert scale responses
        likert_pattern = r'(?:Question\s*)?(\d+)[:.]\s*.*?(?:Scale|Rating)[:\s]*(\d+)'
        likert_matches = re.findall(likert_pattern, raw_response, re.IGNORECASE)
        
        for match in likert_matches:
            question_num, rating = match
            parsed[f'q{question_num}_rating'] = int(rating)
        
        # Extract reasoning/explanations
        reasoning_pattern = r'(?:because|reason|explanation)[:\s]+(.*?)(?:\n|$)'
        reasoning_matches = re.findall(reasoning_pattern, raw_response, re.IGNORECASE)
        
        for i, reasoning in enumerate(reasoning_matches):
            parsed[f'reasoning_{i+1}'] = reasoning.strip()
        
        # Extract key themes
        parsed['key_themes'] = self._extract_themes(raw_response)
        
        return parsed
    
    def _extract_themes(self, text: str) -> List[str]:
        """Extract key themes from response text"""
        
        themes = []
        theme_keywords = {
            'trust': ['trust', 'reliable', 'dependable', 'confidence'],
            'collaboration': ['collaborate', 'work together', 'partnership', 'teamwork'],
            'control': ['control', 'agency', 'autonomy', 'decision'],
            'learning': ['learn', 'understand', 'knowledge', 'education'],
            'uncertainty': ['unsure', 'uncertain', 'doubt', 'confused'],
            'efficiency': ['faster', 'efficient', 'quick', 'time-saving'],
            'creativity': ['creative', 'innovative', 'original', 'new ideas'],
            'cultural': ['culture', 'tradition', 'family', 'community']
        }
        
        text_lower = text.lower()
        for theme, keywords in theme_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                themes.append(theme)
        
        return themes
    
    def _assess_survey_quality(self, response: str) -> Dict[str, float]:
        """Assess quality of survey responses"""
        
        return {
            'completeness': min(1.0, len(response.split()) / 50),  # Expect ~50 words minimum
            'coherence': self._calculate_coherence(response),
            'specificity': self._calculate_specificity(response),
            'cultural_relevance': self._assess_cultural_relevance(response)
        }
    
    def _calculate_coherence(self, text: str) -> float:
        """Simple coherence calculation based on sentence structure"""
        sentences = text.split('.')
        if len(sentences) < 2:
            return 0.5
        
        # Basic coherence indicators
        coherence_indicators = [
            len([s for s in sentences if len(s.split()) > 3]),  # Substantial sentences
            len(re.findall(r'\b(because|since|therefore|however|although)\b', text, re.IGNORECASE)),  # Connectives
            1 if re.search(r'\b(I|my|me)\b', text) else 0  # Personal reference
        ]
        
        return min(1.0, sum(coherence_indicators) / 10)
    
    def _calculate_specificity(self, text: str) -> float:
        """Calculate specificity based on concrete details"""
        specific_indicators = [
            len(re.findall(r'\b\d+\b', text)),  # Numbers
            len(re.findall(r'\b(when|where|how|why)\b', text, re.IGNORECASE)),  # Specific questions
            len(re.findall(r'\b(example|instance|specifically)\b', text, re.IGNORECASE))  # Examples
        ]
        
        return min(1.0, sum(specific_indicators) / 5)
    
    def _assess_cultural_relevance(self, text: str) -> float:
        """Assess cultural context relevance in responses"""
        cultural_indicators = [
            len(re.findall(r'\b(family|community|tradition|culture)\b', text, re.IGNORECASE)),
            len(re.findall(r'\b(teacher|authority|respect|hierarchy)\b', text, re.IGNORECASE)),
            len(re.findall(r'\b(individual|group|collective|together)\b', text, re.IGNORECASE))
        ]
        
        return min(1.0, sum(cultural_indicators) / 3)
    
    def export_comprehensive_dataset(self, filename_prefix: str = "co_thinking_data") -> Dict[str, str]:
        """Export comprehensive dataset in multiple formats"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Convert interaction records to DataFrame
        interactions_df = pd.DataFrame([asdict(record) for record in self.interaction_records])
        
        # Convert survey responses to DataFrame
        surveys_df = pd.DataFrame(self.survey_responses)
        
        # Generate comprehensive analysis
        # Import from absolute paths to avoid relative import issues
        try:
            from co_thinking_agent_simulation.implementation.analysis.data_analyzer import DataAnalyzer
        except ImportError:
            # Fallback for direct execution
            import sys
            from pathlib import Path
            # More robust path resolution to avoid variable scoping issues
            current_file_path = Path(__file__)
            analysis_dir = current_file_path.parent.parent / "analysis"
            sys.path.append(str(analysis_dir))
            from data_analyzer import DataAnalyzer
        analyzer = DataAnalyzer(self.interaction_records, self.survey_responses)
        analysis_results = analyzer.generate_comprehensive_analysis()
        
        # File paths
        files_created = {}
        
        # JSON export (complete data)
        json_file = self.output_dir / f"{filename_prefix}_complete_{timestamp}.json"
        complete_data = {
            'metadata': {
                'export_timestamp': datetime.now().isoformat(),
                'total_interactions': len(self.interaction_records),
                'total_surveys': len(self.survey_responses),
                'unique_agents': len(set(r.agent_id for r in self.interaction_records))
            },
            'interaction_records': [asdict(record) for record in self.interaction_records],
            'survey_responses': self.survey_responses,
            'analysis_results': analysis_results
        }
        
        with open(json_file, 'w') as f:
            json.dump(complete_data, f, indent=2)
        files_created['complete_json'] = str(json_file)
        
        # CSV exports for statistical analysis
        if not interactions_df.empty:
            csv_file = self.output_dir / f"{filename_prefix}_interactions_{timestamp}.csv"
            interactions_df.to_csv(csv_file, index=False)
            files_created['interactions_csv'] = str(csv_file)
        
        if not surveys_df.empty:
            survey_csv = self.output_dir / f"{filename_prefix}_surveys_{timestamp}.csv"
            surveys_df.to_csv(survey_csv, index=False)
            files_created['surveys_csv'] = str(survey_csv)
        
        # Excel export with multiple sheets
        excel_file = self.output_dir / f"{filename_prefix}_analysis_{timestamp}.xlsx"
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            # Always create at least one sheet to avoid Excel error
            if not interactions_df.empty:
                interactions_df.to_excel(writer, sheet_name='Interactions', index=False)
            else:
                pd.DataFrame({'Note': ['No interaction data recorded']}).to_excel(writer, sheet_name='Interactions', index=False)
                
            if not surveys_df.empty:
                surveys_df.to_excel(writer, sheet_name='Surveys', index=False)
            else:
                pd.DataFrame({'Note': ['No survey data recorded']}).to_excel(writer, sheet_name='Surveys', index=False)
            
            # Analysis summary sheet
            if isinstance(analysis_results, dict) and 'summary' in analysis_results and 'error' not in analysis_results:
                analysis_df = pd.DataFrame([analysis_results['summary']])
                analysis_df.to_excel(writer, sheet_name='Analysis_Summary', index=False)
            else:
                pd.DataFrame({'Note': ['No analysis available - insufficient data']}).to_excel(writer, sheet_name='Analysis_Summary', index=False)
            
        files_created['excel_analysis'] = str(excel_file)
        
        # Research report
        report_file = self.output_dir / f"{filename_prefix}_report_{timestamp}.md"
        analyzer.generate_research_report(analysis_results, report_file)
        files_created['research_report'] = str(report_file)
        
        return files_created
    
    def get_summary_statistics(self) -> Dict[str, Any]:
        """Get quick summary statistics"""
        
        if not self.interaction_records:
            return {'error': 'No data collected yet'}
        
        df = pd.DataFrame([asdict(record) for record in self.interaction_records])
        
        return {
            'total_interactions': len(self.interaction_records),
            'unique_agents': df['agent_id'].nunique(),
            'cultural_diversity': df['cultural_background'].nunique(),
            'avg_response_length': df['response_length_words'].mean(),
            'avg_coherence': df['coherence_score'].mean(),
            'avg_foundation_alignment': df['foundation_alignment_score'].mean(),
            'scenario_types': df['scenario_type'].unique().tolist(),
            'date_range': [df['timestamp'].min(), df['timestamp'].max()] if len(df) > 0 else []
        } 