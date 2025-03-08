import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, df):
        self.df = df
    
    def plot_price_distribution(self):
        plt.figure(figsize=(10,5))
        sns.histplot(self.df["price"], bins=50, kde=True)
        plt.title("Distribution des prix des montres")
        plt.xlabel("Prix ($)")
        plt.ylabel("Nombre de montres")
        plt.savefig("outputs/distribution_des_prix.png")
        plt.close()
    
    def plot_top_brands(self):
        top_brands = self.df["brand"].value_counts().head(10)
        plt.figure(figsize=(12,6))
        sns.barplot(x=top_brands.index, y=top_brands.values)
        plt.xticks(rotation=45)
        plt.title("Top 10 des marques les plus présentes")
        plt.xlabel("Marque")
        plt.ylabel("Nombre de montres")
        plt.savefig("outputs/top_brands.png")
        plt.close()
    
    def plot_size_vs_price(self):
        plt.figure(figsize=(10,5))
        sns.scatterplot(x=self.df["size"], y=self.df["price"], alpha=0.5)
        plt.title("Relation entre la taille et le prix des montres (données filtrées)")
        plt.xlabel("Taille (mm)")
        plt.ylabel("Prix ($)")
        plt.savefig("outputs/relation_taille_prix_filtre.png")
        plt.close()
