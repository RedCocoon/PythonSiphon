# Converts images into Minecraft particles mcfunction file.
# To use this, you would need python 3 and PIL.
# This tool is created by Red Cocoon. Please do not remove this line, please :'(
import PIL
from PIL import Image, ImageSequence

# Not recommended to change this.
# Amount of maximum particles = x*y
# Defaults to 4096 particles maximum. (64x64)
particle_resolution = (64,64)

# Can be changed.
# How close particles are. Smaller the value,
# smaller the space between particles.
particle_density = int(8)

# legacy code
# everything below this point have no need to be edited.
#file = "input"
#extension = "png"
#image_path = str("images/{0}.{1}".format(file,extension))
#output_path = str("generated/"+file+".mcfunction")

command = "particle minecraft:dust {0} {1} {2} {3} ~{4} ~ ~{5} 0 0 0 0.001 1"

sequence_command = "schedule function {0} 1s append"

image_path = str(input("Image path: "))
output_path = str(input("Output path (without \".mcfunction\"): ")+".mcfunction")




def open_image(image_path):
    return Image.open(image_path)

def scale_image(image):
    return image.thumbnail(particle_resolution)

def normalize_color(color):
    new_color = []
    for i in range(4):
        new_color.append(color[i]/255)
    return new_color

def get_particles(image):
    scale_image(image)
    img_x, img_y = image.size
    rgba_img = image.convert('RGBA')
    particles = []
    for i in range(img_x):
        for j in range(img_y):
            color = normalize_color(rgba_img.getpixel((i, j)))
            relative_x = float((img_x/2)-i)/particle_density
            relative_y = float((img_y/2)-j)/particle_density
            new_command = command.format(color[0],color[1],color[2],color[3],relative_x,relative_y)
            particles.append(new_command)
    return particles

def write_file(output_path,particles,namespace_path="",i=0):
    with open(output_path, "w") as file:
        for line in particles:
            file.write(line+"\n")
        if !namespace_path = "":
            file.write(sequence_command.format(namespace_path+"_"+str(i))+"\n")

image = open_image(image_path)

if image.format == "GIF":
    namespace_path = str(input("What is the namespace and path to the mcfunction? (in format \"namespace:path/to/\") "))
    index = 1
    for frame in ImageSequence.Iterator(im):
        write_file(output_path, get_particles(image),namespace_path,i)
        index += 1
else:
    write_file(output_path, get_particles(image))

print("All done!(•̀ ω •́ )✧")
