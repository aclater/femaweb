from flask import render_template, flash, redirect
from application import application
from application.fema import disastersearch
from application.forms import FEMAWebForm

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])

def index():
    form = FEMAWebForm()
    if form.validate_on_submit():
        state=form.state.data.upper()
        flash('Disasters requested for {}'.format(state))
        return render_template('index.html', counties=disastersearch(state), state=state)
    return  render_template('state.html', form=form)
