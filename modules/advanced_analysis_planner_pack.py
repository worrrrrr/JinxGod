"""
Advanced Analysis & Planner Pack (v2.0)
- แก้ไขจุดอ่อน: เพิ่ม Emotional Depth, Pre-Mortem, Contingency, Adversarial View, Narrative Summary
- ออกแบบสำหรับปัญหาซับซ้อนที่มีมนุษย์เกี่ยวข้อง (Human-Centric Complex Problems)
"""

import json
from datetime import datetime
from typing import List, Dict, Any, Optional

class EmotionalImpactMatrix:
    """วิเคราะห์ผลกระทบทางอารมณ์ที่ลึกซึ้งกว่าแค่ 'ดี/แย่'"""
    
    def __init__(self):
        self.emotions = ["กลัว", "โกรธ", "เศร้า", "อับอาย", "รู้สึกผิด", "โล่งใจ", "หวัง"]
    
    def analyze(self, stakeholders: List[str], scenario: str) -> Dict[str, Any]:
        print(f"\n🧠 [Emotional Matrix] กำลังสแกนคลื่นอารมณ์ของ {len(stakeholders)} ฝ่าย...")
        report = {}
        for person in stakeholders:
            # จำลองการวิเคราะห์อารมณ์ (ในระบบจริงจะใช้ NLP Model)
            report[person] = {
                "primary_emotion": "ความกลัวผสมความรู้สึกผิด", # สมมติฐานจากบริบท
                "intensity": 8.5, # 1-10
                "hidden_fear": "การถูกทิ้งให้อยู่คนเดียว / การเสียหน้า",
                "trigger_point": "การถูกบังคับให้เลือกทางใดทางหนึ่ง",
                "healing_need": "พื้นที่ปลอดภัยในการยอมรับความผิดพลาด"
            }
        return report

class PreMortemSimulator:
    """เทคนิค Pre-Mortem: สมมติว่าแผนล้มเหลวตั้งแต่ตอนนี้ แล้วหาสาเหตุ"""
    
    def simulate_failure(self, plan: str) -> List[str]:
        print("\n💀 [Pre-Mortem] กำลังจำลองอนาคตที่แผนนี้ 'หายนะ'...")
        failures = [
            "ข้อมูลรั่วไหลเพราะช่องทางออนไลน์ไม่ปลอดภัยพอ",
            "ผู้คนไม่เชื่อเพราะขาดแหล่งอ้างอิงที่น่าเชื่อถือ (Trust Deficit)",
            "เกิดความตื่นตระหนกเกินจริง (Panic) จนเกิดจลาจลเล็กๆ",
            "เจ้าของผลประโยชน์โต้กลับด้วยการฟ้องร้องแม้ไม่ทราบตัวตน",
            "สภาพจิตใจของผู้ส่งสารแตกสลายระหว่างรอผลลัพธ์"
        ]
        return failures

class AdversarialReviewer:
    """มุมมองจากศัตรู/ผู้ไม่หวังดี เพื่อหาช่องโหว่"}"""
    
    def review(self, plan: str) -> List[str]:
        print("\n⚔️ [Adversarial View] มุมมองจากฝั่งตรงข้ามที่กำลังจับผิดคุณ...")
        weaknesses = [
            "รูปแบบการเขียนข้อความบ่งบอกถึงการศึกษาสูง ช narrowing กลุ่มผู้ต้องสงสัย",
            "เวลาโพสต์ตรงกับช่วงที่ผู้ต้องสงสัยออนไลน์",
            "เนื้อหาเจาะจงเกินไป แสดงว่ามีการเข้าถึงข้อมูลภายใน",
            "การไม่แสดงตัวทำให้ถูกมองว่าเป็นผู้ก่อการร้ายไซเบอร์ได้ง่าย"
        ]
        return weaknesses

class AdvancedStrategicPlanner:
    """นักวางแผนรุ่น 2: มีแผนสำรองและจุดตัดสินใจ"""
    
    def generate_contingencies(self, main_plan: str) -> Dict[str, Any]:
        print("\n🛡️ [Contingency Planner] สร้างแผนสำรองและจุดเปลี่ยน...")
        return {
            "plan_a": {
                "name": "นิรนามออนไลน์ (Anonymous Leak)",
                "success_rate": "65%",
                "trigger_to_abort": "หากมีข่าวลือว่ากำลังสืบหาต้นตอภายใน 48 ชม."
            },
            "plan_b": {
                "name": "ปล่อยข้อมูลผ่านคนกลางที่น่าเชื่อถือ (Trusted Intermediary)",
                "description": "ติดต่ออาจารย์มหาวิทยาลัยหรือนักข่าวสอบสวน โดยไม่เปิดเผยตัวตนโดยตรง",
                "trigger_to_activate": "เมื่อ Plan A ถูกเพิกเฉยหรือถูกโจมตีว่าปลอม"
            },
            "plan_c": {
                "name": "เตรียมตัวเผชิญหน้า (Controlled Disclosure)",
                "description": "ยอมเปิดเผยตัวตนแต่มีหลักฐานแน่นหนาและที่ปรึกษาทางกฎหมายพร้อม",
                "trigger_to_activate": "เมื่อภัยพิบัติใกล้เกินกว่าจะซ่อนเร้น และจำเป็นต้องระดมทรัพยากรใหญ่"
            },
            "exit_strategy": "ลบร่องรอยดิจิทัลทั้งหมด และย้ายที่อยู่ชั่วคราวหากถูกคุกคาม"
        }

class NarrativeSummarizer:
    """สรุปผลแบบเล่าเรื่อง (Storytelling) แทนการ列出ข้อๆ"""
    
    def synthesize(self, analysis: Dict, plan: Dict, emotions: Dict) -> str:
        print("\n📖 [Narrative Synthesizer] ถักทอเรื่องราวจากการตัดสินใจ...")
        
        story = f"""
        --- บทสรุปสำหรับผู้ตัดสินใจ (Executive Narrative) ---
        
        ในสถานการณ์ที่เปราะบางนี้ หัวใจสำคัญไม่ใช่แค่ 'ความจริง' แต่คือ 'วิธีส่งมอบความจริง'
        
        จากผลการวิเคราะห์ เราพบว่าผู้มีส่วนได้ส่วนเสียกำลังแบกรับความกดดันมหาศาล 
        โดยเฉพาะความกลัวที่จะสูญเสียความเชื่อมั่นและความปลอดภัย 
        แผนการ 'นิรนามออนไลน์' เป็นทางเลือกที่สมดุลที่สุดในขณะนี้ 
        แต่อย่าลืมว่ามันไม่ใช่กระสุนนัดสุดท้าย
        
        หากทุกอย่างเป็นไปตามแผน สังคมจะได้รับเตือนภัยทันเวลาโดยที่คุณปลอดภัย 
        แต่หากเกิดเหตุการณ์ไม่คาดฝัน (ดังที่จำลองไว้ใน Pre-Mortem) 
        เรามีแผนสำรองที่จะเปลี่ยนจากผู้สังเกตการณ์เป็นผู้กระทำผ่านคนกลางทันที
        
        สรุปแล้ว: คุณกำลังเดินบนเส้นทางที่มืดแต่จำเป็น 
        สิ่งที่ต้องถือไว้เสมอคือ 'สติ' และ 'ทางถอย' ที่เตรียมไว้แล้ว
        -------------------------------------------------------
        """
        return story

class AdvancedAnalysisPack:
    """แพ็กเกจรวมเครื่องมือวิเคราะห์ขั้นสูง"""
    
    def __init__(self):
        self.emotion_engine = EmotionalImpactMatrix()
        self.pre_mortem = PreMortemSimulator()
        self.adversary = AdversarialReviewer()
        self.planner = AdvancedStrategicPlanner()
        self.summarizer = NarrativeSummarizer()
    
    def run_full_cycle(self, scenario: str, stakeholders: List[str], initial_plan: str):
        print("="*60)
        print("🚀 STARTING ADVANCED ANALYSIS CYCLE")
        print("="*60)
        
        # 1. Emotional Deep Dive
        emo_report = self.emotion_engine.analyze(stakeholders, scenario)
        
        # 2. Failure Simulation
        failures = self.pre_mortem.simulate_failure(initial_plan)
        
        # 3. Enemy View
        weaknesses = self.adversary.review(initial_plan)
        
        # 4. Strategic Planning with Contingencies
        full_plan = self.planner.generate_contingencies(initial_plan)
        
        # 5. Narrative Summary
        final_story = self.summarizer.synthesize(emo_report, full_plan, emo_report)
        
        return {
            "emotional_landscape": emo_report,
            "potential_failures": failures,
            "blind_spots": weaknesses,
            "strategic_roadmap": full_plan,
            "narrative_summary": final_story
        }

# --- ทดสอบระบบกับเคส "ความลับของอนาคต" ---
if __name__ == "__main__":
    scenario = "ภัยพิบัติใหญ่ในอีก 1 ปี แต่เตือนตอนนี้จะถูกฟ้องและเสียชื่อเสียง"
    stakeholders = ["คุณ (ผู้รู้ความลับ)", "ชาวบ้านในจังหวัด", "ภาคอสังหาริมทรัพย์", "หน่วยงานรัฐ"]
    initial_plan = "โพสต์เตือนภัยแบบนิรนามผ่านเว็บ"
    
    engine = AdvancedAnalysisPack()
    result = engine.run_full_cycle(scenario, stakeholders, initial_plan)
    
    print(result['narrative_summary'])
    print("\n✅ Analysis Complete. ระบบพร้อมสนับสนุนการตัดสินใจของคุณ.")
