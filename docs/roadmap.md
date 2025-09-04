# Roadmap

## Short Term
- Add COCO TFLite model (EfficientDet-Lite0 or SSD MobileNet V2) and labels to assets.
- Implement `TFLiteDetector` service with preprocessing and output parsing.
- UI toggle for backend selection (ML Kit ↔ TFLite).
- Unify detection model and painter to work with both backends.

## Medium Term
- Performance optimization for TFLite path (Isolate, delegates, throttling).
- Front/back camera switching and mirroring fixes for front camera.
- Improve error handling and user feedback.

## Long Term
- Expand to additional CV tasks (OCR, segmentation, landmarks) as modules.
- Build a sample “Experience” layer on top of detections for user tasks.
- Add automated tests and benchmarking harnesses.
