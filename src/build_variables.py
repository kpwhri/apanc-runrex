import pathlib
import datetime
from loguru import logger

try:
    import runrex.post.variable_builder as vb
except ImportError as ie:
    logger.error('Need to install pandas: `pip install pandas`.')
    raise ie

VARIABLES = {
    'panc_with_competing_dx': ('+pancreatitis', '+competing_dx', '-competing_dx_NEGATIVE'),
    'panc_without_competing_dx': ('+pancreatitis', '=competing_dx_NEGATIVE'),
    'panc_with_pain': ('+pancreatitis', '+pain'),
    'panc_with_radiating_to_back_pain': ('+pancreatitis', '+pain_RADIATING_TO_BACK'),
    'panc_with_abdominal_pain': ('+pancreatitis', '+pain_ABD_PAIN'),
    'acute_panc_without_competing_dx': ('+pancreatitis_ACUTE', '=competing_dx_NEGATIVE'),
    'acute_panc_with_competing_dx': ('+pancreatitis', '+competing_dx', '-competing_dx_NEGATIVE'),
    'panc_with_sudden_onset_pain': ('+pancreatitis', '+pain_SUDDEN_ONSET'),
    'acute_panc_with_sudden_onset_pain': ('+pancreatitis_ACUTE', '+pain_SUDDEN_ONSET'),
    'acute_panc_imaging': ('+pancreatitis_ACUTE', '+is_radiology'),
    'panc_imaging': ('+pancreatitis', '+is_radiology'),
    'panc_with_nausea': ('+pancreatitis', '+nausea'),
    'panc_with_necrosis': ('+pancreatitis', '+necrosis'),
    'panc_with_fluid': ('+pancreatitis', '+fluid'),
    'panc_with_pseudocyst': ('+pancreatitis', '+pseudocyst'),
    'panc_with_recency': ('+pancreatitis', '+pain_RECENT'),
    'acute_panc_consistent': ('+pancreatitis_ACUTE', '+is_radiology'),
    'panc_consistent': ('+pancreatitis', '+is_radiology'),
    'necrosis_in_imaging': ('+is_radiology', '+necrosis'),
    'fluid_in_imaging': ('+is_radiology', '+fluid'),
    'pseudocyst_in_imaging': ('+is_radiology', '+pseudocyst'),
}

TRANSFORMERS = {
    'competing_dx': 'cdx',
    'pancreatits': 'pancr',
    'pseudocyst': 'pscyst',
}


def build_variables(file, metafile, sas_column_names=None):
    if sas_column_names:
        transformers = TRANSFORMERS
        max_col_length = 32
    else:
        transformers = None
        max_col_length = None
    res = vb.build_variables(file, metafile,
                             max_col_length=max_col_length, column_name_transformers=transformers,
                             extra_condition='is_radiology', **VARIABLES)
    outdir = file.parent
    res.to_csv(
        outdir / f'ap_final_variables_{datetime.datetime.now().strftime("%Y%m%d")}.csv',
        index=False
    )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(fromfile_prefix_chars='@!')
    parser.add_argument('-i', '--file', required=True, type=pathlib.Path,
                        help='Fullpath to file output CSV from `extract_and_load_json`.')
    parser.add_argument('-m', '--metafile', required=True, type=pathlib.Path,
                        help='Fullpath to CSV file containing metadata. Must at least contain:'
                             ' doc_id, patient_id, total_text_length, date. May also contain'
                             ' other variables as well.')
    parser.add_argument('--sas-column-names', action='store_true', default=False,
                        help='Limit column names to 32 characters.')
    args = parser.parse_args()
    build_variables(args.file, args.metafile, sas_column_names=args.sas_column_names)
