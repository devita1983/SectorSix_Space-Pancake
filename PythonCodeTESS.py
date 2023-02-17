from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
import astropy.units as u


# Define as coordenadas do objeto
ra = 20.42841
dec = 44.10430
coords = SkyCoord(ra, dec, unit=(u.deg, u.deg), frame='icrs')


# Define o setor desejado
sector = 6


# Busca os setores que cobrem as coordenadas do objeto
sector_table = Tesscut.get_sectors(coordinates=coords)


# Verifica se o objeto está no setor
in_sector = str(sector) in sector_table['sectorName']


if in_sector:
    # Faz o corte na imagem para as coordenadas do objeto
    cutout = Tesscut.get_cutouts(coordinates=coords, size=10, sector=sector, product="SPOC")[0]
    hdu = cutout[0].data
    # Imprime a imagem
    plt.imshow(hdu, origin='lower', cmap='gray')
    plt.colorbar()
    plt.show()
else:
    print("O objeto não está no setor desejado.")

