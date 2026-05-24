# Intent Classification System for Cognitive Analysis

## ภาพรวมของระบบ

ระบบนี้ได้เพิ่ม **Intent Classification Module** เข้ามาเพื่อจับความตั้งใจของผู้ใช้ (Intent Detection) ก่อนที่จะส่งข้อมูลไปวิเคราะห์ต่อ ทำให้ระบบสามารถเลือกเครื่องมือวิเคราะห์ที่เหมาะสมกับความต้องการของผู้ใช้ได้ถูกต้องมากขึ้น

## โครงสร้างไฟล์ที่เพิ่มใหม่

### 1. `intent_classifier.py` - โมดูลจับ Intent
ประกอบด้วย:
- **IntentPattern**: Rule-based pattern matching สำหรับจับรูปแบบประโยค
- **SemanticAnalyzer**: วิเคราะห์ keywords ในข้อความ
- **IntentContext**: เก็บ context การสนทนาเพื่อปรับปรุงความแม่นยำ
- **IntentClassifier**: ตัวจัดประเภท Intent หลัก

#### ประเภทของ Intent ที่รองรับ:
| Intent | คำอธิบาย | ตัวอย่าง |
|--------|----------|---------|
| `advice` | ต้องการคำแนะนำ | "ควรทำยังไงดี?", "ขอคำปรึกษา" |
| `emotional_support` | ต้องการการสนับสนุนทางอารมณ์ | "รู้สึกท้อมาก", "ไม่เข้าใจ" |
| `information` | ต้องการข้อมูล/ความรู้ | "คืออะไร?", "เพราะอะไร?" |
| `decision` | ต้องการช่วยตัดสินใจ | "ระหว่าง A กับ B เลือกอะไร?" |
| `analysis` | ต้องการวิเคราะห์สถานการณ์ | "ช่วยวิเคราะห์หน่อย", "ใครได้ใครเสีย" |
| `action_plan` | ต้องการแผนปฏิบัติการ | "ต้องมีขั้นตอนอะไรบ้าง?" |

### 2. `integrated_cognitive_system.py` - ระบบบูรณาการ
เชื่อม Intent Classifier เข้ากับเครื่องมือวิเคราะห์ที่มีอยู่:
- **EmpathyBuffer** (จาก humanity_tools) - สำหรับ emotional_support
- **ScenarioAnalyzer** (จาก analysis_planner_pack) - สำหรับ advice/decision
- **StrategicPlanner** (จาก analysis_planner_pack) - สำหรับสร้างทางเลือก
- **CognitiveEngine** (จาก cognitive_engine) - สำหรับการวิเคราะห์แบบเต็มรูปแบบ

## วิธีการทำงาน

```
┌─────────────────┐
│  User Input     │
│  (ข้อความเข้า)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Intent          │
│ Classification  │ ← Step 1: จับความตั้งใจ
│                 │    - Pattern Matching
│                 │    - Keyword Analysis
│                 │    - Context Awareness
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Route to        │
│ Appropriate     │ ← Step 2: เลือกเครื่องมือตาม Intent
│ Tool            │
└────────┬────────┘
         │
    ┌────┴────┬───────────┬──────────────┐
    │         │           │              │
    ▼         ▼           ▼              ▼
┌────────┐ ┌────────┐ ┌──────────┐ ┌──────────┐
│Empathy │ │Scenario│ │Cognitive │ │Action    │
│Buffer  │ │Analyzer│ │Engine    │ │Planner   │
└────────┘ └────────┘ └──────────┘ └──────────┘
    │         │           │              │
    └────┬────┴───────────┴──────────────┘
         │
         ▼
┌─────────────────┐
│ Response        │
│ (ผลลัพธ์)       │
└─────────────────┘
```

## การใช้งาน

### แบบง่าย - ใช้ Intent Classifier โดยตรง

```python
from intent_classifier import IntentClassifier

classifier = IntentClassifier(use_context=True)

result = classifier.classify("ฉันควรบอกเพื่อนเรื่องแฟนเขาโกงไหม?")

print(f"Intent: {result['primary_intent']}")
print(f"Confidence: {result['confidence']*100:.1f}%")
print(f"Recommended Action: {result['recommended_action']}")
```

### แบบเต็ม - ใช้ Integrated System

```python
from integrated_cognitive_system import IntegratedCognitiveSystem

system = IntegratedCognitiveSystem()

result = system.process(
    "ฉันควรบอกเพื่อนเรื่องแฟนเขาโกงไหม?",
    context={
        'people_involved': [
            {'name': 'ฉัน', 'role': 'ผู้รู้ความจริง'},
            {'name': 'เพื่อน', 'role': 'ผู้ถูกหักหลัง'}
        ],
        'constraints': ['มิตรภาพ', 'จริยธรรม']
    }
)

# ผลลัพธ์ประกอบด้วย:
# - intent: ข้อมูล Intent ที่ตรวจจับได้
# - analysis: ผลการวิเคราะห์
# - recommendation: คำแนะนำ (ถ้ามี)
# - response: ข้อความตอบกลับ (ถ้ามี)
```

## ตัวอย่างการทำงาน

### Test Case 1: Emotional Support
```
Input: "รู้สึกท้อมาก ไม่รู้จะทำยังไงดี"
Intent Detected: emotional_support (70% confidence)
Action: ใช้ EmpathyBuffer เพื่อรับอารมณ์ก่อน แล้วค่อยวิเคราะห์
```

### Test Case 2: Decision Making
```
Input: "ระหว่างบอกความจริงกับเงียบไว้ เลือกทางไหนดี?"
Intent Detected: decision (73.3% confidence)
Action: ใช้ StrategicPlanner สร้างทางเลือกและประเมิน Trade-off
```

### Test Case 3: Analysis Request
```
Input: "ช่วยวิเคราะห์สถานการณ์นี้หน่อย มีใครได้ใครเสียบ้าง"
Intent Detected: analysis (53.5% confidence)
Action: ใช้ ScenarioAnalyzer แยกองค์ประกอบปัญหา
```

## การขยายระบบในอนาคต

1. **เพิ่ม Patterns**: เพิ่ม regex patterns ใน `IntentPattern.PATTERNS` เพื่อจับรูปแบบประโยคใหม่ๆ
2. **เพิ่ม Intents**: เพิ่มประเภท Intent ใหม่ใน dictionary ทั้ง PATTERNS และ KEYWORDS
3. **Machine Learning**: สามารถแทนที่หรือเสริมด้วย ML model สำหรับ classification ที่แม่นยำขึ้น
4. **Multi-intent Detection**: รองรับกรณีที่ข้อความเดียวมีหลาย intents
5. **Language Support**: ขยายรองรับภาษาอื่นๆ นอกจากภาษาไทย

## ไฟล์ที่เกี่ยวข้อง

- `intent_classifier.py` - โมดูลหลักสำหรับจับ Intent
- `integrated_cognitive_system.py` - ระบบที่รวมทุกอย่างเข้าด้วยกัน
- `analysis_planner_pack.py` - เครื่องมือวิเคราะห์และวางแผน (เดิม)
- `humanity_tools.py` - เครื่องมือจัดการอารมณ์และความสัมพันธ์ (เดิม)
- `cognitive_engine/engines/core.py` - เอนจินวิเคราะห์ปัญหา (เดิม)

## สรุป

การเพิ่ม Intent Classification ช่วยให้ระบบ:
✅ เข้าใจความต้องการของผู้ใช้ได้ดีขึ้น
✅ เลือกเครื่องมือวิเคราะห์ได้เหมาะสม
✅ ให้คำตอบที่ตรงกับสิ่งที่ผู้ใช้ต้องการ
✅ ลดการประมวลผลที่ไม่จำเป็น
✅ ปรับปรุงประสบการณ์การใช้งานโดยรวม
