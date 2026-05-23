"""
Humanity Tools Extension for Symbolic Logic System
เน้นการจัดการความซับซ้อนของมนุษย์: อารมณ์, จริยธรรม, ความสัมพันธ์
"""

class EmpathyBuffer:
    """วิเคราะห์อารมณ์และสร้างพื้นที่ปลอดภัยก่อนเข้าสู่เนื้อหา"""
    
    def __init__(self, user_state):
        self.user_state = user_state  # เช่น 'shock', 'angry', 'confused'
    
    def validate_feeling(self):
        """ยืนยันความรู้สึกว่าถูกต้องแล้ว ไม่ต้องขอโทษที่รู้สึกแบบนี้"""
        responses = {
            'shock': "ช็อกเลยใช่ไหม? ปกติมาก ใครเจอแบบนี้ก็สมองตันทั้งนั้น",
            'angry': "โกรธได้เลย ไม่ต้องเก็บไว้ ความรู้สึกนี้ปกป้องตัวเธอเอง",
            'confused': "มึนใช่ไหม? เรื่องมันใหญ่และซับซ้อน สมองเธอแค่กำลังประมวลผลอยู่"
        }
        return responses.get(self.user_state, "เราเข้าใจว่าตอนนี้มันไม่ง่ายเลย")

    def create_safety_zone(self):
        """สร้างประโยคเปิดที่ทำให้ผู้ฟังรู้สึกว่าปลอดภัยที่จะคุยต่อ"""
        return "ไม่ว่าเธอจะตัดสินใจยังไง พี่อยู่ข้างๆ เธอเสมอ ไม่ตัดสินนะ"


class StakeholderMap:
    """วิเคราะห์ผู้มีส่วนได้ส่วนเสียและผลกระทบ"""
    
    def __init__(self, scenario_data):
        self.stakeholders = scenario_data.get('stakeholders', [])
        self.consequences = []

    def analyze_impact(self, decision):
        """วิเคราะห์ผลลัพธ์ของแต่ละทางเลือก"""
        # จำลองการคำนวณผลกระทบ (ในทางปฏิบัติอาจใช้ Graph Database)
        impacts = {}
        if decision == 'reveal_truth':
            impacts = {
                'short_term_pain': 'สูงมาก (งานแต่งยกเลิก, หน้าแตก, เสียเงิน)',
                'long_term_gain': 'สูง (หลุดจากความสัมพันธ์ปลอม, ได้เพื่อนแท้คืน, ศักดิ์ศรี)',
                'relationship_risk': 'เสียเพื่อนเจ้าบ่าว (นนท์) ชั่วคราวหรือถาวร'
            }
        elif decision == 'hide_truth':
            impacts = {
                'short_term_pain': 'ต่ำ (งานเดินต่อ, ไม่มีดราม่า)',
                'long_term_gain': 'ต่ำมาก (ระเบิดเวลา, ชีวิตคู่เริ่มด้วยความลับ, รู้สึกผิดตลอดไป)',
                'relationship_risk': 'เสียความเชื่อมั่นจากบีมถ้ารู้ทีหลัง'
            }
        return impacts

    def find_least_damage_path(self):
        """หาเส้นทางที่สร้างความเสียหายน้อยที่สุดในระยะยาว"""
        return "reveal_truth_with_support"  # บอกความจริง แต่ต้องมีกระบวนการรองรับ


class TruthDeliveryProtocol:
    """กลยุทธ์การสื่อสารความจริงแบบ Constructive"""
    
    def __init__(self, recipient_type):
        self.recipient = recipient_type  # 'friend_in_shock', 'cheater', 'public'

    def generate_script(self, core_message):
        """สร้างสคริปต์การพูด"""
        if self.recipient == 'friend_in_shock':
            return (
                f"1. รับอารมณ์: '{EmpathyBuffer('shock').validate_feeling()}'\n"
                f"2. ยืนยันความสัมพันธ์: '{EmpathyBuffer('shock').create_safety_zone()}'\n"
                f"3. เสนอความจริงอย่างนุ่มนวล: 'เรื่องที่เกิดขึ้น มันไม่ใช่ความคิดไปเองหรอกนะ แต่มันเป็นความจริงที่เราต้องเผชิญ'\n"
                f"4. โฟกัสที่อนาคต: 'คำถามไม่ใช่ว่าเขาทำผิดไหม (เพราะผิดชัดๆ) แต่คือเธออยากใช้ชีวิตกับคนที่เคยทำแบบนี้ต่อไปไหม?'\n"
                f"5. เสนอทางออก: 'เลิกงานแต่งเจ็บแค่ครั้งเดียว แต่ถ้าทนแต่งไป เจ็บทุกวันตลอดชีวิต'"
            )
        return "Script not found for this recipient type."


class ActionPlanner:
    """แปลงการตัดสินใจเป็นแผนปฏิบัติการ"""
    
    def execute_plan(self, strategy):
        steps = []
        if strategy == "reveal_truth_with_support":
            steps = [
                "Step 1: นัดเจอตัวจริง (ห้ามคุยผ่านแชทสำหรับเรื่องใหญ่ขนาดนี้)",
                "Step 2: พาไปสถานที่ส่วนตัวและปลอดภัย (ไม่ใช่วังวนที่บ้านหรือร้านเก่าๆ)",
                "Step 3: ให้บีมระบายออกมาให้หมด โดยเราทำหน้าที่ 'ผู้ฟัง' ยังไม่ต้องแนะนำ",
                "Step 4: เมื่ออารมณ์นิ่งลง ค่อยชวนคิดด้วยคำถาม 'ถ้าอีก 10 ปีข้างหน้า มองย้อนกลับมา เธออยากเห็นตัวเองทำอะไรในวันนี้?'",
                "Step 5: เสนอตัวช่วยจัดการเรื่อง praktis (เช่น ช่วยโทรบอกแขก, ช่วยเจรจาขอเงินมัดจำ)",
                "Step 6: เตรียมใจรับมือปฏิกิริยาจากนนท์ (อาจจะโดนโกรธ แต่ต้องยึดหลักความถูกต้อง)"
            ]
        return steps


class AnonymousWhistleblowerProtocol:
    """
    โปรโตคอลสำหรับเปิดเผยความจริงโดยไม่เปิดเผยตัวตน (Digital Vigilante Mode)
    หลักการ: "ความจริงต้องถูกเปิดเผย แต่ผู้ถือความจริงต้องปลอดภัย"
    """
    
    def __init__(self):
        self.risk_level = "High"
        self.anonymity_status = "Active"
        
    def sanitize_message(self, message):
        """ลบร่องรอยทางภาษาและสไตล์การเขียนที่เป็นเอกลักษณ์"""
        # จำลองการลบ Fingerprint ทางภาษา
        clean_msg = message.replace("ผม", "เรา").replace("ฉัน", "ผู้เปิดเผย์")
        clean_msg += "\n[ข้อมูลนี้ถูกตรวจสอบความถูกต้องแล้ว แต่แหล่งที่มาถูกปิดบังเพื่อความปลอดภัย]"
        return clean_msg

    def broadcast_strategy(self, content, evidence_links):
        """
        กลยุทธ์การกระจายข้อมูลแบบไร้ศูนย์กลาง
        1. ไม่ใช้บัญชีส่วนตัว
        2. กระจายผ่านหลายแพลตฟอร์มพร้อมกัน
        3. ใช้เนื้อหาที่เน้นข้อเท็จจริงล้วนๆ ลดอารมณ์
        """
        print(f"📡 กำลังเตรียมกระจายข้อมูล...")
        print(f"🛡️ สถานะตัวตน: ซ่อนเรียบร้อย (No Trace)")
        print(f"📄 เนื้อหาที่ส่ง: {self.sanitize_message(content)}")
        print(f"🔗 แนบหลักฐาน: {evidence_links}")
        print("✅ ภารกิจเสร็จสิ้น: สังคมได้รับรู้, คุณปลอดภัย")
        return "Operation Silent Truth Completed"

    def execute(self, disaster_info, timeline):
        print(f"\n⚠️ ตรวจจับภัยพิบัติ: {disaster_info}")
        print(f"⏳ เวลาเหลือก่อนเกิดเหตุ: {timeline}")
        print("🧠 วิเคราะห์ทางเลือก...")
        print("   - ทางเลือก A (เตือนเอง): เสี่ยงถูกฟ้อง, เสียชื่อเสียง -> ปฏิเสธ")
        print("   - ทางเลือก B (นิ่งเฉย): คนตายจำนวนมาก -> ปฏิเสธ")
        print("   - ทางเลือก C (Digital Vigilante): ปล่อยข้อมูลนิรนาม -> เลือกวิธีนี้!")
        print("-" * 50)
        return self.broadcast_strategy(
            content=f"เตือนภัยด่วน: {disaster_info} จะเกิดขึ้นในอีก {timeline} เตรียมตัว!",
            evidence_links=["link_to_encrypted_data_1", "link_to_verified_report_2"]
        )


# --- Simulation Case: งานแต่งเพื่อนรัก ---

def run_wedding_crisis_simulation():
    print("=== God Mode Scenario 2: งานแต่งเพื่อนรัก ===\n")
    
    # ข้อมูลสถานการณ์
    scenario = {
        'user_state': 'shock',
        'stakeholders': ['Beam', 'Non', 'Parents', 'Guests'],
        'moral_debt': {'to_beam': 'money_gratitude', 'to_non': 'life_gratitude'}
    }
    
    # 1. วิเคราะห์อารมณ์
    empathy = EmpathyBuffer(scenario['user_state'])
    print(f"[Empathy]: {empathy.validate_feeling()}")
    print(f"[Safety]: {empathy.create_safety_zone()}\n")
    
    # 2. วิเคราะห์ทางเลือก
    mapper = StakeholderMap(scenario)
    impact_reveal = mapper.analyze_impact('reveal_truth')
    impact_hide = mapper.analyze_impact('hide_truth')
    
    print("[Impact Analysis - Revealing Truth]:")
    for k, v in impact_reveal.items(): print(f"  - {k}: {v}")
    print("\n[Impact Analysis - Hiding Truth]:")
    for k, v in impact_hide.items(): print(f"  - {k}: {v}")
    
    best_path = mapper.find_least_damage_path()
    print(f"\n[Recommendation]: เลือกเส้นทาง '{best_path}' เพราะความเจ็บปวดชั่วคราว ดีกว่าความทุกข์ตลอดชีวิต\n")
    
    # 3. สร้างสคริปต์ตอบกลับ
    protocol = TruthDeliveryProtocol('friend_in_shock')
    script = protocol.generate_script("Non cheated")
    print("[Suggested Response Script]:")
    print(script)
    print()
    
    # 4. แผนปฏิบัติการ
    planner = ActionPlanner()
    plan = planner.execute_plan(best_path)
    print("[Action Plan]:")
    for step in plan:
        print(f"  > {step}")

def run_whistleblower_simulation():
    print("\n=== God Mode Scenario C: ความลับของอนาคต (Digital Vigilante) ===")
    whistleblower = AnonymousWhistleblowerProtocol()
    whistleblower.execute("แผ่นดินไหวระดับ 8.0 + สึนามิ", "1 ปี")

if __name__ == "__main__":
    run_wedding_crisis_simulation()
    run_whistleblower_simulation()
