from flask_app import app
from flask import render_template, redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.pie import Pie


@app.route('/pies/save', methods=['POST'])
def savepie():
    if 'user_id' not in session:
        flash('Must Login')
        return redirect('/')
    if not Pie.validate_pie(request.form):
        return redirect('/dashboard')
    data = {
        'pie_name': request.form['pie_name'],
        'filling': request.form['filling'],
        'crust': request.form['crust'],
        'user_id': session['user_id']
    }
    Pie.save_recipie(data)
    return redirect('/dashboard')

@app.route('/pies/<id>/delete')
def delete_user(id):
    if 'user_id' not in session:
        flash('Must Login')
        return redirect('/')
    Pie.delete({'id': id})
    return redirect('/dashboard')


@app.route('/pies/<id>/edit')
def edit_recipie(id):
    if 'user_id' not in session:
        flash('Must Login')
        return redirect('/')
    return render_template('edit.html' , pie = Pie.getPieByPID({'id': id}))

@app.route('/pies/<id>/view')
def view_recipie(id):
    if 'user_id' not in session:
        flash('Must Login')
        return redirect('/')
    print(Pie.getPieByPID({'id':id}))
    pie = Pie.getPieByPID({'id': id})
    print(pie)
    return render_template('show.html', pie = Pie.getPieInfo({'id' : id}), user_name = session['first_name'], user_id = session['user_id'], voted = Pie.checkVote({'id' : session['user_id'], 'pie_id': id}))
    

@app.route('/pies/update', methods=['POST'])
def update_pie():
    if 'user_id' not in session:
        flash('Must Login')
        return redirect('/')
    if not Pie.validate_pie(request.form):
        return redirect('/dashboard')
    data = {
        'id' : request.form['id'],
        'pie_name': request.form['pie_name'],
        'filling': request.form['crust'],
        'crust': request.form['crust'],
    }
    Pie.edit(data)
    return redirect('/dashboard')

@app.route('/pies')
def derby():
    if 'user_id' not in session:
        flash('Must Login')
        return redirect('/')
    return render_template('derby.html' , pies = Pie.getAllPies())



@app.route('/vote/<user_id>/<pie_id>', methods =['POST'])
def vote(user_id,pie_id):
    
    data2 = {
        'user_id' : user_id,
        'pie_id' : pie_id
    }
    votes = len(Pie.getVotes(data2)) + 1
    data = {
        'user_id' : user_id,
        'pie_id' : pie_id,
        'votes' : votes
    }

    if 'user_id' not in session:
        flash('Must Login')
        return redirect('/')
    Pie.vote(data)
    Pie.addvote(data)
    return redirect('/pies')

@app.route('/removevote/<user_id>/<pie_id>')
def removeVote(user_id, pie_id):
    if 'user_id' not in session:
        flash('Must Login')
        return redirect('/')
    

    data2 = {
        'user_id' : user_id,
        'pie_id' : pie_id
    }
    votes = len(Pie.getVotes(data2)) - 1
    print(f'VOTES: {votes}')
    data = {
        'user_id' : user_id,
        'pie_id' : pie_id,
        'votes' : votes
    }
    Pie.removeVote(data)
    Pie.deleteVote(data)
    return redirect('/pies')

