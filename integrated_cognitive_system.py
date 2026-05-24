"""
Integrated Cognitive System with Intent Classification
ระบบวิเคราะห์ข้อมูลที่จับ Intent ก่อนแล้วส่งไปวิเคราะห์ต่อตามความเหมาะสม
"""

from intent_classifier import IntentClassifier
from analysis_planner_pack import ScenarioAnalyzer, StrategicPlanner, DecisionSummarizer
from humanity_tools import EmpathyBuffer, StakeholderMap, TruthDeliveryProtocol
from cognitive_engine.engines.core import CognitiveEngine


class IntegratedCognitiveSystem:
    """
    ระบบบูรณาการที่จับ Intent ก่อนแล้วเลือกเครื่องมือวิเคราะห์ที่เหมาะสม
    """
    
    def __init__(self):
        self.intent_classifier = IntentClassifier(use_context=True)
        self.cognitive_engine = CognitiveEngine()
        self.scenario_analyzer = ScenarioAnalyzer()
        self.strategic_planner = StrategicPlanner()
        self.decision_summarizer = DecisionSummarizer()
    
    def process(self, user_input: str, context: dict = None) -> dict:
        """
        กระบวนการประมวลผลแบบครบวงจร:
        1. จับ Intent
        2. เลือกเครื่องมือวิเคราะห์ตาม Intent
        3. ดำเนินการวิเคราะห์
        4. ส่งคืนผลลัพธ์
        """
        print(f"\n{'='*60}")
        print(f"📥 รับข้อความเข้า: {user_input[:80]}")
        print(f"{'='*60}")
        
        # Step 1: จับ Intent
        print("\n🎯 Step 1: กำลังจับความตั้งใจ (Intent Detection)...")
        intent_result = self.intent_classifier.classify(user_input, context)
        
        primary_intent = intent_result['primary_intent']
        confidence = intent_result['confidence']
        
        print(f"   Intent หลัก: {primary_intent}")
        print(f"   ความมั่นใจ: {confidence*100:.1f}%")
        print(f"   คำอธิบาย: {intent_result['description']}")
        print(f"   การกระทำที่แนะนำ: {intent_result['recommended_action']}")
        
        # Step 2: เลือกและใช้เครื่องมือตาม Intent
        print(f"\n🛠️  Step 2: กำลังเลือกใช้เครื่องมือตาม Intent '{primary_intent}'...")
        
        result = {
            'intent': intent_result,
            'analysis': None,
            'recommendation': None,
            'response': None
        }
        
        if primary_intent == 'emotional_support':
            # ใช้ Empathy Buffer ก่อน
            print("   >> เปิดใช้งาน EmpathyBuffer...")
            user_state = self._detect_emotional_state(user_input)
            empathy = EmpathyBuffer(user_state)
            
            validation = empathy.validate_feeling()
            safety_zone = empathy.create_safety_zone()
            
            result['response'] = f"{validation}\n\n{safety_zone}"
            result['analysis'] = {'emotional_validation': validation}
            
            # แล้วค่อยวิเคราะห์ต่อ
            print("   >> วิเคราะห์สถานการณ์ต่อ...")
            analysis = self.scenario_analyzer.decompose(user_input, context or {})
            result['analysis']['decomposition'] = analysis
            
        elif primary_intent == 'advice' or primary_intent == 'decision':
            # ใช้ Scenario Analyzer + Strategic Planner
            print("   >> เปิดใช้งาน ScenarioAnalyzer...")
            analysis = self.scenario_analyzer.decompose(user_input, context or {})
            result['analysis'] = analysis
            
            print("   >> เปิดใช้งาน StrategicPlanner...")
            options = self.strategic_planner.generate_options(analysis)
            result['options'] = options
            
            # สรุปคำแนะนำ
            best_option = options[0] if options else None
            if best_option:
                result['recommendation'] = {
                    'strategy': best_option['type'],
                    'description': best_option['description'],
                    'pros': best_option['pros'],
                    'cons': best_option['cons']
                }
                
        elif primary_intent == 'analysis':
            # ใช้ Cognitive Engine แบบเต็มรูปแบบ
            print("   >> เปิดใช้งาน CognitiveEngine...")
            full_analysis = self.cognitive_engine.solve(user_input, context)
            result['analysis'] = full_analysis
            
        elif primary_intent == 'action_plan':
            # สร้างแผนปฏิบัติการ
            print("   >> เปิดใช้งาน ScenarioAnalyzer + Action Planner...")
            analysis = self.scenario_analyzer.decompose(user_input, context or {})
            result['analysis'] = analysis
            
            print("   >> กำลังสร้างแผนปฏิบัติการ...")
            options = self.strategic_planner.generate_options(analysis)
            action_plan = self.strategic_planner.create_action_plan(options[0] if options else {})
            result['action_plan'] = action_plan
            
        elif primary_intent == 'information':
            # ให้ข้อมูลหรืออธิบาย
            print("   >> กำลังค้นหาข้อมูล...")
            # ในระบบจริงจะเชื่อมกับ Knowledge Base
            result['response'] = "ระบบกำลังประมวลผลข้อมูลที่เกี่ยวข้อง..."
            
        elif primary_intent == 'problem_solving':
            # แก้ปัญหา
            print("   >> เปิดใช้งาน Problem Solver...")
            analysis = self.scenario_analyzer.decompose(user_input, context or {})
            result['analysis'] = analysis
            options = self.strategic_planner.generate_options(analysis)
            result['options'] = options
            if options:
                result['recommendation'] = {
                    'strategy': options[0]['type'],
                    'description': options[0]['description'],
                    'solution': options[0]['description']
                }
                
        elif primary_intent == 'clarification':
            # ชี้แจง/อธิบายเพิ่ม
            print("   >> กำลังชี้แจงข้อมูลเพิ่มเติม...")
            result['response'] = "ระบบกำลังเตรียมคำอธิบายเพิ่มเติมและตัวอย่าง..."
            
        elif primary_intent == 'motivation':
            # ให้แรงบันดาลใจ
            print("   >> เปิดใช้งาน Motivation Module...")
            result['response'] = "คุณทำได้! ทุกปัญหามีทางออก แค่อย่าเพิ่งยอมแพ้"
            
        elif primary_intent == 'validation':
            # ตรวจสอบความถูกต้อง
            print("   >> กำลังตรวจสอบความถูกต้อง...")
            result['response'] = "ระบบกำลังตรวจสอบข้อมูลและยืนยันความถูกต้อง..."
            
        elif primary_intent == 'comparison':
            # เปรียบเทียบ
            print("   >> เปิดใช้งาน Comparison Analyzer...")
            analysis = self.scenario_analyzer.decompose(user_input, context or {})
            result['analysis'] = analysis
            result['response'] = "ระบบกำลังเตรียมการเปรียบเทียบระหว่างตัวเลือก..."
            
        elif primary_intent in ['help_request', 'command_request']:
            # คำขอความช่วยเหลือทั่วไป
            print("   >> กำลังประมวลผลคำขอ...")
            analysis = self.scenario_analyzer.decompose(user_input, context or {})
            result['analysis'] = analysis
            
        else:
            # unknown หรือ default - ใช้ Cognitive Engine แบบทั่วไป
            print("   >> ใช้ CognitiveEngine แบบทั่วไป...")
            result['analysis'] = self.cognitive_engine.solve(user_input, context)
        
        # Step 3: สรุปผล (ถ้ามีข้อมูลเพียงพอ)
        if result.get('analysis') and primary_intent not in ['emotional_support', 'information', 'greeting', 'farewell', 'apology', 'compliment']:
            print(f"\n📊 Step 3: กำลังสรุปผล...")
            
            if primary_intent in ['advice', 'decision', 'problem_solving'] and result.get('recommendation'):
                summary = self.decision_summarizer.executive_summary(
                    problem=user_input,
                    decision=result['recommendation']['description'],
                    rationale=f"กลยุทธ์{result['recommendation']['strategy']}",
                    impact="ดูรายละเอียดในตัวเลือก"
                )
                result['summary'] = summary
        
        # สร้างคำตอบสุดท้าย (answer key)
        result['answer'] = self._generate_final_answer(result, primary_intent, user_input)
        
        print(f"\n✅ ประมวลผลเสร็จสิ้น!")
        return result
    
    def _generate_final_answer(self, result: dict, intent: str, user_input: str) -> str:
        """สร้างคำตอบสุดท้ายจากผลลัพธ์"""
        
        # กรณีที่มี response โดยตรง
        if result.get('response'):
            return result['response']
        
        # กรณีที่มี recommendation
        if result.get('recommendation'):
            rec = result['recommendation']
            return f"คำแนะนำ: {rec.get('description', 'ไม่มีคำแนะนำ')}\\n\\nเหตุผล: {rec.get('strategy', '')}"
        
        # กรณีที่มี action plan
        if result.get('action_plan'):
            plan = result['action_plan']
            return f"แผนปฏิบัติการ:\\n{plan}"
        
        # กรณีที่มี summary
        if result.get('summary'):
            return result['summary']
        
        # กรณีที่มี analysis
        if result.get('analysis'):
            return "ผลการวิเคราะห์: ระบบได้ประมวลผลข้อมูลของคุณแล้ว"
        
        # Default response ตาม intent
        default_responses = {
            'greeting': 'สวัสดีครับ! มีอะไรให้ฉันช่วยวันนี้?',
            'farewell': 'ลาก่อนครับ! ยินดีที่ได้ช่วยเหลือ',
            'apology': 'ไม่เป็นไรครับ เข้าใจครับ',
            'compliment': 'ขอบคุณครับ! ยินดีที่ได้ช่วยเหลือ',
            'time_inquiry': 'ขออภัย ฉันไม่สามารถบอกเวลาปัจจุบันได้',
            'location_inquiry': 'ขออภัย ฉันไม่สามารถระบุตำแหน่งสถานที่ได้',
            'confirmation': 'รับทราบครับ',
            'negation': 'เข้าใจครับ',
            'suggestion': 'ขอบคุณสำหรับคำแนะนำครับ',
            'uncertainty': 'ไม่ต้องกังวลครับ เราค่อยๆคิดไปด้วยกัน',
            'priority': 'เข้าใจครับ เรื่องนี้สำคัญมาก',
            'preference': 'เข้าใจครับ ความชอบของคุณสำคัญ',
            'opinion_sharing': 'ขอบคุณที่แบ่งปันความคิดเห็นครับ',
            'reflection': 'การทบทวนเป็นสิ่งที่ดีมากครับ',
        }
        
        return default_responses.get(intent, "ระบบกำลังประมวลผลคำขอของคุณครับ")
    
    def _detect_emotional_state(self, text: str) -> str:
        """ตรวจจับสถานะอารมณ์จากข้อความ"""
        text_lower = text.lower()
        
        emotional_indicators = {
            'shock': ['ช็อก', 'ตกใจ', 'ไม่น่าเชื่อ', '不可思议'],
            'angry': ['โกรธ', 'โมโห', 'หงุดหงิด', 'รำคาญ'],
            'confused': ['งง', 'สับสน', 'ไม่เข้าใจ', 'มึน'],
            'sad': ['เศร้า', 'เสียใจ', 'ทุกข์', 'เจ็บปวด'],
            'stressed': ['เครียด', 'กดดัน', 'ท้อ', 'เหนื่อย'],
        }
        
        for state, indicators in emotional_indicators.items():
            if any(indicator in text_lower for indicator in indicators):
                return state
        
        return 'confused'  # default
    
    def get_conversation_summary(self) -> dict:
        """สรุปประวัติการสนทนา"""
        if self.intent_classifier.context:
            history = self.intent_classifier.context.history
            return {
                'total_interactions': len(history),
                'recent_intents': [h['intent'] for h in history[-5:]],
                'dominant_intent': max(set([h['intent'] for h in history]), 
                                      key=[h['intent'] for h in history].count) if history else None
            }
        return {}


# --- Demo Usage ---
if __name__ == "__main__":
    print("🚀 Initializing Integrated Cognitive System with Intent Classification\n")
    
    system = IntegratedCognitiveSystem()
    
    # Test Case 1: Emotional Support
    print("\n" + "="*60)
    print("TEST 1: ผู้ใช้ต้องการการสนับสนุนทางอารมณ์")
    print("="*60)
    result1 = system.process("รู้สึกท้อมาก ไม่รู้จะทำยังไงดี พบว่าเพื่อนสนิทหักหลัง")
    
    # Test Case 2: Decision Making
    print("\n" + "="*60)
    print("TEST 2: ผู้ใช้ต้องการความช่วยเหลือในการตัดสินใจ")
    print("="*60)
    result2 = system.process(
        "ฉันควรบอกเพื่อนเรื่องแฟนเขาโกงไหม? กลัวเสียความสัมพันธ์แต่ก็รู้สึกผิดที่ไม่บอก",
        context={
            'people_involved': [
                {'name': 'ฉัน', 'role': 'ผู้รู้ความจริง'},
                {'name': 'เพื่อน', 'role': 'ผู้ถูกหักหลัง'},
                {'name': 'แฟนเพื่อน', 'role': 'ผู้กระทำผิด'}
            ],
            'constraints': ['มิตรภาพ', 'จริยธรรม', 'ผลกระทบระยะยาว']
        }
    )
    
    # Test Case 3: Analysis Request
    print("\n" + "="*60)
    print("TEST 3: ผู้ใช้ต้องการการวิเคราะห์สถานการณ์")
    print("="*60)
    result3 = system.process("ช่วยวิเคราะห์สถานการณ์นี้หน่อย มีใครได้ใครเสียบ้าง")
    
    # Test Case 4: Action Plan
    print("\n" + "="*60)
    print("TEST 4: ผู้ใช้ต้องการแผนปฏิบัติการ")
    print("="*60)
    result4 = system.process("ต้องมีขั้นตอนการเตรียมตัวอะไรบ้างเพื่อบอกความจริงให้กระทบน้อยที่สุด")
    
    # สรุปการสนทนา
    print("\n" + "="*60)
    print("📈 สรุปการสนทนาทั้งหมด")
    print("="*60)
    summary = system.get_conversation_summary()
    print(f"จำนวนครั้งโต้ตอบ: {summary['total_interactions']}")
    print(f"Intent ล่าสุด: {summary['recent_intents']}")
    print(f"Intent ที่พบบ่อยที่สุด: {summary['dominant_intent']}")
    
    print("\n\n✅ === Integrated System Demo Complete ===")
