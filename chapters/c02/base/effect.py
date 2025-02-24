


class Effect:
    def __init__(self, name, old_value, new_value, timestamp, agent):
        self.agent = agent
        self.name = name
        self.old_value = old_value
        self.new_value = new_value
        self.timestamp = timestamp

    def __repr__(self):
        return f"Effect(name={self.name}, old_value={self.old_value}, new_value={self.new_value}, timestamp={self.timestamp})"
    
    def get_state(self) -> dict[str, any]:
        return { self.name : self.new_value }
    
    def revert_state(self) -> dict[str, any]:
        return { self.name : self.old_value }