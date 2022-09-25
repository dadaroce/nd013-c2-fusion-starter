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

# Writeup: Track 3D-Objects Over Time

Please use this starter template to answer the following questions:

### 1. Write a short recap of the four tracking steps and what you implemented there (filter, track management, association, camera fusion). Which results did you achieve? Which part of the project was most difficult for you to complete, and why?


### 2. Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)? 


### 3. Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?


### 4. Can you think of ways to improve your tracking results in the future?

