try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from pip.req import parse_requirements
from src.flask_app_generator import __version__

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='flask_app_generator',
    version=__version__,
    packages=['flask-app-generator'],
    package_dir={'flask-app-generator': 'src/flask-app-generator'},
    install_requires=reqs,
    author='Claude.Seo',
    author_email='ehdaudtj@gmail.com',
    url='https://github.com/SeoDongMyeong/flask-app-generator',
    description='Flask Project Generator',
    keywords=['flask', 'flask-project', 'flask-generator'],
    license='MIT License'
)
