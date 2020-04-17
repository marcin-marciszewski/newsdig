from news.models import News
from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    all_news = News.query.order_by(
        News.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', all_news=all_news)


@core.route('/popular')
def popular():
    page = request.args.get('page', 1, type=int)
    all_news = News.query.order_by(
        News.likes.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', all_news=all_news)


@core.route('/info')
def info():
    return render_template('info.html')
