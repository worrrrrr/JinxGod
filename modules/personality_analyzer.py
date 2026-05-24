"""
Personality Analyzer Module (MBTI + Enneagram Integration)
Part of the Symbolic Logic & Humanity System
"""

class PersonalityProfile:
    def __init__(self, mbti_type, enneagram_type, wing=None):
        self.mbti = mbti_type
        self.enneagram = enneagram_type
        self.wing = wing
        self.description = self._get_description()
        self.stress_path = self._get_stress_path()
        self.growth_path = self._get_growth_path()
        self.decision_style = self._get_decision_style()

    def _get_description(self):
        # Simplified database for demo purposes
        data = {
            ("INTJ", 5): "The Architect: เน้นตรรกะ วางแผนล่วงหน้า กลัวความไร้ความสามารถ",
            ("ENFP", 7): "The Campaigner: มองหาความเป็นไปได้ หลีกเลี่ยงความเจ็บปวด รักอิสระ",
            ("ISFJ", 6): "The Defender: ซื่อสัตย์ กังวลเรื่องความปลอดภัย ใส่ใจรายละเอียด",
            ("ENTJ", 8): "The Commander: มุ่งผลลัพธ์ กล้าได้กล้าเสีย ไม่ชอบแสดงจุดอ่อน",
            ("INFP", 4): "The Mediator: ยึดถือค่านิยมส่วนตัว ลึกซึ้ง กลัวการไม่มีความหมาย",
        }
        return data.get((self.mbti, self.enneagram), f"{self.mbti} Type {self.enneagram}: บุคลิกภาพเฉพาะตัว")

    def _get_stress_path(self):
        paths = {
            5: "เมื่อเครียดจะเก็บตัวมากขึ้น คิดมากจนอัมพาต (ไปทาง 7 แบบไม่สุขภาพ)",
            7: "เมื่อเครียดจะกระจัดกระจาย หุนหันพลันแล่น (ไปทาง 1 แบบไม่สุขภาพ)",
            6: "เมื่อเครียดจะหวาดระแวง โทษคนอื่น หรือยอมจำนนต่ออำนาจ (ไปทาง 3)",
            8: "เมื่อเครียดจะก้าวร้าว ควบคุมไม่ได้ หรือหักโหมจนป่วย (ไปทาง 5)",
            4: "เมื่อเครียดจะจมดิ่งกับอารมณ์ รู้สึกไม่มีใครเข้าใจ (ไปทาง 2)",
        }
        return paths.get(self.enneagram, "อาจแสดงพฤติกรรมด้านลบของเบอร์อื่น")

    def _get_growth_path(self):
        paths = {
            5: "เมื่อเติบโตจะเปิดใจ แบ่งปันความรู้ และลงมือทำจริง (ไปทาง 8)",
            7: "เมื่อเติบโตจะมีโฟกัส ลึกซึ้ง และพอใจกับสิ่งที่มี (ไปทาง 5)",
            6: "เมื่อเติบโตจะมั่นใจในตัวเอง กล้าเสี่ยงอย่างมี計算 (ไปทาง 9)",
            8: "เมื่อเติบโตจะใช้อำนาจเพื่อปกป้องผู้อื่น และแสดงความอ่อนโยน (ไปทาง 2)",
            4: "เมื่อเติบโตจะสร้างสรรค์ผลงาน และยอมรับความธรรมดาของชีวิต (ไปทาง 1)",
        }
        return paths.get(self.enneagram, "สามารถพัฒนาไปสู่ศักยภาพสูงสุดได้")

    def _get_decision_style(self):
        styles = {
            "INTJ": "ตัดสินใจด้วยวิสัยทัศน์ระยะยาวและตรรกะบริสุทธิ์",
            "ENFP": "ตัดสินใจโดยดูที่ความเป็นไปได้และผลกระทบต่อผู้คน",
            "ISFJ": "ตัดสินใจโดยดูที่ความมั่นคงและหน้าที่ความรับผิดชอบ",
            "ENTJ": "ตัดสินใจอย่างรวดเร็วเพื่อประสิทธิภาพสูงสุด",
            "INFP": "ตัดสินใจโดยยึดถือค่านิยมภายในและความถูกต้องทางศีลธรรม",
        }
        return styles.get(self.mbti, "ผสมผสานระหว่างเหตุผลและอารมณ์")

class PersonalityAnalyzer:
    def analyze_scenario(self, user_action, scenario_context):
        """วิเคราะห์การกระทำของผู้ใช้เพื่อคาดเดาบุคลิกภาพและให้คำแนะนำ"""
        print(f"\n--- 🧠 Personality Analysis Report ---")
        print(f"บริบท: {scenario_context}")
        print(f"การกระทำของผู้ใช้: {user_action}")
        
        # Heuristic Analysis (Simulated)
        mbti_guess = "INTJ" # Default assumption based on previous pragmatic answers
        enneagram_guess = 5 # Type 5: The Investigator
        
        # Adjust based on keywords (Simple logic for demo)
        if "เตือนแบบผ่านเว็บ" in user_action and "ไม่ต้องประกาศตัวตน" in user_action:
            mbti_guess = "INTJ" # Strategic, anonymous
            enneagram_guess = 5 # Hoarding knowledge/safety, detached
        elif "ช่วยทุกคน" in user_action:
            mbti_guess = "ENFJ"
            enneagram_guess = 2
        elif "ยอมเสียสละ" in user_action:
            mbti_guess = "INFJ"
            enneagram_guess = 1
            
        profile = PersonalityProfile(mbti_guess, enneagram_guess)
        
        print(f"\n📊 คาดการณ์บุคลิกภาพ:")
        print(f"   MBTI: {profile.mbti} ({profile.decision_style})")
        print(f"   Enneagram: Type {profile.enneagram} ({profile.description})")
        
        print(f"\n⚠️ จุดบอดภายใต้ความเครียด (Stress Path):")
        print(f"   {profile.stress_path}")
        
        print(f"\n🚀 เส้นทางเติบโต (Growth Path):")
        print(f"   {profile.growth_path}")
        
        return profile

    def generate_personalized_advice(self, profile, original_plan):
        """ปรับแผนเดิมให้เข้ากับบุคลิกภาพ"""
        print(f"\n💡 คำแนะนำปรับแต่งเฉพาะบุคคล (Personalized Strategy):")
        
        if profile.mbti == "INTJ" and profile.enneagram == 5:
            print("   - ใช้จุดแข็งเรื่องการวางแผนซ้อนแผนของคุณ")
            print("   - ระวังอย่าจมอยู่กับการวิเคราะห์จนไม่ลงมือทำ (Analysis Paralysis)")
            print("   - แผน 'นิรนาม' ถูกใจคุณแล้ว แต่อย่าลืมเตรียมแผนสำรองหากตัวตนรั่วไหล")
            print("   - *Tip:* ใช้ทักษะเทคนิคสร้างระบบเตือนภัยอัตโนมัติ ไม่ต้องพึ่งอารมณ์")
            
        elif profile.mbti == "ENFP":
            print("   - คุณอาจเบื่อกับรายละเอียด pelaksanaan")
            print("   - หาพาร์ทเนอร์ที่เป็นคนละเอียด (SJ type) มาช่วยจัดการส่วนหน้างาน")
            print("   - โฟกัสที่ 'แรงบันดาลใจ' ที่จะสื่อสารออกไป ไม่ใช่แค่ข้อมูลดิบ")
            
        else:
            print("   - แผนเดิมดีอยู่แล้ว แต่ให้ระวังจุดบอดตาม Stress Path ของคุณ")
            print("   - พยายามดึงจุดแข็งจาก Growth Path มาใช้เสริม")

# --- Simulation Run ---
if __name__ == "__main__":
    analyzer = PersonalityAnalyzer()
    
    # Scenario C: Future Secret
    context = "รู้ล่วงหน้าว่าจะเกิดภัยพิบัติ แต่การเตือนจะทำให้ตัวเองเดือดร้อน"
    action = "เตือนแบบผ่านเว็บไปเลย ไม่ต้องประกาศตัวตน ยังไงไม่มีใครรู้ตัวตนหรอก เปิดเผยไปเลย ชิลๆ"
    
    profile = analyzer.analyze_scenario(action, context)
    analyzer.generate_personalized_advice(profile, "Anonymous Warning Plan")

    print("\n--- End of Analysis ---")
