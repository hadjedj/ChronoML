import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.watch_analysis import WatchAnalysis


if __name__ == "__main__":
    analysis = WatchAnalysis("data/Watches.csv")
    analysis.run()
