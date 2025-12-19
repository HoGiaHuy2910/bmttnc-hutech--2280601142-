import sys
from PIL import Image

def encode_image(image_path, message):
    # 🔧 FIX 1: luôn chuyển ảnh sang RGB
    img = Image.open(image_path).convert("RGB")
    width, height = img.size

    # Chuyển thông điệp sang nhị phân
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # delimiter kết thúc

    data_index = 0
    message_length = len(binary_message)

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))  # luôn là [R, G, B]

            for channel in range(3):
                if data_index < message_length:
                    # 🔧 FIX 2: thay bit cuối bằng bit thông điệp
                    pixel[channel] = int(
                        format(pixel[channel], '08b')[:-1] + binary_message[data_index],
                        2
                    )
                    data_index += 1

            img.putpixel((col, row), tuple(pixel))

            if data_index >= message_length:
                encoded_image_path = "encoded_image.png"
                img.save(encoded_image_path)
                print("Steganography complete.")
                print("Encoded image saved as:", encoded_image_path)
                return

    print("❌ Image is too small to hold the message.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()
