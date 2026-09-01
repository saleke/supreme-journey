import os
import pytest
import subprocess

def test_no_arguments():
    """Ensure no file is created and an error is shown when no argument is given."""
    result = subprocess.run(['python', 'request_wikipedia.py'], capture_code=True, text=True)
    assert result.returncode != 0
    assert "Error:" in result.stderr or "Error:" in result.stdout
    # Check that no .wiki file was created
    assert not any(f.endswith('.wiki') for f in os.listdir('.'))

def test_successful_search_and_filename_formatting():
    """Ensure a valid search creates a space-free .wiki file with plain text."""
    filename = "Artificial_intelligence.wiki"
    if os.path.exists(filename):
        os.remove(filename)

    result = subprocess.run(['python', 'request_wikipedia.py', 'Artificial intelligence'], text=True)
    
    assert os.path.exists(filename)
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "JSON" not in content  # Shouldn't be raw JSON
        assert "{" not in content     # Basic check against structural markup
        assert len(content) > 100     # Should have substance

    os.remove(filename)

def test_misspelled_fallback():
    """Ensure typos (like 'pythn') fallback to the correct article ('Python')."""
    filename = "pythn.wiki"
    if os.path.exists(filename):
        os.remove(filename)

    subprocess.run(['python', 'request_wikipedia.py', 'pythn'], text=True)
    
    # Filename matches the original query, but content belongs to the corrected topic
    assert os.path.exists(filename)
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "programming language" in content.lower()

    os.remove(filename)
