from pydantic import BaseModel
from typing import Optional, Union
from datetime import date


class Drug(BaseModel):
    cid: int
    molecular_formula: Optional[str] = None
    molecular_weight: Optional[str] = None
    smiles: Optional[str] = None
    canonical_smiles: Optional[str] = None
    isomeric_smiles: Optional[str] = None
    inchi: Optional[str] = None
    inchikey: Optional[str] = None
    iupac_name: Optional[str] = None
    xlogp: Optional[float] = None
    exact_mass: Optional[str] = None
    monoisotopic_mass: Optional[str] = None
    tpsa: Optional[float] = None
    complexity: Optional[int] = None
    charge: Optional[int] = None
    h_bond_donor_count: Optional[int] = None
    h_bond_acceptor_count: Optional[int] = None
    rotatable_bond_count: Optional[int] = None
    heavy_atom_count: Optional[int] = None
    isotope_atom_count: Optional[int] = None
    atom_stereo_count: Optional[int] = None
    defined_atom_stereo_count: Optional[int] = None
    undefined_atom_stereo_count: Optional[int] = None
    bond_stereo_count: Optional[int] = None
    defined_bond_stereo_count: Optional[int] = None
    undefined_bond_stereo_count: Optional[int] = None
    covalent_unit_count: Optional[int] = None
    volume_3d: Optional[float] = None
    x_steric_quadrupole_3d: Optional[float] = None
    y_steric_quadrupole_3d: Optional[float] = None
    z_steric_quadrupole_3d: Optional[float] = None
    feature_count_3d: Optional[int] = None
    feature_acceptor_count_3d: Optional[int] = None
    feature_donor_count_3d: Optional[int] = None
    feature_anion_count_3d: Optional[int] = None
    feature_cation_count_3d: Optional[int] = None
    feature_ring_count_3d: Optional[int] = None
    feature_hydrophobe_count_3d: Optional[int] = None
    conformer_model_rmsd_3d: Optional[float] = None
    effective_rotor_count_3d: Optional[float] = None
    conformer_count_3d: Optional[int] = None
    fingerprint_2d: Optional[bytes] = None
    title: Optional[str] = None
    patent_count: Optional[int] = None
    patent_family_count: Optional[int] = None
    literature_count: Optional[int] = None
    annotation_types: Optional[str] = None
    annotation_type_count: Optional[int] = None
    chembl_id: Optional[int] = None
    standard_name: Optional[str] = None
    synonyms: Optional[str] = None
    date_added: Optional[date] = None
