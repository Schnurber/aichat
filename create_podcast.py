from pydub import AudioSegment
import os

def combine_mp3_files(input_folder, output_file):
    # Initialize an empty AudioSegment object as the compilation
    combined = AudioSegment.empty()

    # Iterate through all mp3 files in the input folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".mp3"):
            filepath = os.path.join(input_folder, filename)
            
            # Load the current mp3 file
            audio = AudioSegment.from_mp3(filepath)
            
            # Append to the combined audio segment
            combined += audio

    # Export the combined audio to the specified output file
    combined.export(output_file, format="mp3")
    print(f"Combined MP3 saved as {output_file}")