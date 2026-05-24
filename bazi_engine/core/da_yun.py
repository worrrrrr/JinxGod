"""
Bazi Da Yun Calculator - ระบบคำนวณ大运 (10-Year Luck Pillars)
คำนวณช่วงโชคแต่ละสิบปีของชีวิต
"""

from typing import Dict, List, Tuple
from datetime import datetime

class DaYunCalculator:
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
    
    def calculate_da_yun(self, birth_datetime: str, gender: str, 
                         year_stem: str, month_pillar: Tuple[str, str]) -> Dict:
        """
        Calculate 10-Year Luck Pillars (Da Yun)
        
        Args:
            birth_datetime: Birth date and time
            gender: 'male' or 'female'
            year_stem: Year heavenly stem
            month_pillar: (stem, branch) of month pillar
        
        Returns:
            Dictionary containing Da Yun information
        """
        dt = datetime.strptime(birth_datetime, "%Y-%m-%d %H:%M")
        birth_year = dt.year
        
        # Determine direction based on gender and year polarity
        year_stem_idx = self.HEAVENLY_STEMS.index(year_stem)
        is_yang_year = year_stem_idx in [0, 2, 4, 6, 8]  # Yang stems: Jia, Bing, Wu, Geng, Ren
        
        if gender.lower() == 'male':
            forward = is_yang_year
        else:  # female
            forward = not is_yang_year
        
        # Starting age for Da Yun (typically 3-8 years old)
        starting_age = self._calculate_starting_age(birth_datetime, gender, year_stem, forward)
        
        # Get month pillar index
        month_stem, month_branch = month_pillar
        month_stem_idx = self.HEAVENLY_STEMS.index(month_stem)
        month_branch_idx = self.EARTHLY_BRANCHES.index(month_branch)
        
        # Calculate 8-10 periods of Da Yun
        da_yun_periods = []
        current_stem_idx = month_stem_idx
        current_branch_idx = month_branch_idx
        
        for i in range(8):
            if forward:
                current_stem_idx = (month_stem_idx + i) % 10
                current_branch_idx = (month_branch_idx + i) % 12
            else:
                current_stem_idx = (month_stem_idx - i) % 10
                current_branch_idx = (month_branch_idx - i) % 12
            
            period_start_age = starting_age + (i * 10)
            period_end_age = period_start_age + 9
            start_year = birth_year + period_start_age
            end_year = birth_year + period_end_age
            
            stem = self.HEAVENLY_STEMS[current_stem_idx]
            branch = self.EARTHLY_BRANCHES[current_branch_idx]
            
            period_info = {
                'period_number': i + 1,
                'start_age': period_start_age,
                'end_age': period_end_age,
                'start_year': start_year,
                'end_year': end_year,
                'heavenly_stem': stem,
                'earthly_branch': branch,
                'stem_element': self.STEM_ELEMENTS[stem],
                'branch_element': self.BRANCH_ELEMENTS[branch],
                'stem_yin_yang': 'Yang' if current_stem_idx in [0, 2, 4, 6, 8] else 'Yin',
                'branch_yin_yang': 'Yang' if current_branch_idx in [0, 2, 4, 6, 8, 10] else 'Yin',
                'quality': self._assess_period_quality(stem, branch)
            }
            
            da_yun_periods.append(period_info)
        
        return {
            'starting_age': starting_age,
            'direction': 'forward' if forward else 'backward',
            'is_yang_year': is_yang_year,
            'periods': da_yun_periods
        }
    
    def _calculate_starting_age(self, birth_datetime: str, gender: str, 
                                year_stem: str, forward: bool) -> int:
        """
        Calculate the starting age for Da Yun based on distance to nearest solar term
        Simplified calculation - typically between 3-8 years
        """
        dt = datetime.strptime(birth_datetime, "%Y-%m-%d %H:%M")
        
        # Simplified: Use a base of 4 years with slight variation
        # In full implementation, this would calculate exact days to solar term
        base_age = 4
        
        # Add variation based on birth month
        month_variation = (dt.month % 3) * 0.5
        
        starting_age = int(base_age + month_variation)
        
        return max(3, min(8, starting_age))
    
    def _assess_period_quality(self, stem: str, branch: str) -> str:
        """
        Assess the general quality of a Da Yun period
        This is a simplified assessment
        """
        stem_elem = self.STEM_ELEMENTS[stem]
        branch_elem = self.BRANCH_ELEMENTS[branch]
        
        # Check element relationship
        productive_cycle = {'Wood': 'Fire', 'Fire': 'Earth', 'Earth': 'Metal', 
                           'Metal': 'Water', 'Water': 'Wood'}
        
        if productive_cycle.get(stem_elem) == branch_elem:
            return "Harmonious - Productive"
        elif productive_cycle.get(branch_elem) == stem_elem:
            return "Supportive - Nourishing"
        elif stem_elem == branch_elem:
            return "Strong - Concentrated"
        else:
            return "Mixed - Complex"
    
    def get_current_da_yun(self, da_yun_data: Dict, current_age: int) -> Dict:
        """Get the current Da Yun period based on age"""
        for period in da_yun_data['periods']:
            if period['start_age'] <= current_age <= period['end_age']:
                return {
                    'current_period': period,
                    'years_in_period': current_age - period['start_age'],
                    'years_remaining': period['end_age'] - current_age
                }
        return None
