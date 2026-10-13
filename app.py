from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initial mock database with posts featuring stunning internet images
posts = [
    {
        "id": 1,
        "username": "nature_explorer",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop",
        "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&h=600&fit=crop",
        "caption": "Chasing mountain sunsets and fresh alpine air! 🏔️✨ #nature #adventure",
        "likes": 142
    },
    {
        "id": 2,
        "username": "culinary_art",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop",
        "image": "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=800&h=600&fit=crop",
        "caption": "Fresh vibrant organic salad bowls to kickstart the day right. 🥗🌿",
        "likes": 89
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add_post():
    username = request.form.get('username')
    caption = request.form.get('caption')
    image_url = request.form.get('image_url')
    
    # Fallback to an aesthetic image if none is provided
    if not image_url:
        image_url = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&h=600&fit=crop"
        
    new_post = {
        "id": len(posts) + 1,
        "username": username if username else "guest_creator",
        "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop",
        "image": image_url,
        "caption": caption,
        "likes": 0
    }
    posts.insert(0, new_post)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
