from setuptools import setup, find_packages


setup(
    name='galleryserve',
    version='0.1.10',
    description='Adapted from imageserve to fit broader gallery needs such as video embedding and content for controls.',

    author='Imaginary Landscape',
    author_email='dbertrand@imagescape.com',

    install_requires=(
        'Pillow',
    ),
    url='https://github.com/ImaginaryLandscape/django-galleryserve',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=('ez_setup', 'examples', 'tests')),
)
