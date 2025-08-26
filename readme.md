# Welcome
> "The Hipparcos and Tycho Catalogues" (ESA SP-1200, 1997).

This repository contains one of an archives of the HIPPARCOS satelite.

> ## Attention!
> This is NOT an official source. This repository just shares part of official data for everyone to have easier access.

## Files

- `hip_main.dat` - Was taken from https://cdsarc.cds.unistra.fr/ftp/cats/I/239/hip_main.dat
- `hip_main.csv` - Was converted from `hip_main.dat` via `dat_to_csv.py`

Files above contains data about stars found by HIPPARCOS.

Here are `118,218` lines.

# HEASARC Parameter Names

> [Source](https://heasarc.gsfc.nasa.gov/W3Browse/all/hipparcos.html)

The following is a correlation table of the Hipparcos Catalog fields, the parameter names as implemented by the CDS, and the HEASARC names for these parameters:

| Hipparcos Cat. Field | CDS Name      | HEASARC Name        | Description                                      |
| :------------------- | :------------ | :------------------ | :----------------------------------------------- |
| --                   | * New *       | Name                | /Catalog Designation                             |
| H0                   | Catalog       | * Not Displayed *   | /Catalogue (H=Hipparcos)                         |
| H1                   | HIP           | HIP_Number          | /Identifier (HIP number)                         |
| H2                   | Proxy         | Prox_10asec         | /Proximity flag                                  |
| H3                   | RAhms         | RA                  | /RA in h m s, ICRS (J1991.25)                    |
| H4                   | DEdms         | Dec                 | /Dec in deg ' ", ICRS (J1991.25)                 |
| H5                   | Vmag          | Vmag                | /Magnitude in Johnson V                          |
| H6                   | VarFlag       | Var_Flag            | /Coarse variability flag                         |
| H7                   | r_Vmag        | Vmag_Source         | /Source of magnitude                             |
| H8                   | RAdeg         | RA_Deg              | /RA in degrees (ICRS, Epoch-J1991.25)            |
| H9                   | DEdeg         | Dec_Deg             | /Dec in degrees (ICRS, Epoch-J1991.25)           |
| H10                  | AstroRef      | Astrom_Ref_Dbl      | /Reference flag for astrometry                   |
| H11                  | Plx           | Parallax            | /Trigonometric parallax                          |
| H12                  | pmRA          | pm_RA               | /Proper motion in RA                             |
| H13                  | pmDE          | pm_Dec              | /Proper motion in Dec                            |
| H14                  | e_RAdeg       | RA_Error            | /Standard error in RA*cos(Dec_Deg)               |
| H15                  | e_DEdeg       | Dec_Error           | /Standard error in Dec_Deg                       |
| H16                  | e_Plx         | Parallax_Error      | /Standard error in Parallax                      |
| H17                  | e_pmRA        | pm_RA_Error         | /Standard error in pmRA                          |
| H18                  | e_pmDE        | pm_Dec_Error        | /Standard error in pmDE                          |
| H19                  | DE:RA         | Crl_Dec_RA          | /(DE over RA)xCos(delta)                         |
| H20                  | Plx:RA        | Crl_Plx_RA          | /(Plx over RA)xCos(delta)                        |
| H21                  | Plx:DE        | Crl_Plx_Dec         | /(Plx over DE)                                   |
| H22                  | pmRA:RA       | Crl_pmRA_RA         | /(pmRA over RA)xCos(delta)                       |
| H23                  | pmRA:DE       | Crl_pmRA_Dec        | /(pmRA over DE)                                  |
| H24                  | pmRA:Plx      | Crl_pmRA_Plx        | /(pmRA over Plx)                                 |
| H25                  | pmDE:RA       | Crl_pmDec_RA        | /(pmDE over RA)xCos(delta)                       |
| H26                  | pmDE:DE       | Crl_pmDec_Dec       | /(pmDE over DE)                                  |
| H27                  | pmDE:Plx      | Crl_pmDec_Plx       | /(pmDE over Plx)                                 |
| H28                  | pmDE:pmRA     | Crl_pmDec_pmRA      | /(pmDE over pmRA)                                |
| H29                  | F1            | Reject_Percent      | /Percentage of rejected data                     |
| H30                  | F2            | Quality_Fit         | /Goodness-of-fit parameter                       |
| H31                  | ---           | * Not Displayed *   | /HIP number (repetition)                         |
| H32                  | BTmag         | BT_Mag              | /Mean BT magnitude                               |
| H33                  | e_BTmag       | BT_Mag_Error        | /Standard error on BTmag                         |
| H34                  | VTmag         | VT_Mag              | /Mean VT magnitude                               |
| H35                  | e_VTmag       | VT_Mag_Error        | /Standard error on VTmag                         |
| H36                  | m_BTmag       | BT_Mag_Ref_Dbl      | /Reference flag for BT and VTmag                 |
| H37                  | B-V           | BV_Color            | /Johnson BV colour                               |
| H38                  | e_B-V         | BV_Color_Error      | /Standard error on BV                            |
| H39                  | r_B-V         | BV_Mag_Source       | /Source of BV from Ground or Tycho               |
| H40                  | V-I           | VI_Color            | /Colour index in Cousins' system                 |
| H41                  | e_V-I         | VI_Color_Error      | /Standard error on VI                            |
| H42                  | r_V-I         | VI_Color_Source     | /Source of VI                                    |
| H43                  | CombMag       | Mag_Ref_Dbl         | /Flag for combined Vmag, BV, VI                  |
| H44                  | Hpmag         | Hip_Mag             | /Median magnitude in Hipparcos system            |
| H45                  | e_Hpmag       | Hip_Mag_Error       | /Standard error on Hpmag                         |
| H46                  | Hpscat        | Scat_Hip_Mag        | /Scatter of Hpmag                                |
| H47                  | o_Hpmag       | N_Obs_Hip_Mag       | /Number of observations for Hpmag                |
| H48                  | m_Hpmag       | Hip_Mag_Ref_Dbl     | /Reference flag for Hpmag                        |
| H49                  | Hpmax         | Hip_Mag_Max         | /Hpmag at maximum (5th percentile)               |
| H50                  | HPmin         | Hip_Mag_Min         | /Hpmag at minimum (95th percentile)              |
| H51                  | Period        | Var_Period          | /Variability period (days)                       |
| H52                  | HvarType      | Hip_Var_Type        | /Variability type                                |
| H53                  | moreVar       | Var_Data_Annex      | /Additional data about variability               |
| H54                  | morePhoto     | Var_Curv_Annex      | /Light curve Annex                               |
| H55                  | CCDM          | CCDM_Id             | /CCDM identifier                                 |
| H56                  | n_CCDM        | CCDM_History        | /Historical status flag                          |
| H57                  | Nsys          | CCDM_N_Entries      | /Number of entries with same CCDM                |
| H58                  | Ncomp         | CCDM_N_Comp         | /Number of components in this entry              |
| H59                  | MultFlag      | Dbl_Mult_Annex      | /Double and or Multiple Systems flag             |
| H60                  | Source        | Astrom_Mult_Source  | /Astrometric source flag                         |
| H61                  | Qual          | Dbl_Soln_Qual       | /Solution quality flag                           |
| H62                  | m_HIP         | Dbl_Ref_ID          | /Component identifiers                           |
| H63                  | theta         | Dbl_Theta           | /Position angle between components               |
| H64                  | rho           | Dbl_Rho             | /Angular separation of components                |
| H65                  | e_rho         | Rho_Error           | /Standard error of rho                           |
| H66                  | dHp           | Diff_Hip_Mag        | /Magnitude difference of components              |
| H67                  | e_dHp         | dHip_Mag_Error      | /Standard error in dHp                           |
| H68                  | Survey        | Survey_Star         | /Flag indicating a Survey Star                   |
| H69                  | Chart         | ID_Chart            | /Identification Chart                            |
| H70                  | Notes         | Notes               | /Existence of notes                              |
| H71                  | HD            | HD_Id               | /HD number <III 135>                             |
| H72                  | BD            | BD_Id               | /Bonner DM <I 119>, <I 122>                      |
| H73                  | CoD           | CoD_Id              | /Cordoba Durchmusterung (DM) <I 114>             |
| H74                  | CPD           | CPD_Id              | /Cape Photographic DM <I 108>                    |
| H75                  | (V-I)red      | VI_Color_Reduct     | /VI used for reductions                          |
| H76                  | SpType        | Spect_Type          | /Spectral type                                   |
| H77                  | r_SpType      | Spect_Type_Source   | /Source of spectral type                         |
| --                   | * New *       | Class               | /HEASARC BROWSE classification                   |

# License
[DO WHAT THE FUCK YOU WANT TO](LICENSE)

Don't forget about conditions of ESA, include the following line into your work:
> "The Hipparcos and Tycho Catalogues" (ESA SP-1200, 1997).
