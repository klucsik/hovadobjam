from app import app

@app.route('/')
@app.route('/index')
def index():
    return "PIFF, World!"


@app.route('/hullinfo')
def index():
    return "itt lesz a hulladékinfó!"
