"""
Cognitive Decomposition Engine
สถาปัตยกรรม "แยกชั้นความคิด" สำหรับแก้ปัญหาซับซ้อน
"""

class Perception:
    """รับข้อมูล แยกแยะข้อเท็จจริง vs สมมติฐาน"""
    def __init__(self):
        self.facts = []
        self.assumptions = []
        self.stakeholders = []
    
    def analyze(self, situation: str) -> dict:
        # ในระบบจริงจะใช้ AI แยกข้อเท็จจริง
        return {
            "what_happened": "สถานการณ์ที่เกิดขึ้น",
            "who_involved": ["ผู้เกี่ยวข้อง"],
            "real_data": ["ข้อมูลจริง"],
            "assumptions": ["สมมติฐานที่ต้องตรวจสอบ"]
        }

class Classifier:
    """จัดหมวดหมู่ปัญหา"""
    CATEGORIES = {
        "emotional": "ปัญหาด้านอารมณ์",
        "logical": "ปัญหาด้านตรรกะ",
        "resource": "ปัญหาด้านทรัพยากร",
        "time": "ปัญหาด้านเวลา",
        "systemic": "ปัญหาเชิงระบบ"
    }
    
    def categorize(self, problem: str) -> list:
        # วิเคราะห์ว่าปัญหาอยู่ในหมวดไหนบ้าง
        return ["logical", "emotional", "time"]

class Decomposer:
    """แตกปัญหาเป็นองค์ประกอบย่อย"""
    def decompose(self, problem: str) -> dict:
        return {
            "causes": ["สาเหตุ"],
            "effects": ["ผลกระทบ"],
            "variables": ["ตัวแปร"],
            "constraints": ["ข้อจำกัด"],
            "risks": ["ความเสี่ยง"],
            "motivations": ["แรงจูงใจ"]
        }

class CausalReasoner:
    """หา Root Cause ด้วย 5 Whys และ Cause-Effect Chain"""
    def five_whys(self, problem: str) -> list:
        chain = []
        current = problem
        for i in range(5):
            # ถามว่า "ทำไม" ต่อเนื่อง
            chain.append(f"Why {i+1}: {current}")
            current = f"Root cause of {current}"  # ในระบบจริงจะวิเคราะห์ต่อ
        return chain
    
    def find_root_cause(self, problem: str) -> str:
        chain = self.five_whys(problem)
        return chain[-1]  # สาเหตุรากเหง้า

class Planner:
    """สร้างทางเลือกในการแก้ปัญหา"""
    def generate_options(self, root_cause: str) -> dict:
        return {
            "quick_fix": ["ทางแก้เร็ว"],
            "long_term": ["ทางแก้ระยะยาว"],
            "systemic": ["ทางแก้เชิงระบบ"],
            "preventive": ["ทางแก้เชิงป้องกัน"]
        }

class Evaluator:
    """วิเคราะห์ Trade-off ของแต่ละทางเลือก"""
    def evaluate(self, options: dict) -> list:
        evaluated = []
        for category, solutions in options.items():
            for solution in solutions:
                evaluated.append({
                    "solution": solution,
                    "pros": ["ข้อดี"],
                    "cons": ["ข้อเสีย"],
                    "cost": 5,  # เปลี่ยนเป็นตัวเลข
                    "risk": 3,  # เปลี่ยนเป็นตัวเลข
                    "impact": 7,  # เพิ่ม impact
                    "side_effects": ["ผลข้างเคียง"]
                })
        return evaluated

class Decision:
    """ตัดสินใจเลือกทางเลือกที่ดีที่สุด"""
    def choose(self, evaluated_options: list) -> dict:
        # เลือกจาก: impact สูง, cost ต่ำ, scalable, sustainable
        best = max(evaluated_options, 
                  key=lambda x: (x.get('impact', 0), -x.get('cost', 0)))
        return {
            "chosen_solution": best['solution'],
            "reason": "เหตุผลที่เลือก",
            "confidence": 0.95
        }

class Feedback:
    """ตรวจสอบผลและเรียนรู้ย้อนกลับ"""
    def monitor(self, decision: dict) -> dict:
        return {
            "improved": True,
            "side_effects": [],
            "adjustments_needed": [],
            "lessons_learned": []
        }

class CognitiveEngine:
    """เครื่องยนต์หลักที่เชื่อมทุกโมดูล"""
    def __init__(self):
        self.perception = Perception()
        self.classifier = Classifier()
        self.decomposer = Decomposer()
        self.causal_reasoner = CausalReasoner()
        self.planner = Planner()
        self.evaluator = Evaluator()
        self.decision = Decision()
        self.feedback = Feedback()
    
    def solve(self, problem: str, context: dict = None) -> dict:
        print(f"🧠 กำลังวิเคราะห์ปัญหา: {problem[:50]}...")
        
        # Step 1: รับรู้ปัญหา
        print("  1. 📡 รับรู้ปัญหา...")
        perception = self.perception.analyze(problem)
        
        # Step 2: จัดหมวดหมู่
        print("  2. 🏷️ จัดหมวดหมู่...")
        categories = self.classifier.categorize(problem)
        
        # Step 3: แตกปัญหา
        print("  3. 🔪 แยกองค์ประกอบ...")
        components = self.decomposer.decompose(problem)
        
        # Step 4: หา Root Cause
        print("  4. 🎯 หาสาเหตุรากเหง้า...")
        root_cause = self.causal_reasoner.find_root_cause(problem)
        
        # Step 5: สร้างทางเลือก
        print("  5. 💡 สร้างทางเลือก...")
        options = self.planner.generate_options(root_cause)
        
        # Step 6: ประเมินผลกระทบ
        print("  6. ⚖️ วิเคราะห์ Trade-off...")
        evaluated = self.evaluator.evaluate(options)
        
        # Step 7: ตัดสินใจ
        print("  7. ✅ ตัดสินใจ...")
        decision = self.decision.choose(evaluated)
        
        # Step 8: ตรวจสอบผล
        print("  8. 🔄 ตรวจสอบและเรียนรู้...")
        feedback = self.feedback.monitor(decision)
        
        return {
            "problem": problem,
            "categories": categories,
            "root_cause": root_cause,
            "decision": decision,
            "feedback": feedback
        }

# ทดสอบระบบ
if __name__ == "__main__":
    engine = CognitiveEngine()
    
    # ทดสอบกับเคส "ความลับของอนาคต"
    problem = """
    รู้ความลับว่าจะเกิดภัยพิบัติใหญ่ใน 1 ปี แต่การเตือนตอนนี้จะทำให้
    ถูกมองว่าเป็นคนบ้า ถูกฟ้องร้อง และเสียชื่อเสียง
    """
    
    result = engine.solve(problem)
    
    print("\n" + "="*60)
    print("📊 สรุปผลการวิเคราะห์")
    print("="*60)
    print(f"หมวดหมู่ปัญหา: {result['categories']}")
    print(f"สาเหตุรากเหง้า: {result['root_cause']}")
    print(f"ทางเลือกที่เลือก: {result['decision']['chosen_solution']}")
    print(f"เหตุผล: {result['decision']['reason']}")
    print(f"ความมั่นใจ: {result['decision']['confidence']*100:.0f}%")
