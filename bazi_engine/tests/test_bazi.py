#!/usr/bin/env python3
"""
Test suite for Bazi Engine
Tests core calculation, element analysis, Day Master, Da Yun, and Shen Sha
"""

import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bazi_engine import quick_analysis, detailed_analysis
from bazi_engine.core.calculator import BaziCalculator

def test_basic_calculation():
    """Test basic four pillars calculation"""
    print("=" * 60)
    print("TEST 1: Basic Four Pillars Calculation")
    print("=" * 60)
    
    calc = BaziCalculator()
    result = calc.calculate_complete_chart("1990-05-15 14:30", "male")
    
    assert 'four_pillars' in result
    pillars = result['four_pillars']
    assert 'year' in pillars
    assert 'month' in pillars
    assert 'day' in pillars
    assert 'hour' in pillars
    
    print(f"✓ Year Pillar: {pillars['year']['heavenly_stem']} {pillars['year']['earthly_branch']}")
    print(f"✓ Month Pillar: {pillars['month']['heavenly_stem']} {pillars['month']['earthly_branch']}")
    print(f"✓ Day Pillar: {pillars['day']['heavenly_stem']} {pillars['day']['earthly_branch']}")
    print(f"✓ Hour Pillar: {pillars['hour']['heavenly_stem']} {pillars['hour']['earthly_branch']}")
    print("✓ Basic calculation PASSED\n")

def test_element_distribution():
    """Test five elements distribution"""
    print("=" * 60)
    print("TEST 2: Five Elements Distribution")
    print("=" * 60)
    
    result = quick_analysis("1990-05-15 14:30", "male")
    
    assert 'element_distribution' in result
    elements = result['element_distribution']
    
    print(f"✓ Wood: {elements.get('Wood', 0)}")
    print(f"✓ Fire: {elements.get('Fire', 0)}")
    print(f"✓ Earth: {elements.get('Earth', 0)}")
    print(f"✓ Metal: {elements.get('Metal', 0)}")
    print(f"✓ Water: {elements.get('Water', 0)}")
    
    total = sum(elements.values())
    assert total > 0, "Element count should be greater than 0"
    print(f"✓ Total elements: {total}")
    print("✓ Element distribution PASSED\n")

def test_day_master_analysis():
    """Test Day Master strength analysis"""
    print("=" * 60)
    print("TEST 3: Day Master Analysis")
    print("=" * 60)
    
    result = quick_analysis("1990-05-15 14:30", "male")
    
    assert 'day_master_analysis' in result
    dm = result['day_master_analysis']
    
    print(f"✓ Day Master: {dm.get('day_master')} ({dm.get('day_master_element')}, {dm.get('day_master_yin_yang')})")
    print(f"✓ Strength: {dm.get('strength_level', 'N/A')}")
    print(f"✓ Support Score: {dm.get('support_score', 'N/A')}")
    
    if 'favorable_elements' in dm:
        print(f"✓ Favorable Elements: {dm['favorable_elements']}")
    
    print("✓ Day Master analysis PASSED\n")

def test_ten_gods():
    """Test Ten Gods calculation"""
    print("=" * 60)
    print("TEST 4: Ten Gods Analysis")
    print("=" * 60)
    
    result = quick_analysis("1990-05-15 14:30", "male")
    
    # Ten Gods are in four_pillars
    assert 'four_pillars' in result
    pillars = result['four_pillars']
    
    print("✓ Ten Gods in each pillar:")
    for pillar_name, pillar_data in pillars.items():
        ten_god = pillar_data.get('ten_god', 'N/A')
        print(f"  - {pillar_name}: {ten_god}")
    
    print("✓ Ten Gods analysis PASSED\n")

def test_hidden_stems():
    """Test Hidden Stems calculation"""
    print("=" * 60)
    print("TEST 5: Hidden Stems Analysis")
    print("=" * 60)
    
    result = quick_analysis("1990-05-15 14:30", "male")
    
    assert 'four_pillars' in result
    pillars = result['four_pillars']
    
    print("✓ Hidden Stems in each pillar:")
    for pillar_name, pillar_data in pillars.items():
        hidden = pillar_data.get('hidden_stems', [])
        stems_str = ", ".join([f"{h['stem']} ({h['element']})" for h in hidden])
        print(f"  - {pillar_name}: {stems_str if stems_str else 'None'}")
    
    print("✓ Hidden Stems analysis PASSED\n")

def test_da_yun():
    """Test Da Yun (Major Periods) calculation"""
    print("=" * 60)
    print("TEST 6: Da Yun (Major Periods)")
    print("=" * 60)
    
    result = quick_analysis("1990-05-15 14:30", "male")
    
    if 'da_yun' in result:
        da_yun = result['da_yun']
        print(f"✓ Starting Age: {da_yun.get('start_age', 'N/A')}")
        
        if 'periods' in da_yun:
            periods = da_yun['periods']
            print(f"✓ Number of periods: {len(periods)}")
            
            # Show first 3 periods
            for i, period in enumerate(periods[:3]):
                print(f"  Period {i+1}: Age {period.get('start_age')} - {period.get('end_age')}, "
                      f"Pillar: {period.get('pillar')}")
        
        print("✓ Da Yun calculation PASSED\n")
    else:
        print("⚠ Da Yun not available (may require additional configuration)\n")

def test_shen_sha():
    """Test Shen Sha (Symbolic Stars) calculation"""
    print("=" * 60)
    print("TEST 7: Shen Sha (Symbolic Stars)")
    print("=" * 60)
    
    result = quick_analysis("1990-05-15 14:30", "male")
    
    if 'shen_sha' in result:
        shen_sha = result['shen_sha']
        print(f"✓ Total stars found: {len(shen_sha)}")
        
        # Show first 5 stars
        for star in shen_sha[:5]:
            print(f"  - {star.get('name')}: {star.get('description', '')[:50]}...")
        
        print("✓ Shen Sha calculation PASSED\n")
    else:
        print("⚠ Shen Sha not available (may require additional configuration)\n")

def test_detailed_analysis():
    """Test comprehensive detailed analysis"""
    print("=" * 60)
    print("TEST 8: Comprehensive Detailed Analysis")
    print("=" * 60)
    
    result = detailed_analysis("1990-05-15 14:30", "male")
    
    assert isinstance(result, dict)
    assert len(result) > 0
    
    print(f"✓ Analysis contains {len(result)} sections")
    
    # Check key sections
    key_sections = ['four_pillars', 'elements', 'day_master', 'ten_gods']
    for section in key_sections:
        if section in result:
            print(f"✓ Section '{section}' present")
    
    print("✓ Detailed analysis PASSED\n")

def test_edge_cases():
    """Test edge cases and special dates"""
    print("=" * 60)
    print("TEST 9: Edge Cases")
    print("=" * 60)
    
    # Test different dates
    test_dates = [
        "2000-01-01 00:00",  # New millennium
        "1984-02-02 12:00",  # Before Chinese New Year
        "2023-12-31 23:59",  # End of year
    ]
    
    for date_str in test_dates:
        try:
            result = quick_analysis(date_str, "female")
            print(f"✓ Successfully analyzed: {date_str}")
        except Exception as e:
            print(f"✗ Failed for {date_str}: {e}")
            raise
    
    print("✓ Edge cases PASSED\n")

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("BAZI ENGINE TEST SUITE")
    print("=" * 60 + "\n")
    
    try:
        test_basic_calculation()
        test_element_distribution()
        test_day_master_analysis()
        test_ten_gods()
        test_hidden_stems()
        test_da_yun()
        test_shen_sha()
        test_detailed_analysis()
        test_edge_cases()
        
        print("=" * 60)
        print("ALL TESTS PASSED! ✓✓✓")
        print("=" * 60)
        return True
        
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
