import argparse

from moviepy.editor import *
from pytube import YouTube


def videoDownload(urls, path=None, hd=False):
    for url in urls:
        # Check to download the video in the highest resolution
        if hd:
            # Try,except block
            try:

                # Create the data stream in the highest resolution
                data = YouTube(url).streams.get_highest_resolution().download(output_path=path)

                # Get the name of the video
                filename = os.path.basename(data)

                print(f"File Downloaded: {filename}")
                print(f"File Path: {data}\n")

            # Get the error if any occurs
            except Exception as err:

                print(f"Error Occurred: {err}\n")

        else:
            # Try,except block
            try:

                # Create the data stream
                data = YouTube(url).streams.first().download(output_path=path)

                # Get the name of the video
                filename = os.path.basename(data)

                print(f"File Downloaded: {filename}")
                print(f"File Path: {data}\n")

            # Get the error if any occurs
            except Exception as err:

                print(f"Error Occurred: {err}\n")


def audioDownload(urls, path=None, keep_video=False, hd=False):
    for url in urls:
        # Try,except block
        try:

            if hd:
                # Create the data stream
                data = YouTube(url).streams.first().download(output_path=path)

            else:

                # Create the data stream in the highest resolution
                data = YouTube(url).streams.get_highest_resolution().download(output_path=path)

            # Get the filename of the video
            filename, extension = (os.path.splitext(os.path.basename(data)))

            # Create the video object, then get the audio of the video
            video = VideoFileClip(data)
            audio = video.audio

            # Write the audio file, filename as the video name
            audio.write_audiofile(f"{filename}.mp3")

            # Change the location of the file, if path is provided
            if path:
                os.rename(f"{os.getcwd()}\{filename}.mp3", f"{path}\{filename}.mp3")

            # Close the video object
            video.close()

            # Check for to keep the downloaded video
            if keep_video:

                print(f"File Downloaded: {filename}.mp4")
                print(f"File Path: {data}\n")

                print(f"File Downloaded: {filename}.mp3")
                print(f"File Path: {(os.path.splitext(data))[0]}.mp3\n")

            else:
                # Check if file exists
                if os.path.isfile(data):
                    # Remove the video file
                    os.remove(data)

                    print(f"File Downloaded: {filename}.mp3")
                    print(f"File Path: {(os.path.splitext(data))[0]}.mp3\n")

        # Get the error if any occurs
        except Exception as err:

            print(f"Error Occurred: {err}")


def main():
    parser = argparse.ArgumentParser(description='DOWNLOAD AUDIO AND VIDEO FILES FROM YOUTUBE')

    # Argument is for a urls to be provided
    parser.add_argument('-u', dest='urls', nargs='+', type=str, help='URLS To Download From', required=True)

    # Argument is to download audios
    parser.add_argument('-a', dest='audio', action='store_true', help='Download Audio File')

    # Argument is to download videos
    parser.add_argument('-v', dest='video', action='store_true', help='Download Video File')

    # Argument is for filepath
    parser.add_argument('-p', dest='path', type=str, help='Path For To Store The Files')

    # Argument is used to keep the video with the audio file
    parser.add_argument('-k', dest='keepVideo', action='store_true', help='Keep The Video With The Audio File')

    # Argument is used to download video in highest resolution
    parser.add_argument('-hd', dest='hd', action='store_true', help='Download The HD Video')

    args = parser.parse_args()

    if args.urls:

        if args.video:

            if args.path and args.hd:
                videoDownload(args.urls, args.path, True)

            elif args.hd:
                videoDownload(args.urls, None, True)

            elif args.path:
                videoDownload(args.urls, args.path)

            else:
                videoDownload(args.urls)

        elif args.audio:

            if args.path and args.keepVideo and args.hd:
                audioDownload(args.urls, args.path, True, True)

            elif args.path and args.keepVideo:
                audioDownload(args.urls, args.path, True)

            elif args.keepVideo and args.hd:
                audioDownload(args.urls, None, True, True)

            elif args.keepVideo:
                audioDownload(args.urls, None, True)

            elif args.path:
                audioDownload(args.urls, args.path)

            else:
                audioDownload(args.urls)

        else:
            print("Use -v for Video Download and -a For Audio Download")
            print("Use -h for help")


if __name__ == '__main__':
    main()
