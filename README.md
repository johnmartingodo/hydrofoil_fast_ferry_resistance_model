# hydrofoil_fast_ferry_resistance_model
Digital resources for the paper entitled [_"A Resistance Model for Hydrofoil 
Fast Ferries"_](https://doi.org/10.1016/j.oceaneng.2024.117503), by John Martin Kleven Godø, Sverre Steen, and Odd Magnus 
Faltinsen.

## About
This repository contains results from a research project on the hydrodynamic
modelling fully foil supported fast ferries. An automatic design algorithm was
developed, and a series of hydrofoil system designs were analysed through 
a wide span of design parameters, in the form of design speed and vessel mass. 
Details of the modelling and analysis approach can be found in the paper. This 
repository constitutes the digital attachments for the work, and presents 
datasets for the following:

- Resistance estimates at design speed
- Hydrofoil system weight estimates, with and without a buoyancy correction

## Usage
The data directory contains subdirectories for resistance and weight results 
for the hydrofoil systems presented in the paper. A DataExtractor class can 
be found in the data_extraction.py file. Furthermore, the 
data_extraction_test.ipynb notebook presents an example of how to extract and 
interpolate in the presented datasets.


## Authors

  - [**John Martin Kleven Godø**](https://www.ntnu.no/ansatte/john.martin.godo)
  - [**Sverre Steen**](https://www.ntnu.no/ansatte/sverre.steen)
  - [**Odd Magnus Faltinsen**](https://www.ntnu.no/ansatte/odd.faltinsen)

## License

This project is licensed under the [EUROPEAN UNION PUBLIC LICENCE v. 1.2](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments
This repository contains results of a research project that was 
conducted at the NTNU Department of Marine Technology. 
The project was funded by the enabling Zero Emission passenger 
Vessel Services (ZEVS) research project (NFR grant No. 320659) and 
SFI Smart Maritime (NFR grant No. 237917). 