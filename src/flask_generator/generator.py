# -*- coding: utf-8 -*-
import os
import requests
import jinja2
import exceptions


def enum(**enums):
    # support enum type
    return type('Enum', (), enums)


PWD = os.path.dirname(os.path.realpath(__file__))
APP_TYPES = enum(SIMPLE=1, LARGE=2)


def get_file_map(app_type, app_name):
    '''
    - dirs
    Enter the name of the folder to be created.

    - remote_files
    The first argument enter the filename to be used in the project.
    Enter the URL to download as the second argument.

    - local_files
    The first argument is the name of the file in the flask generator project.
    In the second argument, enter the filename to be used in the project.
    '''

    if app_type == APP_TYPES.SIMPLE:
        file_map = {
            'dirs': [
                'templates',
                'static/css',
                'static/js',
                'static/img'
            ],
            'remote_files': [
                ('static/css/bootstrap.min.css', 'URL'),
                ('static/js/bootstrap.min.js', 'URL'),
                ('static/js/jquery.min.js', 'URL')
            ],
            'local_files': [
                ('README.md', 'templates/README.md.j2'),
                ('.gitignore', 'templates/.gitignore'),
                ('config.py', 'config/prod.py.j2'),
                ('app.py', 'templates/app.py'),
                ('requirements.txt', 'templates/requirements.txt'),
                ('templates/layout.html', 'templates/html/layout.html'),
                ('templates/index.html', 'templates/html/index.html')
            ]
        }
    elif app_type == APP_TYPES.LARGE:
        file_map = {
            'dirs': [
                'config',
                'bin',
                app_name,
                app_name + '/templates',
                app_name + '/static/css',
                app_name + '/static/js',
                app_name + '/static/img',
                app_name + '/models',
                app_name + '/api',
                app_name + '/views'
            ],
            'remote_files': [
                ('static/css/bootstrap.min.css', 'URL'),
                ('static/js/bootstrap.min.js', 'URL'),
                ('static/js/jquery.min.js', 'URL')
            ],
            'local_files': [
                ('README.md', 'templates/README.md.j2'),
                ('.gitignore', 'templates/.gitignore'),
                ('config/prod.py', 'config/prod.py.j2'),
                ('config/dev.py', 'config/dev.py.j2'),
                ('manage.py', 'templates/manage.py'),
                ('requirements.txt', 'templates/requirements.txt'),
                (app_name + '/app.py', 'templates/app.py'),
                (app_name + '/templates/layout.html',
                 'templates/html/layout.html'),
                (app_name + '/templates/index.html',
                 'templates/html/index.html'),
                (app_name + '/api/__init__.py', 'templates/api/__init__.py')
            ]
        }
    else:
        raise exceptions.NotSupportAppTypeException(
            'not support app_type: %s' % app_type)
    return file_map


def generate_random_hex():
    return os.urandom(24).encode('hex')


def download_file(files):
    for f in files:
        dest_name = f[0]
        url = f[1]
        r = requests.get(url)
        with open(dest_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)


def create_virtualenv():
    # After creating the virtual environment, install the library
    command = 'virtualenv venv'
    os.system(command)


def install_lib_with_virtualenv():
    command = 'source venv/bin/activate;' \
              'pip install -r requirements.txt'
    os.system(command)


def configure_git(github_user, github_repo, is_git_push=True):
    git_url = 'https://github.com/' + github_user + '/' + github_repo + '.git'
    os.system('git init')
    os.system('git remote add origin %s' % git_url)
    os.system('git add --all')
    os.system('git commit -m "project initialize"')
    if is_git_push:
        os.system('git push origin master')


def render(filename, context):
    loader = jinja2.FileSystemLoader(PWD)
    env = jinja2.Environment(loader=loader)
    template = env.get_template(filename)
    return template.render(context)


class AppGenerator(object):
    def __init__(self, app_type, app_name):
        self.app_type = app_type
        self.app_name = app_name
        self.destination_path = PWD

    def init_app(self):
        os.mkdir(self.app_name)
        os.chdir(self.app_name)
        create_virtualenv()

    def build_app(self):
        file_map = get_file_map(self.app_type, self.app_name)

        # create dirs
        for d in file_map['dirs']:
            os.makedirs(d)

        # create local_files
        for lf in file_map['local_files']:
            file_ext = os.path.splitext(lf[1])[1]
            if file_ext == '.j2':
                context = {
                    'SECRET_KEY': generate_random_hex(),
                    'APP_NAME': self.app_name
                }
                data = render(lf[1], context)
            else:
                path = os.path.join(self.destination_path, lf[1])
                data = self.load_file_data(path)
            with open(lf[0], 'w') as fp:
                fp.write(data)

    def load_file_data(self, file_path):
        with open(file_path, 'r') as fp:
            file_data = fp.read()
        return file_data


if __name__ == '__main__':
    gen = AppGenerator(APP_TYPES.SIMPLE, 'app')
    gen.init_app()
    gen.build_app()
