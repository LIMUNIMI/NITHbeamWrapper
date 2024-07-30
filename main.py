from eyeware.client import TrackerClient
import time
import nithFunctions

tracker = TrackerClient()


def print_default_data(head_pose, head_is_lost, screen_gaze, screen_gaze_is_lost):
    print("  * Head Pose:")
    print("      - Lost track:       ", head_is_lost)
    if not head_is_lost:
        print("      - Session ID:       ", head_pose.track_session_uid)
        rot = head_pose.transform.rotation
        print(
            "      - Rotation:          |%5.3f %5.3f %5.3f|"
            % (rot[0, 0], rot[0, 1], rot[0, 2])
        )
        print(
            "                           |%5.3f %5.3f %5.3f|"
            % (rot[1, 0], rot[1, 1], rot[1, 2])
        )
        print(
            "                           |%5.3f %5.3f %5.3f|"
            % (rot[2, 0], rot[2, 1], rot[2, 2])
        )
        tr = head_pose.transform.translation
        print(
            "      - Translation:       <x=%5.3f m, y=%5.3f m, z=%5.3f m>"
            % (tr[0], tr[1], tr[2])
        )

    print("  * Gaze on Screen:")
    print("      - Lost track:       ", screen_gaze_is_lost)
    if not screen_gaze_is_lost:
        print("      - Screen ID:        ", screen_gaze.screen_id)
        print(
            "      - Coordinates:       <x=%5.3f px,   y=%5.3f px>"
            % (screen_gaze.x, screen_gaze.y)
        )
        print("      - Confidence:       ", screen_gaze.confidence)


while True:
    # Make sure that the connection with the tracker server (Eyeware application) is up and running.
    if tracker.connected:

        # Extract stuff
        head_pose = tracker.get_head_pose_info()
        head_is_lost = head_pose.is_lost
        screen_gaze = tracker.get_screen_gaze_info()
        screen_gaze_is_lost = screen_gaze.is_lost
        rot = head_pose.transform.rotation

        # Print basic data?
        # print_default_data(head_pose, head_is_lost, screen_gaze, screen_gaze_is_lost)

        if not head_is_lost:
            head_pos_pitch, head_pos_yaw, head_pos_roll = (
                rot[0, 0],
                rot[0, 1],
                rot[0, 2],
            )
            head_presence = True
        else:
            head_pos_pitch, head_pos_yaw, head_pos_roll = (0, 0, 0)
            head_presence = False

        if not screen_gaze_is_lost:
            gaze_presence = True
        else:
            gaze_presence = False

        nithFunctions.send_data(
            head_pos_pitch,
            head_pos_yaw,
            head_pos_roll,
            screen_gaze.x,
            screen_gaze.y,
            head_presence,
            gaze_presence,
            verbose=True,
        )

        time.sleep(1 / 30)  # Based on the assumption that tracking data comes at 30 Hz
    else:
        # Print a message every MESSAGE_PERIOD_IN_SECONDS seconds
        MESSAGE_PERIOD_IN_SECONDS = 2
        time.sleep(
            MESSAGE_PERIOD_IN_SECONDS - time.monotonic() % MESSAGE_PERIOD_IN_SECONDS
        )
        print("No connection with tracker server")
