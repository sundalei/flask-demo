from flask import Blueprint, render_template, request, redirect, url_for
from flaskr.auth import login_required
from werkzeug.utils import secure_filename

bp = Blueprint('upload', __name__, url_prefix='/upload')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
	if request.method == 'POST':
		f = request.files['file']
		f.save('uploads/' + secure_filename(f.filename))
		return redirect(url_for('blog.index'))
	return render_template('upload/upload.html')