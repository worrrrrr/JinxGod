"""
Bazi Shen Sha Calculator - ระบบคำนวณเทพ煞 (Symbolic Stars)
คำนวณเทพเจ้าและ煞ต่างๆ ในดวงปาจื้อ
"""

from typing import Dict, List, Optional
from datetime import datetime

class ShenShaCalculator:
    def __init__(self):
        self.HEAVENLY_STEMS = ['Jia', 'Yi', 'Bing', 'Ding', 'Wu', 'Ji', 'Geng', 'Xin', 'Ren', 'Gui']
        self.EARTHLY_BRANCHES = ['Zi', 'Chou', 'Yin', 'Mao', 'Chen', 'Si', 'Wu', 'Wei', 'Shen', 'You', 'Xu', 'Hai']
        
        self.STEM_ELEMENTS = {
            'Jia': 'Wood', 'Yi': 'Wood',
            'Bing': 'Fire', 'Ding': 'Fire',
            'Wu': 'Earth', 'Ji': 'Earth',
            'Geng': 'Metal', 'Xin': 'Metal',
            'Ren': 'Water', 'Gui': 'Water'
        }
        
        self.BRANCH_ELEMENTS = {
            'Zi': 'Water', 'Chou': 'Earth', 'Yin': 'Wood', 'Mao': 'Wood',
            'Chen': 'Earth', 'Si': 'Fire', 'Wu': 'Fire', 'Wei': 'Earth',
            'Shen': 'Metal', 'You': 'Metal', 'Xu': 'Earth', 'Hai': 'Water'
        }
        
        # Nobleman locations by Day Master
        self.TIAN_YI_GUI_REN = {
            'Jia': ['Chou', 'Wei'], 'Yi': ['Zi', 'Shen'],
            'Bing': ['You', 'Hai'], 'Ding': ['Hai', 'You'],
            'Wu': ['Chou', 'Wei'], 'Ji': ['Zi', 'Shen'],
            'Geng': ['Chou', 'Wei'], 'Xin': ['Yin', 'Wu'],
            'Ren': ['Mao', 'Si'], 'Gui': ['Si', 'Mao']
        }
        
        # Wen Chang (Academic Star) locations
        self.WEN_CHANG = {
            'Jia': 'Si', 'Yi': 'Wu', 'Bing': 'Shen', 'Ding': 'You',
            'Wu': 'Shen', 'Ji': 'You', 'Geng': 'Hai', 'Xin': 'Zi',
            'Ren': 'Yin', 'Gui': 'Mao'
        }
        
        # Peach Blossom (Romance Star) locations by branch
        self.TAO_HUA = {
            'Shen': 'You', 'Zi': 'You', 'Chen': 'You',  # Monkey, Rat, Dragon -> Rooster
            'Yin': 'Mao', 'Wu': 'Mao', 'Xu': 'Mao',      # Tiger, Horse, Dog -> Rabbit
            'Si': 'Wu', 'You': 'Wu', 'Chou': 'Wu',       # Snake, Rooster, Ox -> Horse
            'Hai': 'Zi', 'Mao': 'Zi', 'Wei': 'Zi'        # Pig, Rabbit, Goat -> Rat
        }
        
        # Hua Gai (Artistic Star) locations
        self.HUA_GAI = {
            'Shen': 'Chen', 'Zi': 'Chen', 'Chen': 'Chen',
            'Yin': 'Xu', 'Wu': 'Xu', 'Xu': 'Xu',
            'Si': 'Chou', 'You': 'Chou', 'Chou': 'Chou',
            'Hai': 'Wei', 'Mao': 'Wei', 'Wei': 'Wei'
        }
        
        # Yi Ma (Travel Star) locations
        self.YI_MA = {
            'Shen': 'Yin', 'Zi': 'Yin', 'Chen': 'Yin',
            'Yin': 'Shen', 'Wu': 'Shen', 'Xu': 'Shen',
            'Si': 'Hai', 'You': 'Hai', 'Chou': 'Hai',
            'Hai': 'Si', 'Mao': 'Si', 'Wei': 'Si'
        }
        
        # Jie Sha (Robber Star) locations
        self.JIE_SHA = {
            'Yin': 'Si', 'Mao': 'Wu', 'Chen': 'Wei', 'Si': 'Shen',
            'Wu': 'You', 'Wei': 'Xu', 'Shen': 'Hai', 'You': 'Zi',
            'Xu': 'Chou', 'Hai': 'Yin', 'Zi': 'Mao', 'Chou': 'Chen'
        }
        
        # Yang Ren (Blade Star) locations
        self.YANG_REN = {
            'Jia': 'Mao', 'Yi': 'Chen', 'Bing': 'Wu', 'Ding': 'Wei',
            'Wu': 'Wu', 'Ji': 'Wei', 'Geng': 'You', 'Xin': 'Xu',
            'Ren': 'Zi', 'Gui': 'Chou'
        }
    
    def calculate_shen_sha(self, pillars: Dict, day_stem: str, 
                           year_branch: str, day_branch: str) -> Dict:
        """
        Calculate all Symbolic Stars (Shen Sha) in the chart
        
        Args:
            pillars: Four pillars dictionary
            day_stem: Day Master heavenly stem
            year_branch: Year earthly branch
            day_branch: Day earthly branch
            
        Returns:
            Dictionary containing all Shen Sha information
        """
        shen_sha = {
            'tian_yi_gui_ren': self._find_tian_yi_gui_ren(pillars, day_stem),
            'wen_chang': self._find_wen_chang(pillars, day_stem),
            'tao_hua': self._find_tao_hua(pillars, year_branch),
            'hua_gai': self._find_hua_gai(pillars, year_branch),
            'yi_ma': self._find_yi_ma(pillars, year_branch),
            'jie_sha': self._find_jie_sha(pillars, year_branch),
            'yang_ren': self._find_yang_ren(pillars, day_stem),
            'general_interpretation': {}
        }
        
        # Add general interpretation
        shen_sha['general_interpretation'] = self._interpret_shen_sha(shen_sha)
        
        return shen_sha
    
    def _find_tian_yi_gui_ren(self, pillars: Dict, day_stem: str) -> List[Dict]:
        """Find Tian Yi Gui Ren (Heavenly Nobleman) stars"""
        noble_locations = self.TIAN_YI_GUI_REN.get(day_stem, [])
        found = []
        
        for pillar_name, pillar_data in pillars.items():
            branch = pillar_data['earthly_branch']
            if branch in noble_locations:
                found.append({
                    'pillar': pillar_name,
                    'branch': branch,
                    'star': 'Tian Yi Gui Ren',
                    'meaning': 'Noble help, protection from difficulties, good fortune'
                })
        
        return found
    
    def _find_wen_chang(self, pillars: Dict, day_stem: str) -> List[Dict]:
        """Find Wen Chang (Academic Excellence) stars"""
        wen_chang_location = self.WEN_CHANG.get(day_stem)
        found = []
        
        if wen_chang_location:
            for pillar_name, pillar_data in pillars.items():
                branch = pillar_data['earthly_branch']
                if branch == wen_chang_location:
                    found.append({
                        'pillar': pillar_name,
                        'branch': branch,
                        'star': 'Wen Chang',
                        'meaning': 'Academic success, intelligence, literary talent'
                    })
        
        return found
    
    def _find_tao_hua(self, pillars: Dict, year_branch: str) -> List[Dict]:
        """Find Tao Hua (Peach Blossom) romance stars"""
        tao_hua_location = self.TAO_HUA.get(year_branch)
        found = []
        
        if tao_hua_location:
            for pillar_name, pillar_data in pillars.items():
                branch = pillar_data['earthly_branch']
                if branch == tao_hua_location:
                    found.append({
                        'pillar': pillar_name,
                        'branch': branch,
                        'star': 'Tao Hua',
                        'meaning': 'Romance, charm, attractiveness, social appeal'
                    })
        
        return found
    
    def _find_hua_gai(self, pillars: Dict, year_branch: str) -> List[Dict]:
        """Find Hua Gai (Artistic/Religious) stars"""
        hua_gai_location = self.HUA_GAI.get(year_branch)
        found = []
        
        if hua_gai_location:
            for pillar_name, pillar_data in pillars.items():
                branch = pillar_data['earthly_branch']
                if branch == hua_gai_location:
                    found.append({
                        'pillar': pillar_name,
                        'branch': branch,
                        'star': 'Hua Gai',
                        'meaning': 'Artistic talent, spiritual inclination, solitude'
                    })
        
        return found
    
    def _find_yi_ma(self, pillars: Dict, year_branch: str) -> List[Dict]:
        """Find Yi Ma (Travel/Change) stars"""
        yi_ma_location = self.YI_MA.get(year_branch)
        found = []
        
        if yi_ma_location:
            for pillar_name, pillar_data in pillars.items():
                branch = pillar_data['earthly_branch']
                if branch == yi_ma_location:
                    found.append({
                        'pillar': pillar_name,
                        'branch': branch,
                        'star': 'Yi Ma',
                        'meaning': 'Travel, relocation, career changes, movement'
                    })
        
        return found
    
    def _find_jie_sha(self, pillars: Dict, year_branch: str) -> List[Dict]:
        """Find Jie Sha (Robber/Obstacle) stars"""
        jie_sha_location = self.JIE_SHA.get(year_branch)
        found = []
        
        if jie_sha_location:
            for pillar_name, pillar_data in pillars.items():
                branch = pillar_data['earthly_branch']
                if branch == jie_sha_location:
                    found.append({
                        'pillar': pillar_name,
                        'branch': branch,
                        'star': 'Jie Sha',
                        'meaning': 'Obstacles, competition, potential losses, challenges'
                    })
        
        return found
    
    def _find_yang_ren(self, pillars: Dict, day_stem: str) -> List[Dict]:
        """Find Yang Ren (Blade/Intensity) stars"""
        yang_ren_location = self.YANG_REN.get(day_stem)
        found = []
        
        if yang_ren_location:
            for pillar_name, pillar_data in pillars.items():
                branch = pillar_data['earthly_branch']
                if branch == yang_ren_location:
                    found.append({
                        'pillar': pillar_name,
                        'branch': branch,
                        'star': 'Yang Ren',
                        'meaning': 'Intensity, determination, potential conflict, strong will'
                    })
        
        return found
    
    def _interpret_shen_sha(self, shen_sha: Dict) -> Dict:
        """Provide general interpretation of Shen Sha presence"""
        interpretation = {
            'positive_stars_count': 0,
            'challenging_stars_count': 0,
            'summary': [],
            'advice': []
        }
        
        # Count positive stars
        positive_categories = ['tian_yi_gui_ren', 'wen_chang', 'tao_hua', 'hua_gai', 'yi_ma']
        for category in positive_categories:
            interpretation['positive_stars_count'] += len(shen_sha.get(category, []))
        
        # Count challenging stars
        challenging_categories = ['jie_sha', 'yang_ren']
        for category in challenging_categories:
            interpretation['challenging_stars_count'] += len(shen_sha.get(category, []))
        
        # Generate summary
        if interpretation['positive_stars_count'] > 3:
            interpretation['summary'].append("Many auspicious stars present - generally favorable chart")
        elif interpretation['positive_stars_count'] == 0:
            interpretation['summary'].append("Few auspicious stars - rely on personal effort")
        
        if interpretation['challenging_stars_count'] > 2:
            interpretation['summary'].append("Several challenging stars - need caution and strategic planning")
        
        # Generate advice
        if shen_sha['tian_yi_gui_ren']:
            interpretation['advice'].append("Seek help from mentors and nobles when facing difficulties")
        if shen_sha['wen_chang']:
            interpretation['advice'].append("Focus on education and continuous learning")
        if shen_sha['tao_hua']:
            interpretation['advice'].append("Use charm wisely in relationships and networking")
        if shen_sha['yi_ma']:
            interpretation['advice'].append("Be open to travel and new opportunities")
        if shen_sha['jie_sha']:
            interpretation['advice'].append("Avoid risky investments and competitive situations")
        if shen_sha['yang_ren']:
            interpretation['advice'].append("Channel intensity into productive activities, avoid conflicts")
        
        return interpretation
