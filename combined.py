from ultralytics import YOLO


model = YOLO(r'C:\Users\amank\projects\crime-scene-analysis\runs\train\fine_tune_pistol_extended\weights\best.pt')


results = model(r'C:\Users\amank\projects\crime-scene-analysis\images (1).jpeg', save=True, conf=0.25)



for result in results:
    result.plot()  
