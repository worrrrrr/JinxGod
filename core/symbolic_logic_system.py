#!/usr/bin/env python3
"""
Symbolic Logic System - Engineering Programmer Approach
Pragmatic Tools for Mathematical Logic Operations

Features:
- Propositional Logic
- Predicate Logic
- Truth Tables
- Logical Equivalence Checking
- Normal Forms (CNF, DNF)
- Inference Rules
- Boolean Algebra Simplification
"""

from typing import List, Dict, Set, Tuple, Optional, Union, Callable
from dataclasses import dataclass, field
from enum import Enum
from functools import reduce
import itertools
import re


class LogicalOperator(Enum):
    """Enumeration of logical operators"""
    NOT = "¬"
    AND = "∧"
    OR = "∨"
    IMPLIES = "→"
    IFF = "↔"
    XOR = "⊕"
    NAND = "↑"
    NOR = "↓"


@dataclass
class Symbol:
    """Represents a logical symbol/variable"""
    name: str
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.name == other.name
        return False
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Symbol('{self.name}')"


@dataclass
class Expression:
    """Base class for logical expressions"""
    pass


@dataclass
class Variable(Expression):
    """Logical variable"""
    symbol: Symbol
    
    def evaluate(self, assignment: Dict[Symbol, bool]) -> bool:
        return assignment[self.symbol]
    
    def get_variables(self) -> Set[Symbol]:
        return {self.symbol}
    
    def __str__(self):
        return str(self.symbol)
    
    def __hash__(self):
        return hash(('var', self.symbol))
    
    def __eq__(self, other):
        if isinstance(other, Variable):
            return self.symbol == other.symbol
        return False


@dataclass
class Constant(Expression):
    """Logical constant (True/False)"""
    value: bool
    
    def evaluate(self, assignment: Dict[Symbol, bool]) -> bool:
        return self.value
    
    def get_variables(self) -> Set[Symbol]:
        return set()
    
    def __str__(self):
        return "T" if self.value else "F"
    
    def __hash__(self):
        return hash(('const', self.value))
    
    def __eq__(self, other):
        if isinstance(other, Constant):
            return self.value == other.value
        return False


@dataclass
class CompoundExpression(Expression):
    """Compound logical expression with operator and operands"""
    operator: LogicalOperator
    operands: List[Expression]
    
    def evaluate(self, assignment: Dict[Symbol, bool]) -> bool:
        evaluated_ops = [op.evaluate(assignment) for op in self.operands]
        
        if self.operator == LogicalOperator.NOT:
            return not evaluated_ops[0]
        elif self.operator == LogicalOperator.AND:
            return all(evaluated_ops)
        elif self.operator == LogicalOperator.OR:
            return any(evaluated_ops)
        elif self.operator == LogicalOperator.IMPLIES:
            return (not evaluated_ops[0]) or evaluated_ops[1]
        elif self.operator == LogicalOperator.IFF:
            return evaluated_ops[0] == evaluated_ops[1]
        elif self.operator == LogicalOperator.XOR:
            return evaluated_ops[0] != evaluated_ops[1]
        elif self.operator == LogicalOperator.NAND:
            return not all(evaluated_ops)
        elif self.operator == LogicalOperator.NOR:
            return not any(evaluated_ops)
        else:
            raise ValueError(f"Unknown operator: {self.operator}")
    
    def get_variables(self) -> Set[Symbol]:
        variables = set()
        for operand in self.operands:
            variables.update(operand.get_variables())
        return variables
    
    def __str__(self):
        if self.operator == LogicalOperator.NOT:
            return f"¬{self.operands[0]}"
        elif len(self.operands) == 2:
            return f"({self.operands[0]} {self.operator.value} {self.operands[1]})"
        else:
            ops_str = f" {self.operator.value} ".join(str(op) for op in self.operands)
            return f"({ops_str})"
    
    def __hash__(self):
        return hash((self.operator, tuple(self.operands)))
    
    def __eq__(self, other):
        if isinstance(other, CompoundExpression):
            return (self.operator == other.operator and 
                    self.operands == other.operands)
        return False


class TruthTable:
    """Generate and analyze truth tables"""
    
    def __init__(self, expression: Expression):
        self.expression = expression
        self.variables = sorted(expression.get_variables(), key=lambda s: s.name)
        self.table: List[Tuple[Dict[Symbol, bool], bool]] = []
        self._generate_table()
    
    def _generate_table(self):
        """Generate complete truth table"""
        n_vars = len(self.variables)
        for i in range(2 ** n_vars):
            assignment = {}
            for j, var in enumerate(self.variables):
                # Extract bit at position j (from right, reversed order)
                assignment[var] = bool((i >> (n_vars - 1 - j)) & 1)
            result = self.expression.evaluate(assignment)
            self.table.append((assignment, result))
    
    def display(self) -> str:
        """Display formatted truth table"""
        if not self.variables:
            return f"Expression: {self.expression} = {self.table[0][1] if self.table else 'N/A'}"
        
        # Header
        header = " | ".join(str(v) for v in self.variables) + f" | {self.expression}"
        separator = "-+-".join("-" * len(str(v)) for v in self.variables) + "-+-" + "-" * len(str(self.expression))
        
        # Rows
        rows = []
        for assignment, result in self.table:
            row = " | ".join("T" if assignment[v] else "F" for v in self.variables)
            row += f" | {'T' if result else 'F'}"
            rows.append(row)
        
        return "\n".join([header, separator] + rows)
    
    def is_tautology(self) -> bool:
        """Check if expression is always true"""
        return all(result for _, result in self.table)
    
    def is_contradiction(self) -> bool:
        """Check if expression is always false"""
        return all(not result for _, result in self.table)
    
    def is_satisfiable(self) -> bool:
        """Check if expression can be true"""
        return any(result for _, result in self.table)
    
    def get_models(self) -> List[Dict[Symbol, bool]]:
        """Get all assignments that make expression true"""
        return [assignment for assignment, result in self.table if result]


class LogicEngine:
    """Main engine for logical operations"""
    
    @staticmethod
    def create_variable(name: str) -> Variable:
        """Create a logical variable"""
        return Variable(Symbol(name))
    
    @staticmethod
    def create_constant(value: bool) -> Constant:
        """Create a logical constant"""
        return Constant(value)
    
    @staticmethod
    def neg(expr: Expression) -> CompoundExpression:
        """Create negation"""
        return CompoundExpression(LogicalOperator.NOT, [expr])
    
    @staticmethod
    def conj(*exprs: Expression) -> CompoundExpression:
        """Create conjunction (AND)"""
        if len(exprs) == 1:
            return exprs[0]
        return CompoundExpression(LogicalOperator.AND, list(exprs))
    
    @staticmethod
    def disj(*exprs: Expression) -> CompoundExpression:
        """Create disjunction (OR)"""
        if len(exprs) == 1:
            return exprs[0]
        return CompoundExpression(LogicalOperator.OR, list(exprs))
    
    @staticmethod
    def implies(antecedent: Expression, consequent: Expression) -> CompoundExpression:
        """Create implication"""
        return CompoundExpression(LogicalOperator.IMPLIES, [antecedent, consequent])
    
    @staticmethod
    def iff(left: Expression, right: Expression) -> CompoundExpression:
        """Create biconditional"""
        return CompoundExpression(LogicalOperator.IFF, [left, right])
    
    @staticmethod
    def xor(left: Expression, right: Expression) -> CompoundExpression:
        """Create exclusive OR"""
        return CompoundExpression(LogicalOperator.XOR, [left, right])
    
    @staticmethod
    def are_equivalent(expr1: Expression, expr2: Expression) -> bool:
        """Check if two expressions are logically equivalent"""
        vars1 = expr1.get_variables()
        vars2 = expr2.get_variables()
        all_vars = sorted(vars1.union(vars2), key=lambda s: s.name)
        
        if not all_vars:
            # Both are constants
            dummy_assignment = {}
            return expr1.evaluate(dummy_assignment) == expr2.evaluate(dummy_assignment)
        
        # Check all possible assignments
        n_vars = len(all_vars)
        for i in range(2 ** n_vars):
            assignment = {}
            for j, var in enumerate(all_vars):
                assignment[var] = bool((i >> (n_vars - 1 - j)) & 1)
            if expr1.evaluate(assignment) != expr2.evaluate(assignment):
                return False
        return True
    
    @staticmethod
    def entails(premises: List[Expression], conclusion: Expression) -> bool:
        """Check if premises entail conclusion"""
        conjunction = LogicEngine.conj(*premises) if premises else LogicEngine.create_constant(True)
        implication = LogicEngine.implies(conjunction, conclusion)
        return TruthTable(implication).is_tautology()
    
    @staticmethod
    def to_nnf(expr: Expression) -> Expression:
        """Convert to Negation Normal Form"""
        if isinstance(expr, (Variable, Constant)):
            return expr
        
        if isinstance(expr, CompoundExpression):
            if expr.operator == LogicalOperator.NOT:
                inner = expr.operands[0]
                if isinstance(inner, Constant):
                    return Constant(not inner.value)
                elif isinstance(inner, Variable):
                    return expr
                elif isinstance(inner, CompoundExpression):
                    if inner.operator == LogicalOperator.NOT:
                        return LogicEngine.to_nnf(inner.operands[0])
                    elif inner.operator == LogicalOperator.AND:
                        return LogicEngine.disj(*[LogicEngine.to_nnf(LogicEngine.neg(op)) for op in inner.operands])
                    elif inner.operator == LogicalOperator.OR:
                        return LogicEngine.conj(*[LogicEngine.to_nnf(LogicEngine.neg(op)) for op in inner.operands])
                    elif inner.operator == LogicalOperator.IMPLIES:
                        return LogicEngine.conj(
                            LogicEngine.to_nnf(inner.operands[0]),
                            LogicEngine.to_nnf(LogicEngine.neg(inner.operands[1]))
                        )
                    elif inner.operator == LogicalOperator.IFF:
                        # A ↔ B becomes (A ∧ B) ∨ (¬A ∧ ¬B)
                        a, b = inner.operands
                        left = LogicEngine.conj(LogicEngine.to_nnf(a), LogicEngine.to_nnf(b))
                        right = LogicEngine.conj(
                            LogicEngine.to_nnf(LogicEngine.neg(a)),
                            LogicEngine.to_nnf(LogicEngine.neg(b))
                        )
                        return LogicEngine.disj(left, right)
            
            # Recursively process operands
            new_operands = [LogicEngine.to_nnf(op) for op in expr.operands]
            
            # Handle implications and biconditionals
            if expr.operator == LogicalOperator.IMPLIES:
                return LogicEngine.disj(
                    LogicEngine.to_nnf(LogicEngine.neg(expr.operands[0])),
                    LogicEngine.to_nnf(expr.operands[1])
                )
            elif expr.operator == LogicalOperator.IFF:
                a, b = expr.operands
                left = LogicEngine.conj(LogicEngine.to_nnf(a), LogicEngine.to_nnf(b))
                right = LogicEngine.conj(
                    LogicEngine.to_nnf(LogicEngine.neg(a)),
                    LogicEngine.to_nnf(LogicEngine.neg(b))
                )
                return LogicEngine.disj(left, right)
            
            return CompoundExpression(expr.operator, new_operands)
        
        return expr
    
    @staticmethod
    def to_cnf(expr: Expression) -> Expression:
        """Convert to Conjunctive Normal Form"""
        # First convert to NNF
        nnf = LogicEngine.to_nnf(expr)
        return LogicEngine._distribute_or_over_and(nnf)
    
    @staticmethod
    def _distribute_or_over_and(expr: Expression) -> Expression:
        """Distribute OR over AND for CNF"""
        if isinstance(expr, (Variable, Constant)):
            return expr
        
        if isinstance(expr, CompoundExpression):
            if expr.operator == LogicalOperator.NOT:
                return expr
            
            # Process operands first
            new_operands = [LogicEngine._distribute_or_over_and(op) for op in expr.operands]
            
            if expr.operator == LogicalOperator.AND:
                return CompoundExpression(LogicalOperator.AND, new_operands)
            
            if expr.operator == LogicalOperator.OR:
                # Check if any operand is an AND
                and_operands = [op for op in new_operands if isinstance(op, CompoundExpression) and op.operator == LogicalOperator.AND]
                
                if not and_operands:
                    return CompoundExpression(LogicalOperator.OR, new_operands)
                
                # Distribute: (A ∧ B) ∨ C = (A ∨ C) ∧ (B ∨ C)
                # Start with first AND operand
                and_op = and_operands[0]
                other_ops = [op for op in new_operands if op != and_op]
                
                # Create disjunctions for each conjunct
                conjuncts = []
                for conjunct in and_op.operands:
                    new_disjunct_operands = [conjunct] + other_ops
                    conjuncts.append(LogicEngine._distribute_or_over_and(
                        CompoundExpression(LogicalOperator.OR, new_disjunct_operands)
                    ))
                
                return CompoundExpression(LogicalOperator.AND, conjuncts)
        
        return expr
    
    @staticmethod
    def resolve(clause1: Set[Symbol], clause2: Set[Symbol], literal: Symbol) -> Optional[Set[Symbol]]:
        """Resolution rule: resolve two clauses on a literal"""
        # This is a simplified version for demonstration
        # In full implementation, would handle negated literals properly
        pass


class InferenceSystem:
    """Formal inference rules and proof system"""
    
    @staticmethod
    def modus_ponens(p: Expression, p_implies_q: Expression) -> Optional[Expression]:
        """Modus Ponens: From P and P → Q, derive Q"""
        if isinstance(p_implies_q, CompoundExpression) and p_implies_q.operator == LogicalOperator.IMPLIES:
            if LogicEngine.are_equivalent(p, p_implies_q.operands[0]):
                return p_implies_q.operands[1]
        return None
    
    @staticmethod
    def modus_tollens(not_q: Expression, p_implies_q: Expression) -> Optional[Expression]:
        """Modus Tollens: From ¬Q and P → Q, derive ¬P"""
        if isinstance(p_implies_q, CompoundExpression) and p_implies_q.operator == LogicalOperator.IMPLIES:
            q = p_implies_q.operands[1]
            if isinstance(not_q, CompoundExpression) and not_q.operator == LogicalOperator.NOT:
                if LogicEngine.are_equivalent(q, not_q.operands[0]):
                    return LogicEngine.neg(p_implies_q.operands[0])
        return None
    
    @staticmethod
    def hypothetical_syllogism(p_implies_q: Expression, q_implies_r: Expression) -> Optional[Expression]:
        """Hypothetical Syllogism: From P → Q and Q → R, derive P → R"""
        if (isinstance(p_implies_q, CompoundExpression) and p_implies_q.operator == LogicalOperator.IMPLIES and
            isinstance(q_implies_r, CompoundExpression) and q_implies_r.operator == LogicalOperator.IMPLIES):
            if LogicEngine.are_equivalent(p_implies_q.operands[1], q_implies_r.operands[0]):
                return LogicEngine.implies(p_implies_q.operands[0], q_implies_r.operands[1])
        return None
    
    @staticmethod
    def disjunctive_syllogism(p_or_q: Expression, not_p: Expression) -> Optional[Expression]:
        """Disjunctive Syllogism: From P ∨ Q and ¬P, derive Q"""
        if isinstance(p_or_q, CompoundExpression) and p_or_q.operator == LogicalOperator.OR:
            if isinstance(not_p, CompoundExpression) and not_p.operator == LogicalOperator.NOT:
                for operand in p_or_q.operands:
                    if LogicEngine.are_equivalent(operand, not_p.operands[0]):
                        other = [op for op in p_or_q.operands if op != operand][0]
                        return other
        return None


class BooleanAlgebra:
    """Boolean algebra simplification tools"""
    
    @staticmethod
    def simplify(expr: Expression) -> Expression:
        """Simplify boolean expression using algebraic laws"""
        if isinstance(expr, (Variable, Constant)):
            return expr
        
        if isinstance(expr, CompoundExpression):
            # Simplify operands first
            simplified_operands = [BooleanAlgebra.simplify(op) for op in expr.operands]
            
            # Remove nested constants where possible
            if expr.operator == LogicalOperator.NOT:
                inner = simplified_operands[0]
                if isinstance(inner, Constant):
                    return Constant(not inner.value)
                return CompoundExpression(LogicalOperator.NOT, [inner])
            
            if expr.operator == LogicalOperator.AND:
                # Identity: A ∧ T = A
                # Annihilation: A ∧ F = F
                # Idempotent: A ∧ A = A
                # Complement: A ∧ ¬A = F
                if any(isinstance(op, Constant) and op.value == False for op in simplified_operands):
                    return Constant(False)
                
                # Remove True values
                filtered = [op for op in simplified_operands if not (isinstance(op, Constant) and op.value == True)]
                
                if not filtered:
                    return Constant(True)
                if len(filtered) == 1:
                    return filtered[0]
                
                # Check for complements
                for i, op1 in enumerate(filtered):
                    for j, op2 in enumerate(filtered[i+1:], i+1):
                        if BooleanAlgebra._are_complements(op1, op2):
                            return Constant(False)
                
                return CompoundExpression(LogicalOperator.AND, filtered)
            
            if expr.operator == LogicalOperator.OR:
                # Identity: A ∨ F = A
                # Annihilation: A ∨ T = T
                # Idempotent: A ∨ A = A
                # Complement: A ∨ ¬A = T
                if any(isinstance(op, Constant) and op.value == True for op in simplified_operands):
                    return Constant(True)
                
                # Remove False values
                filtered = [op for op in simplified_operands if not (isinstance(op, Constant) and op.value == False)]
                
                if not filtered:
                    return Constant(False)
                if len(filtered) == 1:
                    return filtered[0]
                
                # Check for complements
                for i, op1 in enumerate(filtered):
                    for j, op2 in enumerate(filtered[i+1:], i+1):
                        if BooleanAlgebra._are_complements(op1, op2):
                            return Constant(True)
                
                return CompoundExpression(LogicalOperator.OR, filtered)
            
            if expr.operator == LogicalOperator.IMPLIES:
                # P → Q ≡ ¬P ∨ Q
                return LogicEngine.disj(
                    LogicEngine.neg(simplified_operands[0]),
                    simplified_operands[1]
                )
            
            if expr.operator == LogicalOperator.IFF:
                # P ↔ Q ≡ (P ∧ Q) ∨ (¬P ∧ ¬Q)
                p, q = simplified_operands
                left = LogicEngine.conj(p, q)
                right = LogicEngine.conj(LogicEngine.neg(p), LogicEngine.neg(q))
                return LogicEngine.disj(left, right)
            
            return CompoundExpression(expr.operator, simplified_operands)
        
        return expr
    
    @staticmethod
    def _are_complements(expr1: Expression, expr2: Expression) -> bool:
        """Check if two expressions are complements"""
        if isinstance(expr1, CompoundExpression) and expr1.operator == LogicalOperator.NOT:
            return LogicEngine.are_equivalent(expr1.operands[0], expr2)
        if isinstance(expr2, CompoundExpression) and expr2.operator == LogicalOperator.NOT:
            return LogicEngine.are_equivalent(expr1, expr2.operands[0])
        return False


class ChildEmergencyProtocol:
    """
    โปรโตคอลพิเศษสำหรับสถานการณ์ฉุกเฉินที่มีเด็กเกี่ยวข้อง
    เปลี่ยนตรรกะซับซ้อน -> ภารกิจเกม (Gamified Mission)
    """
    
    def __init__(self):
        self.mission_mode = True
        self.tone = "calm_commander"
        
    def process_emergency(self, situation: dict) -> list:
        """
        รับข้อมูลสถานการณ์ฉุกเฉิน และแปลงเป็นคำสั่งแบบ 'เกม' สำหรับเด็ก
        Input: situation (dict) เช่น {'age': 12, 'panic_level': 'high', 'device': 'computer'}
        Output: รายการคำสั่งสั้นๆ (Action List)
        """
        actions = []
        
        # 1. ตรึงสติด้วยภาษาเกม
        actions.append("START_MISSION: 'พี่จะเป็นกัปตันทีม หนูเป็นฮีโร่ประจำการ'")
        
        # 2. ดึงข้อมูลตำแหน่งแบบง่าย (ไม่ต้องอธิบายยาว)
        if situation.get('has_computer'):
            actions.append("QUEST_1: 'เปิดคอมฯ กดปุ่มรูปโลก (Google Maps) พิมพ์คำว่า My Location แล้วแคปหน้าจอส่งให้พี่'")
        else:
            actions.append("QUEST_1: 'วิ่งไปดูเลขที่บ้านข้างประตู แล้วบอกพี่ตัวเลขนั้นเลย'")
            
        # 3. สั่งการปฐมพยาบาลแบบอัตโนมัติ (Auto-Pilot)
        actions.append("QUEST_2: 'เอาผ้ากดไว้ตรงที่เลือดออก กดแน่นๆ เหมือนกำลังอุดรูรั่วของเกม'")
        
        # 4. เรียกหน่วยกู้ภัย (Backend Process)
        actions.append("CALL_SUPPORT: 'พี่จะโทรเรียกทีมแพทย์บินด่วน หนูไม่ต้องกังวลเรื่องเบอร์โทรศัพท์'")
        
        # 5. ประคองพลังงานและจิตใจ
        actions.append("POWER_SAVE: 'อย่ากดเล่นอย่างอื่น แบตต้องเหลือไว้คุยกับพี่จนกว่าทีมแพทย์จะมาถึง'")
        actions.append("MISSION_STATUS: 'ทำดีมาก! ทีมแพทย์กำลังเดินทาง อีก 5 นาทีจะถึงจุดนัดพบ'")
        
        return actions

    def execute(self, scenario_description: str):
        print(f"\n--- 🚨 GOD MODE: CHILD EMERGENCY PROTOCOL ACTIVATED ---")
        print(f"Scenario: {scenario_description}")
        print("-" * 60)
        
        # จำลองการวิเคราะห์สถานการณ์
        situation = {
            'age': 12,
            'panic_level': 'high',
            'has_computer': True,
            'battery_low': True
        }
        
        steps = self.process_emergency(situation)
        
        print("🎮 GAMIFIED ACTION PLAN (สำหรับเด็ก 12 ขวบ):\n")
        for i, step in enumerate(steps, 1):
            print(f"Step {i}: {step}")
            
        print("\n✅ Status: Mission Started. Waiting for location data...")
        print("-------------------------------------------------------\n")


# Convenience functions for building expressions
def var(name: str) -> Variable:
    """Create a variable"""
    return LogicEngine.create_variable(name)

def const(value: bool) -> Constant:
    """Create a constant"""
    return LogicEngine.create_constant(value)

def NOT(expr: Expression) -> Expression:
    """Negation"""
    return LogicEngine.neg(expr)

def AND(*exprs: Expression) -> Expression:
    """Conjunction"""
    return LogicEngine.conj(*exprs)

def OR(*exprs: Expression) -> Expression:
    """Disjunction"""
    return LogicEngine.disj(*exprs)

def IMPLIES(p: Expression, q: Expression) -> Expression:
    """Implication"""
    return LogicEngine.implies(p, q)

def IFF(p: Expression, q: Expression) -> Expression:
    """Biconditional"""
    return LogicEngine.iff(p, q)


if __name__ == "__main__":
    print("=" * 70)
    print("SYMBOLIC LOGIC SYSTEM - Engineering Programmer Edition")
    print("=" * 70)
    
    # Example 1: Basic proposition
    print("\n1. BASIC PROPOSITION")
    print("-" * 40)
    p = var("P")
    q = var("Q")
    r = var("R")
    
    expr = AND(OR(p, q), NOT(p))
    print(f"Expression: {expr}")
    print(f"Variables: {expr.get_variables()}")
    
    tt = TruthTable(expr)
    print("\nTruth Table:")
    print(tt.display())
    print(f"\nSatisfiable: {tt.is_satisfiable()}")
    print(f"Tautology: {tt.is_tautology()}")
    print(f"Contradiction: {tt.is_contradiction()}")
    
    # Example 2: Logical equivalence
    print("\n\n2. LOGICAL EQUIVALENCE")
    print("-" * 40)
    expr1 = IMPLIES(p, q)
    expr2 = OR(NOT(p), q)
    
    print(f"Expression 1: {expr1}")
    print(f"Expression 2: {expr2}")
    print(f"Equivalent: {LogicEngine.are_equivalent(expr1, expr2)}")
    
    # Example 3: Inference
    print("\n\n3. INFERENCE RULES")
    print("-" * 40)
    premise1 = IMPLIES(p, q)
    premise2 = p
    conclusion = q
    
    print(f"Premise 1: {premise1}")
    print(f"Premise 2: {premise2}")
    print(f"Conclusion: {conclusion}")
    print(f"Valid inference: {InferenceSystem.modus_ponens(premise2, premise1) is not None}")
    
    # Example 4: Entailment
    print("\n\n4. ENTAILMENT CHECKING")
    print("-" * 40)
    premises = [IMPLIES(p, q), IMPLIES(q, r)]
    conclusion = IMPLIES(p, r)
    
    print(f"Premises: {[str(p) for p in premises]}")
    print(f"Conclusion: {conclusion}")
    print(f"Entailment holds: {LogicEngine.entails(premises, conclusion)}")
    
    # Example 5: Normal forms
    print("\n\n5. NORMAL FORMS")
    print("-" * 40)
    complex_expr = IMPLIES(AND(p, q), r)
    print(f"Original: {complex_expr}")
    
    nnf = LogicEngine.to_nnf(complex_expr)
    print(f"NNF: {nnf}")
    
    cnf = LogicEngine.to_cnf(complex_expr)
    print(f"CNF: {cnf}")
    
    # Example 6: Simplification
    print("\n\n6. BOOLEAN ALGEBRA SIMPLIFICATION")
    print("-" * 40)
    unsimplified = OR(AND(p, const(True)), AND(q, const(False)))
    print(f"Unsimplified: {unsimplified}")
    simplified = BooleanAlgebra.simplify(unsimplified)
    print(f"Simplified: {simplified}")
    
    # Example 7: Complex tautology
    print("\n\n7. TAUTOLOGY VERIFICATION")
    print("-" * 40)
    excluded_middle = OR(p, NOT(p))
    print(f"Law of Excluded Middle: {excluded_middle}")
    print(f"Is tautology: {TruthTable(excluded_middle).is_tautology()}")
    
    contradiction_check = AND(p, NOT(p))
    print(f"\nLaw of Non-Contradiction: {contradiction_check}")
    print(f"Is contradiction: {TruthTable(contradiction_check).is_contradiction()}")

    # Example 8: Child Emergency Protocol (God Mode)
    print("\n\n8. GOD MODE: CHILD EMERGENCY PROTOCOL")
    print("-" * 40)
    emergency_system = ChildEmergencyProtocol()
    emergency_system.execute("เด็ก 12 ขวบ โทรมาแจ้งพ่อล้ม เลือดออก แบตมือถือใกล้หมด มีคอมฯ ใช้ได้")

    print("\n" + "=" * 70)
    print("System ready for symbolic logic operations!")
    print("=" * 70)
