try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from pip.req import parse_requirements
from src.flask_generator import __version__

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='flask_generator',
    version=__version__,
    packages=['flask_generator'],
    package_dir={'flask_generator': 'src/flask_generator'},
    install_requires=reqs,
    author='Claude.Seo',
    author_email='ehdaudtj@gmail.com',
    url='https://github.com/SeoDongMyeong/flask-generator',
    description='Flask Project Generator',
    keywords=['flask', 'flask-project', 'flask-generator'],
    license='MIT License'
)
