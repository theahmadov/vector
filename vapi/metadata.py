# from PIL import Image
# from PIL.ExifTags import TAGS
# from colorama import Fore, Back, Style, init

# imagename = input(Fore.GREEN + "Enter the path of the image : ")

# image = Image.open(imagename)

# info_dict = {
#     "Filename": image.filename,
#     "Image Size": image.size,
#     "Image Height": image.height,
#     "Image Width": image.width,
#     "Image Format": image.format,
#     "Image Mode": image.mode,
#     "Image is Animated": getattr(image, "is_animated", False),
#     "Frames in Image": getattr(image, "n_frames", 1)
# }

# for label, value in info_dict.items():
#     print(Fore.RED + f"{label:25}:", Fore.GREEN + f" {value}")

# exifdata = image.getexif()

# for tag_id in exifdata:

#     tag = TAGS.get(tag_id, tag_id)
#     data = exifdata.get(tag_id)

#     if isinstance(data, bytes):
#         data = data.decode()
#     print(Fore.RED + f"{tag:25}:", Fore.GREEN + f" {data}")

# Shahin
