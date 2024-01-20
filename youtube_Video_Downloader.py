import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os


def download_video():
    url = entry_url.get()
    resolutions = resolutions_var.get()

    status_label.pack(pady=(10, 5))
    progress_bar.pack(pady=(10, 5))
    status_label.pack(pady=(10, 5))

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolutions).first()

# Set the output path using os.path.join

        output_path = os.path.join("downloads", f"{yt.title}.mp4")
        stream.download(output_path="downloads")

        # Update status label on successful download
        status_label.configure(text="Downloaded!", text_color="white", fg_color="green")





    except Exception as e:
        status_label.configure(text=f"Error {str(e)}", text_color="white", fg_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100

    progress_label.configure(text=str(int(percentage_completed)) + "%")
    progress_bar.set(float(percentage_completed / 100))
    root.update()


# create a root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# title of the window
root.title("YouTube Downloader!")

# set min and max width and the height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

# create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# create a label and the entry widget for the video url
url_label = ctk.CTkLabel(content_frame, text="Enter the YouTube URL here:")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(10, 5))
entry_url.pack(pady=(10, 5))

# create a download button

download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=(10, 5))

# create a resolutions combo box

resolutions = ["720p", "360p", "240p"]
resolutions_var = ctk.StringVar()
resolutions_combobox = ttk.Combobox(content_frame, values=resolutions, textvariable=resolutions_var)
resolutions_combobox.pack(pady=(10, 5))
resolutions_combobox.set("720p")

# create a label and the progress bar to display the download progress

progress_label = ctk.CTkLabel(content_frame, text="0%")

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)

# Use pack to place the progress label and progress bar on the window

progress_label.pack(pady=(10, 5))
progress_bar.pack(pady=(10, 5))

# create the status label

status_label = ctk.CTkLabel(content_frame, text="")

root.mainloop()
