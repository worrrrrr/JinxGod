"""
Humanity Dynamic Response System
ระบบตอบสนองอย่างมีมนุษยธรรม พร้อมบทพูดและการกระทำที่สมจริง
"""

from engines.core import CognitiveEngine
import random
import time

class DialogueGenerator:
    """สร้างบทพูดที่เป็นธรรมชาติและมีอารมณ์"""
    
    TEMPLATES = {
        "empathy": [
            "เราเข้าใจเลยว่าตอนนี้คุณรู้สึก...",
            "สถานการณ์แบบนี้ใครๆ ก็คงรู้สึก...",
            "ฟังดูแล้วน่าเห็นใจมากเลย...",
        ],
        "validation": [
            "สิ่งที่คุณรู้สึกเป็นเรื่องปกติมากๆ",
            "ไม่มีใครผิดที่คุณคิดแบบนั้น",
            "คุณทำดีที่สุดเท่าที่ทำได้ในสถานการณ์นั้น",
        ],
        "gentle_truth": [
            "มีบางอย่างที่เราต้องคุยกันหน่อย... แต่เราจะค่อยๆ พูดนะ",
            "เราอยากบอกความจริงกับคุณ เพราะเราเชื่อว่าคุณเข้มแข็งพอ...",
            "เรื่องนี้ยากที่จะพูด แต่เราคิดว่าคุณควรได้รู้...",
        ],
        "action_oriented": [
            "เอาล่ะ เรา来做แบบนี้กัน...",
            "แผนของเราคือ...",
            "ขั้นตอนต่อไปที่เราจะทำคือ...",
        ],
        "support": [
            "เราจะอยู่ข้างๆ คุณตลอดนะ",
            "คุณไม่ได้อยู่คนเดียวในเรื่องนี้",
            "เราพร้อมช่วยคุณทุกขั้นตอน",
        ]
    }
    
    @staticmethod
    def generate(emotion: str, context: str) -> str:
        """สร้างบทพูดตามอารมณ์และบริบท"""
        templates = DialogueGenerator.TEMPLATES.get(emotion, [""])
        base = random.choice(templates)
        
        # เพิ่มความเฉพาะเจาะจงตาม context
        additions = {
            "fear": " ไม่ต้องกังวล เราจะผ่านไปด้วยกัน",
            "sadness": " ให้เวลากับตัวเองหน่อยนะ ไม่ต้องรีบ",
            "anger": " ความโกรธของคุณเป็นเรื่องเข้าใจได้",
            "confusion": " เดี๋ยวเราค่อยๆ ไขไปทีละปม",
            "guilt": " คุณไม่จำเป็นต้องแบกทุกอย่างไว้คนเดียว",
        }
        
        return base + additions.get(emotion, "")

class ActionPlanner:
    """วางแผนการกระทำที่เป็นรูปธรรม"""
    
    @staticmethod
    def create_action_plan(decision: dict, urgency: str = "normal") -> list:
        """สร้างแผนการกระทำจากตัดสินใจ"""
        
        plans = {
            "high_urgency": [
                {"step": 1, "action": "ประเมินสถานการณ์ทันที", "time": "0-5 นาที"},
                {"step": 2, "action": "ติดต่อขอความช่วยเหลือ", "time": "5-15 นาที"},
                {"step": 3, "action": "ดำเนินการตามแผน", "time": "15-60 นาที"},
                {"step": 4, "action": "ติดตามผล", "time": "1 ชั่วโมง+"},
            ],
            "normal": [
                {"step": 1, "action": "รวบรวมข้อมูลและวิเคราะห์", "time": "วันแรก"},
                {"step": 2, "action": "ปรึกษาผู้เกี่ยวข้อง", "time": "วันที่ 2-3"},
                {"step": 3, "action": "ลงมือทำอย่างระมัดระวัง", "time": "สัปดาห์ ที่ 1"},
                {"step": 4, "action": "ประเมินและปรับปรุง", "time": "สัปดาห์ ที่ 2"},
            ],
            "long_term": [
                {"step": 1, "action": "ศึกษาปัญหาอย่างลึกซึ้ง", "time": "เดือนที่ 1"},
                {"step": 2, "action": "สร้างเครือข่ายสนับสนุน", "time": "เดือนที่ 2-3"},
                {"step": 3, "action": "ดำเนินการเปลี่ยนแปลง", "time": "เดือนที่ 4-6"},
                {"step": 4, "action": "วัดผลและขยายผล", "time": "เดือนที่ 7+"},
            ]
        }
        
        return plans.get(urgency, plans["normal"])

class HumanityResponseSystem:
    """ระบบตอบสนองแบบมีมนุษยธรรมครบวงจร"""
    
    def __init__(self):
        self.cognitive_engine = CognitiveEngine()
        self.dialogue_gen = DialogueGenerator()
        self.action_planner = ActionPlanner()
    
    def respond(self, situation: str, person_name: str = "เพื่อน") -> dict:
        """สร้างการตอบสนองที่สมบูรณ์"""
        
        print(f"\n{'='*70}")
        print(f"🎭 สถานการณ์: {situation[:80]}...")
        print(f"{'='*70}\n")
        
        # Step 1: ใช้ Cognitive Engine วิเคราะห์
        analysis = self.cognitive_engine.solve(situation)
        
        # Step 2: กำหนดอารมณ์หลักของสถานการณ์
        emotions_map = {
            "emotional": "sadness",
            "logical": "confusion", 
            "time": "fear",
            "systemic": "anger"
        }
        
        primary_emotion = "confusion"
        if analysis["categories"]:
            primary_emotion = emotions_map.get(analysis["categories"][0], "confusion")
        
        # Step 3: สร้างบทพูด
        print("💬 กำลังสร้างบทพูด...")
        dialogue_sequence = []
        
        # เปิดด้วย empathy
        dialogue_sequence.append({
            "speaker": "เรา",
            "emotion": "empathy",
            "text": self.dialogue_gen.generate("empathy", situation),
            "tone": "นุ่มนวล เข้าใจ"
        })
        
        # ตามด้วย validation
        dialogue_sequence.append({
            "speaker": "เรา", 
            "emotion": "validation",
            "text": self.dialogue_gen.generate("validation", situation),
            "tone": "ยอมรับ ไม่ตัดสิน"
        })
        
        # บอกความจริงอย่างอ่อนโยน (ถ้าจำเป็น)
        if "truth" in situation.lower() or "บอก" in situation:
            dialogue_sequence.append({
                "speaker": "เรา",
                "emotion": "gentle_truth", 
                "text": self.dialogue_gen.generate("gentle_truth", situation),
                "tone": "จริงใจ แต่ระมัดระวัง"
            })
        
        # เสนอแผนการกระทำ
        dialogue_sequence.append({
            "speaker": "เรา",
            "emotion": "action_oriented",
            "text": self.dialogue_gen.generate("action_oriented", situation),
            "tone": "มุ่งมั่น เป็นผู้นำ"
        })
        
        # ปิดด้วยการสนับสนุน
        dialogue_sequence.append({
            "speaker": "เรา",
            "emotion": "support",
            "text": self.dialogue_gen.generate("support", situation),
            "tone": "อบอุ่น มั่นคง"
        })
        
        # Step 4: สร้างแผนการกระทำ
        print("📋 กำลังสร้างแผนการกระทำ...")
        urgency = "normal"
        if any(word in situation for word in ["ด่วน", "ฉุกเฉิน", "ตอนนี้", "ทันที"]):
            urgency = "high_urgency"
        elif any(word in situation for word in ["ระยะยาว", "อนาคต", "ปีหน้า"]):
            urgency = "long_term"
            
        action_plan = self.action_planner.create_action_plan(analysis["decision"], urgency)
        
        # Step 5: แสดงผลลัพธ์
        print("\n" + "="*70)
        print("💬 บทสนทนาแนะนำ")
        print("="*70)
        
        for i, line in enumerate(dialogue_sequence, 1):
            print(f"\n[{i}] {line['speaker']} ({line['tone']}):")
            print(f"    \"{line['text']}\"")
            time.sleep(0.3)  # จำลองการคิด
        
        print("\n" + "="*70)
        print("📋 แผนการกระทำ")
        print("="*70)
        
        for step in action_plan:
            print(f"\n  ขั้นตอนที่ {step['step']}: {step['action']}")
            print(f"  ⏰ เวลา: {step['time']}")
        
        print("\n" + "="*70)
        print("📊 สรุปการวิเคราะห์")
        print("="*70)
        print(f"หมวดหมู่: {', '.join(analysis['categories'])}")
        print(f"สาเหตุรากเหง้า: {analysis['root_cause'][:100]}...")
        print(f"ทางเลือกที่เลือก: {analysis['decision']['chosen_solution']}")
        print(f"ความมั่นใจ: {analysis['decision']['confidence']*100:.0f}%")
        
        return {
            "dialogue": dialogue_sequence,
            "action_plan": action_plan,
            "analysis": analysis
        }

# ทดสอบระบบ
if __name__ == "__main__":
    system = HumanityResponseSystem()
    
    # ทดสอบกับเคสเดียวเพื่อความเร็ว
    test_case = {
        "situation": "รู้ความลับว่าจะเกิดภัยพิบัติใหญ่ใน 1 ปี แต่การเตือนตอนนี้จะทำให้ถูกมองว่าเป็นคนบ้า ถูกฟ้องร้อง และเสียชื่อเสียง",
        "name": "ผู้รู้ความลับ"
    }
    
    print(f"\n{'#'*70}")
    print(f"# ทดสอบระบบ: {test_case['name']}")
    print(f"{'#'*70}\n")
    
    result = system.respond(test_case["situation"], test_case["name"])
    
    print("\n\n✅ ทดสอบระบบเสร็จสิ้น!")
