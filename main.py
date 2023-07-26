import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import ttk
from pytube import YouTube
import threading
import os
import moviepy.editor as mp
from tkinter import messagebox

# Video download function
def start_video_download():
    url = url_entry.get()
    location = location_entry.get()
    resolution = resolution_var.get()

    def video_download_thread():
        try:
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4', res=resolution).first()

            if video is not None:
                video.download(location)
                
                # Rename the downloaded video
                rename_file(location, video.default_filename)


                # Download progress bar
                progress_bar.stop()
                progress_label.config(text="Download complete")
            else:
                progress_label.config(text="Video not available for download.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    progress_label.config(text="Downloading video...")
    progress_bar.start()

    # Start the video download 
    video_download_thread = threading.Thread(target=video_download_thread)
    video_download_thread.start()

# Audio download function
def start_audio_download():
    url = url_entry.get()
    location = location_entry.get()

    def audio_download_thread():
        try:
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True).first()

            if audio_stream is not None:
                audio_stream.download(location)
                
                # Rename the downloaded audio
                rename_file(location, audio_stream.default_filename)
                
                audio_path = os.path.join(location, audio_stream.default_filename)
                # Download progress bar
                progress_bar.stop()
                progress_label.config(text="Download complete")
            else:
                progress_label.config(text="Audio not available for download.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    progress_label.config(text="Downloading audio...")
    progress_bar.start()

    # Start the audio download 
    audio_download_thread = threading.Thread(target=audio_download_thread)
    audio_download_thread.start()
def choose_resolution():
    chosen_resolution = resolution_var.get()
    resolution_label.config(text=f"Chosen Resolution: {chosen_resolution}")

# Creating the GUI
window = tk.Tk()
window.title("YouTube Downloader")

# Link Entry
url_label = ttk.Label(window, text="Enter Video URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
url_entry = ttk.Entry(window, width=50)
url_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

# Location Entry
location_label = ttk.Label(window, text="Download Location:")
location_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
location_entry = ttk.Entry(window, width=50)
location_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Resolution Dropdown
resolution_label = ttk.Label(window, text="Chosen Resolution:")
resolution_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

resolution_var = tk.StringVar()
resolution_dropdown = ttk.Combobox(window, textvariable=resolution_var, state="readonly")
resolution_dropdown["values"] = ["720p", "480p", "360p", "240p"]
resolution_dropdown.current(0)
resolution_dropdown.grid(row=3, column=1, padx=10, pady=5)

# Resolution Button
choose_resolution_button = ttk.Button(window, text="Choose Resolution", command=choose_resolution)
choose_resolution_button.grid(row=3, column=2, padx=10, pady=5)

# Download Buttons
video_download_button = ttk.Button(window, text="Download Video", command=start_video_download)
video_download_button.grid(row=4, column=1, padx=10, pady=10)

audio_download_button = ttk.Button(window, text="Download Audio", command=start_audio_download)
audio_download_button.grid(row=4, column=2, padx=10, pady=10)

# Progress Bar
class CustomProgressBar(ttk.Progressbar):
    def __init__(self, master=None, **kw):
        style = ttk.Style()
        style.configure("IDM.Horizontal.TProgressbar",
                        thickness=20,
                        troughcolor="#E0E0E0",
                        bordercolor="#E0E0E0",
                        lightcolor="#E0E0E0",
                        darkcolor="#E0E0E0",
                        background="#E0E0E0",
                        troughrelief="flat",
                        relief="flat")
        ttk.Progressbar.__init__(self, master, style="IDM.Horizontal.TProgressbar", **kw)
        self.config(length=300)
        self.grid(sticky="ew")

progress_bar = CustomProgressBar(window, mode="determinate")
progress_bar.grid(row=5, columnspan=3, padx=10, pady=10)

# Progress Label
progress_label = ttk.Label(window, text="")
progress_label.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

# Function for renaming the file
def rename_file(location, default_filename):
    new_file_name = filedialog.asksaveasfilename(
        initialdir=location,
        initialfile=default_filename,
        title="Rename Downloaded File",
        filetypes=(("MP4 files", "*.mp4"), ("MP3 files", "*.mp3"), ("All files", "*.*")),
    )
    if new_file_name:
        try:
            os.rename(os.path.join(location, default_filename), new_file_name)
        except Exception as e:
            messagebox.showerror("Error", f"Error renaming file: {e}")
    else:
        try:
            os.remove(os.path.join(location, default_filename))
            progress_label.config(text="Download canceled.")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting file: {e}")

# Start the GUI event loop
window.mainloop()
