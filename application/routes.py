import flask
from application import application
from application.handler import handle
from application.forms import FEMAWebForm
@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])

def index():
    form = FEMAWebForm()
    if form.validate_on_submit():
        state=form.state.data.upper()
        flask.flash('Disasters requested for {}'.format(state))
        return flask.render_template('index.html', counties=handle(state), state=state)
    return  flask.render_template('state.html', form=form)
