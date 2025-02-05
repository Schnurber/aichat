from pydub import AudioSegment
import os
import random

def combine_mp3_files(input_folder, start_file, end_file, output_file):
    # Initialize an empty AudioSegment object as the compilation
    combined = AudioSegment.empty()
    combined += AudioSegment.from_mp3(os.path.join('assets', start_file))
    # Iterate through all mp3 files in the input folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".mp3"):
            filepath = os.path.join(input_folder, filename)
            
            # Load the current mp3 file
            audio = AudioSegment.from_mp3(filepath)
            
            # Append to the combined audio segment
            combined += audio
            pause = AudioSegment.silent(duration=random.randint(700, 1300)) 
            combined += pause
    combined += AudioSegment.from_mp3(os.path.join('assets', end_file))
    # Export the combined audio to the specified output file
    combined.export(output_file, format="mp3")
    # Delete all
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".mp3"):
            filepath = os.path.join(input_folder, filename)
            os.remove(filepath)

    print(f"Combined MP3 saved as {output_file}")