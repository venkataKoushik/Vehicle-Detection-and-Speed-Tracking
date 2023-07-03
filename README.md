# Vehicle-Detection-and-Speed-Tracking
<h2>Vehicle Detection and Speed Tracking using OpenCV and Dlib libraries.</h2>
<p>we propose a method that detects vehicles and tracks their speed. This method uses OpenCV and dlib libraries to detect and track four-wheeler vehicles in a video, estimate their speed, and save images of over speeding vehicles.</p>
<p>The script first loads a pre-trained Haar cascade classifier for detecting vehicles, and then tracks each vehicle using dlib correlation tracker. The speed of each vehicle is estimated based on the time it takes to travel between markers on the road.</p>
<p>If a vehicle is over speeding, an image of the vehicle is saved along with its speed, date, and time. The script can be used for monitoring traffic speed and identifying over speeding vehicles in a video.
After identifying the over speeding vehicles, the number plate of these vehicles is detected. This report includes a description of the script's functionality, its implementation details, and examples of its usage.</p>

<h2>Work Flow:</h2>

![image](https://github.com/venkataKoushik/Vehicle-Detection-and-Speed-Tracking/assets/123009890/43d1d800-9b58-4d37-8245-de56e063376b)

<h2>Speed Calculation</h2>
<p>To calculate the speed, the function subtracts the start time of the vehicle from the end time to determine the time taken to travel the marked area. This time is then used to calculate the speed by dividing the length of the marked area by the time taken, resulting in meters per second.</p>

![image](https://github.com/venkataKoushik/Vehicle-Detection-and-Speed-Tracking/assets/123009890/3a19e586-9d82-45f4-ae0a-ebe1534fdc2b)![image](https://github.com/venkataKoushik/Vehicle-Detection-and-Speed-Tracking/assets/123009890/128b3d5a-8cf7-4269-ad5d-7eefde6909e7)

In the provided figure, the vehicle is detected at mark1 in the ith frame, and it crosses mark2 in the nth frame. The number of frames between mark1 and mark2 is (n - i). Considering a video running at 60 frames per second (FPS), the time taken for (n - i) frames is calculated as (n - i) / 60 seconds.

Therefore, the time taken between mark1 and mark2 is determined by dividing the difference of frames by the FPS. The velocity is then calculated by dividing the mark gap by the time difference and multiplying by 3.6 to convert it to kilometers per hour.

To convert the speed from meters per second to kilometers per hour, the calculated value is multiplied by 3.6. The final speed is rounded to two decimal places.

The speed calculated by the estimateSpeed function is used to determine if the vehicle is overspeeding or not.



