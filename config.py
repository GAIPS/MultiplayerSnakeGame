from agents.debug_agent import ForwardAgent
from agents.random_agent import RandomAgent, LessDumbRandomAgent
from agents.algorithm_agent import AStarNearest

scenarios = {
    "randoms": {
        "output": "randoms.json",
        "agents": [
            LessDumbRandomAgent(),
            LessDumbRandomAgent()
        ],
        "grid": (10, 10),
    },
    "basic1": {
        "output": "basic1.json",
        "agents": [
            LessDumbRandomAgent(),
            AStarNearest()
        ],
        "grid": (10, 10),
    },
}
