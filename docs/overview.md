# Vision Aid Overview

Vision Aid is a mobile-first project focused on real-time computer vision assistance. The current milestone delivers on-device object detection with a clean preview and overlays. The codebase is organized to allow swapping detection backends (Google ML Kit vs TensorFlow Lite) and to scale documentation and features as the project grows.

## Goals
- Real-time object detection on-device with stable FPS.
- Correct camera preview aspect ratio and accurate overlay coordinates.
- Swap-in alternative models/backends when needed (e.g., COCO class names).

## Current Status
- Live camera object detection works using Google ML Kit’s on-device Object Detection and Tracking.
- Bounding boxes and labels are drawn over the preview.
- Frame throttling and medium camera resolution are in place to keep the pipeline responsive.
- UI controls added to toggle detection and show FPS.

## Key Components
- `apps/mobile/vision_aid/lib/screens/home_screen.dart`
  - Camera initialization and live preview.
  - Frame streaming and conversion to ML Kit `InputImage` with correct format and rotation.
  - Overlay stack (preview + painter + debug badges + UI controls).
- `apps/mobile/vision_aid/lib/services/object_detection_service.dart`
  - Thin service around ML Kit `ObjectDetector` in stream mode.
- `apps/mobile/vision_aid/lib/widgets/detection_painter.dart`
  - Draws bounding boxes and labels with proper coordinate scaling.

## How to Run (Mobile App)
- Requirements: Flutter SDK ≥ 3.9.0, Android SDK, a physical device recommended.
- From `apps/mobile/vision_aid/`:
  1. `flutter pub get`
  2. `flutter run -d <device_id>`
- Notes:
  - Emulator feeds can be low-quality and may not trigger detections reliably. A physical device is recommended.
  - Android minSdkVersion should be ≥ 21. Ensure camera permissions are allowed.

## Next Milestone
- Add a TensorFlow Lite backend with a COCO model (e.g., EfficientDet-Lite0) to get semantic classes (person, car, dog, etc.).
- Provide a UI switch to toggle between ML Kit and TFLite backends.
