import importlib.util
import json
import sys
import os

# Get the path to lambda-code.py
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, "lambda-code.py")

# Load the module
spec = importlib.util.spec_from_file_location("lambda_code", module_path)
lambda_code = importlib.util.module_from_spec(spec)
sys.modules["lambda_code"] = lambda_code
spec.loader.exec_module(lambda_code)

def test_lambda_handler():
    # Arrange
    event = {}
    context = {}

    # Act
    result = lambda_code.lambda_handler(event, context)

    # Assert
    assert result["statusCode"] == 200
    assert result["body"] == json.dumps("Hello from Lambda!")
    assert result["headers"]["Content-Type"] == "application/json"
