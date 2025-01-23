import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="dckvtvzjg",
    api_key="658545447794538",
    api_secret="mPIsb2z-yvKnWQvdfktq67HCHcY"
)

result = cloudinary.uploader.upload("/mnt/c/Users/joaov/Downloads/pato.jpeg")
print(result)
