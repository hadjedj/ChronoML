import pandas as pd
from termcolor import colored

def print_section(title):
    print(colored(f"\n{'='*40}\n{title}\n{'='*40}", 'cyan', attrs=['bold']))

class WatchDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self._df = None
    
    def load_data(self):
        print_section("🚀 Chargement des données")
        self.df = pd.read_csv(self.file_path, low_memory=False)
    
    def clean_data(self):
        print_section("🧹 Nettoyage des données")
        self.df.drop(columns=["Unnamed: 0", "condition"], inplace=True, errors='ignore')
        
        self.df["price"] = self.df["price"].replace("Price on request", None)
        self.df.loc[:, "price"] = self.df["price"].fillna(self.df["price"].median())
        self.df["price"].fillna(self.df["price"].median(), inplace=True)
        
        self.df["yop"] = pd.to_numeric(self.df["yop"], errors="coerce")
        self.df["size"] = self.df["size"].str.extract(r"(\d+)").astype(float)
        
        self.df = self.df[(self.df["size"] >= 20) & (self.df["size"] <= 60)]
    
    def get_data(self):
        return self.df
    
    def show_summary(self):
        print_section("📊 Aperçu des données après nettoyage")
        print(self.df.info())
        print(self.df.head())
