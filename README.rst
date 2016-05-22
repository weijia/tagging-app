=============================
tagging-app
=============================

.. image:: https://badge.fury.io/py/tagging-app.png
    :target: https://badge.fury.io/py/tagging-app

.. image:: https://travis-ci.org/weijia/tagging-app.png?branch=master
    :target: https://travis-ci.org/weijia/tagging-app

"An tagging application"

Documentation
-------------

The full documentation is at https://tagging-app.readthedocs.org.

Quickstart
----------

Install tagging-app::

    # The following are not available yet
    # pip install tagging-app

    clone to local to use this app

Then use it in a project:

In HTML template file, add js files::

    {% block js %}
        {{ block.super }}
        {% include "tagging_app/tagging_head_inc.html" %}
    {% endblock %}

In HTML template file, add js files::

    {% load gen_tag_attr %}

    <a class="tagged-item"
       {{ node|gen_tag_attr }}>Tags
    </a>


The above codes will generate the following element::

    <a class="tagged-item"
        objectId="1" tags="tag1, tag2" contentType="20">Tags
    </a>


Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
