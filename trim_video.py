import os
import sys
import json
import subprocess


encoder = json.JSONEncoder()


def convert_folder(folder_path, result_path):
    videos = [y for x in list(os.walk(folder_path)) for y in x[2]]
    videos = [x for x in videos if '.mp4' in x]

    print(videos)

    # Convert the videos
    for video in videos:
        print(video)
        results_path = os.path.join(result_path, video)
        # os.mkdir(results_path)
        subprocess.run([
            'ffmpeg',
            '-i',
            os.path.join(folder_path, video),
            '-ss',
            '00:00:00',
            '-t',
            '10',
            results_path])
            # os.path.join(results_path,video)])


if __name__ == "__main__":
    folder_location = sys.argv[1]
    result_path = sys.argv[2]
    convert_folder(folder_location, result_path)
