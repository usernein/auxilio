import re 
import setuptools
    
with open('requirements.txt') as fp:
    requirements = [line.strip() for line in fp]

with open('auxilio/VERSION') as fp:
    version = fp.read()

setuptools.setup(
    name="auxilio",
    version=version,
    author="Cezar H.",
    license="MIT",
    description="Cliente da API de consulta do Auxílio Emergencial",
    url="https://github.com/usernein/auxilio",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points = {
        'console_scripts': ['auxilio=auxilio.__main__:main'],
    }
)
