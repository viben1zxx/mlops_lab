import mlflow
import os

# Create a dummy model directory if it doesn't exist
os.makedirs("models", exist_ok=True)

with mlflow.start_run():
    # Log the parameters used for this training run
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("batch_size", 32)
    
    # Simulate training a model and getting an accuracy score
    simulated_f1_score = 0.95
    mlflow.log_metric("f1_score", simulated_f1_score)
    
    # Save a dummy model file to satisfy DVC
    with open("models/model.pkl", "w") as f:
        f.write("dummy_model_data")
        
    print(f"Training complete. F1 Score: {simulated_f1_score}")
