# A set of agents for environment debugging purposes only.
from msg import Action, Agent
 

class ForwardAgent(Agent):
    def __init__(self):
        super(ForwardAgent, self).__init__("[Debug] Forward-Only Agent")
    
    def action(self, _) -> int:
        return Action.FORWARD.value
