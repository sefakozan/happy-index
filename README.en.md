# YZ Applications for Calculating Correct Mask-Wearing Rate and Happiness Index (Happy Index)

The Turkish Statistical Institute (TÜİK) conducts the “Life Satisfaction Survey” every year. According to TÜİK’s 2019 report, the percentage of men who reported being happy was 47.6%, while for women, this rate was 57.0%. Additionally, Sinop was identified as the happiest province with a rate of 77.6%. TÜİK evaluates satisfaction by categorizing it into areas such as public services and municipal services. The United Nations and the European Statistical Office, on the other hand, conduct annual surveys at the country level and publish the World Happiness Index Report.

Calculating the happiness index with artificial intelligence (AI) applications is still at an experimental stage worldwide. However, analyzing subjective data with AI algorithms enables data analyses that were previously difficult to obtain. For example, IBM uses AI to measure the happiness rates of its employees, Dubai uses it to calculate citizen satisfaction with public services in government buildings, and stores use it to measure consumer satisfaction.

## Project Description
In this project, a **Convolutional Neural Network (CNN)** model was developed using the Python programming language with a dataset of 9,000 CC0-licensed images of human faces, including those wearing medical face masks correctly, incorrectly, or not at all. The trained model achieved a **96% test accuracy rate**.

By integrating a total of **4 CNN models**, a desktop application and a web application were created. This application detects human faces in a video stream and performs the following analyses:
- If a mask is present on the face, it calculates the **correct mask-wearing rate**.
- If no mask is present, it estimates the person’s **gender**, **age**, and **happiness rate**.

The application collects data from people’s real-time facial expressions via a camera and calculates the **correct mask-wearing rate** and the **distribution of the happiness index by age, gender, and time**.

## Use Cases
- Public service satisfaction analysis
- Employee happiness measurement
- Consumer satisfaction analysis
- Monitoring mask-wearing habits during pandemics

## Technical Details
- **Dataset**: 9,000 CC0-licensed images (correct mask, incorrect mask, no mask)
- **Model**: 4 Convolutional Neural Networks (CNNs)
- **Programming Language**: Python
- **Test Accuracy Rate**: 96%
- **Application Type**: Desktop application, Web application
- **Functions**:
  - Face detection
  - Mask-wearing rate analysis
  - Gender and age estimation
  - Happiness index estimation

## Installation and Usage
1. You can access the project by cloning the repository:
   ```bash
   git clone https://github.com/sefakozan/happy-index.git
   ```
2. You can visit the website:
    > [https://sefakozan.github.io/happy-index](https://sefakozan.github.io/happy-index/)
3. You can download the desktop application:
    > [happy-index.exe](https://sefakozan.github.io/happy-index/happy-index.exe)
4. You can review the project documentation:
    > [Happy Index - Project Documentation](https://sefakozan.github.io/happy-index/docs/Happy%20Index%20-%20Proje%20D%C3%B6k%C3%BCman%C4%B1.pdf)  
    > [TÜBİTAK Project Presentation](https://sefakozan.github.io/happy-index/docs/T%C3%9CB%C4%B0TAK%20Proje%20Sunum.pdf)