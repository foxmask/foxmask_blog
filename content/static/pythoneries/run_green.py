from relatorio.templates.opendocument import Template
from maraicher import potager
basic = Template(source=None, filepath='Geant-Vert.odt')
basic_generated = basic.generate(o=potager).render()
file('Geant-Vert1.odt', 'wb').write(basic_generated.getvalue())
