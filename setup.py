from distutils.core import setup


def readme():
	"""Import the README.md Markdown file and try to convert it to RST format."""
	try:
		import pypandoc
		return pypandoc.convert('README.md', 'rst')
	except(IOError, ImportError):
		with open('README.md') as readme_file:
			return readme_file.read()


setup(
	name='Pokemon card image classifier',
	version='0.1',
	description='Pokemon card image classifier application',
	long_description=readme(),
	classifiers=[
		'Programming Language :: Python :: 3',
	],
	install_requires=[
		'pypandoc>=1.4'
	],
	url='https://github.com/Evbor/Pkmn_card_classifier',
	author='Evan Borras',
	author_email='',
	license='MIT',
	packages=['base_set_classifier'],
)