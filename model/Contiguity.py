from dataclasses import dataclass

@dataclass
class Contiguity:
    dyad :int
    state1no: int
    state1ab: str
    state2no: int
    state2ab: str
    year: int
    conttype: int
    version: float

    def __hash__(self):
        return hash(f"{self.state1no}, {self.state2no}, {self.year}")

    def __str__(self):
        return f"Lo stato {self.state1ab} confina con {self.state2ab}"