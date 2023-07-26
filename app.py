from flask import Flask, render_template, redirect, url_for
from forms import CourseForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '76bc3254cacc9d8d5d8e5461451b460e70dc4c8db9ee3d2d'


courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]


@app.route('/', methods=('GET', 'POST'))
def index():
    form = CourseForm()
    if form.validate_on_submit():
        courses_list.append({
            'title': form.title.date,
            'description': form.description.date,
            'available': form.available.date,
            'level': form.level.date
        })
        return redirect(url_for('courses'))
    return render_template('index.html', form=form)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/courses/')
def courses():
    return render_template('courses.html', courses_list=courses_list)
