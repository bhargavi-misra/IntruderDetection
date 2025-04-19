# IntruderDetection
Intruder Detection System using Pose Estimation & OpenCV
This project is a simple yet effective real-time intruder detection system built with Python, OpenCV, and `cvzone`'s Pose Estimation module. When a person is detected, the system sends an SMS alert via Twilio.

Features

- Real-time human detection using webcam
- Pose estimation with `cvzone`
- SMS alert system integrated via Twilio
- Threshold logic to avoid false alarms

Tech Stack

- Python
- OpenCV
- cvzone
- Twilio

How it Works

- The webcam feed is analyzed in real-time.
- If human pose keypoints are detected (using cvzone’s `PoseDetector`), a list counter increases.
- Once a threshold (50 frames) is crossed, the system sends an SMS alert.
- Press `'q'` to quit the app.

Future Improvements

- Add motion detection with OpenCV
- Integrate face recognition for more precision
- Push alerts to a cloud dashboard (Firebase/Flask)
- Record snapshots when detection occurs

For suggestions, collaborations, or improvements — feel free to connect!  
[Your Name] – [Your LinkedIn] – [Your Email]

---

Let me know if you want a `requirements.txt` or `.env` sample too!
