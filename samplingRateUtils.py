import cv2


def get_sampling_rate() -> int:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return 30  # default to 30 if the webcam can't be opened
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return (
        fps if fps > 0 else 30
    )  # default to 30 if the webcam doesn't return a valid FPS
