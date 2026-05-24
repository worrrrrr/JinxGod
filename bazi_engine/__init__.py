"""
Bazi Engine - Complete Chinese Astrology Analysis System

Modules:
- core.calculator: Four Pillars calculation
- core.da_yun: 10-Year Luck Pillars (大运)
- core.liu_nian: Annual Luck Pillars (流年)
- core.shen_sha: Symbolic Stars (神煞)
"""
from .core.calculator import BaziCalculator, quick_analysis, detailed_analysis
from .core.da_yun import DaYunCalculator
from .core.liu_nian import LiuNianCalculator
from .core.shen_sha import ShenShaCalculator
from .interpreters.interpreter import interpret_bazi

__version__ = "2.0.0"
__all__ = [
    'BaziCalculator',
    'DaYunCalculator', 
    'LiuNianCalculator',
    'ShenShaCalculator',
    'quick_analysis',
    'detailed_analysis',
    'complete_analysis',
    'interpret_bazi'
]


def complete_analysis(birth_datetime: str, gender: str, 
                     start_year: int = None, end_year: int = None) -> dict:
    """
    Perform complete Bazi analysis with all components
    
    Args:
        birth_datetime: Birth date and time in "YYYY-MM-DD HH:MM" format
        gender: 'male' or 'female'
        start_year: Starting year for Liu Nian (default: current year)
        end_year: Ending year for Liu Nian (default: current year + 5)
    
    Returns:
        Complete analysis dictionary with all components
    """
    from datetime import datetime
    
    # Initialize calculators
    calc = BaziCalculator()
    da_yun_calc = DaYunCalculator()
    liu_nian_calc = LiuNianCalculator()
    shen_sha_calc = ShenShaCalculator()
    
    # Calculate base chart
    base_chart = calc.calculate_complete_chart(birth_datetime, gender)
    
    # Extract necessary info for additional calculations
    pillars = {}
    for pillar_name in ['year', 'month', 'day', 'hour']:
        pillar_data = base_chart['four_pillars'][pillar_name]
        pillars[pillar_name] = {
            'heavenly_stem': pillar_data['heavenly_stem'],
            'earthly_branch': pillar_data['earthly_branch']
        }
    
    day_stem = pillars['day']['heavenly_stem']
    day_branch = pillars['day']['earthly_branch']
    year_branch = pillars['year']['earthly_branch']
    year_stem = pillars['year']['heavenly_stem']
    month_pillar = (pillars['month']['heavenly_stem'], pillars['month']['earthly_branch'])
    
    birth_year = int(birth_datetime.split('-')[0])
    dm_analysis = base_chart['day_master_analysis']
    
    # Calculate Da Yun
    da_yun = da_yun_calc.calculate_da_yun(
        birth_datetime, gender, year_stem, month_pillar
    )
    
    # Calculate Liu Nian
    if start_year is None:
        start_year = datetime.now().year
    if end_year is None:
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
    
    # Compile complete result
    complete_result = {
        'base_chart': base_chart,
        'da_yun': da_yun,
        'liu_nian': liu_nian,
        'shen_sha': shen_sha,
        'summary': {
            'day_master': f"{dm_analysis['day_master']} ({dm_analysis['day_master_element']}, {dm_analysis['day_master_yin_yang']})",
            'strength': dm_analysis['strength_level'],
            'favorable_elements': base_chart['lucky_elements'],
            'da_yun_start_age': da_yun['starting_age'],
            'current_da_yun_period': da_yun_calc.get_current_da_yun(
                da_yun, datetime.now().year - birth_year
            ),
            'shen_sha_summary': shen_sha['general_interpretation']
        }
    }
    
    return complete_result
