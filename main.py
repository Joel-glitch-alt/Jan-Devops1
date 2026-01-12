import random
import string


def generate_id(length=6):
    """Generate a random image ID."""
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def analyze_image(image_id):
    """Mock image analysis."""
    skin_types = ["Oily", "Dry", "Normal", "Combination"]
    issues = ["Acne", "Hyperpigmentation", "Wrinkles", "Dark spots"]

    return {
        "image_id": image_id,
        "skin_type": random.choice(skin_types),
        "issues": random.sample(issues, k=1),
        "confidence": round(random.uniform(0.7, 0.95), 2),
    }


def save_result(result, filename="result.txt"):
    """Save analysis result to file."""
    with open(filename, "w", encoding="utf-8") as file:
        for key, value in result.items():
            file.write(f"{key}: {value}\n")


def load_previous(filename="result.txt"):
    """Load previous analysis result."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "No previous result found"


def main():
    """Main application entry point."""
    print("Mock Image Analyzer")

    previous = load_previous()
    print(previous)

    image_name = input("Enter image name: ").strip()
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

    save_result(analysis)
    print("Result saved")
    print("Done")


if __name__ == "__main__":
    main()
