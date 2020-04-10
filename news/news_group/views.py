from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from news import db
from news.models import News, Comment
from news.news_group.forms import NewsForm, CommentForm

news_group = Blueprint('news_group', __name__)

# create news
@news_group.route('/create', methods=['GET', 'POST'])
@login_required
def create_news():
    form = NewsForm()

    if form.validate_on_submit():

        new_news = News(title=form.title.data,
                        text=form.text.data, user_id=current_user.id)

        db.session.add(new_news)
        db.session.commit()
        flash('News Created')
        return redirect(url_for('core.index'))

    return render_template('create_news.html', form=form)

# view news
@news_group.route('/<int:news_id>', methods=['GET', 'POST'])
def news_view(news_id):
    form = CommentForm()

    if form.validate_on_submit():

        comment = Comment(text=form.text.data, news_id=news_id,
                          user_name=current_user.username)

        db.session.add(comment)
        db.session.commit()
        flash('Comment Created')
        return redirect(url_for('news_group.news_view', news_id=news_id))

    comments = Comment.query.order_by(
        Comment.date.desc())
    news_view = News.query.get_or_404(news_id)
    return render_template('view_news.html', title=news_view.title, date=news_view.date, news=news_view, form=form, comments=comments)

# update news
@news_group.route("/<int:news_id>/update", methods=['GET', 'POST'])
@login_required
def update(news_id):
    new_news = News.query.get_or_404(news_id)
    if new_news.author != current_user:

        abort(403)

    form = NewsForm()
    if form.validate_on_submit():
        new_news.title = form.title.data
        new_news.text = form.text.data
        db.session.commit()
        flash('News Updated')
        return redirect(url_for('news_group.news_view', news_id=new_news.id))

    elif request.method == 'GET':
        form.title.data = new_news.title
        form.text.data = new_news.text
    return render_template('create_news.html', title='Update', form=form)

# delete news
@news_group.route('/<int:news_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_news(news_id):
    news = News.query.get_or_404(news_id)

    if news.author != current_user:
        abort(403)

    db.session.delete(news)
    db.session.commit()
    flash('News Deleted')
    return redirect(url_for('core.index'))
