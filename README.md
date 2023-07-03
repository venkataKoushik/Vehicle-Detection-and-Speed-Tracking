# Vehicle-Detection-and-Speed-Tracking
<h2>Vehicle Detection and Speed Tracking using OpenCV and Dlib libraries.</h2>
<p>we propose a method that detects vehicles and tracks their speed. This method uses OpenCV and dlib libraries to detect and track four-wheeler vehicles in a video, estimate their speed, and save images of over speeding vehicles.</p>
<p>The script first loads a pre-trained Haar cascade classifier for detecting vehicles, and then tracks each vehicle using dlib correlation tracker. The speed of each vehicle is estimated based on the time it takes to travel between markers on the road.</p>
<p>If a vehicle is over speeding, an image of the vehicle is saved along with its speed, date, and time. The script can be used for monitoring traffic speed and identifying over speeding vehicles in a video.
After identifying the over speeding vehicles, the number plate of these vehicles is detected. This report includes a description of the script's functionality, its implementation details, and examples of its usage.</p>

<h2>Work Flow:</h2>

![Uploading image.png…]()



