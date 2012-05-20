MongoEngine-Pagination
======================

Custom Queryset with pagination support
Shamelessly taken and adapted from `flask-mongoenginee <https://github.com/sbook/flask-mongoengine>`_ to suit my needs
If you are using Flask you will be better using `flask-mongoenginee <https://github.com/sbook/flask-mongoengine>`_

Installing MongoEngine-Pagination
============================

Install with **pip**::

    pip install https://github.com/mechanicalchopsticks/MongoEngine-Pagination/tarball/master


Configuration
=============

Basic setup is easy, just fetch the extension::

    from flask import Flask
    from flaskext.mongoengine import MongoEngine

    app = Flask(__name__)
    app.config.from_pyfile('the-config.cfg')
    db = MongoEngine(app)


Custom Queryset
===============

MongoEngine-Pagination attaches the following methods to Mongoengine's default QuerySet:

* **paginate**: paginates the QuerySet. Takes two arguments, *page* and *per_page*.
* **paginate_field**: paginates a field from one document in the QuerySet. Arguments: *field_name*, *doc_id*, *page*, *per_page*.

Examples::

    # Paginate through todo
    def view_todos(page=1):
        paginated_todos = Todo.objects.paginate(page=page, per_page=10)

    # Paginate through tags of todo
    def view_todo_tags(page=1):
        todo_id = Todo.objects.first().id
        paginated_tags = Todo.objects.paginate_field('tags', todo_id, page,
                                                     per_page=10)

Properties of the pagination object include: iter_pages, next, prev, has_next, has_prev, next_num, prev_num.

In the template::

    {% macro render_pagination(pagination, endpoint) %}
      <div class=pagination>
      {%- for page in pagination.iter_pages() %}
        {% if page %}
          {% if page != pagination.page %}
            <a href="{{ url_for(endpoint, page=page) }}">{{ page }}</a>
          {% else %}
            <strong>{{ page }}</strong>
          {% endif %}
        {% else %}
          <span class=ellipsis>…</span>
        {% endif %}
      {%- endfor %}
      </div>
    {% endmacro %}

Credits
========

Inspired by two repos:

* `sbook <https://github.com/sbook/flask-mongoengine>`_
* `danjac <https://bitbucket.org/danjac/flask-mongoengine>`_
