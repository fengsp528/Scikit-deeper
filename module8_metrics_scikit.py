import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of points (N): "))
    
    x_values = np.zeros(N, dtype=int)
    y_values = np.zeros(N, dtype=int)
    
    for i in range(N):
        x = int(input(f"Enter x value (ground truth) for point {i+1} (0 or 1): "))
        y = int(input(f"Enter y value (predicted class) for point {i+1} (0 or 1): "))
        x_values[i] = x
        y_values[i] = y
    
    precision = precision_score(x_values, y_values)
    recall = recall_score(x_values, y_values)
    
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()