# **YouTube Downloader** ![youtube](https://em-content.zobj.net/content/2020/04/05/yt.png)
## **Introduction**
Welcome to the YouTube Downloader! This simple application allows you to download YouTube videos or audios directly to your computer using a user-friendly graphical interface. You don't need any programming knowledge to use this tool, just follow the instructions below, and you'll be downloading your favorite videos in no time!

## **System Requirements**
+ Windows, macOS, or Linux operating system
+ Python 3 installed on your computer\ (you can download Python from https://www.python.org/downloads/)

## **Getting Started**
Make sure you have Python 3 installed on your computer. If you don't have it installed, visit https://www.python.org/downloads/ to download and install Python.

Download the code files from this repository and save them to a folder on your computer.

Open a terminal (on macOS or Linux) or Command Prompt (on Windows) and navigate to the folder where you saved the code files.

Run the following command to install the required libraries:
```py
    pip install pytube moviepy
```
## **Usage Instructions**
+ Double-click on the **"main.py"** file to run the YouTube Downloader application.

+ The application window will open, showing fields for **"Enter Video URL"** and **"Download Location."**

+ Open your web browser and go to YouTube (https://www.youtube.com).

+ Find the video you want to download and copy its URL from the address bar of your web browser.

+ Go back to the YouTube Downloader application and paste the copied URL into the **"Enter Video URL"** field.

+ Choose the desired resolution from the **"Chosen Resolution"** dropdown menu. Higher resolutions have better quality but may take longer to download. Due to some limitation of the libraries used, you can download 720P maximum.

+ Click on the **"Choose Resolution"** button to confirm your selected resolution.

+ Click on either the **"Download Video"** or **"Download Audio"** button, depending on whether you want to download the video or audio.\
**[**NOTE:** The audio will be downloaded in .mp4 format but you can change the format to .mp3 while renaming the file.]** 

+ A file dialog box will appear, asking you to provide a new name for the downloaded file. Select the folder where you want to save the file and enter a suitable filename (e.g., "my_video.mp4" or "my_audio.mp3").

+ Click **"Save"** to save the downloaded file.

+ Once the download is complete, you will see a message indicating **"Download complete."**

## **Troubleshooting**
+ **Video/Audio Not Available:** If the video or audio is not available for download, you'll see a message saying "Video/Audio not available for download." In this case, try another video or audio URL.

+ **Age-Restricted Videos:** Some videos on YouTube may be age-restricted, meaning you need to log in to your YouTube account to download them. If you encounter an age-restricted video, log in to your YouTube account and then try downloading the video again.

+ **Errors:** If you encounter any errors during the download process, an error message will appear. This could be due to various reasons, such as network issues or invalid URLs. Make sure you have a stable internet connection and try again.

+ **Others:** There may be some other reasons like library limitations for which you won't be able to download the desired video or audio file. I am working on it and hopefully fix it soon.

## **Disclaimer**
Please note that downloading copyrighted content from YouTube without the permission of the content creator may violate YouTube's terms of service and copyright laws in your country. Respect copyright laws and use this tool responsibly for personal and non-commercial purposes only.

## **Happy downloading!**
