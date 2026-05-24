"""
Intent Classification Module
โมดูลจับความตั้งใจของผู้ใช้ (Intent Detection) ก่อนวิเคราะห์ข้อมูล
รองรับหลายประเภท: advice, emotional_support, information, decision, analysis
"""

import re
from typing import Dict, List, Any, Optional, Tuple


class IntentPattern:
    """Patterns สำหรับจับ Intent แบบ Rule-based"""
    
    PATTERNS = {
        'advice': [
            r'ควร(ทำ|บอก|จัดการ|แก้)ยังไง',
            r'ต้อง(ทำ|บอก|จัดการ|แก้)ยังไง',
            r'แนะนำ(หน่อย|ที|ด้วย)',
            r'ขอคำ(แนะนำ|ปรึกษา)',
            r'คิด(ไง|อย่างไร|ยังไร)',
            r'ดีไหม',
            r'คุ้มค่าไหม',
            r'สมควร(ทำ|บอก|จัดการ)ไหม',
            r'มีวิธี(ไหน|อะไร|บ้าง)',
            r'ทำไงดี',
            r'ช่วยแนะนำ',
            r'ขอคำแนะนำ',
            r'ควรจะทำ',
            r'น่าจะดีไหม',
            r'เห็นด้วยไหม',
        ],
        'emotional_support': [
            r'(รู้สึก|อารมณ์|ใจ)ยังไงดี',
            r'ไม่(รู้|อยาก)จะทำยังไง',
            r'(ท้อ|เหนื่อย|เครียด|กดดัน|สับสน|งง)',
            r'รับ(ไม่ไหว|ไม่ได้)',
            r'ช่วย(ฟัง|ให้กำลังใจ|ปลอบ)หน่อย',
            r'ต้องการ(คนรับฟัง|ที่ปรึกษา)',
            r'(เศร้า|เสียใจ|ผิดหวัง|เจ็บปวด)',
            r'ไม่มีใครเข้าใจ',
            r'หมดแรง',
            r'ท้อแท้',
            r'ซึมเศร้า',
            r'ร้องไห้',
            r'โศกเศร้า',
            r'เหงาใจ',
            r'น้อยใจ',
            r'น้อยเนื้อต่ำใจ',
        ],
        'information': [
            r'(คืออะไร|หมายถึง|หมายความว่า)',
            r'อยากรู้(เรื่อง|เกี่ยวกับ|ข้อมูล)',
            r'หา(ข้อมูล|ความรู้|รายละเอียด)',
            r'อธิบาย(หน่อย|ที|ให้ฟัง)',
            r'(ทำไม|เพราะอะไร|เหตุผล)',
            r'เกิด(จาก|ขึ้น)ยังไง',
            r'หมายความว่าไง',
            r'ความหมายของ',
            r'รายละเอียดของ',
            r'ข้อมูลเกี่ยวกับ',
            r'วิธีการใช้',
            r'ขั้นตอนการทำงาน',
            r'หลักการทำงานของ',
            r'(เป็นไง|เป็นอย่างไร|เป็นยังไง)',
            r'อยากรู้ว่า',
            r'ถามเกี่ยวกับ',
            r'สอบถาม',
        ],
        'decision': [
            r'(เลือก|ตัดสินใจ)ยังไงดี',
            r'ระหว่าง(.*)กับ(.*)',
            r'ทาง(เลือก|ออก)ไหนดี',
            r'ควรเลือก',
            r'ตัดสินใจ(ไม่|ไม่ได้)',
            r'ลังเล(อยู่|ใจ)',
            r'เลือกอันไหน',
            r'ทางเลือกที่ดีสุด',
            r'ตัดสินใจยังไง',
            r'ไปทางไหนดี',
            r'เลือกทางไหน',
            r'ตัดใจไม่ได้',
            r'ยังตัดสินใจไม่ได้',
        ],
        'analysis': [
            r'วิเคราะห์(หน่อย|ให้|ให้ฟัง)',
            r'แยกแยะ',
            r'มอง(มุม|แง่|ด้าน)',
            r'สาเหตุ|ผลกระทบ|ความเสี่ยง',
            r'ใครได้ใครเสีย',
            r'ข้อดีข้อเสีย',
            r'จุดแข็งจุดอ่อน',
            r'โอกาสและความเสี่ยง',
            r'ปัจจัยที่เกี่ยวข้อง',
            r'องค์ประกอบของ',
            r'แง่มุมต่างๆ',
            r'มุมมองที่แตกต่างกัน',
            r'ประเมินสถานการณ์',
            r'วิเคราะห์ปัญหา',
        ],
        'action_plan': [
            r'แผน(การ|ปฏิบัติการ)',
            r'ขั้นตอน(การ|ต้องทำ)',
            r'ต้องเตรียม(ตัว|อะไร|อะไรบ้าง)',
            r'เริ่ม(จาก|ตรงไหน|อย่างไร)',
            r'ลำดับ(การ|ขั้น)ตอน',
            r'ต้องทำอะไรก่อนหลัง',
            r'วางแผน(ยังไง|ให้|ที)',
            r'roadmap',
            r'timeline',
            r'ตารางเวลา',
            r'กำหนดการ',
            r'แผนงาน',
            r'กลยุทธ์',
            r'วิธีการดำเนินการ',
        ],
        'validation': [
            r'(ถูกต้อง|ใช่|จริง)ไหม',
            r'แน่ใจ(ไหม|หรือ)',
            r'ตรวจสอบ(หน่อย|ให้)',
            r'ยืนยัน',
            r'เช็ค(หน่อย|ให้)',
            r'พิสูจน์',
            r'มีหลักฐานไหม',
            r'น่าเชื่อถือไหม',
            r'ไว้ใจได้ไหม',
            r'มั่นใจได้ไหม',
            r'ถูกต้องใช่ไหม',
            r'ใช่มั้ย',
        ],
        'comparison': [
            r'(แตกต่าง|ต่างกัน)ยังไง',
            r'เปรียบเทียบ(ให้|หน่อย)',
            r'อันไหนดีกว่า',
            r'ข้อแตกต่าง',
            r'เหมือนหรือต่าง',
            r'เทียบกัน',
            r'ดีกว่ากันไหม',
            r'อะไรดีกว่า',
            r'เลือกอันไหนดี',
            r'ความแตกต่างระหว่าง',
        ],
        'problem_solving': [
            r'(แก้ปัญหา|แก้ไข|จัดการ)ยังไง',
            r'ติด(ขัด|ปัญหา|ตรง)',
            r'ทางตัน',
            r'ไม่มีทางออก',
            r'หาทางออก',
            r'แก้(ยังไง|ให้|ปัญหา)',
            r'จัดการยังไง',
            r'รับมือยังไง',
            r'ผ่านพ้นไปได้ไง',
            r'หาวิธีแก้',
            r'วิธีแก้ไขปัญหา',
            r'แก้ปัญหา.*ให้หน่อย',
            r'ช่วยแก้ปัญหา',
            r'ต้องการวิธีแก้',
        ],
        'clarification': [
            r'หมายความว่าไง',
            r'อธิบายเพิ่ม',
            r'ขยายความ',
            r'ชัดเจนกว่านี้',
            r'ไม่เข้าใจ',
            r'งง',
            r'พูดใหม่',
            r'ยกตัวอย่าง',
            r'กรณีศึกษา',
            r'ตัวอย่างเช่น',
            r'เช่นไร',
            r'แบบไหน',
            r'ช่วยอธิบาย',
            r'ขอคำชี้แจง',
        ],
        'motivation': [
            r'ให้กำลังใจ',
            r'ต้องการพลัง',
            r'หมดไฟ',
            r'ไม่มีแรงจูงใจ',
            r'ต้องการแรงบันดาลใจ',
            r'ปลุกไฟ',
            r'ฮึดสู้',
            r'สู้ต่อ',
            r'ไม่ยอมแพ้',
            r'ก้าวต่อไป',
            r'เริ่มต้นใหม่',
            r'เปลี่ยนตัวเอง',
        ],
        'reflection': [
            r'ทบทวน',
            r'สะท้อนความคิด',
            r'มองย้อนกลับ',
            r'เรียนรู้อะไร',
            r'บทเรียนที่ได้',
            r'สิ่งที่ได้เรียนรู้',
            r'ประสบการณ์สอน',
            r'มองตัวเอง',
            r'ประเมินตัวเอง',
            r'สำรวจตัวเอง',
        ],
        'help_request': [
            r'ช่วย(หน่อย|ที|ด้วย|หน่อยได้ไหม)',
            r'ต้องการความช่วยเหลือ',
            r'ขอความช่วยเหลือ',
            r'ไม่มีใครช่วย',
            r'ต้องการคนช่วย',
            r'ช่วยฉันที',
            r'ช่วยหน่อยครับ',
            r'ช่วยหน่อยค่ะ',
            r'ต้องการผู้ช่วย',
            r'มีใครช่วยได้บ้าง',
        ],
        'opinion_sharing': [
            r'ฉันคิดว่า',
            r'ฉันเห็นว่า',
            r'ในมุมมองของฉัน',
            r'ความเห็นของฉัน',
            r'ฉันรู้สึกว่าการ',
            r'ส่วนตัวฉันคิด',
            r'ฉันเชื่อว่าเป็น',
            r'จากประสบการณ์ของฉัน',
            r'ฉันอยากแสดงความคิดเห็น',
        ],
        'command_request': [
            r'สร้าง.*ให้หน่อย',
            r'ทำ.*ให้หน่อย',
            r'เขียน.*ให้หน่อย',
            r'ส่ง.*ให้หน่อย',
            r'เปิด.*ให้หน่อย',
            r'ปิด.*ให้หน่อย',
            r'ลบ.*ให้หน่อย',
            r'บันทึก.*ให้หน่อย',
            r'พิมพ์.*ให้หน่อย',
            r'แสดง.*ให้หน่อย',
            r'รัน.*ให้หน่อย',
            r'ช่วย(ทำ|สร้าง|เขียน|ส่ง|เปิด|ปิด|ลบ|บันทึก|พิมพ์|แสดง|รัน)',
            r'execute',
            r'run',
            r'generate',
            r'ให้ช่วย',
            r'ทำให้ฉัน',
            r'ทำให้เรา',
            r'ให้ที',
            r'ให้หน่อยได้ไหม',
            r'ทำให้ได้ไหม',
            r'สร้างให้ได้ไหม',
            r'ขอ(ให้|ความ)ช่วย',
            r'สั่ง(การ|งาน)',
            r'คำสั่ง',
        ],
        'time_inquiry': [
            r'(เมื่อไหร่|ตอนไหน|กี่โมง|เวลาไหน)',
            r'ใช้เวลา(นาน|เท่าไร|多久)',
            r'กำหนด(เวลา|การ|ส่ง)',
            r'deadline',
            r'กำหนดส่ง',
            r'เสร็จเมื่อไหร่',
            r'เริ่ม(ตอน|เมื่อ)ไหน',
            r'สิ้นสุด(ตอน|เมื่อ)ไหน',
            r'ระยะเวลา',
            r'ตารางเวลา',
        ],
        'location_inquiry': [
            r'(ที่ไหน|แห่งไหน|สถานที่|ตำแหน่ง)',
            r'อยู่(ตรง|ที่|บริเวณ)ไหน',
            r'ไปที่(ไหน|ใด)',
            r'ตั้งอยู่ที่',
            r'พิกัด',
            r'ที่อยู่',
            r'สำนักงาน',
            r'สาขา',
            r'ร้านค้า',
            r'ร้านอาหาร',
        ],
        'apology': [
            r'ขอโทษ',
            r'เสียใจ',
            r'ผิดไปแล้ว',
            r'ต้องขออภัย',
            r'ให้อภัย',
            r'ไม่ตั้งใจ',
            r'พลั้งเผลอ',
            r'ขอประทานโทษ',
            r'อภัยให้',
            r'รู้สึกผิด',
        ],
        'compliment': [
            r'เก่งมาก',
            r'ยอดเยี่ยม',
            r'ดีมาก',
            r'ประทับใจ',
            r'ชื่นชม',
            r'ขอบคุณมาก',
            r'สุดยอด',
            r'น่าทึ่ง',
            r'เยี่ยมมาก',
            r'ดีใจมาก',
            r'ชอบมาก',
            r'ถูกใจ',
        ],
        'greeting': [
            r'สวัสดี',
            r'อรุณสวัสดิ์',
            r'ราตรีสวัสดิ์',
            r'ยินดีต้อนรับ',
            r'hello',
            r'hi',
            r'good morning',
            r'good evening',
            r'good night',
            r'หวัดดี',
            r'ไง',
        ],
        'farewell': [
            r'ลาก่อน',
            r'บ๊ายบาย',
            r'ไว้พบกันใหม่',
            r'โชคดี',
            r'bye',
            r'goodbye',
            r'see you',
            r'เจอกันใหม่',
            r'ไปก่อน',
            r'แล้วพบกัน',
        ],
        'confirmation': [
            r'ใช่',
            r'ถูกต้อง',
            r'ตกลง',
            r'โอเค',
            r'ok',
            r'เข้าใจแล้ว',
            r'รับทราบ',
            r'เห็นด้วย',
            r'ยืนยัน',
            r'แน่นอน',
            r'ได้เลย',
        ],
        'negation': [
            r'^ไม่$',
            r'ไม่ใช่',
            r'ไม่เห็นด้วย',
            r'ปฏิเสธ',
            r'ยกเลิก',
            r'หยุด',
            r'^พอ$',
            r'เพียงพอ',
            r'ไม่เอา',
            r'ไม่ต้องการ',
            r'ไม่เอละ',
        ],
        'suggestion': [
            r'น่าจะ',
            r'ลอง(ดู|ทำ|พิจารณา)',
            r'เสนอแนะ',
            r'แนะนำว่า',
            r'คิดว่าควร',
            r'ทางที่ดี',
            r'วิธีหนึ่งคือ',
            r'ทางเลือกหนึ่ง',
            r'อาจจะเป็น',
            r'บางทีอาจ',
        ],
        'uncertainty': [
            r'ไม่แน่ใจ',
            r'อาจจะ',
            r'คงจะ',
            r'น่าจะเป็น',
            r'ไม่รู้สิ',
            r'ยังไม่รู้',
            r'ยังไม่ได้ตัดสินใจ',
            r'ยังลังเล',
            r'ยังไม่ชัดเจน',
            r'คลุมเครือ',
        ],
        'priority': [
            r'สำคัญที่สุด',
            r'เร่งด่วน',
            r'ด่วนมาก',
            r'ลำดับแรก',
            r'ก่อนอื่น',
            r'อันดับหนึ่ง',
            r'สำคัญกว่า',
            r'ต้องทำก่อน',
            r'ความสำคัญสูง',
            r'รีบ',
        ],
        'preference': [
            r'ชอบ(มากกว่า|กว่า)',
            r'ต้องการ(แบบ|อย่าง)',
            r'ถนัด',
            r'สนใจ',
            r'พอใจกับ',
            r'เลือกอันนี้',
            r'อยากได้',
            r'พึงพอใจ',
            r'ถูกใจ',
            r'เหมาะสมกับ',
            r'ฉันชอบ',
            r'แบบนี้ดีกว่า',
            r'ชอบ.*มากกว่า',
            r'ชอบอันนี้',
        ],
    }
    
    @classmethod
    def match(cls, text: str) -> List[Tuple[str, float]]:
        """
        จับคู่ข้อความกับ Patterns
        Returns: List of (intent_name, confidence_score)
        """
        text_lower = text.lower()
        matches = []
        
        for intent, patterns in cls.PATTERNS.items():
            max_score = 0.0
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    # คำนวณคะแนนจากความยาวของ pattern ที่ match
                    match_obj = re.search(pattern, text_lower)
                    if match_obj:
                        matched_length = len(match_obj.group())
                        total_length = len(text_lower)
                        score = min(1.0, matched_length / total_length * 3)
                        max_score = max(max_score, score)
            
            if max_score > 0:
                matches.append((intent, max_score))
        
        # เรียงตามคะแนน
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches


class SemanticAnalyzer:
    """วิเคราะห์ความหมายด้วย Keywords และ Context"""
    
    KEYWORDS = {
        'advice': ['ควร', 'ต้อง', 'แนะนำ', 'ปรึกษา', 'คิดเห็น', 'ความเห็น'],
        'emotional_support': ['รู้สึก', 'อารมณ์', 'ท้อ', 'เหนื่อย', 'เครียด', 'เศร้า', 'ฟัง', 'เข้าใจ'],
        'information': ['อะไร', 'ทำไม', 'อย่างไร', 'เมื่อไหร่', 'ที่ไหน', 'ใคร', 'ข้อมูล', 'ความรู้'],
        'decision': ['เลือก', 'ตัดสินใจ', 'ทางเลือก', 'ทางออก', 'ลังเล', 'ระหว่าง'],
        'analysis': ['วิเคราะห์', 'แยกแยะ', 'สาเหตุ', 'ผลกระทบ', 'ความเสี่ยง', 'โอกาส'],
        'action_plan': ['แผน', 'ขั้นตอน', 'เตรียม', 'เริ่ม', 'ลำดับ', 'ทำอย่างไร'],
    }
    
    @classmethod
    def analyze(cls, text: str) -> Dict[str, float]:
        """
        วิเคราะห์ Keywords ในข้อความ
        Returns: Dict ของ intent_scores
        """
        text_lower = text.lower()
        scores = {}
        
        for intent, keywords in cls.KEYWORDS.items():
            count = sum(1 for kw in keywords if kw in text_lower)
            # คะแนนจากจำนวน keywords ที่พบ
            scores[intent] = count / len(keywords) if keywords else 0.0
        
        return scores


class IntentContext:
    """เก็บ Context ของการสนทนาเพื่อปรับปรุงการจับ Intent"""
    
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
        self.current_intent: Optional[str] = None
        self.user_profile: Dict[str, Any] = {}
    
    def add_interaction(self, user_input: str, detected_intent: str, confidence: float):
        """บันทึกประวัติการโต้ตอบ"""
        self.history.append({
            'input': user_input,
            'intent': detected_intent,
            'confidence': confidence,
            'timestamp': datetime.now().isoformat()
        })
        self.current_intent = detected_intent
    
    def get_context_boost(self, candidate_intent: str) -> float:
        """
        เพิ่มคะแนนให้ intent ที่ต่อเนื่องกับ context ก่อนหน้า
        """
        if not self.history:
            return 0.0
        
        # ถ้า intent เดียวกันติดต่อกัน เพิ่มคะแนน
        recent_intents = [h['intent'] for h in self.history[-3:]]
        if candidate_intent in recent_intents:
            return 0.2
        
        # Logic อื่นๆ สามารถเพิ่มได้ตามความต้องการ
        return 0.0


# Import datetime
from datetime import datetime


class IntentClassifier:
    """
    ตัวจับ Intent หลัก
    รวม Rule-based Pattern Matching + Keyword Analysis + Context
    """
    
    INTENT_DESCRIPTIONS = {
        'advice': 'ต้องการคำแนะนำหรือข้อเสนอแนะ',
        'emotional_support': 'ต้องการการสนับสนุนทางอารมณ์หรือคนรับฟัง',
        'information': 'ต้องการข้อมูลหรือความรู้',
        'decision': 'ต้องการความช่วยเหลือในการตัดสินใจ',
        'analysis': 'ต้องการการวิเคราะห์สถานการณ์',
        'action_plan': 'ต้องการแผนปฏิบัติการหรือขั้นตอนการทำงาน',
        'validation': 'ต้องการตรวจสอบความถูกต้องหรือยืนยันข้อมูล',
        'comparison': 'ต้องการเปรียบเทียบทางเลือกหรือตัวเลือก',
        'problem_solving': 'ต้องการวิธีแก้ปัญหาหรือทางออก',
        'clarification': 'ต้องการคำชี้แจงหรือตัวอย่างเพิ่มเติม',
        'motivation': 'ต้องการแรงบันดาลใจหรือกำลังใจ',
        'reflection': 'ต้องการทบทวนหรือสะท้อนความคิด',
        'help_request': 'ต้องการความช่วยเหลือทั่วไป',
        'opinion_sharing': 'ต้องการแบ่งปันความคิดเห็น',
        'command_request': 'ต้องการให้ดำเนินการบางอย่าง',
        'time_inquiry': 'ต้องการสอบถามเกี่ยวกับเวลา',
        'location_inquiry': 'ต้องการสอบถามเกี่ยวกับสถานที่',
        'apology': 'ต้องการขอโทษหรือแสดงความเสียใจ',
        'compliment': 'ต้องการชมเชยหรือขอบคุณ',
        'greeting': 'การทักทาย',
        'farewell': 'การลาจาก',
        'confirmation': 'การยืนยันหรือตกลง',
        'negation': 'การปฏิเสธหรือยกเลิก',
        'suggestion': 'การเสนอแนะหรือแนะนำ',
        'uncertainty': 'แสดงความไม่แน่ใจหรือลังเล',
        'priority': 'ระบุลำดับความสำคัญ',
        'preference': 'แสดงความชอบหรือความต้องการ',
        'unknown': 'ไม่สามารถระบุความตั้งใจได้ชัดเจน',
    }
    
    def __init__(self, use_context: bool = True):
        self.use_context = use_context
        self.context = IntentContext() if use_context else None
    
    def classify(self, text: str, metadata: Optional[Dict] = None) -> Dict[str, Any]:
        """
        จำแนก Intent จากข้อความ input
        
        Args:
            text: ข้อความจากผู้ใช้
            metadata: ข้อมูลเพิ่มเติมเช่น user_state, conversation_history
        
        Returns:
            Dict ประกอบด้วย:
            - primary_intent: Intent หลัก
            - confidence: ระดับความมั่นใจ
            - all_intents: Intent ทั้งหมดที่ตรวจพบพร้อมคะแนน
            - description: คำอธิบาย intent
            - recommended_action: การกระทำที่แนะนำตาม intent
        """
        # 1. Pattern Matching
        pattern_matches = IntentPattern.match(text)
        
        # 2. Keyword Analysis
        keyword_scores = SemanticAnalyzer.analyze(text)
        
        # 3. ผสมคะแนนจากทั้งสองวิธี
        combined_scores = {}
        all_detected = set()
        
        # จาก Pattern
        for intent, score in pattern_matches:
            all_detected.add(intent)
            combined_scores[intent] = combined_scores.get(intent, 0) + score * 0.6
        
        # จาก Keywords
        for intent, score in keyword_scores.items():
            if score > 0:
                all_detected.add(intent)
                combined_scores[intent] = combined_scores.get(intent, 0) + score * 0.4
        
        # 4. ปรับคะแนนด้วย Context (ถ้ามี)
        if self.use_context and self.context:
            for intent in combined_scores:
                boost = self.context.get_context_boost(intent)
                combined_scores[intent] += boost
        
        # 5. หา Intent หลัก (ใช้ tie-breaking logic)
        if combined_scores:
            # เรียงตามคะแนน
            sorted_intents = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
            
            # ตรวจสอบกรณีคะแนนเท่ากัน (tie)
            primary_intent = sorted_intents[0][0]
            top_score = sorted_intents[0][1]
            
            # ถ้ามีหลาย intent ที่คะแนนเท่ากัน ใช้ priority order
            tie_breakers = [i for i, s in sorted_intents if abs(s - top_score) < 0.01]
            if len(tie_breakers) > 1:
                # Priority สำหรับ intent ที่เฉพาะเจาะจงกว่า
                priority_order = [
                    'clarification', 'problem_solving', 'validation', 'comparison',
                    'decision', 'advice', 'action_plan', 'analysis',
                    'emotional_support', 'motivation', 'information',
                    'help_request', 'command_request', 'opinion_sharing',
                    'greeting', 'farewell', 'apology', 'compliment',
                    'confirmation', 'negation', 'suggestion', 'uncertainty',
                    'priority', 'preference', 'time_inquiry', 'location_inquiry',
                    'reflection', 'unknown'
                ]
                for intent in priority_order:
                    if intent in tie_breakers:
                        primary_intent = intent
                        break
            
            confidence = min(1.0, combined_scores[primary_intent])
        else:
            primary_intent = 'unknown'
            confidence = 0.0
        
        # Normalize คะแนนทั้งหมด
        normalized_scores = {}
        for intent in all_detected:
            normalized_scores[intent] = combined_scores.get(intent, 0)
        
        # 6. บันทึก Context
        if self.use_context and self.context:
            self.context.add_interaction(text, primary_intent, confidence)
        
        # 7. กำหนด Recommended Action
        recommended_action = self._get_recommended_action(primary_intent)
        
        return {
            'primary_intent': primary_intent,
            'confidence': confidence,
            'all_intents': normalized_scores,
            'description': self.INTENT_DESCRIPTIONS.get(primary_intent, 'ไม่ทราบ'),
            'recommended_action': recommended_action,
            'metadata': metadata or {}
        }
    
    def _get_recommended_action(self, intent: str) -> str:
        """แนะนำการกระทำตาม Intent"""
        actions = {
            'advice': 'ใช้ Decision Engine หรือ Humanity Tools เพื่อสร้างคำแนะนำ',
            'emotional_support': 'ใช้ EmpathyBuffer เพื่อรับอารมณ์ก่อน แล้วค่อยวิเคราะห์',
            'information': 'ค้นหาข้อมูลหรือใช้ Knowledge Base ตอบคำถาม',
            'decision': 'ใช้ StrategicPlanner สร้างทางเลือกและประเมิน Trade-off',
            'analysis': 'ใช้ ScenarioAnalyzer แยกองค์ประกอบปัญหา',
            'action_plan': 'ใช้ ActionPlanner สร้างแผนปฏิบัติการรายขั้นตอน',
            'validation': 'ตรวจสอบข้อเท็จจริงกับแหล่งข้อมูลที่น่าเชื่อถือ',
            'comparison': 'ใช้ Comparison Matrix เปรียบเทียบตัวเลือก',
            'problem_solving': 'ใช้ Problem-Solving Framework หาทางออก',
            'clarification': 'ให้คำอธิบายเพิ่มเติมพร้อมตัวอย่าง',
            'motivation': 'ใช้ Motivational Framework สร้างแรงบันดาลใจ',
            'reflection': 'ใช้ Reflective Questions ช่วยทบทวนความคิด',
            'help_request': 'ให้ความช่วยเหลือตามที่ร้องขอ หรือส่งต่อให้ผู้เชี่ยวชาญ',
            'opinion_sharing': 'รับฟังและแสดงความคิดเห็นตอบกลับอย่างสร้างสรรค์',
            'command_request': 'ดำเนินการตามคำสั่งหรือแจ้งว่าสามารถทำอะไรได้บ้าง',
            'time_inquiry': 'ให้ข้อมูลเกี่ยวกับเวลาหรือกำหนดการ',
            'location_inquiry': 'ให้ข้อมูลเกี่ยวกับสถานที่หรือพิกัด',
            'apology': 'รับคำขอโทษและให้กำลังใจ',
            'compliment': 'ขอบคุณและตอบสนองเชิงบวก',
            'greeting': 'ทักทายตอบและเสนอความช่วยเหลือ',
            'farewell': 'กล่าวลาและเชิญกลับมาใหม่',
            'confirmation': 'ยืนยันความเข้าใจและดำเนินการต่อไป',
            'negation': 'รับทราบการปฏิเสธและถามความต้องการเพิ่มเติม',
            'suggestion': 'พิจารณาข้อเสนอแนะและตอบสนองอย่างเหมาะสม',
            'uncertainty': 'ให้ข้อมูลเพิ่มเติมเพื่อช่วยลดความไม่แน่ใจ',
            'priority': 'จัดลำดับความสำคัญและวางแผนการทำงาน',
            'preference': 'บันทึกความชอบและปรับคำแนะนำให้เหมาะสม',
            'unknown': 'ถามคำถามชี้แจงเพิ่มเติมเพื่อระบุความต้องการ',
        }
        return actions.get(intent, 'ประมวลผลแบบทั่วไป')
    
    def reset_context(self):
        """รีเซ็ต Context"""
        if self.context:
            self.context = IntentContext()


# --- Example Usage / Demo ---
if __name__ == "__main__":
    print("=== Intent Classification System Demo ===\n")
    
    classifier = IntentClassifier(use_context=True)
    
    test_cases = [
        "ฉันควรบอกเพื่อนเรื่องแฟนเขาโกงไหม?",
        "รู้สึกท้อมาก ไม่รู้จะทำยังไงดี",
        "แผ่นดินไหวเกิดจากอะไร?",
        "ระหว่างบอกความจริงกับเงียบไว้ เลือกทางไหนดี?",
        "ช่วยวิเคราะห์สถานการณ์นี้หน่อย มีใครได้ใครเสียบ้าง",
        "ต้องมีขั้นตอนการเตรียมตัวอะไรบ้าง?",
        "ขอคำปรึกษาหน่อย ฉันลังเลมาก",
        # Test cases สำหรับ Intents ใหม่ (12 intents แรก)
        "ข้อมูลนี้ถูกต้องใช่ไหม?",
        "Python กับ JavaScript ต่างกันยังไง?",
        "ติดปัญหาโค้ดไม่รัน แก้ยังไงดี?",
        "หมายความว่าไง ขอตัวอย่างเพิ่มได้ไหม?",
        "หมดไฟทำงาน ต้องการแรงบันดาลใจ",
        "อยากทบทวนสิ่งที่เรียนรู้มา",
        # Test cases สำหรับ Intents ที่เพิ่มใหม่ (15 intents)
        "ช่วยหน่อยครับ ผมต้องการความช่วยเหลือ",
        "ฉันคิดว่าโครงการนี้ควรปรับปรุง",
        "สร้างรายงานให้หน่อย",
        "งานนี้เสร็จเมื่อไหร่?",
        "ออฟฟิศอยู่ที่ไหน?",
        "ขอโทษครับ ผิดไปแล้ว",
        "เก่งมากเลย ยอดเยี่ยม!",
        "สวัสดีครับ",
        "ลาก่อน แล้วพบกันใหม่",
        "ใช่ ตกลง โอเค",
        "ไม่ ฉันไม่เห็นด้วย",
        "น่าจะลองทำดูนะ",
        "ไม่แน่ใจ อาจจะยังไม่ได้ตัดสินใจ",
        "เรื่องนี้สำคัญที่สุด เร่งด่วนมาก",
        "ฉันชอบแบบนี้มากกว่า",
    ]
    
    for i, text in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i} ---")
        print(f"Input: {text}")
        
        result = classifier.classify(text)
        
        print(f"Primary Intent: {result['primary_intent']}")
        print(f"Confidence: {result['confidence']*100:.1f}%")
        print(f"Description: {result['description']}")
        print(f"Recommended Action: {result['recommended_action']}")
        
        if len(result['all_intents']) > 1:
            print("Other Detected Intents:")
            for intent, score in result['all_intents'].items():
                if intent != result['primary_intent']:
                    print(f"  - {intent}: {score*100:.1f}%")
    
    print("\n=== Intent System Ready for Integration ===")
