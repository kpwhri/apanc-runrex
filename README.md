





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div>
  <p>
    <a href="https://github.com/kpwhri/apanc-runrex">
      <img src="images/logo.png" alt="Logo">
    </a>
  </p>

  <h3 align="center">Acute Pancreatitis Runrex</h3>

  <p>
    Feature extraction for developing an algorithm to identify acute pancreatitis cases.
    Additional steps will require use of these variables to build a predictive algorithm.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.8+
* runrex package: https://github.com/kpwhri/runrex

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/kpwhri/apanc-runrex.git
```
2. Install requirements
```sh
pip install -r requirements.txt -r requirements-dev.txt
```
3. Run tests.
```sh
set/export PYTHONPATH=src
pytest tests
```


<!-- USAGE EXAMPLES -->
## Usage

The first entry (1. Running Runrex Application) is the primary use. This will identity 'concepts' in the text.
 Secondary use converts these 'concepts' into various other formats. For these, additional packages (`pandas` and `sqlalchemy`) are required.
 Install with `pip install -r requirements-extra.txt`.

### 1. Running Runrex Application

* Build a configuration file as defined in [runrex](https://github.com/kpwhri/runrex)
    - Full details defined in that project's [schema.py](https://github.com/kpwhri/runrex/blob/master/src/runrex/schema.py)
* Run the application
    - `python src/run.py runrex.conf.(py|json|yaml)`
* Organize outputs
    - `python src/extract_and_load_json.py  --file [OUTPUT file from RUNREX; ends in jsonl] --version runrex`

### 2. Build Variables
Build secondary variables for subsequent analysis. You can use the pre-built variables (default) or supply your own.
 These secondary variables build on the output of running regex.

To force all output columns to fit within the 32 characters required by a SAS dataset, add the option `--sas-column-names`.

* `python src/build_variables.py --file [PATH to output from 'extract_and_load_json' above] --metafile [PATH to table created in step #1]`

### 3. Build Review Lists
Build CSV files of each algorithm/category for manual review of algorithms/categories output by `run.py`.

#### Step A
* First, you'll need to take a look at the runrex configuration file (something like 'config.py' which is supplied as input?). Open that up and see if you have a line that looks like this:
    - `'loginfo': {'directory': r'C:\path\to\somewhere'}`

* If so, locate that file and use it as the `--log-file` in Step B (you can skip to Step B).
* Otherwise, re-run runrex with the `loginfo` option specified.

#### Step B

* `python build_review_lists.py --output-file [PATH  to runrex output file; original jsonl or the transformed to csv] --log-file [PATH to log file from step B] --metafile [PATH to CSV table created in step #1]`
*  This will generate a series of CSV files (randomly ordered) for manual review. There are currently offset problems in runrex, so this does not currently work as well as desired.

## Variables Identified

Variables (called 'algorithms') are broken down into various 'categories'. Either can be used in building features.

### Output Variable Names
The names of the algorithms/categories below should provide insight into the automatically-generated names of columns in the output.
Some abbreviations:

* `panc`: pancreatitis
* `apanc`: acute pancreatitis
* `is_r`: from radiology/imaging
* `all`: all mentions included (not grouped by date/encounter)

When the column names are reduced (when using the `--sas-column-names` parameter), some additional abbreviations may be used:

* `cdx`: competing diagnosis
* `pancr`: pancreatitis
* `pscyst`: pseudocyst

Certain category names might also appear truncated.

### Variable List

Complete data dictionaries are included in the [res/ directory](res):
* Complete variable names: [data-dictionary.csv](res/data-dictionary.csv)
* Reduced variable names for SAS: [data-dictionary-sas.csv](res/data-dictionary-sas.csv)

|Algorithm|Category|Description|
|---|---|---|
|[pain](src/apanc_nlp/algo/pain.py)|ABD_PAIN|Abdominal pain|
|[pain](src/apanc_nlp/algo/pain.py)|RADIATING_TO_BACK|Pain described as radiating to the back|
|[pain](src/apanc_nlp/algo/pain.py)|ACUTE|Acute pain|
|[pain](src/apanc_nlp/algo/pain.py)|EPIGASTRIC|Epigastric pain|
|[pain](src/apanc_nlp/algo/pain.py)|CHEST|Chest pain|
|[pain](src/apanc_nlp/algo/pain.py)|CHRONIC|Chronic Pain|
|[pain](src/apanc_nlp/algo/pain.py)|RECENT|Recent pain (in weeks)|
|[pain](src/apanc_nlp/algo/pain.py)|VERY_RECENT|Recent pain (in days)|
|[pain](src/apanc_nlp/algo/pain.py)|LONG_AGO|Non-recent pain (in months)|
|[pain](src/apanc_nlp/algo/pain.py)|SUDDEN_ONSET|Sudden onset pain|
|[pain](src/apanc_nlp/algo/pain.py)|WORSENING|Pain described as worsening|
|[pain](src/apanc_nlp/algo/pain.py)|UNKNOWN_DURATION|Likely unrecognized time format for recency|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|POSITIVE|Generic pancreatitis|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|ACUTE|Acute pancreatitis|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|CHRONIC|Chronic pancreatitis|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|INFLAMMATION|inflammation|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|INTERSTITIAL|interstitial pancreatitis|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|PERI_INFLAMMATION|Peri-inflammation|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|CONSISTENT_WITH|Radiology conclusion-like language (e.g., consistent with)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|ACUTE_APPENDICITIS|Presence of acute appendicitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|GALL_BLADDER_DISEASE|Presence of gall bladder disease (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|BOWEL_MOVEMENTS|Presence of bowel_movements (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|COLANGITIS|Presence of colangitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|CHRONIC_PAIN|Presence of chronic pain (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|STROKE|Presence of stroke (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|BLOOD_IN_STOOL|Presence of blood in stool (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|BLOOD_IN_VOMIT|Presence of blood in vomit (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|PEPTIC_ULCER|Presence of peptic ulcer (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|GASTRODUODENITIS|Presence of gastroduodenitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|GERD|Presence of gerd (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|INTESTINAL_OBSTRUCTION|Presence of intestinal_obstruction (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|ILEUS|Presence of ileus (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|CONSTIPATION|Presence of constipation (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|MESENTERIC_ISCHEMIA|Presence of mesenteric ischemia (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|DIVERTICULOSIS|Presence of diverticulosis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|APPENDICITIS|Presence of appendicitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|HEPATITIS|Presence of hepatitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|INFLUENZA|Presence of influenza (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|FOOD_POISONING|Presence of food poisoning (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|ASCITES|Presence of ascites (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|NEPHROLITHIASIS|Presence of nephrolithiasis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|DKA|Presence of dka (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|MYOCARDIAL_ISCHEMIA|Presence of myocardial ischemia (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|BILIARY_CANCER|Presence of biliary cancer (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|IBD|Presence of ibd (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|INFECTIOUS_GE|Presence of infectious gastroenteritis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|ESOPHAGITIS|Presence of esophagitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|NEGATIVE|Presence of negative (competing diagnosis)|
|[fluid](src/apanc_nlp/algo/fluid.py)|APFC|Acute peri-pancreatic fluid|
|[fluid](src/apanc_nlp/algo/fluid.py)|PANCREATIC|Pancreatic fluid|
|[fluid](src/apanc_nlp/algo/fluid.py)|WALLED_OFF|Walled off fluid|
|[nausea](src/apanc_nlp/algo/nausea.py)|VOMITING|Vomiting|
|[nausea](src/apanc_nlp/algo/nausea.py)|NAUSEA|Nausea|
|[necrosis](src/apanc_nlp/algo/necrosis.py)|POSITIVE|Generic mention of necrosis|
|[necrosis](src/apanc_nlp/algo/necrosis.py)|PANCREATITIS|Pancreatic necrosis|
|[necrosis](src/apanc_nlp/algo/necrosis.py)|PERIPANCREATIC|Peri-pancreatic necrosis|
|[necrosis](src/apanc_nlp/algo/necrosis.py)|ACUTE_COLLECTION|Acute necrotic collection|
|[pseudocyst](src/apanc_nlp/algo/pseudocyst.py)|POSITIVE|Generic pseudocyst|
|[pseudocyst](src/apanc_nlp/algo/pseudocyst.py)|PANCREATIC|Pancreatic pseudocyst|

## Output Format

Recommended format is `jsonl`. For more details, see [runrex](https://github.com/kpwhri/runrex).


## Versions

<!-- Uses [SEMVER](https://semver.org/). -->

Updates/changes are not expected. Versioning likely based on release timing in `YYYYmm`. See https://github.com/kpwhri/apanc-runrex/releases.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/kpwhri/apanc-runrex/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` or https://kpwhri.mit-license.org for more information.



<!-- CONTACT -->
## Contact

Please use the [issue tracker](https://github.com/kpwhri/apanc-runrex/issues). 


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* This work was funded as part of the [Sentinel Initiative](https://www.fda.gov/safety/fdas-sentinel-initiative).





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kpwhri/apanc-runrex.svg?style=flat-square
[contributors-url]: https://github.com/kpwhri/apanc-runrex/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kpwhri/apanc-runrex.svg?style=flat-square
[forks-url]: https://github.com/kpwhri/apanc-runrex/network/members
[stars-shield]: https://img.shields.io/github/stars/kpwhri/apanc-runrex.svg?style=flat-square
[stars-url]: https://github.com/kpwhri/apanc-runrex/stargazers
[issues-shield]: https://img.shields.io/github/issues/kpwhri/apanc-runrex.svg?style=flat-square
[issues-url]: https://github.com/kpwhri/apanc-runrex/issues
[license-shield]: https://img.shields.io/github/license/kpwhri/apanc-runrex.svg?style=flat-square
[license-url]: https://kpwhri.mit-license.org/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/kaiserpermanentewashingtonresearch
<!-- [product-screenshot]: images/screenshot.png -->
