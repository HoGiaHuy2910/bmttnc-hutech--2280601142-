import sys
from PIL import Image

def decode_image(image_path):
    # 🔧 FIX 1: luôn chuyển ảnh sang RGB
    img = Image.open(image_path).convert("RGB")
    width, height = img.size

    binary_data = ""
    delimiter = "1111111111111110"

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))  # [R, G, B]

            for channel in range(3):
                binary_data += format(pixel[channel], '08b')[-1]

                # 🔧 FIX 2: gặp delimiter thì dừng ngay
                if binary_data.endswith(delimiter):
                    binary_data = binary_data[:-len(delimiter)]
                    return binary_to_text(binary_data)

    return binary_to_text(binary_data)

def binary_to_text(binary_data):
    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            message += chr(int(byte, 2))
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image>")
        return

    image_path = sys.argv[1]
    message = decode_image(image_path)
    print("Decoded message:", message)

if __name__ == "__main__":
    main()
