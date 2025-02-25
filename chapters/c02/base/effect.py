import datetime


class Effect:
    def __init__(self, agent, name, key, new_value, old_value=None, timestamp=None):
        self.agent = agent
        self.name = name
        self.key = key
        self.old_value = old_value
        self.new_value = new_value
        self.timestamp = timestamp if timestamp is not None else datetime.now()

    def __repr__(self):
        return f"Effect(name={self.name}, key={self.key}, old_value={self.old_value}, new_value={self.new_value}, timestamp={self.timestamp})"
    
    def get_state(self) -> dict[str, any]:
        return { self.key : self.new_value }
    
    def revert_state(self) -> dict[str, any]:
        return { self.key : self.old_value }