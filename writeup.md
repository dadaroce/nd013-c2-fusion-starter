# Writeup: MidTerm Project

Notes:

- The top view show us that the Udacity Car is located on an interception where we could easily identify multiple vehicles around us
- The glasses cannot be identified, because the point cloud "passes through" them \
![Glass](https://user-images.githubusercontent.com/39452483/192159164-2968a083-4fca-406c-b433-dfc90aba9637.png)
- We could identify different kind of vehicles due to the physical shapes, just like SUVs an other \
![SUV](https://user-images.githubusercontent.com/39452483/192159129-29b88ac7-8090-4c36-9145-f647a339bf20.png)
- The occlusion caused by the surrounding vehicles limits the area of vision we have \
![occlusion](https://user-images.githubusercontent.com/39452483/192159221-b1a41c07-7b6f-42d2-a91c-c48b64667592.png)
- Vehicles located in front of our car, only the bumper and minimum characteristics of the rear part of the car can be identified \

| Ex 1      | Ex 2 |
| ----------- | ----------- |
| ![image](https://user-images.githubusercontent.com/39452483/192159342-14f941e9-7a4d-4e6c-aac7-870e8ab4e955.png)|![image](https://user-images.githubusercontent.com/39452483/192159398-9427bf20-2f26-4cd5-8d7f-e176f2feef47.png) |

- The head and tail lights, license plates, grille, and side mirrors as stable features for a vehicle \
- Finally, as we could expect, the wheels are clearly showed on the data

Steps to achieve: 

- Compute Lidar Point-Cloud from Range Image
- Create Birds-Eye View from Lidar PCL
- Model-based Object Detection in BEV Image
- Performance Evaluation for Object Detection

## Compute Lidar Point-Cloud from Range Image

The LIDAR data provided is transformed into a numpy array in order to convert to an image and being displayed. An important characteristic is that the negative data indicate that the range doesn't have a real return, so this data should be removed.

![lidar_to_numpy](https://user-images.githubusercontent.com/39452483/192158090-c6e444b0-3df7-419b-a66c-e25952dc377d.png)

Visualize pointcloud from the LIDAR data using open3D
![top_view](https://user-images.githubusercontent.com/39452483/192158276-738abad4-face-4696-8b1e-0593d75c4774.png)

Also, the user is able to zoom, drag, etc.. the current image
![zoom](https://user-images.githubusercontent.com/39452483/192158327-5962b893-434e-4d98-ae57-ee0fcf610e57.png)

![pull](https://user-images.githubusercontent.com/39452483/192159542-33dd83ed-0052-4084-b838-b44dec747b1c.png)

##  Create Birds-Eye View from Lidar PCL

Image below show the intensity and height channel of the BEV map

| Height      | Intensity |
| ----------- | ----------- |
|![heigjt](https://user-images.githubusercontent.com/39452483/192158631-13ac3407-5b6d-4a8e-b44b-b611ac7ffac4.png)|![intensity](https://user-images.githubusercontent.com/39452483/192158633-db543720-605e-4c17-b9b9-63f7997bc500.png)|



## Model-based Object Detection in BEV Image

3D Boxes and card detected by the BEV view.

![screenshoot](https://user-images.githubusercontent.com/39452483/192158737-c09a1a03-912b-4409-8010-c5a097e03656.png)



## Performance Evaluation for Object Detection

![image](https://user-images.githubusercontent.com/39452483/192159633-29a39c80-3428-4cc9-b5b9-c9b9905bb0fe.png)

![image](https://user-images.githubusercontent.com/39452483/192159798-1a151fad-5c46-4a93-94a1-d845415af050.png)

# Writeup: Track 3D-Objects Over Time Final_Project

### 1. Write a short recap of the four tracking steps and what you implemented there (filter, track management, association, camera fusion). Which results did you achieve? Which part of the project was most difficult for you to complete, and why?

### EKF Implementation

In this step a Kalman Filter is implemented in order to track a single target using the data prvided by a LIDAR over the time.

The RMSE and a Video about this step could be found: 

![rmse](https://user-images.githubusercontent.com/39452483/192173178-e8b99623-84c3-4b39-b343-2ea36f516f5d.png)

<p align="center">
    <video width="560" height="315" src="https://user-images.githubusercontent.com/39452483/192173180-efb3dc31-e8c0-4a10-a5e2-288089c9628e.mp4" autoplay="1" loop="1"></video>
</p>

### Track Management Implementation

The second step main focus is the implementaton of a track management module in charge f initialize and delete tracks, set the current `track.state` and a `track.score`.

The RMSE and a Video about this step could be found: 

![Figure_2](https://user-images.githubusercontent.com/39452483/192173444-20e2803c-7ce2-4842-9b42-20374ae4f45c.png)


<p align="center">
    <video width="560" height="315" src="https://user-images.githubusercontent.com/39452483/192173445-0b5495f5-4027-4f5f-bc12-14990846659f.mp4" autoplay="1" loop="1"></video>
</p>

### Association Module 

On the third step of this project an enhanced in the track algorithm is performed in order to apply and nearest association algorithm to multiple targets. This module is based on `Mahalanobis distances`. 

The RMSE and a Video about this step could be found: 


![Figure_2](https://user-images.githubusercontent.com/39452483/192173670-2df15b8e-9cbf-4e4e-ab9a-6fe3f5fa57f0.png)

<p align="center">
    <video width="560" height="315" src="https://user-images.githubusercontent.com/39452483/192173671-f39a40c1-9388-4e5a-bcc8-31764f142027.mp4" autoplay="1" loop="1"></video>
</p>

### Sensor Fusion

A nonlinear camera measurement model was implement in order to increase the performance of our current LIDAR-Only model.


![Figure_2](https://user-images.githubusercontent.com/39452483/192173771-0a4e1fab-6e2a-434d-932a-65ac066deb9b.png)

> I have some codecs issues. So, I generated the .avi file from the .png images using `ffmpeg -framerate 6 -pattern_type glob -i '*.png' -c:v ffv1 out.avi` and convert this file to a .mp4 in order to attach it here. 


<p align="center">
    <video width="560" height="315" src="https://user-images.githubusercontent.com/39452483/192173874-2bf693b1-9f8d-41c1-aa3e-21eed87bd77a.mp4" autoplay="1" loop="1"></video>
</p>


I think the project has a proper workflow, it is easy to follow. One important thing to note, is that I am not yet so familiar with some operations using numpy, as in certain steps there may be more optimized ways to solve it.

### 2. Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)? 

Once the camera was integrated into our algorithm, the RMSE drops a little. Although it is not that significant a result, since in my results the improvement over using only LIDAR was not that great.

On the other hand, we do notice an improvement in the number of "possible false detections".

### 3. Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?

In a real scenario, the number of objects to be identified and tracked are many more, there are pedestrians and other types of vehicles which results in the need for more redundant and information-rich sensing systems. 

### 4. Can you think of ways to improve your tracking results in the future?

As I said before, I suppose that some parts of the code can be optimized with other functions, reducing its execution time. Also, taking more into account and making an accurate calibration to the different sensors, will result in better data.