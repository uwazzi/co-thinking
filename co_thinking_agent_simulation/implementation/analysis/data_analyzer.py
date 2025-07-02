"""
Data Analysis System
Comprehensive analysis of collected simulation data for research insights
"""

import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
from collections import Counter
from dataclasses import asdict

class DataAnalyzer:
    """Comprehensive analysis of simulation data"""
    
    def __init__(self, interaction_records: List, survey_responses: List[Dict]):
        self.interaction_records = interaction_records
        self.survey_responses = survey_responses
        
    def generate_comprehensive_analysis(self) -> Dict[str, Any]:
        """Generate comprehensive analysis of collected data"""
        
        if not self.interaction_records:
            return {'error': 'No interaction records to analyze'}
        
        # Convert to DataFrame for analysis
        df = pd.DataFrame([asdict(record) for record in self.interaction_records])
        
        analysis = {
            'summary': self._generate_summary_statistics(df),
            'cultural_analysis': self._analyze_cultural_patterns(df),
            'psychological_constructs': self._analyze_psychological_constructs(df),
            'response_quality': self._analyze_response_quality(df),
            'behavioral_patterns': self._analyze_behavioral_patterns(df),
            'foundation_alignment': self._analyze_foundation_alignment(df),
            'demographic_insights': self._analyze_demographic_patterns(df),
            'recommendations': self._generate_recommendations(df)
        }
        
        return analysis
    
    def _generate_summary_statistics(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Generate summary statistics"""
        
        return {
            'total_interactions': len(df),
            'unique_agents': df['agent_id'].nunique(),
            'avg_response_length_words': round(df['response_length_words'].mean(), 1),
            'response_length_std': round(df['response_length_words'].std(), 1),
            'cultural_diversity': df['cultural_background'].nunique(),
            'age_range': [int(df['age'].min()), int(df['age'].max())],
            'avg_coherence_score': round(df['coherence_score'].mean(), 2),
            'avg_foundation_alignment': round(df['foundation_alignment_score'].mean(), 2),
            'scenario_types_covered': df['scenario_type'].unique().tolist(),
            'languages_represented': df['native_language'].unique().tolist()
        }
    
    def _analyze_cultural_patterns(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze patterns by cultural background"""
        
        cultural_analysis = {}
        
        for culture in df['cultural_background'].unique():
            if pd.isna(culture) or culture == '':
                continue
                
            culture_df = df[df['cultural_background'] == culture]
            
            cultural_analysis[culture] = {
                'n_participants': len(culture_df),
                'avg_response_length': round(culture_df['response_length_words'].mean(), 1),
                'avg_trust_level': round(culture_df['trust_level'].mean(), 2),
                'avg_authority_deference': round(culture_df['authority_deference'].mean(), 2),
                'common_constructs': self._get_common_constructs(culture_df),
                'response_quality': {
                    'coherence': round(culture_df['coherence_score'].mean(), 2),
                    'cultural_consistency': round(culture_df['cultural_consistency_score'].mean(), 2),
                    'foundation_alignment': round(culture_df['foundation_alignment_score'].mean(), 2)
                }
            }
        
        return cultural_analysis
    
    def _analyze_psychological_constructs(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze psychological construct manifestation"""
        
        constructs = ['cognitive_partnership', 'trust_calibration', 'agency_distribution', 
                     'metacognitive_awareness', 'cognitive_load_management']
        
        construct_analysis = {}
        
        for construct in constructs:
            # Find interactions where this construct was evident
            construct_records = df[df['psychological_constructs_evident'].apply(
                lambda x: construct in x if isinstance(x, list) else False
            )]
            
            if len(construct_records) > 0:
                construct_analysis[construct] = {
                    'frequency': len(construct_records),
                    'percentage': round(len(construct_records) / len(df) * 100, 1),
                    'cultural_distribution': construct_records['cultural_background'].value_counts().to_dict(),
                    'avg_response_quality': {
                        'coherence': round(construct_records['coherence_score'].mean(), 2),
                        'foundation_alignment': round(construct_records['foundation_alignment_score'].mean(), 2)
                    }
                }
        
        return construct_analysis
    
    def _analyze_response_quality(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze overall response quality metrics"""
        
        return {
            'coherence_distribution': {
                'mean': round(df['coherence_score'].mean(), 2),
                'std': round(df['coherence_score'].std(), 2),
                'min': round(df['coherence_score'].min(), 2),
                'max': round(df['coherence_score'].max(), 2)
            },
            'foundation_alignment_distribution': {
                'mean': round(df['foundation_alignment_score'].mean(), 2),
                'std': round(df['foundation_alignment_score'].std(), 2),
                'min': round(df['foundation_alignment_score'].min(), 2),
                'max': round(df['foundation_alignment_score'].max(), 2)
            },
            'quality_by_culture': df.groupby('cultural_background')[
                ['coherence_score', 'cultural_consistency_score', 'foundation_alignment_score']
            ].mean().round(2).to_dict(),
            'high_quality_responses': len(df[df['coherence_score'] > 0.8]),
            'low_quality_responses': len(df[df['coherence_score'] < 0.5])
        }
    
    def _analyze_behavioral_patterns(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze behavioral patterns across agents"""
        
        return {
            'trust_patterns': {
                'by_culture': df.groupby('cultural_background')['trust_level'].mean().round(2).to_dict(),
                'by_age_group': self._group_by_age(df, 'trust_level'),
                'overall_range': [round(df['trust_level'].min(), 2), round(df['trust_level'].max(), 2)]
            },
            'help_seeking_patterns': {
                'by_culture': df.groupby('cultural_background')['help_seeking_tendency'].mean().round(2).to_dict(),
                'by_emotional_state': df.groupby('emotional_state')['help_seeking_tendency'].mean().round(2).to_dict()
            },
            'authority_patterns': {
                'by_culture': df.groupby('cultural_background')['authority_deference'].mean().round(2).to_dict(),
                'by_ses': df.groupby('socioeconomic_status')['authority_deference'].mean().round(2).to_dict()
            }
        }
    
    def _analyze_foundation_alignment(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze alignment with foundation documents"""
        
        return {
            'overall_alignment': round(df['foundation_alignment_score'].mean(), 2),
            'alignment_by_culture': df.groupby('cultural_background')['foundation_alignment_score'].mean().round(2).to_dict(),
            'alignment_by_scenario': df.groupby('scenario_type')['foundation_alignment_score'].mean().round(2).to_dict(),
            'low_alignment_cases': len(df[df['foundation_alignment_score'] < 0.5]),
            'high_alignment_cases': len(df[df['foundation_alignment_score'] > 0.8]),
            'alignment_trends': self._analyze_alignment_trends(df)
        }
    
    def _analyze_demographic_patterns(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze patterns by demographic characteristics"""
        
        return {
            'age_patterns': {
                'response_length_by_age': self._group_by_age(df, 'response_length_words'),
                'trust_by_age': self._group_by_age(df, 'trust_level')
            },
            'gender_patterns': {
                'response_length_by_gender': df.groupby('gender')['response_length_words'].mean().round(1).to_dict(),
                'help_seeking_by_gender': df.groupby('gender')['help_seeking_tendency'].mean().round(2).to_dict()
            },
            'language_patterns': {
                'response_quality_by_proficiency': df.groupby('english_proficiency')['coherence_score'].mean().round(2).to_dict(),
                'response_length_by_native_language': df.groupby('native_language')['response_length_words'].mean().round(1).to_dict()
            }
        }
    
    def _group_by_age(self, df: pd.DataFrame, column: str) -> Dict[str, float]:
        """Group analysis by age ranges"""
        
        df_copy = df.copy()
        df_copy['age_group'] = pd.cut(df_copy['age'], 
                                     bins=[0, 18, 25, 35, 50, 100], 
                                     labels=['Under 18', '18-25', '26-35', '36-50', 'Over 50'])
        
        return df_copy.groupby('age_group')[column].mean().round(2).to_dict()
    
    def _get_common_constructs(self, culture_df: pd.DataFrame) -> List[str]:
        """Get most common psychological constructs for a cultural group"""
        
        all_constructs = []
        for constructs_list in culture_df['psychological_constructs_evident']:
            if isinstance(constructs_list, list):
                all_constructs.extend(constructs_list)
        
        if not all_constructs:
            return []
        
        # Count frequency and return top 3
        construct_counts = Counter(all_constructs)
        return [construct for construct, count in construct_counts.most_common(3)]
    
    def _analyze_alignment_trends(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze trends in foundation alignment"""
        
        return {
            'alignment_correlation_with_trust': round(df['foundation_alignment_score'].corr(df['trust_level']), 2),
            'alignment_correlation_with_coherence': round(df['foundation_alignment_score'].corr(df['coherence_score']), 2),
            'best_aligned_culture': df.groupby('cultural_background')['foundation_alignment_score'].mean().idxmax(),
            'most_variable_culture': df.groupby('cultural_background')['foundation_alignment_score'].std().idxmax()
        }
    
    def _generate_recommendations(self, df: pd.DataFrame) -> List[str]:
        """Generate research recommendations based on analysis"""
        
        recommendations = []
        
        # Data quality recommendations
        if df['coherence_score'].mean() > 0.7:
            recommendations.append("High response quality suggests simulation is suitable for research use")
        else:
            recommendations.append("Consider improving agent prompts to increase response coherence")
        
        # Cultural diversity recommendations
        if df['cultural_background'].nunique() >= 4:
            recommendations.append("Good cultural diversity achieved for cross-cultural research")
        else:
            recommendations.append("Consider adding more cultural backgrounds for comprehensive diversity")
        
        # Foundation alignment recommendations
        if df['foundation_alignment_score'].mean() > 0.6:
            recommendations.append("Strong foundation alignment validates theoretical consistency")
        else:
            recommendations.append("Review foundation document integration to improve theoretical alignment")
        
        # Sample size recommendations
        if len(df) > 100:
            recommendations.append("Sample size adequate for statistical analysis")
        else:
            recommendations.append("Consider increasing sample size for more robust statistical analysis")
        
        return recommendations
    
    def generate_research_report(self, analysis_results: Dict[str, Any], output_file: Path):
        """Generate comprehensive research report"""
        
        # Handle case where analysis failed due to no data
        if 'error' in analysis_results:
            report_content = f"""# Co-Thinking Research Simulation Analysis Report

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Analysis Status

**Error**: {analysis_results['error']}

This report could not be generated because no interaction data was available for analysis.

### Possible Causes:
1. No scenarios were successfully executed
2. API connection issues prevented agent responses
3. Data collection system failed to record interactions

### Recommended Actions:
1. Check API key configuration and connectivity
2. Review scenario execution logs for errors
3. Verify agent creation and initialization
4. Ensure data collection system is properly configured

---

*This report was generated automatically. Please resolve the underlying issues and re-run the simulation.*
"""
            with open(output_file, 'w') as f:
                f.write(report_content)
            return
        
        # Generate normal report when data is available
        report_content = f"""# Co-Thinking Research Simulation Analysis Report

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Executive Summary

This report analyzes {analysis_results['summary']['total_interactions']} interactions from {analysis_results['summary']['unique_agents']} diverse student agents across {analysis_results['summary']['cultural_diversity']} cultural backgrounds.

### Key Findings

- **Response Quality**: Average coherence score of {analysis_results['summary']['avg_coherence_score']}
- **Foundation Alignment**: Average alignment score of {analysis_results['summary']['avg_foundation_alignment']}
- **Cultural Diversity**: {analysis_results['summary']['cultural_diversity']} cultures represented
- **Age Range**: {analysis_results['summary']['age_range'][0]}-{analysis_results['summary']['age_range'][1]} years
- **Languages**: {len(analysis_results['summary']['languages_represented'])} different native languages

## Cultural Analysis

"""
        
        for culture, data in analysis_results['cultural_analysis'].items():
            report_content += f"""
### {culture}
- **Participants**: {data['n_participants']}
- **Average Response Length**: {data['avg_response_length']} words
- **Trust Level**: {data['avg_trust_level']}
- **Authority Deference**: {data['avg_authority_deference']}
- **Common Constructs**: {', '.join(data['common_constructs']) if data['common_constructs'] else 'None identified'}
- **Response Quality**:
  - Coherence: {data['response_quality']['coherence']}
  - Cultural Consistency: {data['response_quality']['cultural_consistency']}
  - Foundation Alignment: {data['response_quality']['foundation_alignment']}
"""
        
        report_content += f"""
## Psychological Constructs Analysis

"""
        
        for construct, data in analysis_results['psychological_constructs'].items():
            report_content += f"""
### {construct.replace('_', ' ').title()}
- **Frequency**: {data['frequency']} interactions ({data['percentage']}%)
- **Quality Metrics**:
  - Coherence: {data['avg_response_quality']['coherence']}
  - Foundation Alignment: {data['avg_response_quality']['foundation_alignment']}
"""
        
        report_content += f"""
## Foundation Document Alignment

- **Overall Alignment**: {analysis_results['foundation_alignment']['overall_alignment']}
- **High Alignment Cases**: {analysis_results['foundation_alignment']['high_alignment_cases']} interactions (>0.8)
- **Low Alignment Cases**: {analysis_results['foundation_alignment']['low_alignment_cases']} interactions (<0.5)

## Research Recommendations

"""
        
        for i, rec in enumerate(analysis_results['recommendations'], 1):
            report_content += f"{i}. {rec}\n"
        
        report_content += """

---

*This report was generated automatically from simulation data. For questions about methodology or findings, refer to the research framework documentation.*
"""
        
        with open(output_file, 'w') as f:
            f.write(report_content) 