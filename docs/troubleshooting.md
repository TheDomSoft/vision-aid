# Troubleshooting

## No detections on emulator
- Emulators often have poor/low-contrast feeds. Test on a physical device.
- Ensure the camera permission is granted.

## Buffer exhaustion warnings
- Symptoms: `Unable to acquire a buffer item...`, `Pipeline is reset`.
- Mitigations:
  - Use `ResolutionPreset.medium` (or lower) for the camera.
  - Throttle analysis (e.g., ~8 FPS).
  - Avoid heavy work on the UI thread; use Isolates for TFLite where necessary.

## Boxes misaligned with preview
- Verify the preview aspect ratio.
- Ensure `InputImageMetadata.size` matches the camera image and rotation is set correctly.
- Our painter scales from the detector image-space to the canvas; mismatches typically mean an AR or rotation issue.

## Performance is low
- Lower camera resolution, or increase throttle interval.
- Prefer physical device testing.
- Consider enabling a GPU delegate for TFLite models.
