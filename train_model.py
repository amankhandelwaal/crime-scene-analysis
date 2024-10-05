import torch
from ultralytics import YOLO

def train_yolo_model(model_path, data_config, epochs, batch_size, image_size, device, project_name, experiment_name, continue_training=False):
    """
    Train YOLO model with specified parameters.

    Args:
        model_path (str): Path to the pre-trained model.
        data_config (str): Path to the dataset configuration file.
        epochs (int): Number of epochs for training.
        batch_size (int): Batch size for training.
        image_size (int): Image size for training.
        device (str): Device to use for training (e.g., '0' for GPU).
        project_name (str): Directory for saving results.
        experiment_name (str): Name for the current experiment.
        continue_training (bool): Flag to resume training or start fresh.
    """
    model = YOLO(model_path)

    model.train(
        data=data_config,
        epochs=epochs,
        batch=batch_size,
        imgsz=image_size,
        device=device,
        project=project_name,
        name=experiment_name,
        resume=continue_training  
    )

if __name__ == "__main__":
 
    
    if torch.cuda.is_available():
        print("Training on GPU")
        device = '0'
    else:
        print("Training on CPU")
        device = 'cpu'

    
    model_path = r'C:\Users\amank\projects\crime-scene-analysis\runs\train\fine_tune_pistol_extended\weights\best.pt'  
    data_config = 'data/vandalism/data.yaml'  
    epochs = 100 
    batch_size = 16  
    image_size = 640 
    project_name = 'runs/train'  
    experiment_name = 'fine_tune_vandalism'  
    continue_training = False  

  
    train_yolo_model(
        model_path=model_path,
        data_config=data_config,
        epochs=epochs,
        batch_size=batch_size,
        image_size=image_size,
        device=device,
        project_name=project_name,
        experiment_name=experiment_name,
        continue_training=continue_training
    )
