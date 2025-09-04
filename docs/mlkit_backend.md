# ML Kit Backend (On-Device Object Detection)

This backend uses `google_mlkit_object_detection` for real-time object detection and tracking.

## Why ML Kit (Initial Choice)
- Zero model bundling required; uses Google’s on-device model out of the box.
- Straightforward integration in Flutter.
- Good baseline to verify the camera pipeline and overlays.

## Implementation
- Detector service: `apps/mobile/vision_aid/lib/services/object_detection_service.dart`
  - `ObjectDetectorOptions` with `DetectionMode.stream`, `classifyObjects: true`, `multipleObjects: true`.
  - Methods: `init()`, `detect(InputImage)`, `dispose()`.
- Frame handling: `apps/mobile/vision_aid/lib/screens/home_screen.dart`
  - Convert `CameraImage` to `InputImage.fromBytes` with `InputImageMetadata`.
  - Rotation: `InputImageRotationValue.fromRawValue(sensorOrientation)`.
  - Formats: NV21 (Android) / BGRA8888 (iOS).
  - Throttle to ~8 FPS.

## Output and Overlay
- ML Kit returns `DetectedObject` with `boundingBox` and coarse label categories (e.g., Home goods, Food).
- We draw boxes and the first label (if present) via `DetectionPainter`.

## Known Limitations
- Category labels are coarse and not COCO semantic classes.
- Emulator may not trigger detections due to feed quality.

## Next Step
- Add an alternative backend using TensorFlow Lite to get COCO classes.
