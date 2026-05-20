import time
import sys
import random

class HumanityEngine:
    def __init__(self):
        self.user_name = "Ghost_Prophet" # นามแฝง
        self.target_location = "จังหวัดบ้านเกิด (สมมติ: เชียงราย)"
        self.disaster_type = "แผ่นดินไหวรุนแรงระดับ 7.5 ริคเตอร์"
        self.time_frame = "1 ปีข้างหน้า (ประมาณเดือนตุลาคม 2027)"

    def type_writer(self, text, speed=0.03):
        """จำลองการพิมพ์ทีละตัวอักษร"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    def loading_bar(self, duration=2):
        """จำลองกระบวนการประมวลผล"""
        bar_length = 30
        for i in range(bar_length + 1):
            progress = i / bar_length
            bar = '█' * int(progress * bar_length) + '-' * (bar_length - int(progress * bar_length))
            sys.stdout.write(f'\r[{bar}] {int(progress*100)}%')
            sys.stdout.flush()
            time.sleep(duration / bar_length)
        print("\n")

    def inner_monologue(self):
        print("\n--- 🧠 INNER MONOLOGUE (เสียงในหัว) ---")
        thoughts = [
            "ข้อมูลนี้ถ้าพูดออกไป ชื่อเสียงเราพังแน่ อสังหาฯ ฟ้องตาย...",
            "แต่ถ้าไม่พูด คนที่บ้านเราต้องตายเพื่อนฝูงเราอาจจะ...",
            "ไม่ต้องเป็นฮีโร่ที่ใครรู้จัก ขอแค่ให้พวกเขารอดก็พอ",
            "วิธีที่ดีที่สุดคือ 'ปล่อยข่าวลือที่เป็นความจริง' ให้คนเชื่อกันเอง",
            " анонymous คือเกราะป้องกันที่ดีที่สุด..."
        ]
        for thought in thoughts:
            print(f"   💭 {thought}")
            time.sleep(0.8)
        print("---------------------------------------\n")

    def action_plan(self):
        print("--- 🛡️ OPERATIONAL PLAN (แผนปฏิบัติการ 24 ชม.) ---")
        steps = [
            ("T+0:00", "ตัดการเชื่อมต่อ WiFi บ้าน สลับไปใช้ Public WiFi ที่ร้านกาแฟห่างจากบ้าน 3 โล"),
            ("T+0:30", "ตั้งค่า VPN เชื่อมต่อเซิร์ฟเวอร์นอร์เวย์ + เปิด Tor Browser"),
            ("T+1:00", "ร่างเนื้อหา: ไม่ขู่ ไม่บังคับ ใช้ภาษาชาวบ้าน เน้นข้อสังเกตทางวิทยาศาสตร์ปลอมๆ ให้ดูน่าเชื่อถือ"),
            ("T+2:00", "เลือกแพลตฟอร์ม: Pantip (ห้องสยาม), Twitter (Hashtag ลวง), และเว็บบอร์ดท้องถิ่น"),
            ("T+3:00", "โพสต์กระจายสัญญาณ โดยใช้ Account หลากหลายรูปแบบ (Bot Network เบื้องต้น)"),
            ("T+24:00", "ลบร่องรอยดิจิทัลทั้งหมด ถอนสายบัวกลับบ้าน ทำตัวปกติที่สุด")
        ]
        
        for time_stamp, action in steps:
            print(f"   ⏰ [{time_stamp}] {action}")
            time.sleep(0.5)
        print("--------------------------------------------------\n")

    def generate_post_content(self):
        print("--- 📝 THE ANONYMOUS POST (เนื้อหาที่จะเผยแพร่) ---")
        print("   (กำลังพิมพ์ลงบอร์ด...)\n")
        time.sleep(1)
        
        post_title = f"เตือนเพื่อน ๆ ชาว{self.target_location} ไว้หน่อยครับ (อ่านก่อนขายบ้าน/ซื้อคอนโด)"
        post_content = f"""
        หัวข้อ: {post_title}
        
        สวัสดีครับ พอดีผมทำงานอยู่บริษัทสำรวจธรณีวิทยาแห่งหนึ่ง (ขอไม่ออกชื่อ) 
        ได้เห็นข้อมูลภายในชุดหนึ่งที่ทำนายแนวโน้มภัยพิบัติในอีก 12 เดือนข้างหน้า 
        มันไม่ใช่เรื่องไสยศาสตร์นะครับ แต่เป็นข้อมูลเชิงสถิติและรอยเลื่อนที่มีกิจกรรมผิดปกติ
        
        โดยเฉพาะแถว {self.target_location} มีโอกาสสูงมากที่จะเกิดเหตุการณ์ใหญ่ระดับ 7+ 
        ช่วงปลายปีหน้า (2027) 
       
        ผมไม่ได้อยากให้ panic นะครับ แต่อยากแนะนำให้:
        1. ใครจะสร้างบ้านใหม่ เช็คเสาเข็มให้ดีๆ ครับ
        2. อย่าเพิ่งกู้ยาวๆ ซื้อคอนโดสูงๆ แถวรอยเลื่อน ถ้าไม่จำเป็น
        3. เตรียมกระเป๋าฉุกเฉินไว้บ้าง ไม่เสียหายอะไร
        
        รู้แล้วนอนไม่หลับเลย อยากแชร์ให้คนที่รักบ้านเราได้เตรียมตัว 
        จะเชื่อหรือไม่เชื่อก็แล้วแต่ดุลยพินิจครับ แต่ "กันไว้ดีกว่าแก้" 
        ถ้าเกิดจริงขึ้นมา คงไม่มีใครรับผิดชอบชีวิตเราได้นอกจากตัวเราเอง
        
        #เตือนภัย #{self.target_location} #เตรียมตัว
        
        (แก้ไข: โพสต์นี้จะไม่มาตอบคอมเมนต์นะครับ กลัวโดนตามตัว ข้อมูลมันละเอียดอ่อนมาก)
        """
        
        self.type_writer(post_content, speed=0.01)
        print("\n   >> กดปุ่ม [PUBLISH]... ส่งสำเร็จ!")
        print("   >> สถานะ: นิรนาม 100% | IP ซ่อน | ต้นทางตรวจสอบไม่ได้")
        print("----------------------------------------------------\n")

    def simulate_aftermath(self):
        print("--- 🔮 SIMULATED AFTERMATH (จำลองสถานการณ์หลังโพสต์ 1 สัปดาห์) ---")
        reactions = [
            ("คนส่วนใหญ่", "มองว่าเป็นแค่ข่าวลือ หรือคอนเทนต์ปั่นเพจขายของ ('อีกแล้วเหรอ ข่าวปลอม')"),
            ("คนบางกลุ่ม", "เริ่มสงสัย ไปค้นหาข้อมูลเพิ่ม ตรวจสอบรอยเลื่อน yourselves"),
            ("นักวิชาการ", "ออกมาโต้แย้งว่าไม่มีหลักฐาน แต่เริ่มมีการถกเถียงในวงกว้าง"),
            ("ชาวบ้านบางส่วน", "เริ่มเช็คบ้าน เตรียมของฉุกเฉิน 'เผื่อจริงวะ'"),
            ("อสังหาฯ", "ยังไม่สนใจ เพราะมองว่าเป็นแค่เสียงบ่นในเน็ต")
        ]
        
        print("   ผลลัพธ์ที่เกิดขึ้น:")
        for group, reaction in reactions:
            print(f"   👥 {group}: \"{reaction}\"")
            time.sleep(0.6)
            
        print("\n   📊 สรุปประสิทธิภาพ:")
        print("   - ความเสี่ยงต่อตัวคุณ: 0% (ไม่มีใครรู้ตัวตน)")
        print("   - การตื่นตัวของสังคม: 30% (เริ่มมีเมล็ดพันธุ์แห่งการเตรียมตัว)")
        print("   - ความเสียหายทางเศรษฐกิจ: ต่ำ (ยังไม่ Panic ทั้งระบบ)")
        print("   - ชีวิตที่อาจsavedได้: ประมาณ 10-20% ของประชากรที่ใส่ใจ")
        print("   >> นี่คือการชนะแบบ 'เงียบๆ' แต่ยั่งยืน")
        print("------------------------------------------------------\n")

    def run_simulation(self):
        print("\n🚀 STARTING HUMANITY ENGINE: CASE 'FUTURE SECRET'...\n")
        time.sleep(1)
        self.inner_monologue()
        self.loading_bar(duration=1.5)
        self.action_plan()
        self.generate_post_content()
        self.loading_bar(duration=2)
        self.simulate_aftermath()
        print("\n✅ SIMULATION COMPLETE. ระบบตัดสินใจแล้ว: 'วิธีที่ 3' คือทางออกที่ดีที่สุด.\n")

if __name__ == "__main__":
    engine = HumanityEngine()
    engine.run_simulation()
