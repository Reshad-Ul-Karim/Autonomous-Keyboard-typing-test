import torch
from ultralytics import YOLO  # Import your YOLO library

# Check if MPS is available and set it as the device
device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
print(f"Using device: {device}")

# Load the YOLO model
model = YOLO("yolov8n.pt")  # Load your YOLO model

# Train the model and specify the device
model.train(data="merged_dataset2/merged_dataset.yaml", epochs=50, imgsz=640, device=device)

# Save the trained model
model.save("trained_yolov8n_model.pt")  # Save the model to a specified file path
