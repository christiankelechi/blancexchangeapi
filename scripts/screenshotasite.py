import base64
import webview
from PIL import Image
from io import BytesIO

def capture_screenshot(url, output_file='screenshot.png'):
    # Create a webview window
    window = webview.create_window('Screenshot', url, width=1200, height=800)

    # Load the page
    webview.start(lambda: window.eval('window.print()'), window)

    # Capture the screenshot
    screenshot_base64 = window.eval('document.querySelector("html").outerHTML')

    # Convert base64 to image
    image_data = base64.b64decode(screenshot_base64)
    image = Image.open(BytesIO(image_data))

    # Save image
    image.save(output_file)

    return output_file

# Capture screenshot and save as image
capture_screenshot('http://127.0.0.1:4321/customtemplates/render_activation_code/', 'screenshot.png')
