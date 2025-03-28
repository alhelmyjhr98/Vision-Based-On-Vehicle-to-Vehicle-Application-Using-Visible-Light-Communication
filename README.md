# Vision-Based On-Vehicle-to-Vehicle Application Using Visible Light Communication

## Project Description
This project aims to develop a **Vision System Prototype** using a **Raspberry Pi 3** with a **NoIR Camera** as an image sensor and an **LCD display** as an output. The system detects and tracks the **tail lights of front vehicles**, estimates the **distance between vehicles**, and displays this information on the **LCD screen**.

The project leverages **OpenCV** for image processing, with the **HSV algorithm** used to filter and isolate the red intensity of tail lights. The estimated distance is calculated using a predefined equation. Additionally, data transmission is implemented using **On-Off Keying (OOK) Modulation**, enabling communication between vehicles through **Visible Light Communication (VLC)**.

This prototype is designed to enhance road safety by providing **real-time distance estimation** and warnings, reducing the risk of rear-end collisions.

## Project Objectives
1. **Vision System Development:** Detect and track the **tail light of front vehicles** using the **HSV algorithm** to isolate red color intensity.
2. **Distance Estimation & Display:** Compute and **display the distance** between the front and back vehicles on the **Raspberry Pi LCD**.
3. **Visible Light Communication (VLC):** Implement **data transmission** between vehicles using **On-Off Keying (OOK) Modulation** to communicate distance information through visible light signals.

## Features
- **Real-time tail light detection** using OpenCV
- **Distance estimation based on image processing**
- **Live output on Raspberry Pi LCD display**
- **VLC-based data transmission** with On-Off Keying

## Hardware & Software Requirements
### Hardware:
- Raspberry Pi 3
- Raspberry Pi NoIR Camera
- LCD Display
- LED/Laser for VLC transmission
- LDR (Light Dependent Resistor) for VLC reception

### Software:
- Python 3
- OpenCV (Computer Vision Library)
- NumPy
- RPi.GPIO Library (for Raspberry Pi GPIO control)

## Installation & Setup
1. **Install Required Libraries**
   ```sh
   sudo apt update
   sudo apt install python3-opencv
   pip install numpy RPi.GPIO
   ```
2. **Run the Transmitter Module:**
   ```sh
   python3 transmitter.py
   ```
3. **Run the Receiver Module:**
   ```sh
   python3 receiver.py
   ```

## Future Improvements
- Implementing **Machine Learning** for improved object detection.
- Enhancing **data transmission speed** using **advanced modulation techniques**.
- Integrating the system with **vehicle-to-vehicle (V2V) communication networks**.

---
**Developed as a Final Year Project**


