"""
Bazi Liu Nian Calculator - ระบบคำนวณ流年 (Annual Luck Pillars)
คำนวณดวงรายปีสำหรับแต่ละปี
"""

from typing import Dict, List
from datetime import datetime

class LiuNianCalculator:
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
        
        # 12 Life Stages (Chang Sheng Shi Er Shen)
        self.LIFE_STAGES = [
            'Birth (Chang Sheng)', 
            'Bathing (Mu Yu)', 
            'Building Up (Guan Dai)', 
            'Reaching Maturity (Lin Guan)', 
            'Prosperity (Di Wang)', 
            'Decline (Shuai)', 
            'Sickness (Bing)', 
            'Death (Si)', 
            'Burial (Mu)', 
            'Extinction (Jue)', 
            'Conception (Tai)', 
            'Nurturing (Yang)'
        ]
    
    def calculate_liu_nian(self, birth_year: int, start_year: int, end_year: int,
                           day_master_element: str, day_master_yy: str) -> List[Dict]:
        """
        Calculate Annual Luck Pillars (Liu Nian) for a range of years
        
        Args:
            birth_year: Year of birth
            start_year: Starting year for calculation
            end_year: Ending year for calculation
            day_master_element: Element of Day Master
            day_master_yy: Yin/Yang of Day Master
            
        Returns:
            List of dictionaries containing annual luck information
        """
        liu_nian_results = []
        
        for year in range(start_year, end_year + 1):
            age = year - birth_year
            
            # Calculate year pillar
            stem_idx = (year - 4) % 10
            branch_idx = (year - 4) % 12
            
            year_stem = self.HEAVENLY_STEMS[stem_idx]
            year_branch = self.EARTHLY_BRANCHES[branch_idx]
            
            # Get elements and yin/yang
            stem_element = self.STEM_ELEMENTS[year_stem]
            branch_element = self.BRANCH_ELEMENTS[year_branch]
            stem_yy = 'Yang' if stem_idx % 2 == 0 else 'Yin'
            branch_yy = 'Yang' if branch_idx % 2 == 0 else 'Yin'
            
            # Calculate Ten Gods relationship with Day Master
            ten_god = self._get_ten_god(day_master_element, day_master_yy, 
                                       stem_element, stem_yy)
            
            # Calculate Life Stage based on age
            life_stage_idx = age % 12
            life_stage = self.LIFE_STAGES[life_stage_idx]
            
            # Assess year quality
            year_quality = self._assess_year_quality(
                day_master_element, stem_element, branch_element
            )
            
            # Check for clashes, combinations, harms
            interactions = self._check_interactions(year_branch)
            
            year_info = {
                'year': year,
                'age': age,
                'heavenly_stem': year_stem,
                'earthly_branch': year_branch,
                'stem_element': stem_element,
                'branch_element': branch_element,
                'stem_yin_yang': stem_yy,
                'branch_yin_yang': branch_yy,
                'ten_god': ten_god,
                'life_stage': life_stage,
                'quality': year_quality,
                'interactions': interactions
            }
            
            liu_nian_results.append(year_info)
        
        return liu_nian_results
    
    def _get_ten_god(self, dm_element: str, dm_yy: str, 
                     stem_element: str, stem_yy: str) -> str:
        """Calculate Ten Gods relationship"""
        # Simplified Ten Gods calculation
        if dm_element == stem_element:
            return 'Friend' if dm_yy == stem_yy else 'Rob Wealth'
        
        productive_cycle = {'Wood': 'Fire', 'Fire': 'Earth', 'Earth': 'Metal', 
                           'Metal': 'Water', 'Water': 'Wood'}
        controlling_cycle = {'Wood': 'Earth', 'Fire': 'Metal', 'Earth': 'Water', 
                            'Metal': 'Wood', 'Water': 'Fire'}
        
        if productive_cycle.get(dm_element) == stem_element:
            return 'Eating God' if dm_yy == stem_yy else 'Hurting Officer'
        elif productive_cycle.get(stem_element) == dm_element:
            return 'Direct Resource' if dm_yy != stem_yy else 'Indirect Resource'
        elif controlling_cycle.get(dm_element) == stem_element:
            return 'Direct Wealth' if dm_yy != stem_yy else 'Indirect Wealth'
        elif controlling_cycle.get(stem_element) == dm_element:
            return 'Direct Officer' if dm_yy != stem_yy else 'Seven Killings'
        
        return 'Unknown'
    
    def _assess_year_quality(self, dm_element: str, stem_elem: str, branch_elem: str) -> str:
        """Assess the general quality of the year"""
        supportive_elements = {
            'Wood': ['Water', 'Wood'],
            'Fire': ['Wood', 'Fire'],
            'Earth': ['Fire', 'Earth'],
            'Metal': ['Earth', 'Metal'],
            'Water': ['Metal', 'Water']
        }
        
        favorable = supportive_elements.get(dm_element, [])
        
        support_count = 0
        if stem_elem in favorable:
            support_count += 1
        if branch_elem in favorable:
            support_count += 1
        
        if support_count == 2:
            return "Very Favorable"
        elif support_count == 1:
            return "Moderately Favorable"
        else:
            return "Challenging"
    
    def _check_interactions(self, branch: str) -> Dict:
        """Check for clashes, combinations, and harms with the year branch"""
        # Six Clashes (Liu Chong)
        clashes = {
            'Zi': 'Wu', 'Chou': 'Wei', 'Yin': 'Shen',
            'Mao': 'You', 'Chen': 'Xu', 'Si': 'Hai',
            'Wu': 'Zi', 'Wei': 'Chou', 'Shen': 'Yin',
            'You': 'Mao', 'Xu': 'Chen', 'Hai': 'Si'
        }
        
        # Six Combinations (Liu He)
        combinations = {
            'Zi': 'Chou', 'Yin': 'Hai', 'Mao': 'Xu',
            'Chen': 'You', 'Si': 'Shen', 'Wu': 'Wei'
        }
        
        # Six Harms (Liu Hai)
        harms = {
            'Zi': 'Wei', 'Chou': 'Wu', 'Yin': 'Si',
            'Mao': 'Chen', 'Shen': 'Hai', 'You': 'Xu'
        }
        
        return {
            'clash_with': clashes.get(branch, 'None'),
            'combine_with': combinations.get(branch, 'None'),
            'harm_with': harms.get(branch, 'None')
        }
    
    def get_current_liu_nian(self, liu_nian_list: List[Dict], current_year: int) -> Dict:
        """Get the current year's luck pillar"""
        for year_info in liu_nian_list:
            if year_info['year'] == current_year:
                return year_info
        return None
