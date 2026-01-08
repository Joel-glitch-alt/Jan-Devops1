import random
import string
def generate_id(length=6):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
def analyze_image(image_id):
    skin_types = ["Oily", "Dry", "Normal", "Combination"]
    issues = ["Acne", "Hyperpigmentation", "Wrinkles", "Dark spots"]
    result = {}
    result["image_id"] = image_id
    result["skin_type"] = random.choice(skin_types)
    result["issues"] = random.sample(issues, k=1)
    result["confidence"] = round(random.uniform(0.7, 0.95), 2)
    return result
def main():
    print("Mock Image Analyzer")
    image_name = input("Enter image name: ")
    if not image_name:
        print("Invalid image name")
        return
    image_id = generate_id()
    print(f"Image '{image_name}' uploaded successfully")
    print(f"Generated image_id: {image_id}")
    analysis = analyze_image(image_id)
    print("Analysis Result:")
    for key, value in analysis.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    main()
def save_result(result):
    with open("result.txt", "w") as f:
        for k, v in result.items():
            f.write(f"{k}: {v}\n")
def load_previous():
    try:
        with open("result.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No previous result found"
print("Starting application...")
previous = load_previous()
print(previous)
if __name__ == "__main__":
    img_id = generate_id()
    res = analyze_image(img_id)
    save_result(res)
    print("Result saved")
    print(res)
    print("Done")
    pass
