from rembg import remove
from PIL import Image 
input_path = 'GRDshmOaMAEkMo1.jpg'  #SimpleImageName 
output_path = 'GRDshmOaMAEkMo1.jpg'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
