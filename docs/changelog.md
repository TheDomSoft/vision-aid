# Changelog

## 2025-09-04
- Integrated Google ML Kit real-time object detection:
  - `ObjectDetectionService` wrapper in stream mode.
  - Live camera stream with frame throttling (~8 FPS) and medium resolution.
  - `DetectionPainter` overlay for bounding boxes and labels.
  - Correct camera preview aspect ratio in the UI.
- Fixed `InputImage` creation:
  - Android: NV21; iOS: BGRA8888; rotation from sensor orientation.
- Added UI controls:
  - Detection on/off toggle.
  - FPS overlay.
- Known notes:
  - Emulator may show buffer exhaustion warnings; physical device recommended.
