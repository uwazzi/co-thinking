"""
Secure Configuration Management
Loads environment variables from .env file with validation and helpful error messages
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any, List
from dotenv import load_dotenv

class SecureConfig:
    """Secure configuration management for Co-Thinking Research System"""
    
    def __init__(self, env_file_path: Optional[str] = None):
        """
        Initialize secure configuration
        
        Args:
            env_file_path: Path to .env file (defaults to .env in project root)
        """
        self.project_root = Path(__file__).parent.parent.parent
        self.env_file_path = env_file_path or self.project_root / ".env"
        
        # Load environment variables
        self._load_environment()
        
        # Validate required settings
        self._validate_configuration()
    
    def _load_environment(self):
        """Load environment variables from .env file"""
        
        if self.env_file_path.exists():
            load_dotenv(self.env_file_path)
            print(f"✅ Loaded environment variables from {self.env_file_path}")
        else:
            print(f"⚠️  No .env file found at {self.env_file_path}")
            print(f"💡 To set up configuration:")
            print(f"   1. Create a .env file in the project root: {self.env_file_path}")
            print(f"   2. Add your API key: GEMINI_API_KEY=your_actual_api_key_here")
            print(f"   3. Get your API key from: https://makersuite.google.com/app/apikey")
    
    def _validate_configuration(self):
        """Validate that required configuration is present"""
        
        required_vars = {
            'GEMINI_API_KEY': 'Google Gemini API key'
        }
        
        missing_vars = []
        for var, description in required_vars.items():
            if not self.get(var):
                missing_vars.append(f"  - {var}: {description}")
        
        if missing_vars:
            print(f"❌ Missing required environment variables:")
            for var in missing_vars:
                print(var)
            print(f"\n💡 Setup instructions:")
            print(f"  1. Create a .env file in project root: {self.env_file_path}")
            print(f"  2. Add the following line:")
            print(f"     GEMINI_API_KEY=your_actual_api_key_here")
            print(f"  3. Get your Gemini API key from: https://makersuite.google.com/app/apikey")
            print(f"  4. Replace 'your_actual_api_key_here' with your real API key")
            print(f"\n📋 Example .env file content:")
            print(f"GEMINI_API_KEY=your_api_key_here")
            print(f"DEFAULT_AGENT_COUNT=20")
            print(f"DEBUG_MODE=false")
            raise ValueError("Missing required environment variables. Please create .env file with GEMINI_API_KEY.")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get environment variable with type conversion"""
        
        value = os.getenv(key, default)
        
        # Convert string booleans to actual booleans
        if isinstance(value, str):
            if value.lower() in ('true', '1', 'yes', 'on'):
                return True
            elif value.lower() in ('false', '0', 'no', 'off'):
                return False
            elif value.isdigit():
                return int(value)
            elif value.replace('.', '', 1).isdigit():
                return float(value)
        
        return value
    
    def get_list(self, key: str, default: List[str] = None, separator: str = ',') -> List[str]:
        """Get environment variable and split into list"""
        
        value = self.get(key)
        if not value:
            return default or []
        
        return [item.strip() for item in str(value).split(separator) if item.strip()]
    
    @property
    def gemini_api_key(self) -> str:
        """Get Gemini API key"""
        return self.get('GEMINI_API_KEY')
    
    @property
    def default_agent_count(self) -> int:
        """Get default number of agents"""
        return self.get('DEFAULT_AGENT_COUNT', 20)
    
    @property
    def default_research_context(self) -> str:
        """Get default research context"""
        return self.get('DEFAULT_RESEARCH_CONTEXT', 'university_diverse')
    
    @property
    def data_output_dir(self) -> str:
        """Get data output directory"""
        return self.get('DATA_OUTPUT_DIR', './simulation_data')
    
    @property
    def api_timeout(self) -> int:
        """Get API timeout in seconds"""
        return self.get('API_TIMEOUT', 30)
    
    @property
    def max_concurrent_requests(self) -> int:
        """Get maximum concurrent API requests"""
        return self.get('MAX_CONCURRENT_REQUESTS', 10)
    
    @property
    def debug_mode(self) -> bool:
        """Get debug mode setting"""
        return self.get('DEBUG_MODE', False)
    
    @property
    def log_level(self) -> str:
        """Get log level"""
        return self.get('LOG_LEVEL', 'INFO')
    
    @property
    def min_coherence_threshold(self) -> float:
        """Get minimum coherence threshold"""
        return self.get('MIN_COHERENCE_THRESHOLD', 0.5)
    
    @property
    def min_foundation_alignment(self) -> float:
        """Get minimum foundation alignment threshold"""
        return self.get('MIN_FOUNDATION_ALIGNMENT', 0.6)
    
    @property
    def enable_quality_filtering(self) -> bool:
        """Get quality filtering setting"""
        return self.get('ENABLE_QUALITY_FILTERING', True)
    
    @property
    def enabled_cultures(self) -> List[str]:
        """Get list of enabled cultures"""
        return self.get_list('ENABLED_CULTURES', [
            'us_individualistic', 'east_asian_collectivistic', 'european_balanced',
            'latin_american_familistic', 'middle_eastern_traditional', 'african_ubuntu'
        ])
    
    @property
    def export_formats(self) -> List[str]:
        """Get export formats"""
        return self.get_list('EXPORT_FORMATS', ['json', 'csv', 'excel', 'markdown'])
    
    @property
    def include_raw_responses(self) -> bool:
        """Get raw responses inclusion setting"""
        return self.get('INCLUDE_RAW_RESPONSES', True)
    
    @property
    def enable_auto_analysis(self) -> bool:
        """Get auto analysis setting"""
        return self.get('ENABLE_AUTO_ANALYSIS', True)
    
    def get_all_settings(self) -> Dict[str, Any]:
        """Get all configuration settings as dictionary"""
        
        return {
            'api': {
                'gemini_api_key': '***' if self.gemini_api_key else None,
                'api_timeout': self.api_timeout,
                'max_concurrent_requests': self.max_concurrent_requests
            },
            'research': {
                'default_agent_count': self.default_agent_count,
                'default_research_context': self.default_research_context,
                'data_output_dir': self.data_output_dir
            },
            'system': {
                'debug_mode': self.debug_mode,
                'log_level': self.log_level
            },
            'quality': {
                'min_coherence_threshold': self.min_coherence_threshold,
                'min_foundation_alignment': self.min_foundation_alignment,
                'enable_quality_filtering': self.enable_quality_filtering
            },
            'cultural': {
                'enabled_cultures': self.enabled_cultures,
                'enable_all_cultures': self.get('ENABLE_ALL_CULTURES', True)
            },
            'export': {
                'export_formats': self.export_formats,
                'include_raw_responses': self.include_raw_responses,
                'enable_auto_analysis': self.enable_auto_analysis
            }
        }
    
    def print_configuration_summary(self):
        """Print a summary of current configuration"""
        
        print("🔧 Co-Thinking Research System Configuration")
        print("=" * 50)
        
        settings = self.get_all_settings()
        
        for category, config in settings.items():
            print(f"\n📋 {category.title()} Settings:")
            for key, value in config.items():
                if isinstance(value, list):
                    print(f"  - {key}: {', '.join(map(str, value))}")
                else:
                    print(f"  - {key}: {value}")

# Create global config instance
def get_config() -> SecureConfig:
    """Get global configuration instance"""
    return SecureConfig()

# Convenience function for getting API key
def get_api_key() -> str:
    """Get API key with helpful error message"""
    try:
        config = get_config()
        return config.gemini_api_key
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        return None 