"""
Demo: แสดงความสามารถในการสร้าง Response หลายรูปแบบจากระบบวิเคราะห์
"""
import json
from datetime import datetime

# จำลองผลลัพธ์จากการวิเคราะห์ของ Cognitive Engine (สมมติว่าวิเคราะห์เสร็จแล้ว)
analysis_result = {
    "problem": "พนักงานเก่งมากแต่ทัศนคติเป็นพิษ ทำลายทีม",
    "core_conflict": "ผลประโยชน์ระยะสั้น (งานเสร็จเร็ว) vs ความยั่งยืนของทีม (ขวัญและกำลังใจ)",
    "risk_level": "High",
    "emotional_impact": {
        "team": "หมดไฟ, รู้สึกไม่ยุติธรรม",
        "individual": "รู้สึกว่าตัวเองสำคัญจนไม่มีใครแทนได้"
    },
    "recommended_action": "คุยส่วนตัวอย่างจริงจัง (Direct Conversation) + ตั้งขอบเขตชัดเจน (Clear Boundary)",
    "ethical_note": "ต้องให้โอกาสแก้ไขก่อนเลิกจ้าง แต่ต้องปกป้องส่วนรวมเป็นหลัก"
}

class ResponseGenerator:
    def __init__(self, data):
        self.data = data

    def generate_raw_json(self):
        """แบบที่ 1: Raw Data สำหรับระบบอื่นประมวลผลต่อ"""
        return json.dumps({
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "analysis": self.data,
            "format": "machine_readable"
        }, ensure_ascii=False, indent=2)

    def generate_structured_report(self):
        """แบบที่ 2: Structured Report สำหรับผู้บริหารอ่าน"""
        report = []
        report.append("=" * 50)
        report.append("📊 รายงานการวิเคราะห์สถานการณ์ (Executive Summary)")
        report.append("=" * 50)
        report.append(f"🔍 ปัญหาหลัก: {self.data['problem']}")
        report.append(f"⚖️ ความขัดแย้งแกนกลาง: {self.data['core_conflict']}")
        report.append(f"⚠️ ระดับความเสี่ยง: {self.data['risk_level']}")
        report.append("-" * 50)
        report.append("💡 ข้อเสนอแนะ:")
        report.append(f"   - การกระทำ: {self.data['recommended_action']}")
        report.append(f"   - ข้อควรระวังทางจริยธรรม: {self.data['ethical_note']}")
        report.append("-" * 50)
        report.append("ผลกระทบทางอารมณ์ที่คาดการณ์:")
        for party, impact in self.data['emotional_impact'].items():
            report.append(f"   - {party.capitalize()}: {impact}")
        report.append("=" * 50)
        return "\n".join(report)

    def generate_human_dialogue(self):
        """แบบที่ 3: Human-Centric Dialogue สำหรับพูดคุยกับผู้ใช้โดยตรง"""
        # ใช้เทคนิค Empathy Mapping ในการสร้างประโยค
        opening = "ผมเข้าใจว่าสถานการณ์นี้คงทำให้คุณปวดหัวไม่น้อยเลยครับ "
        empathy = f"การที่ต้องรักษาคนที่ 'ทำงานเก่ง' แต่ทำให้ 'ทีมแตกแยก' เป็นโจทย์ที่ยากมาก "
        insight = f"จากข้อมูลที่วิเคราะห์มา จุดสำคัญไม่ใช่แค่เรื่องงาน แต่คือความรู้สึก 'ไม่ยุติธรรม' ที่เกิดขึ้นในทีมครับ"
        advice = f"ผมแนะนำให้ลองหาเวลาคุยส่วนตัวกับเขาตรงๆ ดูครับ โดยเน้นตั้งขอบเขตให้ชัดเจนว่าทักษะอย่างเดียวไม่พอถ้าทำลายทีม "
        closing = "อย่าลืมว่าเป้าหมายคือการปกป้องทีมในระยะยาวนะครับ คุณทำได้ดีแน่ๆ"
        
        return f"{opening}{empathy}\n\n{insight}\n\n{advice}\n\n{closing}"

# รัน Demo
if __name__ == "__main__":
    generator = ResponseGenerator(analysis_result)

    print("\n--- 🟢 แบบที่ 1: Raw Data (สำหรับ Machine) ---")
    print(generator.generate_raw_json())

    print("\n\n--- 🔵 แบบที่ 2: Structured Report (สำหรับอ่านเอาสาระ) ---")
    print(generator.generate_structured_report())

    print("\n\n--- 🟠 แบบที่ 3: Human Dialogue (สำหรับพูดคุยให้กำลังใจ) ---")
    print(generator.generate_human_dialogue())
    print("\n")
