from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='UNEP',
    version=version,
    description="",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone',
    author='Rok Garbas',
    author_email='rok@garbas.si',
    url='https://github.com/garbas/unep',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api',
        'plone.app.contenttypes',
        'plone.app.event[dexterity]',
        'plone.app.widgets[dexterity]',
        'collective.dexteritytextindexer',
        #'wildcard.foldercontents',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.robotframework',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
