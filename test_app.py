from main import generate_id, analyze_image


def test_generate_id_length():
    img_id = generate_id()
    assert len(img_id) == 6


def test_analyze_image_structure():
    img_id = generate_id()
    result = analyze_image(img_id)

    assert "image_id" in result
    assert "skin_type" in result
    assert "issues" in result
    assert "confidence" in result
