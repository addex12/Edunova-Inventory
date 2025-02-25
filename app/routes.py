from flask import render_template, redirect, url_for
from app import app, db
from app.models import Item
from app.forms import ItemForm

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('inventory.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        new_item = Item(name=form.name.data, quantity=form.quantity.data)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_item.html', form=form)
    
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))
