
import os

input_dir = ''
output_dir = ''
map_file = ''

for in_filename in os.listdir(input_dir):
    in_file = os.path.join(input_dir, in_filename)
    out_file = os.path.join(output_dir, in_filename)
    print(in_file)

    # For transparent background and shadow
    command = 'magick convert {} -ordered-dither o8x8,32 -write MPR:orig +dither -remap {} MPR:orig -compose copyalpha -composite {}'.format(in_file, map_file, out_file)
    
    # Simpler version that doesn't include alpha copy. Transparency is lost.
    #command = 'convert {} -ordered-dither o4x4,4 +dither -remap {} {}'.format(in_file, map_file, out_file)
    
    os.system(command)