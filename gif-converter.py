# Import packages
import imageio
import os

# Fetch file from location
original_file = os.path.abspath('input/rad.mp4')     # Input File directory

def make_gif(input_path, target_format):
    # output path
    output_path = os.path.splitext(input_path)[0] + target_format

    print('[INFO]...Converting {input_path} \n to {output_path}')

    # read metadata
    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data()['fps'] 

    writer =  imageio.get_writer(output_path, fps = fps)

    # Append frames
    for frames in reader:
        writer.append_data(frames)
        print(f'Frame: {frames}')
    
    print("[INFO]... File successfully converted to gif")
    writer.close()

make_gif(original_file, '.gif')



