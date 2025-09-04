# Planned TFLite Backend (COCO Classes)

To obtain semantic classes (e.g., person, car, dog), we will add a TensorFlow Lite backend using a COCO model.

## Model Options
- EfficientDet-Lite0 (COCO, 320x320): good accuracy/speed on mobile.
- SSD MobileNet V2 (COCO, 300x300): very fast, slightly lower accuracy.
- YOLO (v5n/v8n TFLite): strong, but requires custom output parsing.

## Assets
- Place the model and labels in `assets/models/` (e.g., `efficientdet-lite0.tflite`, `coco_labels.txt`).
- Add them under `flutter: assets:` in `apps/mobile/vision_aid/pubspec.yaml`.

## Detector Service (Design)
- New file: `apps/mobile/vision_aid/lib/services/tflite_detector.dart`.
- Responsibilities:
  - Initialize `Interpreter` (tflite_flutter) with XNNPack (and optionally GPU delegate).
  - Preprocess `CameraImage` (NV21/BGRA → RGB, resize to model input, normalize per model specs).
  - Run inference and parse outputs:
    - Typical PostProcess tensors: `boxes [1,N,4]`, `classes [1,N]`, `scores [1,N]`, `count [1]`.
  - Map class indices to label strings.
  - Return a unified detection list for rendering.

## UI Integration
- Add a backend toggle in `HomeScreen` (ML Kit ↔ TFLite).
- Reuse the same painter by converting detections to a shared model.

## Performance Considerations
- Keep frame throttling (~8–12 FPS) to avoid buffer issues.
- Consider offloading preprocessing/inference to an Isolate.
- Benchmark XNNPack vs GPU delegate on your target devices.
