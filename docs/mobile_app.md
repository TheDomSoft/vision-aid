# Mobile App: Real-Time Detection Pipeline

This page describes how the Flutter app acquires camera frames, runs detection, and renders overlays.

## Camera and Preview
- File: `apps/mobile/vision_aid/lib/screens/home_screen.dart`
- Uses `camera` plugin with:
  - `ResolutionPreset.medium` for a balanced FPS/quality.
  - Image format:
    - Android: `ImageFormatGroup.nv21`
    - iOS: `ImageFormatGroup.bgra8888`
- Aspect ratio handling:
  - Uses `AspectRatio` based on `CameraController.value.aspectRatio`.
  - In portrait UI, we invert the camera AR to avoid stretching.

## Frame Streaming and Throttling
- Frames arrive via `startImageStream` callback.
- We throttle processing to ~8 FPS (`_analysisIntervalMs ~ 120 ms`) to avoid buffer exhaustion.
- The pipeline updates an FPS indicator for runtime monitoring.

## Image Conversion for ML Kit
- We assemble bytes from `CameraImage` planes and build `InputImage.fromBytes` with `InputImageMetadata`:
  - `format`: NV21 (Android) or BGRA8888 (iOS)
  - `rotation`: derived from the camera sensor orientation
  - `size`: camera image width/height
- This configuration follows ML Kit recommendations and is essential for correct processing.

## Detection Service
- File: `apps/mobile/vision_aid/lib/services/object_detection_service.dart`
- Wraps `ObjectDetector` with `DetectionMode.stream`, `classifyObjects`, and `multipleObjects` enabled.
- Exposes `init`, `detect`, and `dispose`.

## Overlay Rendering
- File: `apps/mobile/vision_aid/lib/widgets/detection_painter.dart`
- Draws bounding boxes scaled from ML Kit image space to the preview canvas.
- Renders first label (if any) at the top-left corner of the box.

## UI Controls
- Detection toggle button (start/stop) in the bottom-right corner.
- Debug badges (top): detection count and FPS.

## Performance Tips
- Prefer a physical device for testing. Emulator camera feeds are often low-contrast and low-FPS.
- Consider reducing the resolution further if you see buffer exhaustion or jank.
- If you add a TFLite backend, consider moving preprocessing and inference to an Isolate.
