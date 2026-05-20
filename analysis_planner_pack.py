"""
Analysis, Planner, and Summary Pack for Cognitive Decomposition Engine
รวมเครื่องมือวิเคราะห์ วางแผน และสรุปผล สำหรับการตัดสินใจเชิงซ้อน
"""

import json
from datetime import datetime
from typing import List, Dict, Any, Optional

class ScenarioAnalyzer:
    """โมดูลวิเคราะห์สถานการณ์แบบเจาะลึก (Deep Dive Analysis)"""
    
    @staticmethod
    def decompose(problem_statement: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        แยกองค์ประกอบปัญหา (Decomposition)
        Returns: โครงสร้างข้อมูลที่มี เหตุ, ผล, ตัวแปร, ข้อจำกัด, ความเสี่ยง
        """
        # จำลองกระบวนการคิดแบบ Decomposition
        analysis = {
            "core_problem": problem_statement,
            "components": {
                "causes": [],          # สาเหตุ
                "effects": [],         # ผลกระทบ
                "variables": [],       # ตัวแปรที่เปลี่ยนแปลงได้
                "constraints": [],     # ข้อจำกัด (เวลา, ทรัพยากร, กฎ)
                "risks": []            # ความเสี่ยงที่อาจเกิดขึ้น
            },
            "stakeholders": {},        # ผู้มีส่วนได้ส่วนเสีย
            "emotional_layer": {}      # ชั้นอารมณ์ (Empathy Map)
        }
        
        # Logic จำลองการแยกส่วน (ในระบบจริงจะใช้ LLM หรือ Rule Engine วิเคราะห์)
        # ตัวอย่างการเติมข้อมูลจาก Context
        if "people_involved" in context:
            for person in context["people_involved"]:
                analysis["stakeholders"][person["name"]] = {
                    "role": person.get("role", "Unknown"),
                    "interest": person.get("interest", "Unknown"),
                    "pain_point": person.get("pain_point", "")
                }
        
        if "constraints" in context:
            analysis["components"]["constraints"] = context["constraints"]
            
        if "time_limit" in context:
            analysis["components"]["constraints"].append(f"Time Limit: {context['time_limit']}")
            analysis["risks"].append("Time pressure may lead to hasty decisions")

        return analysis

    @staticmethod
    def find_root_cause(components: Dict[str, Any]) -> List[str]:
        """
        ใช้เทคนิค 5 Whys เพื่อหาสาเหตุรากเหง้า
        """
        root_causes = []
        # จำลองกระบวนการหา Root Cause จากสาเหตุเบื้องต้น
        for cause in components.get("causes", []):
            # ในระบบจริงจะทำการถาม "ทำไม" ซ้อนๆ
            root_causes.append(f"Root of '{cause}': [Simulated 5 Whys Process]")
        return root_causes if root_causes else ["Unable to determine root cause without specific data"]


class StrategicPlanner:
    """โมดูลวางแผนกลยุทธ์และปฏิบัติการ (Strategic & Operational Planning)"""
    
    @staticmethod
    def generate_options(analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        สร้างทางเลือกในการแก้ปัญหา (Solution Space)
        แบ่งเป็น: เร็ว, ยั่งยืน, เชิงระบบ, เชิงป้องกัน
        """
        options = [
            {
                "id": "OPT-FAST",
                "type": "Quick Fix",
                "description": "แก้ปัญหาเฉพาะหน้าทันที",
                "pros": ["เร็ว", "ลดความเสียหายทันที"],
                "cons": ["อาจไม่ยั่งยืน", "มีผลข้างเคียงสูง"],
                "estimated_impact": "High Short-term, Low Long-term"
            },
            {
                "id": "OPT-SYS",
                "type": "Systemic Change",
                "description": "แก้ที่โครงสร้างหรือระบบ",
                "pros": ["ยั่งยืน", "ป้องกันปัญหาซ้ำ"],
                "cons": ["ใช้เวลานาน", "ต้องการทรัพยากรสูง"],
                "estimated_impact": "Medium Short-term, High Long-term"
            },
            {
                "id": "OPT-HUMAN",
                "type": "Human-Centric",
                "description": "เน้นความเข้าใจและความสัมพันธ์",
                "pros": ["รักษาความสัมพันธ์", "ลดความขัดแย้ง"],
                "cons": ["อาจไม่ได้ผลลัพธ์ทางตัวเลขสูงสุด"],
                "estimated_impact": "High Emotional, Variable Practical"
            }
        ]
        return options

    @staticmethod
    def evaluate_tradeoffs(options: List[Dict[str, Any]], criteria: List[str]) -> Dict[str, Any]:
        """
        ประเมินผลกระทบแลกเปลี่ยน (Tradeoff Analysis)
        """
        evaluation_matrix = {}
        for opt in options:
            score = 0
            reasoning = []
            # จำลองการให้คะแนนตามเกณฑ์ (ในของจริงจะมี Weighting)
            if "Speed" in criteria and opt["type"] == "Quick Fix":
                score += 5
                reasoning.append("High speed score")
            if "Sustainability" in criteria and opt["type"] == "Systemic Change":
                score += 5
                reasoning.append("High sustainability score")
            
            evaluation_matrix[opt["id"]] = {
                "score": score,
                "reasoning": reasoning,
                "recommendation": "Recommended" if score >= 5 else "Alternative"
            }
        return evaluation_matrix

    @staticmethod
    def create_action_plan(selected_option: Dict[str, Any], timeline: str = "24h") -> List[Dict[str, str]]:
        """
        สร้างแผนปฏิบัติการรายขั้นตอน (Step-by-Step Action Plan)
        """
        plan = [
            {"step": 1, "action": "เตรียมความพร้อมและรวบรวมทรัพยากร", "timeframe": "Immediate"},
            {"step": 2, "action": "สื่อสารกับผู้มีส่วนได้ส่วนเสียหลัก", "timeframe": "Within 1 hour"},
            {"step": 3, "action": "ดำเนินการตามแผนหลัก (Primary Action)", "timeframe": "Within 4 hours"},
            {"step": 4, "action": "ติดตามผลและประเมินสถานการณ์", "timeframe": "Every 2 hours"},
            {"step": 5, "action": "ปรับแผนหากจำเป็น (Plan B Activation)", "timeframe": "As needed"},
            {"step": 6, "action": "สรุปผลและบันทึกบทเรียน", "timeframe": "End of timeline"}
        ]
        return plan


class DecisionSummarizer:
    """โมดูลสรุปผลการตัดสินใจ (Decision Summarization)"""
    
    @staticmethod
    def executive_summary(problem: str, decision: str, rationale: str, impact: str) -> str:
        """
        สรุปแบบผู้บริหาร (กระชับ ได้ใจความ)
        """
        summary = f"""
        --- EXECUTIVE SUMMARY ---
        ปัญหาหลัก: {problem}
        การตัดสินใจ: {decision}
        เหตุผลสำคัญ: {rationale}
        ผลกระทบที่คาดการณ์: {impact}
        -------------------------
        """
        return summary.strip()

    @staticmethod
    def narrative_report(analysis: Dict, plan: List, context: Dict) -> str:
        """
        สรุปแบบเล่าเรื่อง (Narrative Report) เหมาะสำหรับอธิบายให้มนุษย์เข้าใจ
        """
        report = []
        report.append(f"**สถานการณ์:** {analysis.get('core_problem', 'N/A')}")
        report.append("\n**การวิเคราะห์:**")
        report.append(f"- ผู้เกี่ยวข้องหลัก: {', '.join(analysis.get('stakeholders', {}).keys())}")
        report.append(f"- ข้อจำกัดสำคัญ: {', '.join(analysis.get('components', {}).get('constraints', []))}")
        
        report.append("\n**แผนปฏิบัติการ:**")
        for step in plan[:3]: # เอาแค่ 3 ขั้นตอนแรกสำหรับสรุป
            report.append(f"{step['step']}. {step['action']} ({step['timeframe']})")
            
        report.append("\n**บทสรุป:** การตัดสินใจนี้มุ่งเน้นการสร้างสมดุลระหว่างความถูกต้องและความเห็นอกเห็นใจ โดยยอมรับความเสี่ยงบางประการเพื่อผลประโยชน์ระยะยาว")
        
        return "\n".join(report)


# --- Example Usage / Demo ---
if __name__ == "__main__":
    print("=== Initializing Analysis Planner Pack ===\n")
    
    # 1. กำหนดสถานการณ์ (จำลองเคส "ความลับของอนาคต")
    scenario_text = "รู้ล่วงหน้าว่าจะเกิดภัยพิบัติ แต่การเตือนจะทำให้เสียชื่อเสียงและถูกฟ้องร้อง"
    context_data = {
        "people_involved": [
            {"name": "ตัวคุณ", "role": "ผู้รู้ความจริง", "pain_point": "กลัวเสียชื่อเสียง"},
            {"name": "ชาวบ้าน", "role": "ผู้ประสบภัย", "pain_point": "อันตรายถึงชีวิต"},
            {"name": "ภาคอสังหาฯ", "role": "ผู้ได้รับผลกระทบทางเศรษฐกิจ", "pain_point": "ความเสียหายทางการเงิน"}
        ],
        "constraints": ["เวลา 1 ปีก่อนเกิดเหตุ", "ความเสี่ยงถูกฟ้องร้อง", "ความน่าเชื่อถือของแหล่งข้อมูล"],
        "time_limit": "24 ชั่วโมงในการตัดสินใจเบื้องต้น"
    }

    # 2. วิเคราะห์ (Analyze)
    analyzer = ScenarioAnalyzer()
    decomposition = analyzer.decompose(scenario_text, context_data)
    root_causes = analyzer.find_root_cause(decomposition["components"])
    
    print(">> Step 1: Analysis Complete")
    print(f"   Stakeholders identified: {list(decomposition['stakeholders'].keys())}")
    print(f"   Constraints: {decomposition['components']['constraints']}")
    
    # 3. วางแผน (Plan)
    planner = StrategicPlanner()
    options = planner.generate_options(decomposition)
    # สมมติเลือกทางเลือกที่ 3 (Human-Centric / Anonymous Warning)
    selected_opt = options[2] 
    action_plan = planner.create_action_plan(selected_opt)
    
    print("\n>> Step 2: Planning Complete")
    print(f"   Selected Strategy: {selected_opt['type']} - {selected_opt['description']}")
    print(f"   First Action: {action_plan[0]['action']}")

    # 4. สรุป (Summary)
    summarizer = DecisionSummarizer()
    exec_sum = summarizer.executive_summary(
        problem=scenario_text,
        decision="เผยแพร่ข้อมูลแบบนิรนามผ่านช่องทางออนไลน์ที่ตรวจสอบยาก",
        rationale="เพื่อเตือนภัยประชาชนโดยไม่เปิดเผยตัวตน ลดความเสี่ยงส่วนตัวแต่ยังคงจริยธรรม",
        impact="ชาวบ้านเตรียมตัวได้, ตัวคุณปลอดภัย, ภาคอสังหาฯ อาจเสียหายแต่ไม่สามารถฟ้องร้องได้"
    )
    
    print("\n>> Step 3: Summary Generated")
    print(exec_sum)
    
    print("\n=== Pack Ready for Integration ===")
