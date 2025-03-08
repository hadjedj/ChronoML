from src.watch_data_processor import WatchDataProcessor
from src.visualizer import Visualizer
from src.watch_data_processor import print_section


class WatchAnalysis:
    def __init__(self, file_path):
        self.processor = WatchDataProcessor(file_path)
    
    def run(self):
        self.processor.load_data()
        self.processor.clean_data()
        self.processor.show_summary()
        
        visualizer = Visualizer(self.processor.get_data())
        print_section("📈 Analyse exploratoire des données")
        visualizer.plot_price_distribution()
        visualizer.plot_top_brands()
        visualizer.plot_size_vs_price()
        print_section("✅ Analyse terminée !")
