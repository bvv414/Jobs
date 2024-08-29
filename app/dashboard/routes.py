from flask import render_template
from flask_login import login_required, current_user
from . import dashboard

@dashboard.route('/')
@login_required
def dashboard_view():
    return render_template('dashboard/user_profile.html', username=current_user.name)
#gh