import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

DATA_DIR = "data"
DELIVERIES_FILE = os.path.join(DATA_DIR, "deliveries.csv")
OUTPUT_FILE = os.path.join(DATA_DIR, "deliveries_clustered.csv")
OUTPUT_IMG = os.path.join("docs", "outputs", "clusters.png")

os.makedirs(os.path.dirname(OUTPUT_IMG), exist_ok=True)

def load_deliveries(file_path=DELIVERIES_FILE):
    return pd.read_csv(file_path)

def cluster_deliveries(data, k=3):
    coords = data[['x', 'y']]
    kmeans = KMeans(n_clusters=k, random_state=0)
    data['cluster'] = kmeans.fit_predict(coords)
    return data, kmeans.cluster_centers_

def save_results(data, centers, csv_path=OUTPUT_FILE, img_path=OUTPUT_IMG):
    data.to_csv(csv_path, index=False)
    plt.figure(figsize=(8, 6))
    plt.scatter(data['x'], data['y'], c=data['cluster'], cmap='viridis', s=50, alpha=0.6)
    plt.scatter(centers[:,0], centers[:,1], c='red', s=200, marker='X', label='Centros')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Clusters de Entregas')
    plt.legend()
    plt.savefig(img_path)
    plt.close()

def main():
    deliveries = load_deliveries()
    clustered_data, centers = cluster_deliveries(deliveries, k=3)
    save_results(clustered_data, centers)
    print(f"Clustering concluído! Resultados salvos em {OUTPUT_FILE} e {OUTPUT_IMG}")

if __name__ == "__main__":
    main()