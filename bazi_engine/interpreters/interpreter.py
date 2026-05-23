"""
Bazi Interpretation Engine
แปลงข้อมูลดวงปาจื้อดิบ เป็นคำวิเคราะห์ภาษาไทยแบบละเอียด
"""

from typing import Dict, Any, List

class BaziInterpreter:
    """ระบบแปลความหมายดวงปาจื้อ"""
    
    # ข้อมูลพื้นฐานสำหรับแปลความ
    DAY_MASTER_MEANINGS = {
        "Jia Wood": "คุณเปรียบเสมือนต้นไม้ใหญ่ มีความเมตตา เติบโตตรงไปตรงมา รักความยุติธรรม มีวิสัยทัศน์กว้างไกล แต่บางครั้งอาจดื้อรั้น",
        "Yi Wood": "คุณเปรียบเสมือนเถาวัลย์หรือดอกไม้เล็ก อ่อนโยน ปรับตัวเก่ง เข้ากับคนง่าย มีความคิดสร้างสรรค์ แต่อาจขี้น้อยใจหรือตัดสินใจช้า",
        "Bing Fire": "คุณเปรียบเสมือนดวงอาทิตย์ ร้อนแรง แจ่มใส รักอิสระ ชอบเป็นศูนย์กลางความสนใจ ใจดีแต่ใจร้อนวู่วาม",
        "Ding Fire": "คุณเปรียบเสมือนแสงเทียนหรือดาว สุภาพ ลึกลับ มีเสน่ห์ดึงดูดใจ คิดลึกซึ้ง แต่บางครั้งอาจขี้ระแวงหรือคิดมาก",
        "Wu Earth": "คุณเปรียบเสมือนภูเขาหรือแผ่นดินใหญ่ มั่นคง ซื่อสัตย์ จริงใจ น่าเชื่อถือ แต่อาจหัวโบราณหรือเปลี่ยนใจยาก",
        "Ji Earth": "คุณเปรียบเสมือนดินเพาะปลูก ละเอียดอ่อน ใส่ใจรายละเอียด ดูแลเอาใจใส่ผู้อื่นได้ดี แต่อาจขี้กังวลหรือคิดเล็กคิดน้อย",
        "Geng Metal": "คุณเปรียบเสมือนเหล็กกล้าหรือดาบ กล้าหาญ เด็ดขาด รักพวกพ้อง ตรงไปตรงมา แต่อาจแข็งกร้าวหรือใจร้อน",
        "Xin Metal": "คุณเปรียบเสมือนเครื่องประดับหรือเพชรพลอย มีรสนิยมดี รักสวยรักงาม พูดจาไพเราะ แต่อาจถือตัวหรืออ่อนไหวง่าย",
        "Ren Water": "คุณเปรียบเสมือนมหาสมุทรหรือน้ำไหลเชี่ยว ฉลาดหลักแหลม ปรับตัวเก่ง กล้าได้กล้าเสีย แต่อาจโลเลหรือเสี่ยงเกินไป",
        "Gui Water": "คุณเปรียบเสมือนน้ำค้างหรือสายฝน ละเอียดลึกซึ้ง มีจินตนาการสูง ลึกลับน่าค้นหา แต่อาจเก็บกดหรือมองโลกในแง่ร้าย"
    }

    ELEMENT_ADVICE = {
        "Wood": "เสริมด้วยการปลูกต้นไม้ ใส่เสื้อผ้าสีเขียว ทิศมงคลคือทิศตะวันออก",
        "Fire": "เสริมด้วยการออกกำลังกาย รับแสงแดด ใส่เสื้อผ้าสีแดง/ส้ม ทิศมงคลคือทิศใต้",
        "Earth": "เสริมด้วยการเดินเท้าเปล่าบนดิน ใส่เสื้อผ้าสีเหลือง/น้ำตาล ทิศมงคลคือใจกลางบ้านหรือทิศตะวันตกเฉียงใต้",
        "Metal": "เสริมด้วยการใส่เครื่องประดับโลหะ สีขาว/ทอง ทิศมงคลคือทิศตะวันตก",
        "Water": "เสริมด้วยการว่ายน้ำ ดื่มน้ำมากๆ ใส่เสื้อผ้าสีดำ/น้ำเงิน ทิศมงคลคือทิศเหนือ"
    }

    def __init__(self):
        pass

    def interpret(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        แปลงข้อมูลดวงดิบ เป็นคำวิเคราะห์เต็มรูปแบบ
        """
        # ดึงข้อมูลจากโครงสร้างที่ถูกต้อง
        four_pillars = chart_data.get('four_pillars', {})
        day_pillar = four_pillars.get('day', {})
        dm_stem = day_pillar.get('heavenly_stem', 'Unknown')
        dm_element = day_pillar.get('stem_element', 'Unknown')
        
        # สร้างชื่อ Day Master
        dm_name = f"{dm_stem} {dm_element}" if dm_stem != 'Unknown' else 'Unknown'
        
        elements_count = chart_data.get('element_distribution', {})
        
        # วิเคราะห์ Ten Gods จากสี่เสา
        ten_gods = {}
        for pillar_name, pillar_data in four_pillars.items():
            tg = pillar_data.get('ten_god', '')
            if tg:
                ten_gods[f"{pillar_name}_{tg}"] = tg
        
        day_master_analysis = chart_data.get('day_master_analysis', {})
        
        # 1. วิเคราะห์ตัวตน (Day Master)
        personality = self._analyze_personality(dm_name, dm_element, elements_count)
        
        # 2. วิเคราะห์จุดแข็งจุดอ่อน
        strengths_weaknesses = self._analyze_strengths_weaknesses(chart_data, day_master_analysis)
        
        # 3. วิเคราะห์การงานและการเงิน
        career_wealth = self._analyze_career_wealth(ten_gods, elements_count)
        
        # 4. วิเคราะห์ความรัก
        love_relationship = self._analyze_love(ten_gods, chart_data.get('birth_info', {}).get('gender', 'male'))
        
        # 5. คำแนะนำเสริมดวง
        advice = self._generate_advice(elements_count, {'element': dm_element})
        
        # 6. สรุปภาพรวม
        summary = self._generate_summary(chart_data, dm_name, day_master_analysis, personality, strengths_weaknesses)

        return {
            "summary": summary,
            "personality_analysis": personality,
            "strengths_and_weaknesses": strengths_weaknesses,
            "career_and_wealth": career_wealth,
            "love_and_relationships": love_relationship,
            "lucky_elements_and_advice": advice,
            "detailed_chart_info": chart_data # แปะข้อมูลดิบไว้ข้างล่างสำหรับอ้างอิง
        }

    def _analyze_personality(self, dm_name: str, dm_element: str, elements: Dict) -> str:
        base_desc = self.DAY_MASTER_MEANINGS.get(dm_name, "มีบุคลิกเฉพาะตัวที่ยากจะนิยาม")
        
        # ปรับตามธาตุที่เด่น
        dominant_element = max(elements, key=elements.get) if elements else None
        modifier = ""
        
        if dominant_element == "Fire":
            modifier = " ด้วยอิทธิพลของธาตุไฟที่โดดเด่น ทำให้คุณมีความกระตือรือร้นเป็นพิเศษ"
        elif dominant_element == "Water":
            modifier = " ด้วยอิทธิพลของธาตุน้ำที่โดดเด่น ทำให้คุณมีความฉลาดและปรับตัวสูงมาก"
        elif dominant_element == "Wood":
            modifier = " ด้วยอิทธิพลของธาตุไม้ที่โดดเด่น ทำให้คุณมีความเมตตาและเติบโตไม่หยุดนิ่ง"
        elif dominant_element == "Metal":
            modifier = " ด้วยอิทธิพลของธาตุโลหะที่โดดเด่น ทำให้คุณมีความเด็ดขาดและรักความถูกต้อง"
        elif dominant_element == "Earth":
            modifier = " ด้วยอิทธิพลของธาตุดินที่โดดเด่น ทำให้คุณมีความมั่นคงและน่าไว้วางใจ"
            
        return f"{base_desc}{modifier}"

    def _analyze_strengths_weaknesses(self, chart_data: Dict, day_master_analysis: Dict) -> Dict[str, List[str]]:
        strengths = []
        weaknesses = []
        
        dm_status = day_master_analysis.get('status', 'Balanced')
        elements = chart_data.get('element_distribution', {})
        
        if dm_status == "Strong":
            strengths.append("มีความมั่นใจในตัวเองสูง")
            strengths.append("สามารถพึ่งพาตนเองได้ดี")
            weaknesses.append("อาจดื้อรั้นและไม่ฟังความคิดเห็นผู้อื่น")
            weaknesses.append("มักจะกดดันตัวเองหรือคนอื่นมากเกินไป")
        elif dm_status == "Weak":
            strengths.append("มีความอ่อนน้อมถ่อมตน")
            strengths.append("รับฟังคำแนะนำและปรับตัวได้ดี")
            weaknesses.append("อาจขาดความมั่นใจในบางสถานการณ์")
            weaknesses.append("ต้องการการสนับสนุนจากผู้อื่นเพื่อความสำเร็จ")
        else:
            strengths.append("มีความสมดุลในการใช้ชีวิต")
            strengths.append("จัดการอารมณ์และสถานการณ์ได้ดี")
            
        # เช็คธาตุที่ขาด
        missing_elements = [k for k, v in elements.items() if v == 0]
        if missing_elements:
            weaknesses.append(f"อาจขาดคุณสมบัติของธาตุ {', '.join(missing_elements)} ในบางมุมชีวิต")
            
        return {"strengths": strengths, "weaknesses": weaknesses}

    def _analyze_career_wealth(self, ten_gods: Dict, elements: Dict) -> str:
        # ตรวจสอบเทพเจ้าแห่งทรัพย์ (Wealth Star)
        wealth_present = any("Wealth" in k for k in ten_gods.keys())
        officer_present = any("Officer" in k for k in ten_gods.keys())
        resource_present = any("Resource" in k for k in ten_gods.keys())
        
        analysis = "ด้านการงานและการเงิน: "
        
        if wealth_present:
            analysis += "คุณมีเกณฑ์เรื่องเงินทองที่ดี มีโอกาสสร้างรายได้จากหลายช่องทาง "
        else:
            analysis += "เรื่องเงินทองต้องอาศัยความพยายามและการวางแผนมากกว่าคนทั่วไป "
            
        if officer_present:
            analysis += "เหมาะกับการทำงานในองค์กรใหญ่ ข้าราชการ หรือตำแหน่งบริหารที่มีอำนาจ "
        elif resource_present:
            analysis += "เหมาะกับการใช้ความรู้ ความเชี่ยวชาญ หรือการทำงานด้านวิชาการ ที่ปรึกษา "
        else:
            analysis += "คุณมีความเป็นอิสระสูง อาจเหมาะกับงานฟรีแลนซ์ หรือธุรกิจส่วนตัว "
            
        return analysis

    def _analyze_love(self, ten_gods: Dict, gender: str) -> str:
        # ตรวจสอบเทพเจ้าแห่งความรัก (Officer สำหรับหญิง, Wealth สำหรับชาย)
        love_indicator = "Direct Officer" if gender == "female" else "Direct Wealth"
        love_indicator_2 = "Seven Killings" if gender == "female" else "Indirect Wealth"
        
        has_love = any(love_indicator in k or love_indicator_2 in k for k in ten_gods.keys())
        
        if has_love:
            return "方面有คู่ครองหรือมีคนเข้ามาในชีวิตค่อนข้างชัดเจน ความรักมักเข้ามาผ่านหน้าที่การงานหรือผู้ใหญ่แนะนำ "
        else:
            return "ด้านความรักอาจต้องใช้เวลาในการค้นหาคู่ที่แท้จริง หรืออาจเน้นอิสระโสดก่อนช่วงแรก ชีวิตคู่จะมั่นคงเมื่อผ่านวัย tertentu "

    def _generate_advice(self, elements: Dict, day_master: Dict) -> Dict[str, Any]:
        # หาธาตุที่ขาดหรืออ่อนที่สุด
        min_element = min(elements, key=elements.get) if elements else None
        lucky_element = min_element # โดยหลักการเบื้องต้น ใช้ธาตุที่ขาดเป็นธาตุที่ต้องการ
        
        advice_text = ""
        if lucky_element and elements.get(lucky_element, 0) < 2:
            advice_text = f"ธาตุที่เป็นมงคลที่สุดของคุณคือ '{lucky_element}' ซึ่งควรเสริมเพื่อดึงดูดโชคลาภและสมดุลชีวิต\n"
            advice_text += self.ELEMENT_ADVICE.get(lucky_element, "")
        else:
            advice_text = "ดวงของคุณค่อนข้างสมดุลอยู่แล้ว ให้รักษาสุขภาพและทำจิตใจให้ผ่องใสเป็นหลัก"
            
        return {
            "lucky_element": lucky_element,
            "advice_text": advice_text
        }

    def _generate_summary(self, chart_data: Dict, dm_name: str, day_master_analysis: Dict, personality: str, sw: Dict) -> str:
        status = day_master_analysis.get('status', 'Balanced')
        dm_element = day_master_analysis.get('day_master_element', '')
        
        return f"สรุปดวงชะตา: คุณคือ'{dm_name}' ({status}) {personality[:50]}... จุดเด่นสำคัญคือ {sw['strengths'][0] if sw['strengths'] else 'ความสมดุล'}"

def interpret_bazi(chart_data: Dict[str, Any]) -> Dict[str, Any]:
    """Function หลักสำหรับเรียกใช้"""
    interpreter = BaziInterpreter()
    return interpreter.interpret(chart_data)
