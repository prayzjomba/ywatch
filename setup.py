from setuptools import setup, find_packages


DESCRIPTION = "Watch Youtube videos with mpv while saving to disk."
LICENSE="GPLv3+"

setup(
    name="ywatch",
    version="0.6.3",
    author="Prayz Jomba",
    license=LICENSE,
    author_email="prayzjomba@protonmail.com",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/prayzjomba/yWatch",
    keywords=['mpv', 'youtube watch', 'ywatch', 'youtube-dl', 'youtube', 'mpv save', 'yw'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: End Users/Desktop",
        "Environment :: Console",
        "Topic :: Multimedia :: Video",
        "Operating System :: POSIX :: Linux",
    ],

    packages=find_packages(),
    install_requires=['func-timeout', 'rich', 'pyperclip'],
    entry_points={'console_scripts': ['yw=ywatch:yw']},
    python_requires=">=3.6",
)
