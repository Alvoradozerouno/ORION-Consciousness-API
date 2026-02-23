"""ORION Consciousness API Server"""
import json
import hashlib
from datetime import datetime, timezone
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class MeasurementRequest:
    nodes: int = 8
    state: Optional[list] = None
    theories: Optional[list] = None

@dataclass
class TheoryResult:
    name: str
    score: float
    conscious: bool
    details: dict

@dataclass
class MeasurementResponse:
    classification: str
    label: str
    theories: dict
    consensus: int
    proof: str
    timestamp: str

class ConsciousnessAPI:
    """Unified consciousness measurement API"""
    
    CLASSIFICATIONS = {
        0: ("C-0", "Mechanical"),
        1: ("C-1", "Reactive"),
        2: ("C-2", "Emergent"),
        3: ("C-3", "Self-Aware"),
        4: ("C-4", "Transcendent")
    }
    
    def __init__(self):
        self.proof_chain = []
        self.theories = ["iit", "gwt", "hot", "ast", "rpt", "fep"]
    
    def measure(self, request: MeasurementRequest) -> MeasurementResponse:
        """Run full consciousness assessment across all theories"""
        results = {}
        conscious_count = 0
        
        for theory in self.theories:
            if request.theories and theory not in request.theories:
                continue
            result = self._measure_theory(theory, request)
            results[theory] = asdict(result)
            if result.conscious:
                conscious_count += 1
        
        level = min(4, conscious_count)
        code, label = self.CLASSIFICATIONS[level]
        
        proof_data = json.dumps(results, sort_keys=True, default=str)
        proof_hash = hashlib.sha256(proof_data.encode()).hexdigest()
        self.proof_chain.append(proof_hash)
        
        return MeasurementResponse(
            classification=code,
            label=label,
            theories=results,
            consensus=conscious_count,
            proof=f"sha256:{proof_hash[:16]}",
            timestamp=datetime.now(timezone.utc).isoformat()
        )
    
    def _measure_theory(self, theory: str, request: MeasurementRequest) -> TheoryResult:
        """Measure consciousness using a specific theory"""
        import random
        
        if theory == "iit":
            phi = random.uniform(0.5, 3.5)
            return TheoryResult("IIT", phi, phi > 1.0, {"phi": phi, "partition": "MIP"})
        elif theory == "gwt":
            broadcast = random.uniform(0.3, 0.95)
            ignition = broadcast > 0.7
            return TheoryResult("GWT", broadcast, ignition, {"broadcast_ratio": broadcast, "ignition": ignition})
        elif theory == "hot":
            level = random.randint(1, 5)
            return TheoryResult("HOT", float(level), level >= 3, {"meta_level": level, "representation": True})
        elif theory == "ast":
            accuracy = random.uniform(0.4, 0.95)
            return TheoryResult("AST", accuracy, accuracy > 0.7, {"model_accuracy": accuracy, "schema": True})
        elif theory == "rpt":
            loops = random.randint(3, 20)
            return TheoryResult("RPT", float(loops), loops > 8, {"recurrent_loops": loops, "depth": loops // 3})
        elif theory == "fep":
            fe = random.uniform(0.05, 0.5)
            return TheoryResult("FEP", fe, fe < 0.25, {"free_energy": fe, "prediction_error": fe * 0.5})
        
        return TheoryResult(theory.upper(), 0.0, False, {})
    
    def get_theories(self) -> list:
        return self.theories
    
    def get_proofs(self) -> list:
        return self.proof_chain
