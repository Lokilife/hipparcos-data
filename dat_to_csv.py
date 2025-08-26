#!/usr/bin/env python3
"""
dat_to_csv.py

Converts Hipparcos DAT (pipe '|' separated, 78 fields H0..H77) to CSV.
https://heasarc.gsfc.nasa.gov/W3Browse/all/hipparcos.html

Example:
    python dat_to_csv.py hip_main.dat hip_main.csv
"""

import csv
import argparse
import sys

HEADER = [
    "Name",                 # H0
    "HIP_Number",           # H1
    "Unused_H2",            # H2 (Proxy / Prox flag) -- kept for position
    "RA",                   # H3 (RA h m s)
    "Dec",                  # H4 (Dec d m s)
    "Vmag",                 # H5
    "Unused_H6",            # H6 (VarFlag in original - kept position)
    "Vmag_Source",          # H7 (r_Vmag)
    "RA_Deg",               # H8
    "Dec_Deg",              # H9
    "Astrom_Ref_Dbl",       # H10
    "Parallax",             # H11
    "pm_RA",                # H12
    "pm_Dec",               # H13
    "RA_Error",             # H14
    "Dec_Error",            # H15
    "Parallax_Error",       # H16
    "pm_RA_Error",          # H17
    "pm_Dec_Error",         # H18
    "Crl_Dec_RA",           # H19
    "Crl_Plx_RA",           # H20
    "Crl_Plx_Dec",          # H21
    "Crl_pmRA_RA",          # H22
    "Crl_pmRA_Dec",         # H23
    "Crl_pmRA_Plx",         # H24
    "Crl_pmDec_RA",         # H25
    "Crl_pmDec_Dec",        # H26
    "Crl_pmDec_Plx",        # H27
    "Crl_pmDec_pmRA",       # H28
    "Reject_Percent",       # H29
    "Quality_Fit",          # H30
    "HIP_repeated",         # H31 (not displayed in HEASARC; repetition) 
    "BT_Mag",               # H32
    "BT_Mag_Error",         # H33
    "VT_Mag",               # H34
    "VT_Mag_Error",         # H35
    "BT_Mag_Ref_Dbl",       # H36
    "BV_Color",             # H37
    "BV_Color_Error",       # H38
    "BV_Mag_Source",        # H39
    "VI_Color",             # H40
    "VI_Color_Error",       # H41
    "VI_Color_Source",      # H42
    "Mag_Ref_Dbl",          # H43
    "Hip_Mag",              # H44
    "Hip_Mag_Error",        # H45
    "Scat_Hip_Mag",         # H46
    "N_Obs_Hip_Mag",        # H47
    "Hip_Mag_Ref_Dbl",      # H48
    "Hip_Mag_Max",          # H49
    "Hip_Mag_Min",          # H50
    "Var_Period",           # H51
    "HIP_Var_Type",         # H52
    "Var_Data_Annex",       # H53
    "Var_Curv_Annex",       # H54
    "CCDM_ID",              # H55
    "CCDM_History",         # H56
    "CCDM_N_Entries",       # H57
    "CCDM_N_Comp",          # H58
    "Dbl_Mult_Annex",       # H59
    "Astrom_Mult_Source",   # H60
    "Dbl_Soln_Qual",        # H61
    "Dbl_Ref_ID",           # H62
    "Dbl_Theta",            # H63
    "Dbl_Rho",              # H64
    "Rho_Error",            # H65
    "Diff_Hip_Mag",         # H66
    "DHip_Mag_Error",       # H67
    "Survey_Star",          # H68
    "ID_Chart",             # H69
    "Notes",                # H70
    "HD_ID",                # H71
    "BD_ID",                # H72
    "CoD_ID",               # H73
    "CPD_ID",               # H74
    "VI_Color_Reduct",      # H75
    "Spect_Type",           # H76
    "Spect_Type_Source"     # H77
]

EXPECTED_FIELDS = len(HEADER)  # should be 78


def parse_line_to_fields(line: str) -> list:
    raw = line.rstrip('\n\r')
    parts = raw.split('|', EXPECTED_FIELDS - 1)
    if len(parts) < EXPECTED_FIELDS:
        parts += [''] * (EXPECTED_FIELDS - len(parts))
    if len(parts) > EXPECTED_FIELDS:
        parts = parts[:EXPECTED_FIELDS]
    parts = [p.strip() for p in parts]
    return parts


def convert_file(infile: str, outfile: str, allow_all: bool = False):
    with open(infile, 'r', encoding='latin-1') as fin, open(outfile, 'w', newline='', encoding='utf-8') as fout:
        writer = csv.writer(fout)
        writer.writerow(HEADER)
        line_no = 0
        written = 0
        for raw_line in fin:
            line_no += 1
            if not raw_line.strip():
                continue
            if (not allow_all) and (not raw_line.startswith('H|')):
                continue
            fields = parse_line_to_fields(raw_line)
            if all(f == '' for f in fields):
                continue
            writer.writerow(fields)
            written += 1
        print(f"Lines read: {line_no}. Rows written to CSV: {written}.")


def main():
    ap = argparse.ArgumentParser(description="Convert Hipparcos DAT (| separated) to CSV")
    ap.add_argument("input", help="Input DAT file")
    ap.add_argument("output", help="Output CSV file")
    args = ap.parse_args()
    try:
        convert_file(args.input, args.output)
    except FileNotFoundError as e:
        print("File not found:", e, file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
