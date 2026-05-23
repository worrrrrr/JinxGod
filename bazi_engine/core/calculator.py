"""
Bazi Core Calculator - ระบบคำนวณปาจื้อ (Four Pillars of Destiny) แบบละเอียด
รองรับการคำนวณ:
1. ปีนักษัตร (Year Pillar)
2. เดือนนักษัตร (Month Pillar) 
3. วันนักษัตร (Day Pillar)
4. ยามนักษัตร (Hour Pillar)
5. ธาตุทั้ง 5 (Wood, Fire, Earth, Metal, Water)
6. Yin/Yang
7. Heavenly Stems และ Earthly Branches
8. 10 เทพเจ้า (Ten Gods)
9. กิ่งแฝง (Hidden Stems)
10. ความแข็งแรงของ Day Master
"""

from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import math

class BaziCalculator:
    # ลำดับธาตุและกิ่งฟ้า
    HEAVENLY_STEMS = ['Jia', 'Yi', 'Bing', 'Ding', 'Wu', 'Ji', 'Geng', 'Xin', 'Ren', 'Gui']
    EARTHLY_BRANCHES = ['Zi', 'Chou', 'Yin', 'Mao', 'Chen', 'Si', 'Wu', 'Wei', 'Shen', 'You', 'Xu', 'Hai']
    
    # ธาตุของกิ่งฟ้า
    STEM_ELEMENTS = {
        'Jia': 'Wood', 'Yi': 'Wood',
        'Bing': 'Fire', 'Ding': 'Fire',
        'Wu': 'Earth', 'Ji': 'Earth',
        'Geng': 'Metal', 'Xin': 'Metal',
        'Ren': 'Water', 'Gui': 'Water'
    }
    
    # ธาตุของก้านดิน
    BRANCH_ELEMENTS = {
        'Zi': 'Water', 'Chou': 'Earth', 'Yin': 'Wood', 'Mao': 'Wood',
        'Chen': 'Earth', 'Si': 'Fire', 'Wu': 'Fire', 'Wei': 'Earth',
        'Shen': 'Metal', 'You': 'Metal', 'Xu': 'Earth', 'Hai': 'Water'
    }
    
    # กิ่งแฝงในก้านดิน (Hidden Stems) พร้อมน้ำหนัก
    HIDDEN_STEMS_WEIGHTS = {
        'Zi': [('Gui', 1.0)],
        'Chou': [('Ji', 0.6), ('Gui', 0.25), ('Xin', 0.15)],
        'Yin': [('Jia', 0.6), ('Bing', 0.25), ('Wu', 0.15)],
        'Mao': [('Yi', 1.0)],
        'Chen': [('Wu', 0.6), ('Yi', 0.25), ('Gui', 0.15)],
        'Si': [('Bing', 0.6), ('Wu', 0.25), ('Geng', 0.15)],
        'Wu': [('Ding', 0.7), ('Ji', 0.3)],
        'Wei': [('Ji', 0.6), ('Ding', 0.25), ('Yi', 0.15)],
        'Shen': [('Geng', 0.6), ('Ren', 0.25), ('Wu', 0.15)],
        'You': [('Xin', 1.0)],
        'Xu': [('Wu', 0.6), ('Xin', 0.25), ('Ding', 0.15)],
        'Hai': [('Ren', 0.7), ('Jia', 0.3)]
    }
    
    # Yin/Yang ของกิ่งฟ้า
    STEM_YIN_YANG = {
        'Jia': 'Yang', 'Yi': 'Yin', 'Bing': 'Yang', 'Ding': 'Yin', 'Wu': 'Yang',
        'Ji': 'Yin', 'Geng': 'Yang', 'Xin': 'Yin', 'Ren': 'Yang', 'Gui': 'Yin'
    }
    
    # Yin/Yang ของก้านดิน
    BRANCH_YIN_YANG = {
        'Zi': 'Yang', 'Chou': 'Yin', 'Yin': 'Yang', 'Mao': 'Yin',
        'Chen': 'Yang', 'Si': 'Yin', 'Wu': 'Yang', 'Wei': 'Yin',
        'Shen': 'Yang', 'You': 'Yin', 'Xu': 'Yang', 'Hai': 'Yin'
    }
    
    # 10 Gods relationships
    TEN_GODS_MAP = {
        ('Wood', 'Yang'): {'Wood': {'Yang': 'Friend', 'Yin': 'Rob Wealth'},
                          'Fire': {'Yang': 'Eating God', 'Yin': 'Hurting Officer'},
                          'Earth': {'Yang': 'Indirect Wealth', 'Yin': 'Direct Wealth'},
                          'Metal': {'Yang': 'Seven Killings', 'Yin': 'Direct Officer'},
                          'Water': {'Yang': 'Indirect Resource', 'Yin': 'Direct Resource'}},
        ('Wood', 'Yin'): {'Wood': {'Yang': 'Rob Wealth', 'Yin': 'Friend'},
                         'Fire': {'Yang': 'Hurting Officer', 'Yin': 'Eating God'},
                         'Earth': {'Yang': 'Direct Wealth', 'Yin': 'Indirect Wealth'},
                         'Metal': {'Yang': 'Direct Officer', 'Yin': 'Seven Killings'},
                         'Water': {'Yang': 'Direct Resource', 'Yin': 'Indirect Resource'}},
        ('Fire', 'Yang'): {'Wood': {'Yang': 'Indirect Resource', 'Yin': 'Direct Resource'},
                          'Fire': {'Yang': 'Friend', 'Yin': 'Rob Wealth'},
                          'Earth': {'Yang': 'Eating God', 'Yin': 'Hurting Officer'},
                          'Metal': {'Yang': 'Indirect Wealth', 'Yin': 'Direct Wealth'},
                          'Water': {'Yang': 'Seven Killings', 'Yin': 'Direct Officer'}},
        ('Fire', 'Yin'): {'Wood': {'Yang': 'Direct Resource', 'Yin': 'Indirect Resource'},
                         'Fire': {'Yang': 'Rob Wealth', 'Yin': 'Friend'},
                         'Earth': {'Yang': 'Hurting Officer', 'Yin': 'Eating God'},
                         'Metal': {'Yang': 'Direct Wealth', 'Yin': 'Indirect Wealth'},
                         'Water': {'Yang': 'Direct Officer', 'Yin': 'Seven Killings'}},
        ('Earth', 'Yang'): {'Wood': {'Yang': 'Seven Killings', 'Yin': 'Direct Officer'},
                           'Fire': {'Yang': 'Indirect Resource', 'Yin': 'Direct Resource'},
                           'Earth': {'Yang': 'Friend', 'Yin': 'Rob Wealth'},
                           'Metal': {'Yang': 'Eating God', 'Yin': 'Hurting Officer'},
                           'Water': {'Yang': 'Indirect Wealth', 'Yin': 'Direct Wealth'}},
        ('Earth', 'Yin'): {'Wood': {'Yang': 'Direct Officer', 'Yin': 'Seven Killings'},
                          'Fire': {'Yang': 'Direct Resource', 'Yin': 'Indirect Resource'},
                          'Earth': {'Yang': 'Rob Wealth', 'Yin': 'Friend'},
                          'Metal': {'Yang': 'Hurting Officer', 'Yin': 'Eating God'},
                          'Water': {'Yang': 'Direct Wealth', 'Yin': 'Indirect Wealth'}},
        ('Metal', 'Yang'): {'Wood': {'Yang': 'Indirect Wealth', 'Yin': 'Direct Wealth'},
                           'Fire': {'Yang': 'Seven Killings', 'Yin': 'Direct Officer'},
                           'Earth': {'Yang': 'Indirect Resource', 'Yin': 'Direct Resource'},
                           'Metal': {'Yang': 'Friend', 'Yin': 'Rob Wealth'},
                           'Water': {'Yang': 'Eating God', 'Yin': 'Hurting Officer'}},
        ('Metal', 'Yin'): {'Wood': {'Yang': 'Direct Wealth', 'Yin': 'Indirect Wealth'},
                          'Fire': {'Yang': 'Direct Officer', 'Yin': 'Seven Killings'},
                          'Earth': {'Yang': 'Direct Resource', 'Yin': 'Indirect Resource'},
                          'Metal': {'Yang': 'Rob Wealth', 'Yin': 'Friend'},
                          'Water': {'Yang': 'Hurting Officer', 'Yin': 'Eating God'}},
        ('Water', 'Yang'): {'Wood': {'Yang': 'Eating God', 'Yin': 'Hurting Officer'},
                           'Fire': {'Yang': 'Indirect Wealth', 'Yin': 'Direct Wealth'},
                           'Earth': {'Yang': 'Seven Killings', 'Yin': 'Direct Officer'},
                           'Metal': {'Yang': 'Indirect Resource', 'Yin': 'Direct Resource'},
                           'Water': {'Yang': 'Friend', 'Yin': 'Rob Wealth'}},
        ('Water', 'Yin'): {'Wood': {'Yang': 'Hurting Officer', 'Yin': 'Eating God'},
                          'Fire': {'Yang': 'Direct Wealth', 'Yin': 'Indirect Wealth'},
                          'Earth': {'Yang': 'Direct Officer', 'Yin': 'Seven Killings'},
                          'Metal': {'Yang': 'Direct Resource', 'Yin': 'Indirect Resource'},
                          'Water': {'Yang': 'Rob Wealth', 'Yin': 'Friend'}}
    }
    
    # Solar Terms สำหรับเดือน (ประมาณ)
    SOLAR_TERMS_MONTH_START = {
        1: (2, 4),   # Li Chun - Feb 4
        2: (3, 5),   # Jing Zhe - Mar 5
        3: (4, 5),   # Qing Ming - Apr 5
        4: (5, 5),   # Li Xia - May 5
        5: (6, 6),   # Mang Zhong - Jun 6
        6: (7, 7),   # Xiao Shu - Jul 7
        7: (8, 8),   # Li Qiu - Aug 8
        8: (9, 8),   # Bai Lu - Sep 8
        9: (10, 8),  # Han Lu - Oct 8
        10: (11, 7), # Li Dong - Nov 7
        11: (12, 7), # Da Xue - Dec 7
        12: (1, 6)   # Xiao Han - Jan 6
    }
    
    def __init__(self):
        pass
    
    def _get_solar_month(self, month: int, day: int) -> int:
        """Determine the solar month based on solar terms"""
        # Month branches: 1=Yin, 2=Mao, 3=Chen, 4=Si, 5=Wu, 6=Wei, 
        #                 7=Shen, 8=You, 9=Xu, 10=Hai, 11=Zi, 12=Chou
        if month == 1:
            if day >= 6:
                return 12  # Chou month
            else:
                return 11  # Zi month (previous year)
        
        term_month, term_day = self.SOLAR_TERMS_MONTH_START.get(month, (month, 5))
        
        if day >= term_day:
            return term_month - 1 if term_month > 1 else 12
        else:
            prev_month = month - 1 if month > 1 else 12
            return prev_month - 1 if prev_month > 1 else 12
    
    def get_year_pillar(self, year: int, month: int, day: int) -> Tuple[str, str]:
        """Calculate Year Pillar considering solar new year (Li Chun)"""
        # Check if before Li Chun (Feb 4)
        actual_year = year
        if month == 1 and day < 4:
            actual_year = year - 1
        elif month == 2 and day < 4:
            actual_year = year - 1
        
        stem_idx = (actual_year - 4) % 10
        branch_idx = (actual_year - 4) % 12
        return self.HEAVENLY_STEMS[stem_idx], self.EARTHLY_BRANCHES[branch_idx]
    
    def get_month_pillar(self, year: int, month: int, day: int) -> Tuple[str, str]:
        """Calculate Month Pillar using Five Tigers Method with solar terms"""
        # Get year stem (considering solar year)
        year_stem, _ = self.get_year_pillar(year, month, day)
        
        # Determine solar month
        solar_month = self._get_solar_month(month, day)
        
        # Month branches starting from Yin (1st solar month)
        month_branches = ['Chou', 'Yin', 'Mao', 'Chen', 'Si', 'Wu', 'Wei', 
                         'Shen', 'You', 'Xu', 'Hai', 'Zi']
        
        month_branch = month_branches[solar_month]
        
        # Five Tigers Method
        stem_start_map = {
            'Jia': 2, 'Yi': 2,
            'Bing': 6, 'Ding': 6,
            'Wu': 0, 'Ji': 0,
            'Geng': 4, 'Xin': 4,
            'Ren': 8, 'Gui': 8
        }
        
        start_idx = stem_start_map[year_stem]
        
        # Calculate stem offset from Yin month
        yin_pos = 1
        current_pos = solar_month
        
        if current_pos >= yin_pos:
            stem_offset = current_pos - yin_pos
        else:
            stem_offset = (12 + current_pos) - yin_pos
        
        month_stem_idx = (start_idx + stem_offset) % 10
        month_stem = self.HEAVENLY_STEMS[month_stem_idx]
        
        return month_stem, month_branch
    
    def get_day_pillar(self, year: int, month: int, day: int) -> Tuple[str, str]:
        """Calculate Day Pillar using reference date method"""
        ref_date = datetime(1900, 1, 1)
        target_date = datetime(year, month, day)
        
        days_diff = (target_date - ref_date).days
        
        stem_idx = (0 + days_diff) % 10
        branch_idx = (10 + days_diff) % 12
        
        return self.HEAVENLY_STEMS[stem_idx], self.EARTHLY_BRANCHES[branch_idx]
    
    def get_hour_pillar(self, day_stem: str, hour: int, minute: int) -> Tuple[str, str]:
        """Calculate Hour Pillar using Five Rats Method"""
        hour_branches = ['Zi', 'Chou', 'Yin', 'Mao', 'Chen', 'Si', 
                        'Wu', 'Wei', 'Shen', 'You', 'Xu', 'Hai']
        
        # Handle late night (23:00-24:00) as early Zi hour of next day
        if hour >= 23:
            hour_branch_idx = 0
        else:
            hour_branch_idx = ((hour + 1) // 2) % 12
        
        hour_branch = hour_branches[hour_branch_idx]
        
        # Five Rats Method
        stem_start_map = {
            'Jia': 0, 'Yi': 0,
            'Bing': 2, 'Ding': 2,
            'Wu': 4, 'Ji': 4,
            'Geng': 6, 'Xin': 6,
            'Ren': 8, 'Gui': 8
        }
        
        start_idx = stem_start_map[day_stem]
        hour_stem_idx = (start_idx + hour_branch_idx) % 10
        hour_stem = self.HEAVENLY_STEMS[hour_stem_idx]
        
        return hour_stem, hour_branch
    
    def get_ten_gods(self, day_stem: str, other_stem: str) -> str:
        """Determine Ten Gods relationship"""
        dm_element = self.STEM_ELEMENTS[day_stem]
        dm_yy = self.STEM_YIN_YANG[day_stem]
        
        other_element = self.STEM_ELEMENTS[other_stem]
        other_yy = self.STEM_YIN_YANG[other_stem]
        
        return self.TEN_GODS_MAP[(dm_element, dm_yy)][other_element][other_yy]
    
    def calculate_element_strength(self, pillars: Dict) -> Dict[str, float]:
        """Calculate the strength of each element with weighted scoring"""
        element_scores = {'Wood': 0.0, 'Fire': 0.0, 'Earth': 0.0, 'Metal': 0.0, 'Water': 0.0}
        
        # Weights
        stem_weight = 1.0
        branch_weight = 0.8
        
        # Process Heavenly Stems
        for pillar in ['year', 'month', 'day', 'hour']:
            stem = pillars[pillar]['heavenly_stem']
            element = self.STEM_ELEMENTS[stem]
            element_scores[element] += stem_weight
        
        # Process Earthly Branches
        for pillar in ['year', 'month', 'day', 'hour']:
            branch = pillars[pillar]['earthly_branch']
            element = self.BRANCH_ELEMENTS[branch]
            element_scores[element] += branch_weight
            
            # Process Hidden Stems with weights
            hidden = self.HIDDEN_STEMS_WEIGHTS[branch]
            for h_stem, weight in hidden:
                h_element = self.STEM_ELEMENTS[h_stem]
                element_scores[h_element] += branch_weight * weight
        
        # Normalize scores
        total = sum(element_scores.values())
        if total > 0:
            for elem in element_scores:
                element_scores[elem] = round(element_scores[elem] / total * 100, 2)
        
        return element_scores
    
    def analyze_day_master_strength(self, pillars: Dict, element_scores: Dict) -> Dict:
        """Analyze whether Day Master is strong or weak with detailed metrics"""
        day_stem = pillars['day']['heavenly_stem']
        dm_element = self.STEM_ELEMENTS[day_stem]
        dm_yy = self.STEM_YIN_YANG[day_stem]
        
        # Supporting elements
        producing_elements = {
            'Wood': 'Water', 'Fire': 'Wood', 'Earth': 'Fire',
            'Metal': 'Earth', 'Water': 'Metal'
        }
        resource_element = producing_elements[dm_element]
        
        support_score = element_scores[dm_element] + element_scores[resource_element]
        
        # Seasonal influence
        month_branch = pillars['month']['earthly_branch']
        month_element = self.BRANCH_ELEMENTS[month_branch]
        
        seasonal_bonus = 0
        if month_element == dm_element:
            seasonal_bonus = 15
        elif month_element == resource_element:
            seasonal_bonus = 10
        
        # Check if month branch contains DM or resource in hidden stems
        month_hidden = self.HIDDEN_STEMS_WEIGHTS[month_branch]
        for h_stem, weight in month_hidden:
            h_element = self.STEM_ELEMENTS[h_stem]
            if h_element == dm_element:
                seasonal_bonus += 5 * weight
            elif h_element == resource_element:
                seasonal_bonus += 3 * weight
        
        adjusted_support = support_score + seasonal_bonus
        
        # Determine strength level
        if adjusted_support >= 55:
            strength_level = "Strong"
        elif adjusted_support >= 45:
            strength_level = "Balanced"
        else:
            strength_level = "Weak"
        
        return {
            'day_master': day_stem,
            'day_master_element': dm_element,
            'day_master_yin_yang': dm_yy,
            'support_score': round(support_score, 2),
            'seasonal_bonus': round(seasonal_bonus, 2),
            'adjusted_score': round(adjusted_support, 2),
            'strength_level': strength_level,
            'favorable_elements': self._get_favorable_elements(dm_element, strength_level, element_scores)
        }
    
    def _get_favorable_elements(self, dm_element: str, strength: str, scores: Dict) -> List[str]:
        """Determine favorable elements"""
        if strength == "Strong":
            controlling = {
                'Wood': ['Fire', 'Earth', 'Metal'],
                'Fire': ['Earth', 'Metal', 'Water'],
                'Earth': ['Metal', 'Water', 'Wood'],
                'Metal': ['Water', 'Wood', 'Fire'],
                'Water': ['Wood', 'Fire', 'Earth']
            }
            return controlling[dm_element]
        else:
            supporting = {
                'Wood': ['Water', 'Wood'],
                'Fire': ['Wood', 'Fire'],
                'Earth': ['Fire', 'Earth'],
                'Metal': ['Earth', 'Metal'],
                'Water': ['Metal', 'Water']
            }
            return supporting[dm_element]
    
    def calculate_complete_chart(self, birth_datetime: str, gender: str) -> Dict:
        """Calculate complete Bazi chart with all details"""
        dt = datetime.strptime(birth_datetime, "%Y-%m-%d %H:%M")
        year, month, day, hour, minute = dt.year, dt.month, dt.day, dt.hour, dt.minute
        
        # Calculate Four Pillars
        year_stem, year_branch = self.get_year_pillar(year, month, day)
        month_stem, month_branch = self.get_month_pillar(year, month, day)
        day_stem, day_branch = self.get_day_pillar(year, month, day)
        hour_stem, hour_branch = self.get_hour_pillar(day_stem, hour, minute)
        
        pillars = {
            'year': {'heavenly_stem': year_stem, 'earthly_branch': year_branch},
            'month': {'heavenly_stem': month_stem, 'earthly_branch': month_branch},
            'day': {'heavenly_stem': day_stem, 'earthly_branch': day_branch},
            'hour': {'heavenly_stem': hour_stem, 'earthly_branch': hour_branch}
        }
        
        # Ten Gods
        ten_gods = {}
        for pillar_name, pillar_data in pillars.items():
            stem = pillar_data['heavenly_stem']
            if pillar_name == 'day':
                ten_gods[pillar_name] = 'Day Master'
            else:
                ten_gods[pillar_name] = self.get_ten_gods(day_stem, stem)
        
        # Hidden Stems details
        hidden_details = {}
        for pillar_name, pillar_data in pillars.items():
            branch = pillar_data['earthly_branch']
            hidden = self.HIDDEN_STEMS_WEIGHTS[branch]
            hidden_details[pillar_name] = []
            for h_stem, weight in hidden:
                h_god = self.get_ten_gods(day_stem, h_stem)
                hidden_details[pillar_name].append({
                    'stem': h_stem,
                    'element': self.STEM_ELEMENTS[h_stem],
                    'yin_yang': self.STEM_YIN_YANG[h_stem],
                    'ten_god': h_god,
                    'weight': round(weight, 2)
                })
        
        # Element distribution
        element_scores = self.calculate_element_strength(pillars)
        
        # Day Master analysis
        dm_analysis = self.analyze_day_master_strength(pillars, element_scores)
        
        # Build result
        result = {
            'birth_info': {
                'datetime': birth_datetime,
                'gender': gender,
                'solar_date': f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"
            },
            'four_pillars': {
                'year': {
                    'heavenly_stem': year_stem,
                    'earthly_branch': year_branch,
                    'stem_element': self.STEM_ELEMENTS[year_stem],
                    'stem_yin_yang': self.STEM_YIN_YANG[year_stem],
                    'branch_element': self.BRANCH_ELEMENTS[year_branch],
                    'branch_yin_yang': self.BRANCH_YIN_YANG[year_branch],
                    'ten_god': ten_gods['year'],
                    'hidden_stems': hidden_details['year']
                },
                'month': {
                    'heavenly_stem': month_stem,
                    'earthly_branch': month_branch,
                    'stem_element': self.STEM_ELEMENTS[month_stem],
                    'stem_yin_yang': self.STEM_YIN_YANG[month_stem],
                    'branch_element': self.BRANCH_ELEMENTS[month_branch],
                    'branch_yin_yang': self.BRANCH_YIN_YANG[month_branch],
                    'ten_god': ten_gods['month'],
                    'hidden_stems': hidden_details['month']
                },
                'day': {
                    'heavenly_stem': day_stem,
                    'earthly_branch': day_branch,
                    'stem_element': self.STEM_ELEMENTS[day_stem],
                    'stem_yin_yang': self.STEM_YIN_YANG[day_stem],
                    'branch_element': self.BRANCH_ELEMENTS[day_branch],
                    'branch_yin_yang': self.BRANCH_YIN_YANG[day_branch],
                    'ten_god': 'Day Master',
                    'hidden_stems': hidden_details['day'],
                    'spouse_palace': True
                },
                'hour': {
                    'heavenly_stem': hour_stem,
                    'earthly_branch': hour_branch,
                    'stem_element': self.STEM_ELEMENTS[hour_stem],
                    'stem_yin_yang': self.STEM_YIN_YANG[hour_stem],
                    'branch_element': self.BRANCH_ELEMENTS[hour_branch],
                    'branch_yin_yang': self.BRANCH_YIN_YANG[hour_branch],
                    'ten_god': ten_gods['hour'],
                    'hidden_stems': hidden_details['hour']
                }
            },
            'element_distribution': element_scores,
            'day_master_analysis': dm_analysis,
            'lucky_elements': dm_analysis['favorable_elements'],
            'unlucky_elements': [e for e in ['Wood', 'Fire', 'Earth', 'Metal', 'Water'] 
                                if e not in dm_analysis['favorable_elements']]
        }
        
        return result


def quick_analysis(birth_datetime: str, gender: str) -> Dict:
    """Quick function to get Bazi analysis"""
    calculator = BaziCalculator()
    return calculator.calculate_complete_chart(birth_datetime, gender)


def detailed_analysis(birth_datetime: str, gender: str) -> Dict:
    """Detailed function to get complete Bazi analysis with all components"""
    from .da_yun import DaYunCalculator
    from .liu_nian import LiuNianCalculator
    from .shen_sha import ShenShaCalculator
    from datetime import datetime
    
    calculator = BaziCalculator()
    da_yun_calc = DaYunCalculator()
    liu_nian_calc = LiuNianCalculator()
    shen_sha_calc = ShenShaCalculator()
    
    # Calculate base chart
    base_chart = calculator.calculate_complete_chart(birth_datetime, gender)
    
    # Extract pillars info
    pillars = {}
    for pillar_name in ['year', 'month', 'day', 'hour']:
        pillar_data = base_chart['four_pillars'][pillar_name]
        pillars[pillar_name] = {
            'heavenly_stem': pillar_data['heavenly_stem'],
            'earthly_branch': pillar_data['earthly_branch']
        }
    
    day_stem = pillars['day']['heavenly_stem']
    year_branch = pillars['year']['earthly_branch']
    day_branch = pillars['day']['earthly_branch']
    year_stem = pillars['year']['heavenly_stem']
    month_pillar = (pillars['month']['heavenly_stem'], pillars['month']['earthly_branch'])
    
    birth_year = int(birth_datetime.split('-')[0])
    dm_analysis = base_chart['day_master_analysis']
    
    # Calculate Da Yun
    da_yun = da_yun_calc.calculate_da_yun(
        birth_datetime, gender, year_stem, month_pillar
    )
    
    # Calculate Liu Nian
    start_year = datetime.now().year
    end_year = start_year + 5
    
    liu_nian = liu_nian_calc.calculate_liu_nian(
        birth_year, start_year, end_year,
        dm_analysis['day_master_element'],
        dm_analysis['day_master_yin_yang']
    )
    
    # Calculate Shen Sha
    shen_sha = shen_sha_calc.calculate_shen_sha(
        pillars, day_stem, year_branch, day_branch
    )
    
    # Compile detailed result
    detailed_result = {
        'four_pillars': base_chart['four_pillars'],
        'elements': base_chart['element_distribution'],
        'day_master': base_chart['day_master_analysis'],
        'ten_gods': base_chart.get('ten_gods', {}),
        'hidden_stems': base_chart.get('hidden_stems', {}),
        'lucky_elements': base_chart['lucky_elements'],
        'da_yun': da_yun,
        'liu_nian': liu_nian,
        'shen_sha': shen_sha
    }
    
    return detailed_result

