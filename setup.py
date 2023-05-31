from setuptools import setup

install_requires = [
    'numpy>=1.17.4',
    'pandas>=0.25.3',
    'scikit-learn>=0.22',
    'tensorflow-probability>=0.8.0',
    'wget>=3.2',
    'pyunpack>=0.1.2',
    'patool>=1.12',
]

setup(
    name='tft_self',
    version='1.0.0',
    packages=['libs', 'expt_settings', 'data_formatters'],
    url='https://github.com/adrenalin97/tft_self',
    license='',
    author='',
    author_email='',
    description='Self version of TFT google research repo',
    install_requires=install_requires,
    include_package_data=True,
)
