# Mask-and-Temperature-detector
This project is made to avoid customers/people who are not wearing mask. The system checks people for mask and temperature at the entrance before opening the door.   

Using Python and Machine Learning the program is able to distinguish between people wearing mask and people not wearing mask. 

Raspberry Pi 4 B is used as the CPU that runs this python program. It is connected with Pi camera for video capture, temperature sensor, servo motor that acts as a gate and LEDs to indicate mask status.

For Training the ML model I am using MobileNetV2 which is a very small and efficient CNN. You can learn about MobileNetV2 from this link- https://towardsdatascience.com/review-mobilenetv2-light-weight-model-image-classification-8febb490e61c


**Algorithm**
1. Person places their hand near the IR sensor
2. When hand is close enough Temp sensor will check their body temp
3. Simultaneously the camera detects mask on their face
4. The gate opens only if their body temp within limits and wearing mask
5. For all other cases gate doesn't open execpt [4] 

**Circuit Diagram**
![circuit](https://github.com/MahmoudDaasan/Mask-and-Temperature-detector-main/assets/117162454/866db9ef-5ddc-4500-b475-9fad07242873)


**Real-Life Representation**
Here is the real-life project image made by me.
![WhatsApp Image 2022-01-12 at 12 08 42 AM](https://github.com/MahmoudDaasan/Mask-and-Temperature-detector-main/assets/117162454/c85716f5-ebfd-4db9-bbb5-1f0cd5b46396)


**Live working Demo**
https://www.youtube.com/watch?v=enurVth-rzc


