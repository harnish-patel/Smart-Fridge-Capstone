# Smart Fridge Capstone
This project includes the machine vision portion of my Smart Fridge Capstone Project for my final year of my Comp Eng Undergrad.

## Achievements
I am proud to say this project won 1st place in the Software Engineering category for 2022's Queen's University Computer and Electrical Engineering Open House Design Projects!

# Table of Contents

- [Smart Fridge Capstone](#smart-fridge-capstone)  
  - [Overview](#overview)  
  - [Problem Statement](#problem-statement)  
  - [Key Features](#key-features)  
  - [Stakeholders](#stakeholders)  
  - [Design](#design)  
  - [Implementation](#implementation)  
  - [Testing and Validation](#testing-and-validation)  
  - [Specifications](#specifications)

## Overview
The Smart Fridge Module is a cost-effective and modular solution designed to address the environmental impact of food waste. With a focus on reducing forgotten food spoilage, the module employs a Raspberry Pi with a PiCamera for object detection, coupled with a mobile app for user interaction.

## Problem Statement
As global food waste and environmental concerns rise, the Smart Fridge Module aims to combat the issue of forgotten food spoilage. Conventional solutions, such as expensive smart fridges, present a significant barrier. This module offers an affordable and retrofittable alternative.

## Key Features
* Modular Design: The module can be added to any existing fridge, minimizing the need for costly replacements.
* Object Detection: Utilizes a trained YOLO (You Only Look Once) model to identify groceries and quantities within the fridge.
* Mobile App Integration: Provides users with real-time information on fridge contents, a shopping list feature, and alerts for low quantities.

## Stakeholders
* End Users: Concerned with cost, usability, and privacy. The module addresses these by being cost-effective, user-friendly, and incorporating secure login features.
* Environment: Aims to reduce food waste and its associated environmental impact.

## Design
* Hardware: Raspberry Pi 4 Model B, PiCamera, BrightPi for lighting, and other off-the-shelf components.
* Software: Object detection model trained using Darknet and YOLO, Python for Raspberry Pi application, Android Studio for mobile app, Firebase for database management.

## Implementation
* Hardware Setup: Raspberry Pi components assembled, including PiCamera and BrightPi.
* Software Development: Object detection model trained on Google Colab, Python program for Raspberry Pi developed in Visual Studio, Android app created in Android Studio using Java.
* Database: Firebase used for real-time database management, integrating with the mobile app.

## Testing and Validation
* Detection Model: Achieved 83% accuracy on test data, exceeding the 70% target.
* Raspberry Pi: On-board camera and detection model tested successfully, meeting functional requirements.
* Mobile App and Database: Responsive performance, secure login, and real-time updates achieved.

## Specifications
* Hardware: Raspberry Pi 4 with camera and lighting components.
* Software: YOLO-based object detection model, Python for Raspberry Pi, Android Studio for mobile app, Firebase for database.
