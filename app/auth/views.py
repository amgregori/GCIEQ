
from . import auth_bp
from flask import render_template, redirect, url_for, flash
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from app.extensions import BCrypt
from app.extensions import db
from app.extensions import login_manager
from app.models.users import Users
from app.auth.forms import UserForm
from app.auth.forms import LoginForm


login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(id):
    user = Users.query.get(int(id))
    return user


@auth_bp.route('/')
def register():
    userlist = Users.query.all()
    return render_template('auth/register.html', list=userlist)

@auth_bp.route('/adduser', methods=['GET', 'POST'])
def add_user():
    name_first = None
    name_last = None
    email = None
    password = None

    form = UserForm()

    #Form Validation
    if form.validate_on_submit():
        
        user = Users.query.filter_by(email=form.email.data).first()

        

        if user is None:
            hashed_pw = BCrypt.generate_password_hash(form.password.data) 
            user = Users(name_first=form.name_first.data, name_last=form.name_last.data, email=form.email.data, password=hashed_pw)

            db.session.add(user)
            db.session.commit()

            
    else:
        flash("There was a problem.")
    user_list = Users.query.order_by(Users.name_last)

    return render_template('auth/add_user.html', form = form,
        name_first = name_first,
        name_last = name_last,
        email = email,
        password = password, user_list=user_list)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()


    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if BCrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('auth.dashboard'))
                


    return render_template('auth/login.html', form = form)


@auth_bp.route('/dashboard', methods=['GET', 'POST'])
#@login_required
def dashboard():
    return render_template('auth/dashboard.html')


@auth_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


