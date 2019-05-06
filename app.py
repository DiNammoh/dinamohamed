from flask import Flask, render_template
import random
app = Flask(__name__)
# list of  images
images = [
"http://4.bp.blogspot.com/-yse8CFoxJYw/Vp3c_K7PVsI/AAAAAAAACT8/Nvn5TJKneWo/s640/03n.jpg",
"http://1.bp.blogspot.com/-Nz9VLzNbxjA/Vg0pkaKpq2I/AAAAAAAACIU/69_t2UlGxV8/s1600/27.jpg",
"http://4.bp.blogspot.com/-seIl8eIRIWY/UyydsOdaKLI/AAAAAAAAAbA/qEwZcxqi_IA/s1600/22.jpg",
"https://assets.lybrate.com/q_auto:eco,f_auto,w_450/imgs/dt/tp/6ee155982237a0baba59965ba7fde2a4/e1ea055ec9497037df83f42f388eea52/e6b8fb.jpg",
"https://assets.lybrate.com/q_auto:eco,f_auto,w_450/imgs/dt/tp/6ee155982237a0baba59965ba7fde2a4/e1ea055ec9497037df83f42f388eea52/0ec340.jpg"
]
@app.route('/')
def index():
url = random.choice(images)
return render_template('index.html', url=url)
if __name__ == "__main__":
app.run(host="0.0.0.0")