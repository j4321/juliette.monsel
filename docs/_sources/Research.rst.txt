Research
========

See also the *Dynamics and thermodynamics of nanoscale devices* group `webpage <https://sites.google.com/site/splettchalmers/research-group>`_.

Quantum thermodynamics
----------------------

.. image:: assets/thermo.svg
    :width: 500

Thermodynamics was developed in the 19th century to study steam engines using the cyclical transformations of a
working substance to extract heat from thermal baths and convert it into work, possibly stored in a battery. This applied
science eventually led to the development of fundamental concepts such as irreversibility. Quantum thermodynamics
aims at revisiting these results when the working substances, baths and batteries become quantum systems. See for instance 
the book `Thermodynamics in the quantum regime: fundamental aspects and new directions <https://link.springer.com/book/10.1007/978-3-319-99046-0>`_ 
(most of the chapters can also be found on arXiv) for a review of the field.

My research mainly focus on the thermodynamics of quantum open systems, in regimes relevant for experimental implementations, both in quantum optics and quantum transport.

- PhD dissertation: `Quantum Thermodynamics and Optomechanics <https://tel.archives-ouvertes.fr/tel-02517050>`_

Quantum optics
--------------

.. rubric:: Cavity optomechanics

.. image:: assets/cavity.svg
    :width: 420

The light field in an optical cavity interacts with a mechanical resonator via radiation pressure. In a typical setup, the cavity has one moving end-mirror which constitutes the mechanical degree of freedom. When the mechanical position varies, the cavity length changes which modifies its resonance frequency. On the other hand, when adding more photons in the cavity, the radiation pressure on the mirror increases, which shifts the resonator's rest position. This optomechanical coupling gives a high degree of control on the dynamics of the mechanical resonator through the cavity, making it possible to use this platform for applications such as ground state cooling, sensing or quantum manipulations of the mechanics. It also makes it of great interest for thermodynamics: work and entropy measurements, heat engines proposals, ...


In collaboration with `Witlef Wieczorek's experimental group <https://wieczorek-lab.com>`_, we have studied the thermodynamic performance of optomechanical cooling,

- *Optomechanical cooling with coherent and squeezed light: The thermodynamic cost of opening the heat valve* -- `Phys. Rev. A 103, 063519 (2021) <https://doi.org/10.1103/PhysRevA.103.063519>`_  -- `Video of my talk at the TIQuR workshop <https://www.youtube.com/watch?v=5BT9kkFDPCQ>`_
   
and modeled all the optomechanical effects taking place in a microcavity with a suspended photonic crystal mirror.

- *Integrated microcavity optomechanics with a suspended photonic crystal mirror above a distributed Bragg reflector* -- `Opt. Express 31, 30212 (2023) <https://doi.org/10.1364/OE.496447>`_

- *Dissipative and dispersive cavity optomechanics with a frequency-dependent mirror* -- `Phys. Rev. A 109, 043532 (2024) <https://doi.org/10.1103/PhysRevA.109.043532>`_

- *Coherent feedback control for cavity optomechanical systems with a frequency-dependent mirror* -- `Phys. Rev. A 111, 013506 (2025) <https://doi.org/10.1103/PhysRevA.111.013506>`_



.. rubric::  Hybrid optomechanical systems

.. image:: assets/hybrid.svg
    :width: 430
    
This is a different kind of optomechanical system where the optical part is a qubit instead of a cavity. 
The qubit’s transition frequency is modulated by the vibrations of the mechanical system. 
The mechanical degree of freedom exchanges work with the qubit and therefore behaves like a dispersive battery, i.e. whose natural frequency is very
different from the one of the qubit’s transition. The electromagnetic environment of the qubit plays the role of the thermal bath.
The fluctuations of the mechanical energy are equal to the fluctuations of work, which allows the direct measurement
of entropy production. As a result, hybrid optomechanical systems are promising for experimentally testing fluctuation
theorems in open quantum systems.

- *An Autonomous Quantum Machine to Measure the Thermodynamic Arrow of Time* -- `npj Quantum Inf. 4, 1 (2018) <https://doi.org/10.1038/s41534-018-0109-8>`_  -- `Video of my talk at the II Workshop on Quantum Information and Thermodynamics <https://www.youtube.com/watch?v=jhzOAz8H2UU>`_
  
.. ~- *Evaporative cooling and amplification in hybrid optomechanical systems* -- in preparation
     
        
.. rubric::  One-dimensional atoms   

.. image:: assets/WGQED.svg
    :width: 350    

A qubit is embeded in a one-dimenstional waveguide and the battery is the waveguide mode of same frequency as
the qubit’s transition. Therefore, this is a resonant battery, unlike in the optomechanical case, which makes this platform 
especially promising to study the impact of coherences on work exchanges.


- *The Energetic Cost of Work Extraction* -- `Phys. Rev. Lett. 124, 130601 (2020) <https://doi.org/10.1103/PhysRevLett.124.130601>`_ -- `Video of my talk at the QTD2020 conference <https://www.youtube.com/watch?v=AItlKhvJBt0>`_


Electronic systems
------------------


.. rubric::  Mesoscopic conductors

.. image:: assets/conductor.svg
    :width: 450
    
We study transport in mesoscopic conductors connected to two terminal or more with a scattering approach. We are particularly interested in properties of the current fluctuations in nonequilibrium situations where the average current is zero (for spin, charge, heat, ...).

- *Charge, spin, and heat shot noises in the absence of average currents: Conditions on bounds at zero and finite frequencies* -- `Phys. Rev. B 107, 075409 (2023) <https://journals.aps.org/prb/abstract/10.1103/PhysRevB.107.075409>`_  


.. rubric::  Quantum dots

.. image:: assets/transport.svg
    :width: 450
    
*Driven quantum dot*
    
We study a quantum dot weakly coupled to two baths, namely two electron reservoirs characterize by a temperature and a chemical potential. Electrons can tunnel (sequentially) in and out of the quantum dot. Parameters of this system can be driven (energies, chemical potentials, tunnel couplings, temperatures, ...). We investigate particle and energy currents for slow periodic driving up to the first non-adiabatic correction using a master equation approach and a dissipative symmetry of the system called fermionic duality, We are particularly interested in the role of the onsite electron-electron interaction, both in the usual case of Coulomb repulsion and the case of effective attractive interaction.
    
- *Geometric energy transport and refrigeration with driven quantum dots* -- `Phys. Rev. B 106, 035405 (2022) <https://doi.org/10.1103/PhysRevB.106.035405>`_  -- `My poster at the QTD2022 conference <https://blogs.qub.ac.uk/qtd2022/wp-content/uploads/sites/310/2022/06/poster_Juliette_Monsel.pdf>`_

and beyond the first correction, for a more traditional four-stroke refrigeration cycle.

- *Non-geometric pumping effects on the performance of interacting quantum-dot heat engines* -- `Eur. Phys. J. Spec. Top. 232, 3267–3272 (2023) <https://arxiv.org/abs/2303.15420>`_ 

We also use fermionic duality at the jump operator level to explore the stochastic thermodynamics of such kind of systems.

*Mpemba effect*

We explore the Mpemba effect, an anomalous relaxation effect where the system relaxes faster from a state farther from equilibrium 
than from another state, closer to equilibrium, in a quantum dot weakly coupled to a single bath. We investigate in particular the role of the electron-electron interaction, which has an important impact on the relaxation rates involved in this effect.

- *Role of electron-electron interaction in the Mpemba effect in quantum dots* -- `J. Phys.: Condens. Matter 37, 195302 (2025) <https://arxiv.org/abs/2303.15420>`_ 

*Capacitively coupled quantum dots*

Capacitively coupled quantum dots in contact with several baths can be used to implement an autonomous demon-type system where a useful task (cooling, power generation ...) is performed in the absence of average energy flow from the resource region into the working substance. 
We use a combination of stochastic thermodynamics and full counting statistics to understand the performances of the device, in particular in term of precision, and the role of information exchanges.

- *Role of nonequilibrium fluctuations and feedback in a quantum dot thermal machine* -- `Video of my talk at the Quantum Energy Initiative workshop 2023 <https://www.youtube.com/watch?v=Y7QskAPNSfQ>`_ 
- *Autonomous demon exploiting heat and information at the trajectory level* -- `Phys. Rev. B 111, 045419 (2025) <https://arxiv.org/abs/2409.05823>`_ 
- *Precision of an autonomous demon exploiting nonthermal resources and information* -- `arXiv:2510.14578 <https://arxiv.org/abs/2510.14578>`_ 




.. rubric::  Suspended carbon nanotubes

.. image:: assets/CNT.svg
    :width: 350
    

These devices combine electronic transport and mechanical degrees of freedom which makes them a very promising platform for thermodynamics. Charge or spin qubits can be created inside the nanotube, making these devices similar to hybrid optomechanical systems. 

I am taking part in the `FQxI-funded <https://fqxi.org/programs/zenith-grants/>`_ project Nanomechanics in the solid-state for quantum information thermodynamics led by `Natalia Ares <https://www.natalia-ares.com/>`_ (Oxford University, UK).

- *Ultrastrong coupling between electron tunnelling and mechanical motion* --  `Phys. Rev. Research 4, 043168  (2022) <https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.4.043168>`_

- *Stability of long-sustained oscillations induced by electron tunneling* --  `Phys. Rev. Research 6, 013291  (2024)  <https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.013291>`_

- *Extra cost of erasure due to quantum lifetime broadening* --  `Phys. Rev. A 112, L010601 (2025) <https://arxiv.org/abs/2410.02546>`_

- *Coupling a single spin to high-frequency motion* --  `arXiv:2402.19288 <https://arxiv.org/abs/2402.19288>`_

- *Sources of nonlinearity in the response of a driven nano-electromechanical resonator* --  `arXiv:2509.12830 <https://arxiv.org/abs/2509.12830>`_


