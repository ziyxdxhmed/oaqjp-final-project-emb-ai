from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (950, 280), color=(30, 30, 30))
d = ImageDraw.Draw(img)
font = ImageFont.load_default()

text = """(venv) C:\\Users\\ziyad\\OneDrive\\Desktop\\EmotionDetection> python server.py
 * Serving Flask app 'Emotion Detection'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.100:5000
Press CTRL+C to quit
127.0.0.1 - - [18/Aug/2026 12:00:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [18/Aug/2026 12:01:23] "GET /emotionDetector?textToAnalyze=I%20am%20glad%20this%20happened HTTP/1.1" 200 -"""

d.text((20, 20), text, fill=(230, 230, 230), font=font)
img.save('6b_deployment_test.png')
