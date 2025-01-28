# e-Paper ESP8266 Driver_Board
ESPHome YAML example for Waveshare e-Paper ESP8266 Driver Board

To monitor indoor and outdoor ultra fine dust status and indoor CO2 level, I utilized a spare e-Paper HAT for Raspberry Pi(https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT_Manual#Introduction).

Waveshare e-Paper ESP8266 Driver Board is useful of various usages, due to ESP8266 it can be anything especially in the field of IoT(https://www.waveshare.com/wiki/E-Paper_ESP8266_Driver_Board).  

Home Assistant gets external ultra-fine dust value from Naver weather information installed through HACS, and DIY board which has the fine dust sensor (SDS021) and carbon dioxide sensor (MH-Z19B) is connected to Home Assistant through ESPHome. 

![110357](https://github.com/sevengivings/e-Paper_ESP8266_Driver_Board/assets/2328500/f76a3f0a-ffae-47dd-8e88-1f7f148db241)

I added more information and 3D printed front case. 

![Image](https://github.com/user-attachments/assets/10ac7d0a-b2b8-4a48-a87b-3f67a2640eb8)

If you have plan to use 7.5inch e-Paper, you should know that ESP8266 version of e-Paper driver board doesn't have enough memory. So, please buy e-Paper ESP32 driver board instead. 

Waveshare e-Paper ESP32 Driver board: https://www.waveshare.com/wiki/E-Paper_ESP32_Driver_Board 

I attached esp32-eink75.yaml for 7.5inch E-Paper (B) E-Ink Raw Display, 800x480, Red/Black/White SPI without PCB. 



