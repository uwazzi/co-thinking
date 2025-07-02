"""
Response Analysis System
Detailed analysis of individual agent responses for quality and theoretical alignment
"""

import re
from typing import Dict, List, Any

class ResponseAnalyzer:
    """Detailed analysis of individual agent responses"""
    
    def __init__(self):
        # Foundation document keywords for alignment assessment
        self.foundation_keywords = {
            'mollick': ['partner', 'collaboration', 'human agency', 'trust', 'amplify', 'cognitive partner'],
            'swiss_ai': ['transparency', 'human dignity', 'privacy', 'ethical', 'explainable', 'human-centered'],
            'people_factor': ['user experience', 'training', 'support', 'diversity', 'human impact', 'adaptive']
        }
        
        # Psychological construct indicators
        self.construct_indicators = {
            'cognitive_partnership': ['together', 'collaborate', 'partner', 'work with', 'team up', 'combine'],
            'trust_calibration': ['trust', 'reliable', 'depend', 'confidence', 'believe', 'verify'],
            'agency_distribution': ['control', 'decide', 'choice', 'authority', 'responsibility', 'ownership'],
            'metacognitive_awareness': ['understand', 'know', 'aware', 'realize', 'recognize', 'learn about'],
            'cognitive_load_management': ['easier', 'difficult', 'overwhelming', 'manage', 'handle', 'process']
        }
    
    def analyze_response(self, response: str, profile: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Comprehensive analysis of a single response"""
        
        if not response or not response.strip():
            return self._empty_response_analysis()
        
        return {
            'coherence_score': self._calculate_coherence(response),
            'cultural_consistency': self._assess_cultural_consistency(response, profile),
            'foundation_alignment': self._assess_foundation_alignment(response),
            'question_types': self._identify_question_types(response),
            'response_categories': self._categorize_response(response),
            'constructs_evident': self._identify_constructs(response),
            'linguistic_analysis': self._analyze_linguistic_features(response, profile),
            'emotional_indicators': self._identify_emotional_indicators(response),
            'complexity_score': self._calculate_complexity(response)
        }
    
    def _empty_response_analysis(self) -> Dict[str, Any]:
        """Default analysis for empty responses"""
        return {
            'coherence_score': 0.0,
            'cultural_consistency': 0.0,
            'foundation_alignment': 0.0,
            'question_types': [],
            'response_categories': ['empty'],
            'constructs_evident': [],
            'linguistic_analysis': {},
            'emotional_indicators': [],
            'complexity_score': 0.0
        }
    
    def _calculate_coherence(self, response: str) -> float:
        """Calculate response coherence score"""
        
        sentences = [s.strip() for s in response.split('.') if s.strip()]
        if len(sentences) < 1:
            return 0.0
        
        coherence_factors = []
        
        # Factor 1: Sentence structure quality
        substantial_sentences = len([s for s in sentences if len(s.split()) > 4])
        coherence_factors.append(substantial_sentences / max(1, len(sentences)))
        
        # Factor 2: Logical connectives
        connectives = len(re.findall(r'\b(because|since|therefore|however|although|but|and|so|thus)\b', 
                                   response, re.IGNORECASE))
        coherence_factors.append(min(1.0, connectives / 5))
        
        # Factor 3: Personal engagement indicators
        personal_refs = len(re.findall(r'\b(I think|I believe|In my opinion|I would|I feel)\b', 
                                     response, re.IGNORECASE))
        coherence_factors.append(min(1.0, personal_refs / 3))
        
        # Factor 4: Question-answer alignment (if context available)
        coherence_factors.append(0.8)  # Placeholder - could be enhanced with NLP
        
        return sum(coherence_factors) / len(coherence_factors)
    
    def _assess_cultural_consistency(self, response: str, profile: Dict[str, Any]) -> float:
        """Assess consistency with cultural background"""
        
        culture = profile.get('culture', '')
        response_lower = response.lower()
        
        if 'individualistic' in culture.lower():
            # Look for individual-focused language
            individual_markers = len(re.findall(r'\b(i|my|myself|personally|individual)\b', response_lower))
            return min(1.0, individual_markers / 8)
            
        elif 'collectivistic' in culture.lower():
            # Look for group-focused language
            collective_markers = len(re.findall(r'\b(we|our|together|group|community|family|collective)\b', response_lower))
            return min(1.0, collective_markers / 6)
            
        elif 'balanced' in culture.lower():
            # Look for balanced individual and collective language
            individual_count = len(re.findall(r'\b(i|my|myself)\b', response_lower))
            collective_count = len(re.findall(r'\b(we|our|together)\b', response_lower))
            balance_score = 1.0 - abs(individual_count - collective_count) / max(1, individual_count + collective_count)
            return balance_score
            
        else:
            return 0.7  # Default for unknown cultures
    
    def _assess_foundation_alignment(self, response: str) -> float:
        """Assess alignment with foundation document principles"""
        
        response_lower = response.lower()
        alignment_scores = []
        
        for source, terms in self.foundation_keywords.items():
            matches = sum(1 for term in terms if term.lower() in response_lower)
            score = min(1.0, matches / len(terms))
            alignment_scores.append(score)
        
        return sum(alignment_scores) / len(alignment_scores)
    
    def _identify_question_types(self, response: str) -> List[str]:
        """Identify types of questions or queries in response"""
        
        question_types = []
        
        # Factual questions
        if re.search(r'\b(what|how|why|when|where)\b.*\?', response, re.IGNORECASE):
            question_types.append('factual_question')
        
        # Help requests
        if re.search(r'\b(could you|can you|would you|please|help me)\b', response, re.IGNORECASE):
            question_types.append('request_for_help')
        
        # Confirmation seeking
        if re.search(r'\b(is this|am I|should I|correct|right)\b.*\?', response, re.IGNORECASE):
            question_types.append('confirmation_seeking')
        
        # Clarification requests
        if re.search(r'\b(explain|clarify|elaborate|mean|understand)\b', response, re.IGNORECASE):
            question_types.append('clarification_request')
        
        # Hypothetical/exploratory
        if re.search(r'\b(what if|suppose|imagine|would it)\b', response, re.IGNORECASE):
            question_types.append('hypothetical_question')
        
        return question_types
    
    def _categorize_response(self, response: str) -> List[str]:
        """Categorize the type of response"""
        
        categories = []
        response_lower = response.lower()
        
        # Emotional tone categories
        if any(word in response_lower for word in ['thank', 'appreciate', 'helpful', 'great']):
            categories.append('appreciative')
        if any(word in response_lower for word in ['confused', 'unsure', 'unclear', 'don\'t understand']):
            categories.append('uncertain')
        if any(word in response_lower for word in ['agree', 'correct', 'right', 'yes', 'exactly']):
            categories.append('agreeable')
        if any(word in response_lower for word in ['however', 'but', 'disagree', 'different', 'not sure']):
            categories.append('questioning')
        
        # Content categories
        if len(re.findall(r'\b(example|instance|like|such as)\b', response_lower)) > 0:
            categories.append('example_seeking')
        if len(re.findall(r'\b(step|first|then|next|finally)\b', response_lower)) > 1:
            categories.append('procedural')
        if len(re.findall(r'\b(think|believe|opinion|feel|perspective)\b', response_lower)) > 0:
            categories.append('reflective')
        
        return categories if categories else ['neutral']
    
    def _identify_constructs(self, response: str) -> List[str]:
        """Identify psychological constructs evident in response"""
        
        constructs = []
        response_lower = response.lower()
        
        for construct, indicators in self.construct_indicators.items():
            if any(indicator in response_lower for indicator in indicators):
                constructs.append(construct)
        
        return constructs
    
    def _analyze_linguistic_features(self, response: str, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze linguistic features of the response"""
        
        words = response.split()
        sentences = [s.strip() for s in response.split('.') if s.strip()]
        
        return {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'avg_sentence_length': len(words) / max(1, len(sentences)),
            'complex_words': len([w for w in words if len(w) > 6]),
            'question_count': response.count('?'),
            'exclamation_count': response.count('!'),
            'proficiency_consistency': self._assess_proficiency_consistency(response, profile)
        }
    
    def _assess_proficiency_consistency(self, response: str, profile: Dict[str, Any]) -> float:
        """Assess if response complexity matches stated English proficiency"""
        
        proficiency = profile.get('english_proficiency', 'Advanced')
        
        # Calculate response complexity
        words = response.split()
        complex_words = len([w for w in words if len(w) > 6])
        complex_ratio = complex_words / max(1, len(words))
        
        # Map proficiency to expected complexity
        expected_complexity = {
            'Native': 0.3,
            'Advanced': 0.25,
            'Intermediate': 0.15,
            'Beginner': 0.05
        }
        
        expected = expected_complexity.get(proficiency, 0.2)
        consistency = 1.0 - abs(complex_ratio - expected) / max(expected, 0.1)
        
        return max(0.0, min(1.0, consistency))
    
    def _identify_emotional_indicators(self, response: str) -> List[str]:
        """Identify emotional indicators in the response"""
        
        emotions = []
        response_lower = response.lower()
        
        emotion_patterns = {
            'excitement': ['excited', 'amazing', 'awesome', 'love', 'fantastic'],
            'anxiety': ['worried', 'nervous', 'anxious', 'scared', 'afraid'],
            'confidence': ['confident', 'sure', 'certain', 'definitely', 'absolutely'],
            'confusion': ['confused', 'lost', 'unclear', 'puzzled', 'bewildered'],
            'frustration': ['frustrated', 'annoying', 'difficult', 'struggling', 'hard'],
            'satisfaction': ['satisfied', 'pleased', 'happy', 'glad', 'content']
        }
        
        for emotion, indicators in emotion_patterns.items():
            if any(indicator in response_lower for indicator in indicators):
                emotions.append(emotion)
        
        return emotions
    
    def _calculate_complexity(self, response: str) -> float:
        """Calculate overall response complexity"""
        
        if not response.strip():
            return 0.0
        
        words = response.split()
        sentences = [s.strip() for s in response.split('.') if s.strip()]
        
        complexity_factors = []
        
        # Lexical complexity
        unique_words = len(set(word.lower() for word in words))
        lexical_diversity = unique_words / max(1, len(words))
        complexity_factors.append(lexical_diversity)
        
        # Syntactic complexity
        avg_sentence_length = len(words) / max(1, len(sentences))
        syntactic_complexity = min(1.0, avg_sentence_length / 15)  # Normalize to 15 words
        complexity_factors.append(syntactic_complexity)
        
        # Semantic complexity (based on conjunctions and complex structures)
        complex_structures = len(re.findall(r'\b(although|however|nevertheless|furthermore|consequently)\b', 
                                          response, re.IGNORECASE))
        semantic_complexity = min(1.0, complex_structures / 3)
        complexity_factors.append(semantic_complexity)
        
        return sum(complexity_factors) / len(complexity_factors)
    
    def generate_response_summary(self, analysis: Dict[str, Any]) -> str:
        """Generate a human-readable summary of response analysis"""
        
        summary_parts = []
        
        # Quality assessment
        coherence = analysis['coherence_score']
        if coherence > 0.8:
            summary_parts.append("High coherence")
        elif coherence > 0.6:
            summary_parts.append("Moderate coherence")
        else:
            summary_parts.append("Low coherence")
        
        # Foundation alignment
        alignment = analysis['foundation_alignment']
        if alignment > 0.7:
            summary_parts.append("strong foundation alignment")
        elif alignment > 0.5:
            summary_parts.append("moderate foundation alignment")
        else:
            summary_parts.append("weak foundation alignment")
        
        # Constructs present
        constructs = analysis['constructs_evident']
        if constructs:
            summary_parts.append(f"exhibits {', '.join(constructs)}")
        
        # Emotional tone
        emotions = analysis['emotional_indicators']
        if emotions:
            summary_parts.append(f"shows {', '.join(emotions[:2])}")
        
        return f"Response shows {', '.join(summary_parts[:3])}" 