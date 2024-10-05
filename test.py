from ultralytics import YOLO

def test_model(model_path, data_config, img_dir, save_dir):
    model = YOLO(model_path)
    
    
    results = model.predict(
        source=img_dir,  
        conf=0.5,  
        save=True,  
        save_dir=save_dir, 
        project='runs/test', 
        name='vandalism_test'  
    )
    return results


model_path = r'runs\train\fine_tune_vandalism3\weights\best.pt'  
img_dir = r'data\vandalism\test\images'  
save_dir = r'runs\test\vandalism_test'
data_config = r'data/vandalism/data.yaml'  


test_model(model_path, data_config, img_dir, save_dir)
