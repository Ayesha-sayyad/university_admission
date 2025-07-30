from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

applications = []

@app.route('/')
def home():
    print("Home page requested")
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            
            'email': request.form['email'],
            'course': request.form['course']
        }
        applications.append(data)
        return render_template('success.html', name=data['name'])
    return render_template('register.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', applications=applications)

if __name__ == '__main__':
    app.run(debug=True)
